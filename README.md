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

<p align="center">
<a href="#overview">Overview</a> •
<a href="#featured-projects">Featured Projects</a> •
<a href="#active-systems">Active Systems</a> •
<a href="#proficiencies">Proficiencies</a> •
<a href="#architecture-deep-dives">Architecture</a> •
<a href="#operating-principles">Principles</a> •
<a href="#collaboration">Collaboration</a>
</p>

---

## Overview

I build systems at the intersection of:

**product direction → platform architecture → operational automation**

My focus is on systems that are:

- **Observable** — telemetry, traces, and audit trails built in
- **Reliable** — designed for degraded states and partial failures
- **Traceable** — every decision reconstructable from logs
- **Operationally clear** — runbooks, not runaway automation

I optimize for real operations, not demo environments.

**Current focus:** deterministic AI execution, reconciliation infrastructure, and governance-first automation.

## Strategic Snapshot

- Building platform systems that prioritize explainability and operational safety
- Designing automation that remains deterministic under production stress
- Integrating product delivery with governance, policy, and auditability from day one

## Why Teams Bring Me In

- When systems are growing fast but operational risk is rising
- When automation exists but reliability, traceability, or governance is weak
- When product, architecture, and execution need to align under one operating model

---

## Core Platform Systems

| System | Role | Status |
|------|------|--------|
| **AIAS** | AI workflow architecture — document ingestion, agent orchestration, human oversight | Active |
| **Requiem** | Unified AI control plane (kernel + policy + web UI) — governance, orchestration, traceability | Active |
| **Settler** | Reconciliation control plane — deterministic matching, audit trails, human review checkpoints | Active |

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

> Selected projects that best represent my architecture and operating model.

<sub>Tip: Start with <strong>Requiem + Settler</strong> for the clearest view of my governance-first systems approach.</sub>

| Project | What it does | Focus | Stack |
|------|------|------|------|
| **[Requiem](https://github.com/Hardonian/Requiem)** | Unified AI control plane — kernel, policy engine, web UI. Centralized governance for AI workflows with full traceability. | Governance, orchestration, traceability, reproducible execution | TypeScript, Node.js, React, PostgreSQL |
| **[Settler](https://github.com/Hardonian/Settler)** | Resend-style payment reconciliation API for developers. Deterministic matching engine with human review gates and full audit logs. | Deterministic matching, auditability, financial workflow traceability | Node.js, TypeScript, PostgreSQL, Prisma |
| **[ControlPlane](https://github.com/Hardonian/ControlPlane)** | Execution engine for agent-driven systems. Reliable automation at scale with idempotency, retries, and policy enforcement. | Reliable automation, idempotency, policy-guarded execution | TypeScript, Node.js, PostgreSQL |
| **[ReadyLayer](https://github.com/Hardonian/ReadyLayer)** | CI-integrated code governance — review, test, and document AI-generated code before merge. Quality gates for generated code. | Code governance, CI integration, AI code verification | TypeScript, GitHub Actions, Node.js |
| **[JobForge](https://github.com/Hardonian/JobForge)** | Postgres-native, language-agnostic job orchestrator. Idempotency keys, exponential backoff, RPC-first design. | Job orchestration, idempotency, retries, observability | Go, PostgreSQL, SQL |
| **[castor](https://github.com/Hardonian/castor)** | Podcast sponsor analytics + ROI attribution stack. Ingestion pipelines, normalization, reporting dashboards. | Data pipelines, attribution modeling, reporting systems | Python, PostgreSQL, Apache Airflow |
| **[truthcore](https://github.com/Hardonian/truthcore)** | Deterministic verification platform. Reproducible builds, anomaly detection, supply-chain verification. | Reproducibility, anomaly detection, verification | Rust, Go, WebAssembly |

**What this portfolio emphasizes:** systems that can be operated, audited, and evolved safely under real production constraints.

---

## Active Systems (Extended Portfolio)

> Additional production systems in active development — each addressing a specific operational domain.

| System | Domain | Description | Key Tech |
|------|--------|-------------|----------|
| **[AI-Automated-Systems (AIAS)](https://github.com/Hardonian/AI-Automated-Systems_AIAS)** | AI Workflow Architecture | Document ingestion → agent orchestration → human oversight → operational output. Multi-agent pipelines with policy gates. | TypeScript, React, Node.js, PostgreSQL, LangGraph |
| **[EvidenceVault](https://github.com/Hardonian/EvidenceVault)** | Compliance & Audit | Immutable evidence store with cryptographic verification. WORM storage, Merkle proofs, regulatory export packs. | Go, PostgreSQL, WASM, OpenTelemetry |
| **[MissionLedger](https://github.com/Hardonian/MissionLedger)** | Operational Ledger | Double-entry ledger for operational events. Idempotent writes, temporal queries, audit-grade immutability. | Rust, PostgreSQL, SQLx |
| **[Nautilus](https://github.com/Hardonian/Nautilus)** | Operator Substrate | Kubernetes-native operator framework. Reconciliation loops, CRD management, multi-cluster governance. | Go, controller-runtime, Helm, CUE |
| **[TokenGoblin](https://github.com/Hardonian/TokenGoblin)** | Token Efficiency | LLM token measurement & optimization. Prompt compression, routing, cost attribution per tenant/feature. | Go, React, TypeScript, ClickHouse |
| **[FindingNemos](https://github.com/Hardonian/FindingNemos)** | Reconciliation Intelligence | Transaction matching with ML-assisted rules. Deterministic core + human-in-the-loop exception handling. | Zig, TypeScript, PostgreSQL |
| **[MEL / MeshEdgeLayer](https://github.com/Hardonian/MeshEdgeLayer)** | Edge Coordination | Distributed coordination layer for edge workloads. Conflict-free replication, offline-first sync. | Rust, CRDTs, WebRTC, WASM |

---

## Proficiencies

| Area | Proficiency | Notes |
|------|------|-------|
| Platform architecture | Advanced | Multi-tenant SaaS, operator patterns, control planes |
| SaaS systems (multi-tenant) | Advanced | RLS, tenant isolation, billing integration |
| API/backend systems (Node/REST/Webhooks) | Advanced | Idempotency, versioning, observability |
| Frontend product systems (React/Next.js) | Advanced | CWV optimization, accessibility, design systems |
| Data systems (Postgres/Supabase/RLS) | Advanced | Partitioning, read replicas, row-level security |
| AI workflow automation | Advanced | Governance layers, deterministic execution, human gates |
| CI/CD and delivery engineering | Advanced | GitHub Actions, ArgoCD, verification matrices |
| Security boundaries (auth, tenant isolation) | Advanced | OAuth2/OIDC, mTLS, capability-based auth |
| Performance and web quality (CWV) | Strong | LCP/CLS/INP optimization, bundle analysis |
| Accessibility (WCAG-aware delivery) | Strong | Semantic HTML, ARIA, focus management |

## Outcomes I Optimize For

- Faster delivery **without** sacrificing governance
- Deterministic execution **over** brittle automation
- Auditable operations with clear failure paths
- Practical architecture that supports product velocity

## Production-Grade Defaults

- Explicit policy + guardrail layers before autonomy
- Observability designed in (not retrofitted)
- Reproducible deployment and verification workflows
- Human escalation paths for high-risk decisions

---

## Architecture Deep Dives

### Settler Architecture

```mermaid
flowchart LR

    Sources["Data Sources<br/>Bank • ERP • Payment APIs"]
    Ingestion["Ingestion<br/>ETL • Webhooks • Normalization"]
    Matcher["Matching Engine<br/>Deterministic Rules + ML Assist"]
    Review["Human Review<br/>Exception Queue • Policy Gates"]
    Ledger["Verified Ledger<br/>Immutable • Auditable"]
    Audit["Audit Reporting<br/>Traces • Exports • Compliance"]

    Sources --> Ingestion
    Ingestion --> Matcher
    Matcher --> Review
    Review --> Ledger
    Ledger --> Audit
```

**Goals:**

- Deterministic matching logic with configurable rules
- Full auditability — every match traceable to source
- Traceable financial workflows with human checkpoints
- Extensible for new payment rails and data formats

### Requiem Architecture

```mermaid
flowchart TB

    Inputs["Inputs<br/>Events • Agents • Tasks • Schedules"]
    Kernel["Execution Kernel<br/>DAG Runtime • Idempotency • Retries"]
    Trace["Trace Engine<br/>Spans • Decisions • Artifacts"]
    Policy["Policy Layer<br/>Guardrails • Approvals • Budgets"]
    State["System State<br/>PostgreSQL • Event Store"]

    Inputs --> Kernel
    Kernel --> Trace
    Kernel --> Policy
    Trace --> State
    Policy --> State
```

**Focus areas:**

- Deterministic workflows with replay capability
- Execution traceability — every decision logged
- Governance layers: policies, budgets, approval gates
- Reproducible automation via event sourcing

### AIAS Architecture

```mermaid
flowchart LR

    Docs["Documents<br/>Web Data • APIs • Feeds"]
    Agents["AI Agents<br/>Specialized • Composable"]
    Review["Human Oversight<br/>Review • Approve • Redirect"]
    Output["Operational Systems<br/>APIs • DBs • Queues"]

    Docs --> Agents
    Agents --> Review
    Review --> Output
```

**Goal:** AI systems that remain **observable, governable, and operationally safe**.

---

## Platform Stack

```mermaid
flowchart LR

    UI["UI<br/>React • Next.js • Tailwind • shadcn/ui"]
    API["API<br/>Node.js • REST • Webhooks • tRPC"]
    Middleware["Middleware<br/>Auth • SDKs • Rate Limiting"]
    Data["Data<br/>PostgreSQL • Supabase • RLS • ClickHouse"]
    Infra["Infrastructure<br/>GitHub Actions • ArgoCD • Terraform"]
    Obs["Observability<br/>OpenTelemetry • Logs • Verification"]

    UI --> API
    API --> Middleware
    Middleware --> Data
    API --> Infra
    Infra --> Obs
```

---

## Technical Surface

**Primary:** TypeScript/JavaScript, Python, SQL, Go, HTML/CSS, Bash  
**Systems familiarity:** Rust, C++, Zig  
**Execution environments:** WebAssembly (WASM), Node.js, Deno, Bun  
**Infrastructure:** Kubernetes, PostgreSQL, Redis, ClickHouse, Supabase  
**AI/ML:** LangGraph, OpenTelemetry, custom agent runtimes

---

## Operating Principles

- **Reduce complexity before automating it** — automation codifies; don't codify chaos
- **Prefer observable systems over opaque abstractions** — if you can't trace it, you can't trust it
- **Design for degraded states** — partial failure is the normal case
- **Keep humans in the loop where judgment matters** — approval gates, not just notifications
- **Build systems that survive real-world conditions** — network partitions, clock skew, bad inputs

If a system cannot be debugged, explained, or recovered, it probably is not ready to ship.

## Collaboration

If you're building platform-heavy products or AI-enabled operational systems, I'm always open to exchanging architecture notes and practical implementation patterns.

## Contact

- GitHub discussions/issues on relevant repos
- Connect here: [github.com/Hardonian](https://github.com/Hardonian)

## Profile Changelog

- **v1:** clarity and structure upgrade
- **v2:** narrative + credibility polish
- **v3:** production-grade framing, scanability, and strategic positioning
- **v4:** conversion optimization, decision-context framing, and collaboration pathing
- **v5:** extended active systems, deeper repo details, architecture diagrams, technical surface expansion

---

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0ea5e9,100:7c3aed&height=90&section=footer"/>
</p>
