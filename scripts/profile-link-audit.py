import concurrent.futures
import ipaddress
import re
import socket
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urljoin, urlparse

ALLOWED_WARNING_CODES = {403, 429, 530, 999}
USER_AGENT = "Hardonian-profile-audit/1.0"


class UnsafeURL(ValueError):
    pass


def extract_urls(text: str) -> list[str]:
    pattern = r'!\[[^]]*\]\(([^)]+)\)|\[[^]]*\]\(([^)]+)\)|<(?:a|img)[^>]+(?:href|src)=["\']([^"\']+)'
    urls = []
    for match in re.finditer(pattern, text):
        value = next((item for item in match.groups() if item), "")
        if value:
            urls.append(value.strip().split(" ")[0])
    return urls


def validate_public_http_url(target: str) -> None:
    parsed = urlparse(target)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise UnsafeURL(f"unsupported URL: {target}")
    try:
        addresses = socket.getaddrinfo(parsed.hostname, parsed.port or (443 if parsed.scheme == "https" else 80))
    except socket.gaierror as exc:
        raise UnsafeURL(f"DNS resolution failed for {parsed.hostname}: {exc}") from exc
    for address in {entry[4][0] for entry in addresses}:
        ip = ipaddress.ip_address(address)
        if not ip.is_global:
            raise UnsafeURL(f"non-public address blocked for {parsed.hostname}: {ip}")


class ValidatingRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        validate_public_http_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def resolve_link(raw: str, root: Path) -> tuple[str | None, Path | None]:
    if raw.startswith(("http://", "https://")):
        return raw, None

    root = root.resolve()
    local_suffix = raw.lstrip("/")
    if raw.startswith("/Hardonian/"):
        local_suffix = raw.split("/tree/main/", 1)[-1] if "/tree/main/" in raw else raw.split("/Hardonian/", 1)[-1]
    local = (root / local_suffix).resolve()

    if raw.startswith(("products/", "architecture-playbook/", "assets/", "/Hardonian/")):
        if not local.is_relative_to(root):
            raise UnsafeURL(f"local path escapes repository: {raw}")
        return None, local

    return urljoin("https://github.com/Hardonian/Hardonian/blob/main/", raw), None


def check_url(raw: str, target: str) -> tuple[str, tuple | str]:
    try:
        validate_public_http_url(target)
        opener = urllib.request.build_opener(ValidatingRedirectHandler())
        request = urllib.request.Request(target, headers={"User-Agent": USER_AGENT})
        with opener.open(request, timeout=20) as response:
            code = response.status
            if code >= 400 and code not in ALLOWED_WARNING_CODES:
                return "fail", (raw, code, response.headers.get("content-type", ""))
            return "ok", f"OK {code} {raw}"
    except urllib.error.HTTPError as exc:
        if exc.code in ALLOWED_WARNING_CODES:
            return "warn", f"WARN {exc.code} {raw}"
        return "fail", (raw, exc.code, str(exc))
    except Exception as exc:
        return "fail", (raw, "ERROR", str(exc))


def audit(readme: Path = Path("README.md")) -> int:
    root = readme.parent.resolve()
    urls = list(dict.fromkeys(extract_urls(readme.read_text(encoding="utf-8"))))
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

    with concurrent.futures.ThreadPoolExecutor(max_workers=min(8, max(1, len(external)))) as pool:
        futures = {pool.submit(check_url, raw, target): raw for raw, target in external}
        for future in concurrent.futures.as_completed(futures):
            status, detail = future.result()
            if status == "fail":
                failures.append(detail)
                print(f"FAIL {detail[1]} {detail[0]}")
            else:
                print(detail)

    if failures:
        print("FAILURES", len(failures))
        for failure in failures:
            print(failure)
        return 1
    print(f"CHECKED {len(urls)} UNIQUE_LINKS_AND_IMAGES; FAILURES 0")
    return 0


if __name__ == "__main__":
    sys.exit(audit())
