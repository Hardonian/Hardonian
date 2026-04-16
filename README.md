<!-- ========================================================= -->
<!-- HERO -->
<!-- ========================================================= -->

<h1 align="center">Scott Hardie</h1>

<h3 align="center">
Technical Product Manager • Solutions Architect • Platform Systems
</h3>

<p align="center">
<em>Designing operational platforms where architecture, product, and automation intersect.</em>
</p>

<p align="center">
Solutions Architect @ <strong>McGraw Hill</strong><br>
Canada • Platform Architecture • SaaS Systems • Automation Infrastructure
</p>

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Inter&size=20&pause=1200&center=true&vCenter=true&width=900&lines=Architecture+%2B+Execution;Operational+systems+over+demo+systems;Automation+that+survives+real+operations;Platforms%2C+integrations%2C+and+product+delivery;Useful+%3E+clever.&cache_seconds=1800"/>
</p>

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0ea5e9,100:7c3aed&height=40&section=header&text=Platform%20Architecture%20•%20Automation%20Systems%20•%20Product%20Delivery&fontSize=18&fontColor=ffffff"/>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Product%20Systems-Architecture-blueviolet"/>
<img src="https://img.shields.io/badge/SaaS-Multi%20Tenant-orange"/>
<img src="https://img.shields.io/badge/Frontend-React%20%2B%20Next.js-06b6d4"/>
<img src="https://img.shields.io/badge/Backend-Node.js%20APIs-3c873a"/>
<img src="https://img.shields.io/badge/Data-Postgres%20%2B%20RLS-green"/>
<img src="https://img.shields.io/badge/Automation-AI%20Workflows-purple"/>
<img src="https://img.shields.io/badge/CI-GitHub%20Actions-orange"/>
</p>

<p align="center">
<img src="https://img.shields.io/badge/C%2B%2B-Systems%20Knowledge-00599C?logo=c%2B%2B"/>
<img src="https://img.shields.io/badge/Rust-Systems%20Knowledge-black?logo=rust"/>
<img src="https://img.shields.io/badge/TypeScript-Primary-3178C6?logo=typescript"/>
</p>

---

## Overview

I build systems at the intersection of:

**product direction → platform architecture → operational automation**

My focus is on systems that remain:

- observable
- reliable
- traceable
- operationally clear

I optimize for real operations, not demo environments.

---

## Core Platform Systems

| System | Role |
|------|------|
| **AIAS** | AI workflow architecture |
| **Requiem** | deterministic execution kernel |
| **Settler** | reconciliation control plane |

---

## Platform Relationship

```mermaid
flowchart TB

Users["Operators<br/>Product Systems"]
AIAS["AIAS<br/>AI Workflow Architecture"]
Requiem["Requiem<br/>Execution Kernel"]
Settler["Settler<br/>Reconciliation Control Plane"]
External["External Systems<br/>Payments • APIs • SaaS"]

Users --> AIAS
AIAS --> Requiem
Requiem --> Settler
Settler --> External
```

---

## Featured Projects

| Project | What it does | Focus |
|------|------|------|
| [Settler](https://github.com/Hardonian/Settler) | Resend-style payment reconciliation API for developers | Deterministic matching, auditability |
| [Requiem](https://github.com/Hardonian/Requiem) | Unified AI control plane (kernel + policy + web) | Governance, orchestration, traceability |
| [ControlPlane](https://github.com/Hardonian/ControlPlane) | Execution engine for agent-driven systems | Reliable automation at scale |
| [ReadyLayer](https://github.com/Hardonian/ReadyLayer) | Review/test/document AI-generated code before merge | CI-integrated code governance |
| [JobForge](https://github.com/Hardonian/JobForge) | Postgres-native, language-agnostic job orchestrator | Idempotency, retries, RPC-first design |
| [castor](https://github.com/Hardonian/castor) | Podcast sponsor analytics + ROI attribution stack | Ingestion pipelines, reporting systems |
| [truthcore](https://github.com/Hardonian/truthcore) | Deterministic verification platform | Reproducibility, anomaly detection |

---

## Proficiencies

| Area | Proficiency |
|------|------|
| Platform architecture | Advanced |
| SaaS systems (multi-tenant) | Advanced |
| API/backend systems (Node/REST/Webhooks) | Advanced |
| Frontend product systems (React/Next.js) | Advanced |
| Data systems (Postgres/Supabase/RLS) | Advanced |
| AI workflow automation | Advanced |
| CI/CD and delivery engineering | Advanced |
| Security boundaries (auth, tenant isolation) | Advanced |
| Performance and web quality (CWV) | Strong |
| Accessibility (WCAG-aware delivery) | Strong |

---

## Architecture Deep Dives

### Settler Architecture

```mermaid
flowchart LR

Sources["Data Sources<br/>Bank • ERP • Payment APIs"]
Ingestion["Ingestion<br/>ETL • Webhooks"]
Matcher["Matching Engine"]
Review["Human Review"]
Ledger["Verified Ledger"]
Audit["Audit Reporting"]

Sources --> Ingestion
Ingestion --> Matcher
Matcher --> Review
Review --> Ledger
Ledger --> Audit
```

Goals:

- deterministic matching logic
- auditability
- traceable financial workflows
- human review checkpoints

### Requiem Architecture

```mermaid
flowchart TB

Inputs["Inputs<br/>Events • Agents • Tasks"]
Kernel["Execution Kernel"]
Trace["Trace Engine"]
Policy["Policy Layer"]
State["System State"]

Inputs --> Kernel
Kernel --> Trace
Kernel --> Policy
Trace --> State
Policy --> State
```

Focus areas:

- deterministic workflows
- execution traceability
- governance layers
- reproducible automation

### AIAS Architecture

```mermaid
flowchart LR

Docs["Documents<br/>Web Data"]
Agents["AI Agents"]
Review["Human Oversight"]
Output["Operational Systems"]

Docs --> Agents
Agents --> Review
Review --> Output
```

Goal:

AI systems that remain **observable, governable, and operationally safe**.

---

## Platform Stack

```mermaid
flowchart LR

UI["UI<br/>React • Next.js • Tailwind"]
API["API<br/>Node.js • REST • Webhooks"]
Middleware["Middleware<br/>Auth • SDKs"]
Data["Data<br/>Postgres • Supabase • RLS"]
Infra["Infrastructure<br/>CI/CD"]
Obs["Observability<br/>Logs • Verification"]

UI --> API
API --> Middleware
Middleware --> Data
API --> Infra
Infra --> Obs
```

---

## Technical Surface

**Primary:** TypeScript/JavaScript, Python, SQL, Go, HTML/CSS, Bash  
**Systems familiarity:** Rust, C++  
**Execution environments:** WebAssembly (WASM), Node.js, Deno, Bun

---

## Operating Principles

- reduce complexity before automating it
- prefer observable systems over opaque abstractions
- design for degraded states
- keep humans in the loop where judgment matters
- build systems that survive real-world conditions

If a system cannot be debugged, explained, or recovered, it probably is not ready to ship.

---

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0ea5e9,100:7c3aed&height=90&section=footer"/>
</p>
