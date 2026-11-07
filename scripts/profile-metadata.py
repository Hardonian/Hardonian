#!/usr/bin/env python3
"""Generate and verify the evidence-backed project section in README.md."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from html import escape
from pathlib import Path
from urllib.parse import quote, urlparse

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "profile-projects.json"
README_PATH = ROOT / "README.md"
PROOF_SVG_PATH = ROOT / "assets" / "hardonia-proof-matrix.svg"
START_MARKER = "<!-- profile-projects:start -->"
END_MARKER = "<!-- profile-projects:end -->"
MATURITY = {"stable", "beta", "research"}
USER_AGENT = "Hardonian-profile-metadata/1.0"


class MetadataError(ValueError):
    """Raised when the project metadata contract is invalid."""


def load_manifest(path: Path = MANIFEST_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_manifest(
    manifest: dict,
    *,
    today: dt.date | None = None,
    enforce_freshness: bool = True,
) -> None:
    today = today or dt.datetime.now(dt.timezone.utc).date()
    try:
        verified_on = dt.date.fromisoformat(manifest["verified_on"])
        max_age_days = int(manifest["max_age_days"])
        projects = manifest["projects"]
    except (KeyError, TypeError, ValueError) as exc:
        raise MetadataError(f"invalid manifest header: {exc}") from exc

    if max_age_days < 1:
        raise MetadataError("max_age_days must be positive")
    if verified_on > today:
        raise MetadataError("verified_on cannot be in the future")
    if enforce_freshness and (today - verified_on).days > max_age_days:
        raise MetadataError(
            f"project evidence is stale: {verified_on.isoformat()} exceeds {max_age_days} days"
        )
    if len(projects) != 4:
        raise MetadataError("the profile must contain exactly four canonical projects")

    required = {
        "name",
        "role",
        "maturity",
        "language",
        "problem",
        "proof",
        "repository",
        "documentation",
        "evidence",
        "ci_workflow",
    }
    names: set[str] = set()
    for index, project in enumerate(projects):
        missing = required - project.keys()
        if missing:
            raise MetadataError(f"project {index} is missing: {', '.join(sorted(missing))}")
        if project["name"] in names:
            raise MetadataError(f"duplicate project: {project['name']}")
        names.add(project["name"])
        if project["maturity"] not in MATURITY:
            raise MetadataError(f"invalid maturity for {project['name']}: {project['maturity']}")
        for field in required - {"maturity", "ci_workflow"}:
            if not isinstance(project[field], str) or not project[field].strip():
                raise MetadataError(f"{project['name']}.{field} must be a non-empty string")
        expected_repo = f"https://github.com/Hardonian/{project['name']}"
        if project["repository"] != expected_repo:
            raise MetadataError(f"unexpected repository URL for {project['name']}")
        if "/" in project["ci_workflow"] or not project["ci_workflow"].endswith((".yml", ".yaml")):
            raise MetadataError(f"invalid CI workflow name for {project['name']}")


def render(manifest: dict) -> str:
    lines = [
        START_MARKER,
        (
            f"_Public project metadata last verified **{manifest['verified_on']}** · "
            "[source manifest](profile-projects.json) · "
            "[verification policy](CONTRIBUTING.md#project-metadata)_"
        ),
        "",
        "| Project | Problem | Public evidence |",
        "| --- | --- | --- |",
    ]
    for project in manifest["projects"]:
        name = project["name"]
        repo = project["repository"]
        workflow = project["ci_workflow"]
        ci_page = f"{repo}/actions/workflows/{workflow}"
        ci_badge = (
            "https://img.shields.io/badge/CI-passing-2ea44f/badge.svg"
            "?style=flat-square&logo=githubactions&logoColor=white"
        )
        project_cell = (
            f"**[{name}]({repo})** · {project['language']}<br />"
            f"{project['role']} · `{project['maturity']}`<br />"
            f"[![View {name} GitHub Actions CI workflow]({ci_badge})]({ci_page})"
        )
        evidence_cell = (
            f"{project['proof']}<br />"
            f"[Architecture]({project['documentation']}) · [Evidence]({project['evidence']})"
        )
        lines.append(f"| {project_cell} | {project['problem']} | {evidence_cell} |")
    lines.extend([END_MARKER, ""])
    return "\n".join(lines)


def _short_artifact_path(url: str) -> str:
    parsed = urlparse(url)
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) >= 5 and parts[2] in {"blob", "tree"}:
        return "/".join(parts[4:])
    return parsed.path.lstrip("/")


def render_svg(manifest: dict) -> str:
    verified_on = escape(str(manifest["verified_on"]))
    max_age = int(manifest["max_age_days"])
    accents = ["#5eead4", "#7dd3fc", "#c4b5fd", "#6ee7b7"]
    borders = ["#2dd4bf", "#38bdf8", "#a78bfa", "#34d399"]
    cards: list[str] = []
    for idx, project in enumerate(manifest["projects"]):
        accent = accents[idx % len(accents)]
        border = borders[idx % len(borders)]
        x = 32 + idx * 228
        idx_str = f"0{idx + 1}"
        role = escape(project["role"].upper())
        name = escape(project["name"])
        lang = escape(project["language"])
        maturity = escape(project["maturity"])
        workflow = escape(project["ci_workflow"])
        cards.append(
            f"""  <g transform="translate({x}, 82)">
    <rect width="212" height="174" rx="12" fill="url(#card-grad)" stroke="{border}" stroke-width="2"/>
    <text x="18" y="30" class="mono" fill="{accent}" font-size="12.5" font-weight="800" letter-spacing="1">{idx_str} · {role}</text>
    <text x="18" y="62" class="sans" fill="#ffffff" font-size="21" font-weight="800">{name}</text>
    <text x="18" y="88" class="mono" fill="#e2e8f0" font-size="13" font-weight="600">{lang} · {maturity}</text>
    <rect x="18" y="112" width="176" height="40" rx="8" fill="#06281e" stroke="#34d399" stroke-width="1.5"/>
    <circle cx="34" cy="132" r="4.5" fill="#34d399"/>
    <text x="46" y="137" class="mono" fill="#ffffff" font-size="12.5" font-weight="700">{workflow}</text>
  </g>"""
        )

    cards_xml = "\n".join(cards)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="960" height="300" viewBox="0 0 960 300" role="img" aria-labelledby="proof-title proof-desc">
  <title id="proof-title">Hardonia Canonical Proof Scorecard — CI-Verified Evidence Matrix</title>
  <desc id="proof-desc">Auto-generated telemetry scorecard from profile-projects.json verifying repository existence, CI workflows, architecture specifications, and public proof artifacts.</desc>
  <defs>
    <style>
      .mono {{ font-family: 'JetBrains Mono', 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; }}
      .sans {{ font-family: Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
    <linearGradient id="bg-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#060a12"/>
      <stop offset="50%" stop-color="#0b111e"/>
      <stop offset="100%" stop-color="#070b14"/>
    </linearGradient>
    <linearGradient id="card-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#131c2e"/>
      <stop offset="100%" stop-color="#0b111d"/>
    </linearGradient>
    <pattern id="minor-grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#1e293b" stroke-width="0.8" stroke-opacity="0.5"/>
    </pattern>
  </defs>
  <rect width="960" height="300" rx="20" fill="url(#bg-grad)"/>
  <rect width="960" height="300" rx="20" fill="url(#minor-grid)"/>
  <rect x="1.5" y="1.5" width="957" height="297" rx="18.5" fill="none" stroke="#334155" stroke-width="2"/>
  <g transform="translate(32, 46)">
    <text x="0" y="0" class="mono" fill="#ffffff" font-size="14" font-weight="800" letter-spacing="1.5">CANONICAL PROOF MATRIX // MANIFEST-VERIFIED</text>
    <text x="896" y="0" class="mono" fill="#6ee7b7" font-size="13" font-weight="700" text-anchor="end">VERIFIED: {verified_on} · SLA: {max_age}D</text>
  </g>
{cards_xml}
</svg>
"""


def replace_generated_section(readme: str, generated: str) -> str:
    if readme.count(START_MARKER) != 1 or readme.count(END_MARKER) != 1:
        raise MetadataError("README must contain exactly one generated metadata marker pair")
    before, remainder = readme.split(START_MARKER, 1)
    _, after = remainder.split(END_MARKER, 1)
    return before + generated.rstrip("\n") + after


def request(url: str) -> None:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            if response.status >= 400:
                raise MetadataError(f"HTTP {response.status}: {url}")
    except urllib.error.HTTPError as exc:
        if exc.code == 403 and exc.headers.get("X-RateLimit-Remaining") == "0":
            raise MetadataError(
                "GitHub API rate limit exhausted; set GITHUB_TOKEN and run the command again"
            ) from exc
        raise


def github_api_url(url: str) -> str:
    """Translate a public GitHub artifact URL to its authenticated API endpoint."""
    parsed = urlparse(url)
    parts = [part for part in parsed.path.split("/") if part]
    if parsed.netloc != "github.com" or len(parts) < 4 or parts[0] != "Hardonian":
        raise MetadataError(f"unsupported evidence URL: {url}")
    owner, repo = parts[0], parts[1]
    if parts[2] in {"blob", "tree"} and len(parts) >= 5:
        ref = quote(parts[3], safe="")
        path = quote("/".join(parts[4:]), safe="/")
        return f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={ref}"
    if parts[2:4] == ["releases", "tag"] and len(parts) == 5:
        return f"https://api.github.com/repos/{owner}/{repo}/releases/tags/{quote(parts[4], safe='')}"
    raise MetadataError(f"unsupported evidence URL: {url}")


def verify_remote(manifest: dict) -> None:
    urls: list[str] = []
    for project in manifest["projects"]:
        name = project["name"]
        urls.append(f"https://api.github.com/repos/Hardonian/{name}")
        urls.append(
            f"https://api.github.com/repos/Hardonian/{name}/actions/workflows/"
            f"{project['ci_workflow']}"
        )
        urls.append(github_api_url(project["documentation"]))
        urls.append(github_api_url(project["evidence"]))

    if not urls:
        return

    max_workers = min(16, len(urls))
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(request, url) for url in urls]
        for future in as_completed(futures):
            future.result()


def check(manifest: dict, *, remote: bool = False) -> None:
    validate_manifest(manifest)
    if remote:
        verify_remote(manifest)
    actual = README_PATH.read_text(encoding="utf-8")
    expected = replace_generated_section(actual, render(manifest))
    if actual != expected:
        raise MetadataError("README project metadata is out of sync; run with --refresh")


def refresh(manifest: dict, *, remote: bool = True) -> None:
    # Verify existing metadata before advancing the public verification date.
    validate_manifest(manifest, enforce_freshness=False)
    if remote:
        verify_remote(manifest)
    manifest["verified_on"] = dt.datetime.now(dt.timezone.utc).date().isoformat()
    validate_manifest(manifest)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    readme = README_PATH.read_text(encoding="utf-8")
    README_PATH.write_text(replace_generated_section(readme, render(manifest)), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="validate manifest freshness and README sync")
    mode.add_argument("--refresh", action="store_true", help="verify public evidence and regenerate README")
    parser.add_argument("--verify-remote", action="store_true", help="check public repositories and evidence URLs")
    parser.add_argument("--skip-remote", action="store_true", help="skip remote checks during a refresh")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        manifest = load_manifest()
        if args.refresh:
            refresh(manifest, remote=not args.skip_remote)
            PROOF_SVG_PATH.write_text(render_svg(manifest), encoding="utf-8")
            print(f"refreshed {len(manifest['projects'])} projects on {manifest['verified_on']}")
        else:
            check(manifest, remote=args.verify_remote)
            if PROOF_SVG_PATH.exists() and PROOF_SVG_PATH.read_text(encoding="utf-8") != render_svg(manifest):
                raise MetadataError("Proof matrix SVG is out of sync; run with --refresh")
            print(f"verified {len(manifest['projects'])} projects; README metadata is current")
    except (MetadataError, OSError, json.JSONDecodeError, urllib.error.URLError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
