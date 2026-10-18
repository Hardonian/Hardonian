import concurrent.futures
import ipaddress
import re
import socket
import sys
import threading
import time
import urllib.error
import http.client
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

ALLOWED_WARNING_CODES = {403, 429, 500, 502, 503, 504, 530, 999}
USER_AGENT = "Hardonian-profile-audit/1.0"
REQUEST_TIMEOUT_SECONDS = 8
TRANSIENT_ATTEMPTS = 2
HOST_CONCURRENCY = 2
HOST_SEMAPHORES: defaultdict[str, threading.BoundedSemaphore] = defaultdict(
    lambda: threading.BoundedSemaphore(HOST_CONCURRENCY)
)


class UnsafeURL(ValueError):
    pass


def extract_urls(text: str) -> list[str]:
    pattern = r'!\[[^]]*\]\(([^)]*)\)|\[[^]]*\]\(([^)]*)\)|<(?:a|img)[^>]+(?:href|src)=["\']([^"\']*)'
    urls = []
    for match in re.finditer(pattern, text):
        value = next((item for item in match.groups() if item is not None), "")
        urls.append(value.strip().split(" ")[0])
    return urls


def validate_public_http_url(target: str) -> None:
    parsed = urlparse(target)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise UnsafeURL(f"unsupported URL: {target}")
    try:
        addresses = socket.getaddrinfo(
            parsed.hostname,
            parsed.port or (443 if parsed.scheme == "https" else 80),
            type=socket.SOCK_STREAM,
        )
    except socket.gaierror as exc:
        raise UnsafeURL(f"DNS resolution failed for {parsed.hostname}: {exc}") from exc
    for address in {entry[4][0] for entry in addresses}:
        ip = ipaddress.ip_address(address)
        if not ip.is_global:
            raise UnsafeURL(f"non-public address blocked for {parsed.hostname}: {ip}")


class SafeHTTPConnection(http.client.HTTPConnection):
    def connect(self) -> None:
        try:
            infos = socket.getaddrinfo(self.host, self.port, type=socket.SOCK_STREAM)
        except socket.gaierror as exc:
            raise UnsafeURL(f"DNS resolution failed for {self.host}: {exc}") from exc

        valid_ip = None
        for _family, _type, _proto, _canonname, sockaddr in infos:
            ip = ipaddress.ip_address(sockaddr[0])
            if not ip.is_global:
                raise UnsafeURL(f"non-public address blocked for {self.host}: {ip}")
            if valid_ip is None:
                valid_ip = sockaddr[0]

        if not valid_ip:
            raise UnsafeURL(f"No valid address entries resolved for {self.host}")

        original_host = self.host
        self.host = valid_ip
        try:
            super().connect()
        finally:
            self.host = original_host


class SafeHTTPSConnection(http.client.HTTPSConnection, SafeHTTPConnection):
    def connect(self) -> None:
        try:
            infos = socket.getaddrinfo(self.host, self.port, type=socket.SOCK_STREAM)
        except socket.gaierror as exc:
            raise UnsafeURL(f"DNS resolution failed for {self.host}: {exc}") from exc

        valid_ip = None
        for _family, _type, _proto, _canonname, sockaddr in infos:
            ip = ipaddress.ip_address(sockaddr[0])
            if not ip.is_global:
                raise UnsafeURL(f"non-public address blocked for {self.host}: {ip}")
            if valid_ip is None:
                valid_ip = sockaddr[0]

        if not valid_ip:
            raise UnsafeURL(f"No valid address entries resolved for {self.host}")

        original_host = self.host
        self.sock = self._create_connection((valid_ip, self.port), self.timeout, self.source_address)
        try:
            self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        except OSError:
            pass

        if self._tunnel_host:
            self._tunnel()

        server_hostname = self._tunnel_host if self._tunnel_host else original_host
        self.sock = self._context.wrap_socket(self.sock, server_hostname=server_hostname)


class SafeHTTPHandler(urllib.request.HTTPHandler):
    def http_open(self, req: urllib.request.Request) -> http.client.HTTPResponse:
        return self.do_open(SafeHTTPConnection, req)


class SafeHTTPSHandler(urllib.request.HTTPSHandler):
    def https_open(self, req: urllib.request.Request) -> http.client.HTTPResponse:
        return self.do_open(SafeHTTPSConnection, req, context=self._context)


class ValidatingRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(
        self,
        req: urllib.request.Request,
        fp: Any,
        code: int,
        msg: str,
        headers: Any,
        newurl: str,
    ) -> urllib.request.Request | None:
        """Return a Request or None in response to a redirect after validating security."""
        validate_public_http_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def resolve_link(raw: str, root: Path) -> tuple[str | None, Path | None]:
    if not raw.strip():
        raise UnsafeURL(f"empty URL: '{raw}'")
    if raw.startswith(("http://", "https://")):
        return raw, None

    root = root.resolve()
    parsed = urlparse(raw)
    local_suffix = unquote(parsed.path).lstrip("/")
    if raw.startswith("/Hardonian/"):
        local_suffix = raw.split("/tree/main/", 1)[-1] if "/tree/main/" in raw else raw.split("/Hardonian/", 1)[-1]
    local = (root / local_suffix).resolve()

    if not local.is_relative_to(root):
        raise UnsafeURL(f"local path escapes repository: {raw}")
    return None, local


def is_transient_network_error(exc: BaseException) -> bool:
    current: BaseException | object | None = exc
    visited: set[int] = set()
    while current is not None and id(current) not in visited:
        visited.add(id(current))
        if isinstance(current, (TimeoutError, socket.timeout, ConnectionResetError)):
            return True
        message = str(current).lower()
        if any(
            fragment in message
            for fragment in ("timed out", "temporarily unavailable", "connection reset", "remote end closed")
        ):
            return True
        current = getattr(current, "reason", None) or getattr(current, "__cause__", None)
    return False



def _check_url_attempt(
    opener: urllib.request.OpenerDirector,
    request: urllib.request.Request,
    hostname: str,
    raw: str,
    attempt: int,
) -> tuple[str, tuple | str]:
    semaphore = HOST_SEMAPHORES[hostname]
    with semaphore:
        try:
            with opener.open(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
                if response.status in ALLOWED_WARNING_CODES:
                    return "warn", f"WARN {response.status} {raw}"
                if response.status >= 400:
                    return "fail", (raw, "ERROR", f"HTTP {response.status}")
                return "ok", f"OK 200 {raw}"
        except urllib.error.HTTPError as exc:
            if exc.code in ALLOWED_WARNING_CODES:
                return "warn", f"WARN {exc.code} {raw}"
            return "fail", (raw, "ERROR", f"HTTP {exc.code}")
        except Exception as exc:
            if is_transient_network_error(exc) and attempt < TRANSIENT_ATTEMPTS:
                time.sleep(2**attempt)
                return "retry", "retry"
            raise


def check_url(
    raw: str, target: str, opener: urllib.request.OpenerDirector | None = None
) -> tuple[str, tuple | str]:
    try:
        validate_public_http_url(target)
        opener = urllib.request.build_opener(SafeHTTPHandler(), SafeHTTPSHandler(), ValidatingRedirectHandler())
        request = urllib.request.Request(target, headers={"User-Agent": USER_AGENT})
        hostname = urlparse(target).hostname or ""
        for attempt in range(1, TRANSIENT_ATTEMPTS + 1):
            status, detail = _check_url_attempt(opener, request, hostname, raw, attempt)
            if status != "retry":
                return status, detail
        return "warn", f"WARN TRANSIENT {raw} (transient error)"
    except Exception as exc:
        return "fail", (raw, "ERROR", str(exc))


def collect_and_validate_links(urls: list[str], root: Path) -> tuple[list[tuple[str, str]], list]:
    failures = []
    external = []
    for raw in urls:
        if raw.startswith(("#", "mailto:")):
            continue
        try:
            target, local = resolve_link(raw, root)
        except UnsafeURL as exc:
            failures.append((raw, "UNSAFE", str(exc)))
            continue
        if local is not None:
            if not local.exists():
                failures.append((raw, "LOCAL_MISSING", str(local)))
            else:
                print(f"LOCAL 200 {raw}")
        elif target is not None:
            external.append((raw, target))
    return external, failures


def check_external_links(external: list[tuple[str, str]]) -> list:
    failures = []
    if not external:
        return failures
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(8, max(1, len(external)))) as pool:
        futures = {pool.submit(check_url, raw, target): raw for raw, target in external}
        for future in concurrent.futures.as_completed(futures):
            status, detail = future.result()
            if status == "fail":
                if isinstance(detail, tuple):
                    failures.append(detail)
                    print(f"FAIL {detail[1]} {detail[0]}")
                else:
                    failures.append((futures[future], "FAIL", detail))
                    print(f"FAIL {detail}")
            else:
                print(detail)
    return failures


def report_results(urls_count: int, failures: list) -> int:
    if failures:
        print("FAILURES", len(failures))
        for failure in failures:
            print(failure)
        return 1
    print(f"CHECKED {urls_count} UNIQUE_LINKS_AND_IMAGES; FAILURES 0")
    return 0


def audit(readme: Path = Path("README.md")) -> int:
    root = readme.parent.resolve()
    urls = list(dict.fromkeys(extract_urls(readme.read_text(encoding="utf-8"))))
    external, failures = collect_and_validate_links(urls, root)
    failures.extend(check_external_links(external))
    return report_results(len(urls), failures)


if __name__ == "__main__":
    sys.exit(audit())
