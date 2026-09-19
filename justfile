# Hardonian standard justfile — works for any stack.
# Install just: pipx install rust-just

# Detect and install deps + create .env
bootstrap:
    ./scripts/bootstrap.sh

# Run the app (override per repo)
dev:
    @echo "Override 'dev' in your repo justfile"

# Run tests
test:
    uv run python -m unittest discover tests
    uv run python scripts/profile-metadata.py --check

# Verify every public and local README link
audit:
    uv run python scripts/profile-link-audit.py

# Verify public project evidence and regenerate the canonical-project section
refresh-profile:
    uv run python scripts/profile-metadata.py --refresh

# Smoke / health check
smoke:
    @echo "Override 'smoke' in your repo justfile"

# Show status
status:
    @curl -fsS http://127.0.0.1:8000/health || echo "no health endpoint on :8000"
