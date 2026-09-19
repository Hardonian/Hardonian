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
from pathlib import Path
from urllib.parse import quote, urlparse

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "profile-projects.json"
README_PATH = ROOT / "README.md"
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
        ci_badge = f"{ci_page}/badge.svg"
        project_cell = (
            f"**[{name}]({repo})** · {project['language']}<br />"
            f"{project['role']} · `{project['maturity']}`<br />"
            f"[![{name} CI]({ci_badge})]({ci_page})"
        )
        evidence_cell = (
            f"{project['proof']}<br />"
            f"[Architecture]({project['documentation']}) · [Evidence]({project['evidence']})"
        )
        lines.append(f"| {project_cell} | {project['problem']} | {evidence_cell} |")
    lines.extend([END_MARKER, ""])
    return "\n".join(lines)


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
    for project in manifest["projects"]:
        name = project["name"]
        request(f"https://api.github.com/repos/Hardonian/{name}")
        request(
            f"https://api.github.com/repos/Hardonian/{name}/actions/workflows/"
            f"{project['ci_workflow']}"
        )
        request(github_api_url(project["documentation"]))
        request(github_api_url(project["evidence"]))


def check(manifest: dict, *, remote: bool = False) -> None:
    validate_manifest(manifest)
    if remote:
        verify_remote(manifest)
    expected = replace_generated_section(README_PATH.read_text(encoding="utf-8"), render(manifest))
    actual = README_PATH.read_text(encoding="utf-8")
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
            print(f"refreshed {len(manifest['projects'])} projects on {manifest['verified_on']}")
        else:
            check(manifest, remote=args.verify_remote)
            print(f"verified {len(manifest['projects'])} projects; README metadata is current")
    except (MetadataError, OSError, json.JSONDecodeError, urllib.error.URLError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
