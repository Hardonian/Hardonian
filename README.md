<h1 align="center">Scott Hardie</h1>

<h3 align="center">
Solutions Architect • AI Systems Operator • Platform Builder
</h3>

<p align="center">
Solutions Architect @ <strong>McGraw Hill</strong><br>
Ontario, Canada • SaaS Architecture • Local-First AI Infrastructure • Revenue Automation
</p>

<p align="center">
<img src="https://img.shields.io/badge/Role-Solution%20Architect-blueviolet"/>
<img src="https://img.shields.io/badge/Focus-Operator%20Systems-0ea5e9"/>
<img src="https://img.shields.io/badge/Backend-Python%20%2F%20FastAPI-3c873a"/>
<img src="https://img.shields.io/badge/Web-Next.js%20%2F%20TypeScript-111827"/>
<img src="https://img.shields.io/badge/Data-PostgreSQL%20%2F%20Redis%20%2F%20SQLite-2563eb"/>
<img src="https://img.shields.io/badge/AI-Ollama%20%2F%20ComfyUI-8A05FF"/>
<img src="https://img.shields.io/badge/Billing-Stripe%20Payment%20Links-orange"/>
</p>

<p align="center">
<a href="#what-i-build">What I Build</a> •
<a href="#live-operator-managed-products">Live Products</a> •
<a href="#repositories">Repositories</a> •
<a href="#architecture-maps">Architecture Maps</a> •
<a href="#proficiencies">Proficiencies</a>
</p>

---

## What I Build

I build systems that sit between architecture and operations:
- local-first AI control planes
- multi-tenant SaaS and backend services
- workflow and observability tooling
- monetization infrastructure with checkout, landing pages, and deliverables
- operator dashboards that make internal systems sellable and supportable

Recent work has focused on turning private AI-lab tooling into a real operating surface: health, automation, product admin, checkout wiring, packaging, and proof-first delivery.

---

## Live Operator-Managed Products

These are admin-managed through the **AI Lab Command Center / Revenue OS** dashboard and now include verified live Stripe checkout links. High-ticket services are listed first so visitors see the clearest purchase paths before lower-cost kits.

|| Product | Offer | Price | Buy (Stripe) | Gumroad ||
||---------|-------|-------|--------------|--------||
|| Local Automation Retainer | Recurring local automation and operator support for teams with messy manual workflows. | $750-$2500/mo | [Buy](https://buy.stripe.com/8x2fZg0Ra6hS34C6atb3q0r) | — ||
|| SaaS Repo Rescue Audit | Auth, billing, RLS, webhook, and deployment audit for SaaS repos that need to stop pretending. | $499 audit / $1500 fix sprint | [Buy](https://buy.stripe.com/00wfZgfM4bCc9t0buNb3q0q) | — ||
|| Local AI Lab Audit | Private AI lab / workstation audit with remediation plan and optional implementation day. | $499 fixed / $997 with implementation day | [Buy](https://buy.stripe.com/7sYaEW9nG6hSdJggP7b3q0i) | — ||
|| AI Command Center Setup | Private AI workstation control plane template with optional managed checks or done-for-you setup. | $297 lifetime template / $29-mo managed checks / $997 done-for-you | [Buy](https://buy.stripe.com/9B68wO57qbCc7kSeGZb3q0j) | — ||
|| APVA AI ROI Benchmark | Reliability-adjusted AI workflow ROI scoring for teams validating automation investments. | $199 self-serve / $799 team benchmark | [Buy](https://buy.stripe.com/aFa28qeI08q0dJggP7b3q0k) | — ||
|| Floyo Workflow Radar | Workflow-pattern audit, setup, and monitoring to find repeatable automation wins. | $149 pattern audit / $499 setup / $49-mo monitor | [Buy](https://buy.stripe.com/9B66oG9nGdKk8oW42lb3q0y) | — ||
|| AI Character Generator Kit | Fictional character generation prompt/workflow kit. | $49 one-time | [Buy](https://buy.stripe.com/3cI8wO1Veay8fRo6atb3q0s) | — ||
|| AI Video Storyboard Studio | Storyboard planning assets for AI video workflows. | $79 one-time | [Buy](https://buy.stripe.com/9B65kCgQ8eOodJg6atb3q0u) | — ||
|| AI Voice Clone Training Kit | Training kit for safe, consent-based voice workflow setup. | $89 one-time | [Buy](https://buy.stripe.com/bJeeVc7fy35GgVs6atb3q0v) | — ||
|| ComfyUI Fashion Lookbook Kit | Fictional editorial lookbook workflow pack for private/local creative workflows. | $69 creator pack / $149 agency pack | [Buy](https://buy.stripe.com/dRm4gy6bu5dO48G7exb3q0o) | [Gumroad](https://scottrmhardie.gumroad.com/l/ictrbg) ||
|| ComfyUI Node Starter Kit | Starter scaffold for sellable ComfyUI custom node packs. | $39 lite / $99 commercial | [Buy](https://buy.stripe.com/9B6cN41Veay8eNkfL3b3q0m) | [Gumroad](https://scottrmhardie.gumroad.com/l/cauzzx) ||
|| ComfyUI Product Photo Kit | Repeatable ecommerce product image workflow kit. | $59 niche pack / $129 studio pack | [Buy](https://buy.stripe.com/cNibJ057q21C34C7exb3q0n) | [Gumroad](https://scottrmhardie.gumroad.com/l/cqfiev) ||
|| ComfyUI Thumbnail Creator Kit | Thumbnail generation workflow product for creators and channels. | $49 solo creator / $119 channel pack | [Buy](https://buy.stripe.com/00wcN443m7lW8oWbuNb3q0p) | [Gumroad](https://scottrmhardie.gumroad.com/l/bsjqfm) ||
|| ComfyUI Workflow Pack Shop | Productized private ComfyUI workflow packs for repeatable image generation pipelines. | $29 starter / $79 pro / $149 niche pack / $499 custom pack | [Buy](https://buy.stripe.com/3cIbJ0bvO6hS0WuaqJb3q0l) | — ||
|| Defend-Your-AI Legal Kit | Practical AI-use legal/readiness kit for small operators. | $149 one-time | [Buy](https://buy.stripe.com/9B600i1Ve8q020y0Q9b3q0x) | — ||
|| Prompt Engineering Laboratory | Prompt testing and iteration lab kit. | $39 one-time | [Buy](https://buy.stripe.com/fZufZg9nGbCc0WufL3b3q0t) | — ||
|| Research Paper Visualizer | Research-paper visual summary workflow kit. | $59 one-time | [Buy](https://buy.stripe.com/8x228qczS0Xy48G2Yhb3q0w) | — ||

---

## Latest Pushed Architecture / Platform Work

The newest public pushes on the profile now also include enterprise architecture and platform reference work beyond the AI-lab product line.

| Repo | Focus | State |
|------|-------|-------|
| [commercial-architecture-simulator](https://github.com/Hardonian/commercial-architecture-simulator) | Elixir-based commercial architecture simulator scaffold / experimental modeling repo | Early scaffold |
| [identity-entitlement-broker](https://github.com/Hardonian/identity-entitlement-broker) | Enterprise identity + entitlement broker with SSO, SCIM, tenant isolation, and OPA policy decisions | Active reference build |
| [enterprise-integration-fabric](https://github.com/Hardonian/enterprise-integration-fabric) | Governed integration layer for LMS, SIS, CRM, billing, identity, analytics, and support workflows | Active reference architecture |
| [golden-path-platform](https://github.com/Hardonian/golden-path-platform) | Internal developer platform / golden-path architecture for standardized service delivery and policy gates | Active reference architecture |
| [JupyterNotebooks](https://github.com/Hardonian/JupyterNotebooks) | Interactive notebooks, AI experiments, and applied workflow/tooling research | Active applied R&D |

These repos round out the profile beyond product SKUs: they show architecture depth in identity, integration, platform engineering, workflow simulation, and applied AI experimentation.

---

## Flagship Build: AI Lab Command Center

**What it is:** a local-first FastAPI dashboard and operator console for private AI infrastructure.

**What it manages:**
- Ollama multi-lane routing
- ComfyUI health and workflow surfaces
- GPU / disk / service truth
- self-heal and smoke checks
- Revenue OS product queue
- public offer + checkout routing
- deliverable and readiness state

**Why it matters:** it turns an internal AI workstation into a real, operator-grade product surface.

Repo: [Hardonian/ai-lab-command-center](https://github.com/Hardonian/ai-lab-command-center)

---

## Repositories

### AI Infrastructure & Operator Systems

| Repo | What It Does | Status | Stack |
|------|--------------|--------|-------|
| [ai-lab-command-center](https://github.com/Hardonian/ai-lab-command-center) | Local AI operator dashboard with Revenue OS, health, routing, smoke, and product admin | Running locally / active | FastAPI, Python, JS |
| [apva-framework](https://github.com/Hardonian/apva-framework) | Benchmarking framework for reliability-adjusted AI workflow ROI | Active / productized | Python, FastAPI |
| [floyo](https://github.com/Hardonian/floyo) | Workflow-pattern intelligence and automation discovery platform | Active / productized | Next.js, FastAPI, Supabase |
| [Keys](https://github.com/Hardonian/Keys) | Backendless CLI for structured AI asset packs and local workflows | Active | TypeScript, Node.js |

### Payments, Reconciliation & SaaS Systems

| Repo | What It Does | Status | Stack |
|------|--------------|--------|-------|
| [Settler](https://github.com/Hardonian/Settler) | Reconciliation intelligence system for finance and operations workflows | Active development | TypeScript, Node.js, PostgreSQL |
| [TokenGoblin](https://github.com/Hardonian/TokenGoblin) | Token usage measurement and routing/cost tooling for LLM workloads | Active development | Go, React, ClickHouse |
| [ai-lab-audit-api](https://github.com/Hardonian/ai-lab-audit-api) | Local-first AI-lab audit API with reports and checkout flow | Live-ready | FastAPI, Python, Stripe |

### Webhook / Infra / Platform Tooling

| Repo | What It Does | Status | Stack |
|------|--------------|--------|-------|
| [webhook-witness](https://github.com/Hardonian/webhook-witness) | Capture, inspect, and replay webhook traffic | Deployed / phase 2 | Cloudflare Workers, D1 |
| [api-changelog-radar](https://github.com/Hardonian/api-changelog-radar) | API changelog monitoring scaffold | Proof-of-concept | Cloudflare Workers, D1 |
| [tfstate-drift-inspector](https://github.com/Hardonian/tfstate-drift-inspector) | Terraform drift scanning and alerting | Experimental | Python, Docker |
| [cloudflare-app-ops-dashboard](https://github.com/Hardonian/cloudflare-app-ops-dashboard) | Portfolio status board for Cloudflare services | Deployed | TypeScript, Workers |

---

## Architecture Maps

### Operator Revenue Surface

```mermaid
flowchart LR
    Repo["Source Repos"] --> RevenueOS["Revenue OS"]
    RevenueOS --> Landing["Landing Pages"]
    RevenueOS --> Checkout["Stripe Payment Links"]
    RevenueOS --> Deliverables["Tar Deliverables"]
    RevenueOS --> Dashboard["Admin Dashboard"]
    Dashboard --> Smoke["Verification / Smoke"]
```

### Private AI Lab Control Plane

```mermaid
flowchart LR
    UI["Dashboard UI"] --> API["FastAPI Control Plane"]
    API --> Ollama["Ollama Lanes"]
    API --> Comfy["ComfyUI"]
    API --> Jobs["Automation / Cron / systemd"]
    API --> Revenue["Revenue OS"]
    Revenue --> Products["Offers / Checkout / Deliverables"]
```

### Reconciliation / Financial Systems Pattern

```mermaid
flowchart LR
    Sources["Payment Sources"] --> Normalize["Normalization"]
    Normalize --> Match["Deterministic Matching"]
    Match --> Review["Human Review"]
    Review --> Ledger["Verified Ledger"]
    Ledger --> Audit["Audit Trail / Exports"]
```

---

## Proficiencies

| Area | Notes |
|------|-------|
| Solution architecture | SaaS workflows, integration design, stakeholder translation |
| AI platform operations | local-first inference, routing, workflow systems, operator control |
| Backend systems | FastAPI, Node.js, REST APIs, webhooks, service hardening |
| Revenue infrastructure | Stripe checkout, landing flows, packaging, monetization ops |
| Data systems | PostgreSQL, Redis, SQLite, Supabase, ClickHouse |
| Automation | cron, systemd, smoke testing, verification-led delivery |
| Frontend/admin surfaces | dashboard UX, product admin, operator consoles |

---

## Technical Surface

**Primary:** Python, TypeScript, SQL, Bash, JavaScript  
**Infrastructure:** FastAPI, Next.js, PostgreSQL, Redis, SQLite, Supabase, Cloudflare  
**AI:** Ollama, ComfyUI, local GPU workflows  
**Execution style:** verification-first, low-bloat, operator-grade

---

## Background

- Solutions Architect at **McGraw Hill**
- 15+ years across **McGraw Hill** and **Pearson**
- Strong mix of technical architecture, commercial execution, and operator thinking
- Recent focus: building systems that connect internal tooling to revenue, not just demos

---

*If you want to collaborate, the best starting points are [Settler](https://github.com/Hardonian/Settler) and [ai-lab-command-center](https://github.com/Hardonian/ai-lab-command-center).*