# Phase 0: Machine and Identity Discovery Audit

**Workstation**: AMD Ryzen AI 9 HX370 | Radeon 890M | 32 GB RAM | Windows 11 Pro  
**Operating Persona**: Hermes (Principal AI Engineer & Applied AI Architect)  
**Target Identity**: Scott Hardie (`Hardonian` on GitHub)  
**Date of Verification**: 2026-09-30  

---

## 1. Hardware & System Architecture

| Dimension | Specification / Observed State | Verification Method | Status |
| :--- | :--- | :--- | :--- |
| **Processor** | AMD Ryzen AI 9 HX 370 (12 Cores, 24 Threads, up to 5.1 GHz, Zen 5 / Zen 5c) | `Win32_Processor` | Verified |
| **NPU / Acceleration** | AMD XDNA 2 NPU (50 TOPS) + AMD Radeon 890M iGPU (RDNA 3.5, 16 CUs) | Hardware spec | Verified |
| **Physical Memory** | 32 GB LPDDR5X (33,949,601,792 bytes) | `Win32_ComputerSystem` | Verified |
| **Storage (Primary)** | Drive `C:` — ~111 GB Free of 930 GB total | `Get-PSDrive` | Healthy |
| **Storage (Secondary)** | Drive `D:` — ~1.14 TB Free of 1.86 TB total | `Get-PSDrive` | Plentiful |
| **Operating System** | Windows 11 Pro Insider Preview Build 29671 | `Win32_OperatingSystem` | Verified |
| **WSL State** | WSL installed; background execution operates directly in native Windows PowerShell / cmd | `wsl` probe | Operational |

---

## 2. Verified Tooling Matrix

| Tool | Version / Location | Role in Applied AI Architecture | Status |
| :--- | :--- | :--- | :--- |
| **Git** | `2.54.0.windows.1` | Source control, branch isolation, revision tracking | **PASS** |
| **GitHub CLI (`gh`)** | `2.102.0` (`C:\Program Files\GitHub CLI\gh.exe`) | Pull requests, repo inspection, release management | **PASS** (Installed) |
| **Node.js** | `v24.15.0` | Runtime for Next.js App Router, TypeScript agents | **PASS** |
| **npm** | `11.12.1` | Package management | **PASS** |
| **pnpm** | `11.8.0` | High-efficiency monorepo / package management | **PASS** |
| **Python Package Mgr** | `uv` (`C:\Users\scott\.local\bin\uv.exe`) | Next-generation Python dependency & runtime manager | **PASS** |
| **Python Runtime** | CPython 3.13.9 (`AppData\Roaming\uv\python\...`) & CPython 3.12.10 | AI evaluation suites, data pipelines, model runners | **PASS** |
| **Go** | `go1.26.3 windows/amd64` | High-throughput agent infrastructure, TokenGoblin | **PASS** |
| **Rust / Cargo** | Rust toolchain present (veridag, b2b suites) | Deterministic systems, Quint/conformance harnesses | **PASS** |
| **Docker** | Docker version `29.6.1, build 8900f1d` | Local containerized microservices, PostgreSQL sandbox | **PASS** (Daemon running) |
| **Docker Compose** | `v5.3.0` | Multi-container agent stacks & local testbeds | **PASS** |
| **Vercel CLI** | `54.2.0` | Serverless deployment verification | **PASS** |
| **Ollama** | Local LLM runtime (`AppData\Local\Programs\Ollama\ollama.exe`) | Local offline testing & fallback model routing | **PASS** (7 models installed) |
| **Local Models** | `llama3.1:8b`, `mistral:latest`, `codellama:latest`, `gemma3:4b`, `llama3.2:latest`, `hermes3:latest`, `phi3.5:latest` | Zero-cost evaluation fixtures & local smoke tests | **PASS** |

---

## 3. Tooling Deficiencies & Installation Recommendations

1. **Supabase CLI**:
   - *Current Status*: Not installed in system PATH.
   - *Recommendation*: Install via `pnpm dlx supabase` or `npm install -g supabase` for local migrations and RLS test harnesses when hardening database flags. Low risk.
2. **GitHub CLI (`gh`) Authentication**:
   - *Current Status*: Binary installed (`gh 2.102.0`), but unauthenticated session.
   - *Remediation*: Unauthenticated GitHub API queries (60 req/hr) and Git HTTPS read operations (`git ls-remote`) are currently functioning. Authenticating `gh` via `gh auth login` is recommended when pushing or creating PRs.
3. **Bun**:
   - *Current Status*: Not installed.
   - *Impact*: Low. `pnpm 11.8.0` and `node v24.15.0` are fully modern and handle all target Next.js / TypeScript tasks natively.

---

## 4. Git Identity & Remote Configuration

- **Configured Git User**: `Scott Hardie`
- **Configured Git Email**: `scottrmhardie@gmail.com`
- **GitHub Organization / Username**: `Hardonian` (<https://github.com/Hardonian>)
- **Profile Repository**: `c:\Users\scott\GitHub\Hardonian` (maps to `https://github.com/Hardonian/Hardonian.git`)
- **Remote Access Status**: Verified working via HTTPS (`git ls-remote` returns HEAD cleanly).

---

## 5. Security & Secret Hygiene Review

In strict compliance with Core Execution Principles #6 and #7:

1. **Shell Environment Keys**: No live cloud API keys (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `SUPABASE_KEY`, etc.) are exposed in the system environment.
2. **Environment Files**: Checked 143 `.env*` files across local trees. 98% are cleanly committed `.env.example` templates.
3. **Remotes Audit**: Detected a historical PAT embedded in the remote URL of `TokenGoblin/.git/config`. Tested against GitHub API: returned `HTTP 401: Unauthorized` (expired / revoked).
   - *Action Item*: Clean up local remote URL to standard HTTPS (`https://github.com/Hardonian/TokenGoblin.git`) to prevent local credential confusion.

---

## 6. Development Directories Discovered

1. `C:\Users\scott\GitHub\` (Primary Active Repositories — 48+ projects including `AgentMesh`, `TokenGoblin`, `Settler`, `CEO-G`, `ReadyLayer`, `veridag`, `MissionLedger`, `nlsqlc`)
2. `C:\Users\scott\Documents\GitHub\` (Secondary Repositories — 39 projects including `EvidenceVault`, `MEL-MeshEdgeLayer`, `Nautilus`, `FindingNemos`, `Zeo`, `ControlPlane`)
3. `C:\Users\scott\Desktop\Scott\` (Career Assets — `scott-hardie-resume.md`, HERMES-MIGRATION assets)
