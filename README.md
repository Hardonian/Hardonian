<!-- ========================================================= -->
<!-- HERO -->
<!-- ========================================================= -->

<h1 align="center">Scott Hardie</h1>

<h3 align="center">
Technical Product Manager • Solutions Architect • Platform Systems
</h3>

<p align="center">
<em>Designing operational platforms where product thinking, architecture, and automation meet.</em>
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

I work on systems that sit at the intersection of:

**product direction → platform architecture → operational automation**

These systems often involve:

- distributed integrations  
- SaaS platforms  
- automation pipelines  
- reconciliation and operational tooling  

The goal is to build systems that remain:

- **observable**
- **reliable**
- **traceable**
- **operationally clear**

Many systems must function in **messy real-world environments**, not idealized demos.

---

# Core Platform Systems

Several projects explore different layers of operational infrastructure.

| System | Role |
|------|------|
| **AIAS** | AI workflow architecture |
| **Requiem** | deterministic execution kernel |
| **Settler** | reconciliation control plane |

---

# Platform Relationship

```mermaid
flowchart TB

classDef users fill:#f3f4f6,stroke:#6b7280,color:#111
classDef ai fill:#dbeafe,stroke:#3b82f6,color:#111
classDef kernel fill:#ede9fe,stroke:#7c3aed,color:#111
classDef control fill:#dcfce7,stroke:#22c55e,color:#111
classDef external fill:#fff7ed,stroke:#fb923c,color:#111

Users["Operators\nProduct Systems"]
AIAS["AIAS\nAI Workflow Architecture"]
Requiem["Requiem\nExecution Kernel"]
Settler["Settler\nReconciliation Control Plane"]
External["External Systems\nPayments • APIs • SaaS"]

Users --> AIAS
AIAS --> Requiem
Requiem --> Settler
Settler --> External

class Users users
class AIAS ai
class Requiem kernel
class Settler control
class External external
```

---

# Settler

**Reconciliation Control Plane**

Settler explores how reconciliation workflows can move from manual processes toward deterministic automation.

```mermaid
flowchart LR

classDef data fill:#e0f2fe,stroke:#0284c7
classDef process fill:#ede9fe,stroke:#7c3aed
classDef human fill:#fef3c7,stroke:#f59e0b
classDef ledger fill:#dcfce7,stroke:#16a34a
classDef audit fill:#fee2e2,stroke:#ef4444

Sources["Data Sources\nBank • ERP • Payment APIs"]
Ingestion["Ingestion\nETL • Webhooks"]
Matcher["Matching Engine"]
Review["Human Review"]
Ledger["Verified Ledger"]
Audit["Audit Reporting"]

Sources --> Ingestion
Ingestion --> Matcher
Matcher --> Review
Review --> Ledger
Ledger --> Audit

class Sources data
class Ingestion process
class Matcher process
class Review human
class Ledger ledger
class Audit audit
```

Goals:

- deterministic matching logic  
- auditability  
- traceable financial workflows  
- human-review checkpoints  

---

# Requiem

**Deterministic Execution Kernel**

Explores traceable execution systems for automation and orchestration.

```mermaid
flowchart TB

classDef input fill:#e0f2fe,stroke:#0284c7
classDef engine fill:#ede9fe,stroke:#7c3aed
classDef policy fill:#fef3c7,stroke:#f59e0b
classDef state fill:#dcfce7,stroke:#16a34a

Inputs["Inputs\nEvents • Agents • Tasks"]
Kernel["Execution Kernel"]
Trace["Trace Engine"]
Policy["Policy Layer"]
State["System State"]

Inputs --> Kernel
Kernel --> Trace
Kernel --> Policy
Trace --> State
Policy --> State

class Inputs input
class Kernel engine
class Trace engine
class Policy policy
class State state
```

Focus areas:

- deterministic workflows  
- execution traceability  
- governance layers  
- reproducible automation  

---

# AIAS

**Applied AI Workflow Architecture**

```mermaid
flowchart LR

classDef data fill:#e0f2fe,stroke:#0284c7
classDef ai fill:#ede9fe,stroke:#7c3aed
classDef human fill:#fef3c7,stroke:#f59e0b
classDef output fill:#dcfce7,stroke:#16a34a

Docs["Documents\nWeb Data"]
Agents["AI Agents"]
Review["Human Oversight"]
Output["Operational Systems"]

Docs --> Agents
Agents --> Review
Review --> Output

class Docs data
class Agents ai
class Review human
class Output output
```

Goal:

AI systems that remain **observable, governable, and operationally safe**.

---

# Platform Stack

```mermaid
flowchart LR

classDef ui fill:#dbeafe,stroke:#3b82f6
classDef api fill:#ede9fe,stroke:#7c3aed
classDef middleware fill:#fef3c7,stroke:#f59e0b
classDef data fill:#dcfce7,stroke:#16a34a
classDef infra fill:#fee2e2,stroke:#ef4444
classDef obs fill:#e0f2fe,stroke:#0284c7

UI["UI\nReact • Next.js • Tailwind"]
API["API\nNode.js • REST • Webhooks"]
Middleware["Middleware\nAuth • SDKs"]
Data["Data\nPostgres • Supabase • RLS"]
Infra["Infrastructure\nCI/CD"]
Obs["Observability\nLogs • Verification"]

UI --> API
API --> Middleware
Middleware --> Data
API --> Infra
Infra --> Obs

class UI ui
class API api
class Middleware middleware
class Data data
class Infra infra
class Obs obs
```

---

# Technical Surface

Primary languages:

- TypeScript / JavaScript  
- SQL  
- Python  
- Bash  

Systems familiarity:

- Rust  
- C++  

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

Operational reliability is treated as **part of product quality**.

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

If a system cannot be **debugged, explained, or recovered**, it probably is not ready to ship.

---

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0ea5e9,100:7c3aed&height=90&section=footer"/>
</p>