# Contributing

This repository is the source for Scott Hardie's GitHub profile, its product pages, and the automated evidence checks that keep public claims inspectable.

## Workflow

1. Open an issue with context.
2. Branch from `main`.
3. Keep PRs focused.
4. Include validation notes.
5. Merge after CI and review.

## Local validation

The only required runtime is Python 3.11 or newer. [`uv`](https://docs.astral.sh/uv/) and [`just`](https://just.systems/) are convenient but optional.

```bash
git clone https://github.com/Hardonian/Hardonian.git
cd Hardonian

# Unit tests and generated-metadata consistency
uv run python -m unittest discover tests
uv run python scripts/profile-metadata.py --check

# Public and local link verification
uv run python scripts/profile-link-audit.py
```

With `just` installed, `just test` runs the unit and metadata checks and `just audit` verifies all README links.

## Project metadata

The four canonical projects shown in `README.md` are generated from `profile-projects.json`. Do not edit the generated block between `profile-projects:start` and `profile-projects:end` by hand.

After changing a project description, maturity label, proof link, or workflow:

```bash
uv run python scripts/profile-metadata.py --refresh
```

Refresh performs live checks against each public repository, documentation page, evidence artifact, and CI workflow before advancing the verification date. Profile CI rejects:

- metadata older than 90 days;
- missing or inaccessible evidence;
- unsupported maturity labels;
- anything other than exactly four canonical projects; and
- generated README content that no longer matches the manifest.

Unauthenticated GitHub API requests are rate-limited. If the refresh reports an exhausted limit, export a scoped `GITHUB_TOKEN` and run it again; the workflow supplies its token automatically in CI.

Maturity labels are intentionally conservative:

- `stable` — a versioned public release exists;
- `beta` — the public system is functional, but interfaces may change;
- `research` — the architecture or performance model is still being validated.

## Content standards

- Link performance or reliability claims to a public benchmark, test, release, or specification.
- Do not present static badges as live operational telemetry.
- Keep provider-correlated revenue evidence separate from catalog, checkout, and local database state.
- Never publish credentials, customer identifiers, private paths, raw webhook payloads, or confidential research details.
