<!-- ========================================================= -->
<!-- HERO -->
<!-- ========================================================= -->

<h1 align="center">🚀 Scott Hardie</h1>

<h3 align="center">
Technical Product Manager • Solutions Architect • Platform & Automation Systems
</h3>

<p align="center">
<em>Designing and shipping reliable systems where product thinking, architecture, and operations intersect.</em>
</p>

<p align="center">
🏢 Solutions Architect @ <strong>McGraw Hill</strong><br>
🇨🇦 Canada • EdTech • SaaS Platforms • Ecommerce Systems
</p>

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Inter&size=20&pause=1200&center=true&vCenter=true&width=950&lines=Systems+thinking+with+execution;Architecture+%2B+product+delivery;Automation+that+survives+real+operations;Platforms%2C+integrations%2C+and+operational+tooling;Useful+%3E+clever.&cache_seconds=1800"/>
</p>

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0ea5e9,100:7c3aed&height=40&section=header&text=Platforms%20%7C%20Automation%20%7C%20Product%20Systems&fontSize=18&fontColor=ffffff"/>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Product-Systems-blueviolet"/>
<img src="https://img.shields.io/badge/Architecture-Platform-blue"/>
<img src="https://img.shields.io/badge/AI-Applied-green"/>
<img src="https://img.shields.io/badge/SaaS-Multi--Tenant-orange"/>
<img src="https://img.shields.io/badge/Frontend-React%20%2B%20Next.js-06b6d4"/>
<img src="https://img.shields.io/badge/Backend-Node.js%20%2F%20APIs-3c873a"/>
<img src="https://img.shields.io/badge/CI-GitHub%20Actions-orange"/>
</p>

<p align="center">
<img src="https://img.shields.io/badge/C%2B%2B-Systems%20Knowledge-00599C?logo=c%2B%2B"/>
<img src="https://img.shields.io/badge/Rust-Systems%20Knowledge-black?logo=rust"/>
<img src="https://img.shields.io/badge/TypeScript-Primary-3178C6?logo=typescript"/>
<img src="https://img.shields.io/badge/SDKs-Integration%20%26%20Design-6366f1"/>
</p>

---

# About

I’m **Scott Hardie**, a Solutions Architect at **McGraw Hill** working across:

- platform architecture  
- operational automation  
- applied AI systems  
- SaaS and ecommerce platforms  

My work sits at the intersection of:

**product direction → system architecture → shipped systems**

with emphasis on reliability, observability, and operational clarity.

Many systems I work on must function in **messy real-world environments**, not controlled demos.

---

# Core Platform Projects

## System Relationship Map

```mermaid
flowchart TB

AIAS["AIAS<br>AI Architecture Systems"]
Requiem["Requiem<br>Deterministic Execution Kernel"]
Settler["Settler<br>Reconciliation Control Plane"]

Users["Operators / Product Systems"]
External["External Systems<br>APIs • SaaS • Payments • Ecommerce"]

Users --> AIAS
AIAS --> Requiem
Requiem --> Settler
Settler --> External
```

---

# Settler Architecture (Reconciliation Control Plane)

```mermaid
flowchart LR

Sources["Data Sources<br>Bank • ERP • Payment APIs"]
Ingestion["Ingestion Layer<br>ETL • Webhooks"]
Matcher["Matching Engine<br>Deterministic Matching"]
Review["Human Review Layer"]
Ledger["Verified Ledger"]
Audit["Audit & Reporting"]

Sources --> Ingestion
Ingestion --> Matcher
Matcher --> Review
Review --> Ledger
Ledger --> Audit
```

Purpose:

A control plane exploring how reconciliation workflows can move from **manual accounting tasks to deterministic automation systems with traceability**.

---

# Requiem Architecture (Deterministic Kernel)

```mermaid
flowchart TB

Inputs["Inputs<br>Agents • Events • Tasks"]
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

Focus:

- deterministic execution
- system traceability
- agent orchestration
- governance and reproducibility

---

# AIAS Architecture (AI Workflow Layer)

```mermaid
flowchart LR

Docs["Documents / Web Data"]
Agents["AI Agents"]
Review["Human Review"]
Output["Operational Systems"]

Docs --> Agents
Agents --> Review
Review --> Output
```

Purpose:

AI workflows that remain **observable, governable, and operationally safe**.

---

# Platform Stack

Most systems span multiple layers of the stack.

```mermaid
flowchart LR

UI["UI Layer<br>React • Next.js • Tailwind"]
API["API Layer<br>Node.js • REST • Webhooks"]
Middleware["Middleware<br>Auth • Routing • SDK Integration"]
Data["Data Layer<br>Postgres • Supabase • RLS"]
Infra["Infrastructure<br>CI/CD • GitHub Actions"]
Observability["Observability<br>Logs • Verification"]

UI --> API
API --> Middleware
Middleware --> Data
API --> Infra
Infra --> Observability
```

---

# Technical Surface

## Languages

Primary working stack

- TypeScript / JavaScript
- SQL
- Python
- Bash

Systems familiarity

- Rust
- C++

Used selectively for systems-oriented experimentation.

---

# Capability Map

| Layer | Technologies |
|-----|-----|
| Frontend | React, Next.js, Tailwind |
| Backend | Node.js APIs, REST, Webhooks |
| Data | Postgres, Supabase, RLS |
| Integration | OAuth, SDKs, SaaS APIs |
| Automation | AI Agents, Workflow Systems |
| DevOps | GitHub Actions, CI/CD |
| Security | Auth layers, tenant isolation |
| Performance | Core Web Vitals, SEO |
| Accessibility | WCAG aware design |
| Growth | CRO-informed UX |

---

# Backend & Platform Systems

Typical backend architecture includes:

- Node.js API services  
- REST APIs  
- webhook pipelines  
- event-driven automation  
- service integrations  

Data architecture commonly includes:

- Postgres  
- Supabase  
- Row-Level Security  
- multi-tenant boundaries  
- migration discipline  

Focus areas include **traceability, reliability, and operational clarity**.

---

# Frontend & Product Surface

User-facing systems typically use:

- React  
- Next.js  
- Tailwind CSS  

Design priorities:

- truthful system states  
- degraded-state UX  
- accessibility-first thinking  
- performance-aware UI  
- component-driven architecture  

---

# APIs, Middleware & Integrations

Typical architecture includes:

- API route design  
- middleware layers  
- authentication boundaries  
- SDK integrations  
- third-party platform integrations  

Common integrations include:

- SaaS APIs  
- OAuth systems  
- webhook pipelines  
- ecommerce platforms  
- payment providers  

---

# Security & System Integrity

Operational systems require careful boundaries.

Typical concerns include:

- authentication and authorization  
- tenant isolation  
- webhook verification  
- secrets management  
- operational auditability  

The goal is systems that **fail safely and predictably**.

---

# Testing, CI & Delivery

Delivery workflows typically include:

- GitHub Actions  
- CI verification pipelines  
- regression testing  
- smoke tests  
- reproducible builds  
- safe deployment practices  

Operational reliability is treated as **part of product quality**.

---

# Performance, SEO & Product Optimization

Public-facing systems require attention to:

- SEO architecture  
- Core Web Vitals  
- crawler compatibility  
- accessibility (WCAG)

For SaaS and ecommerce platforms:

- CRO-informed UX  
- funnel friction reduction  
- performance-aware UI architecture  

---

# Additional Projects

- **Hardonia** — ecommerce automation experiments  
- **eCommerce Manager** — AI-assisted ecommerce operations  
- **AI-Agent-Portfolio** — applied AI workflows  
- **hardonia-intel-scraper** — research automation  

---

# Operating Principles

Design heuristics I return to frequently:

- reduce complexity before automating it  
- prefer observable systems over opaque abstractions  
- design for degraded states  
- keep humans in the loop where judgment matters  
- optimize for systems that survive real-world conditions  

If a system cannot be **explained, debugged, or recovered**, it probably is not ready to ship.

---

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0ea5e9,100:7c3aed&height=90&section=footer"/>
</p>

<p align="center">
<em>
Reduce friction ✨  
Automate responsibly 🤖  
Keep humans in control 🧠
</em>
</p>