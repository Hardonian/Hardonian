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

# Overview

I build systems that sit at the intersection of:

**product direction → platform architecture → operational automation**

These systems often involve:

- distributed integrations
- SaaS platforms
- automation pipelines
- reconciliation and operational tooling

The goal is to build systems that remain:

- observable
- reliable
- traceable
- operationally clear

Many systems must function in messy real-world environments, not controlled demos.

---

# Core Platform Systems

| System | Role |
|------|------|
| **AIAS** | AI workflow architecture |
| **Requiem** | deterministic execution kernel |
| **Settler** | reconciliation control plane |

---

# Platform Relationship

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

# Settler Architecture

Settler explores how reconciliation workflows can move from manual processes toward deterministic automation.

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

---

# Requiem Architecture

Requiem explores traceable execution systems for automation and orchestration.

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

---

# AIAS Architecture

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

# Platform Stack

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

# Technical Surface

Primary languages:

- TypeScript / JavaScript
- Python
- SQL
- Go
- HTML
- CSS
- Bash

Systems familiarity:

- Rust
- C++

Execution environments
- WebAssembly (WASM)
- Node.js
- Deno
- Bun

---

# Capabilities

| Domain | Areas |
|------|------|
| Frontend | React, Next.js, Tailwind |
| Backend | Node APIs, REST services |
| Data | Postgres, Supabase, RLS |
| Integration | OAuth, SaaS APIs |
| Automation | AI workflows |
| DevOps | GitHub Actions |
| Security | Auth layers, tenant isolation |
| Performance | Core Web Vitals |
| Accessibility | WCAG design |
| Growth | CRO-aware UX |

---

# Platform Concerns

Operational systems require attention to:

- authentication boundaries
- tenant isolation
- webhook verification
- secrets management
- audit logging
- failure visibility

Systems should **fail predictably and recover safely**.

---

# Delivery

Delivery workflows typically include:

- CI pipelines
- regression testing
- smoke tests
- reproducible builds
- staged deployments

Operational reliability is treated as **product quality**.

---

# Additional Projects

- Hardonia — ecommerce automation experiments
- AI-Agent-Portfolio — applied AI workflow systems
- hardonia-intel-scraper — research automation

---

# Operating Principles

Guidelines that shape most systems I design:

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
