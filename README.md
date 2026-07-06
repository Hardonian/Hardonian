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
<a href="#repositories">Repositories</a> •
<a href="#architecture-maps">Architecture Maps</a> •
<a href="#live-operator-managed-products">Live Products</a> •
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
Recent work has focused on turning private AI-lab tooling into a real operating surface: health, automation, product admin, checkout wiring, packaging, and proof-first delivery.

---

## Latest Pushed Architecture / Platform Work

The newest public pushes on the profile now also include enterprise architecture and platform reference work beyond the AI-lab product line.

| Repo | Focus | State |
|------|-------|-------|
| [commercial-architecture-simulator](https://github.com/Hardonian/commercial-architecture-simulator) | Elixir-based commercial architecture simulator / experimental modeling | Early scaffold |
| [identity-entitlement-broker](https://github.com/Hardonian/identity-entitlement-broker) | Enterprise identity + entitlement broker with SSO, SCIM, tenant isolation, and OPA policy decisions | Active reference build |
| [enterprise-integration-fabric](https://github.com/Hardonian/enterprise-integration-fabric) | Governed integration layer for LMS, SIS, CRM, billing, identity, analytics, and support workflows | Active reference architecture |
| [golden-path-platform](https://github.com/Hardonian/golden-path-platform) | Internal developer platform / golden-path architecture for standardized service delivery and policy gates | Active reference architecture |
| [JupyterNotebooks](https://github.com/Hardonian/JupyterNotebooks) | Interactive notebooks, AI experiments, and applied workflow/tooling research | Active applied R&D |

These repos round out the profile beyond product SKUs: they show architecture depth in identity, integration, platform engineering, workflow simulation, and applied AI experimentation.

---

## Architecture Portfolio & Playbook

I also maintain a reusable architecture delivery kit under [architecture-playbook](/Hardonian/tree/main/architecture-playbook). It covers current-state assessment, target-state architecture, ADRs, migration planning, rollout risk, and executive briefs.

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

## Live Operator-Managed Products

These are managed through the **AI Lab Command Center / Revenue OS** dashboard and are listed below for visibility. To keep the profile clean and secure, this README shows offer summaries only; checkout links live on each product page, not here.

| Product | Headline | Price | Product Page | Notes |
|---------|----------|-------|--------------|-------|
| Local AI Lab Audit | Find and fix the hidden bottlenecks in your local AI lab in one day. | $499 fixed / $997 with implementation day | [Product page](products/local-ai-lab-audit.md) | Audit-first entry point |
| AI Command Center Setup | Local control plane template with optional managed checks or done-for-you setup. | $297 lifetime template / $29-mo managed checks / $997 done-for-you | [Product page](products/ai-command-center-setup.md) | |
| APVA AI ROI Benchmark | Reliability-adjusted AI workflow ROI scoring for automation investments. | $199 self-serve / $799 team benchmark | [Product page](products/apva-roi-benchmark.md) | |
| SaaS Repo Rescue Audit | Audit and fix auth, billing, RLS, webhooks, and deployment gaps in SaaS repos. | $499 audit / $1500 fix sprint | [Product page](products/repo-rescue-saas-audit.md) | |
| Local Automation Retainer | Recurring automation and operator support for messy manual workflows. | $750-$2500/mo | [Product page](products/automation-retainer.md) | Retainer |
| ComfyUI Node Starter Kit | Sellable starter scaffold for custom ComfyUI node packs. | $39 lite / $99 commercial | [Product page](products/comfyui-node-starter-kit.md) | Gumroad also |
| ComfyUI Product Photo Kit | Repeatable local ecommerce product image workflow kit. | $59 niche pack / $129 studio pack | [Product page](products/comfyui-product-photo-kit.md) | Gumroad also |
| ComfyUI Fashion Lookbook Kit | Fictional editorial lookbook workflow pack. | $69 creator pack / $149 agency pack | [Product page](products/comfyui-fashion-lookbook-kit.md) | Gumroad also |
| ComfyUI Thumbnail Creator Kit | Local thumbnail generation workflow for creators and channels. | $49 solo creator / $119 channel pack | [Product page](products/comfyui-thumbnail-creator-kit.md) | Gumroad also |
| ComfyUI Workflow Pack Shop | Productized private ComfyUI workflow packs. | $29 starter / $79 pro / $149 niche pack / $499 custom pack | [Product page](products/comfyui-workflow-packs.md) | |
| Floyo Workflow Radar | Workflow-pattern audit, setup, and monitoring. | $149 pattern audit / $499 setup / $49-mo monitor | [Product page](products/floyo-workflow-radar.md) | |
| Settler FinOps Reconciliation Engine | Payment reconciliation with deterministic matching and audit trails. | $2,500 self-serve / $10,000 enterprise setup / $500/mo managed | [Product page](products/settler-finops-platform.md) | Enterprise |
| TokenGoblin LLM Cost Optimizer | Token usage measurement, smart routing, and cost optimization. | $1,499 self-serve / $5,000 enterprise / $299/mo managed | [Product page](products/tokengoblin-cost-optimizer.md) | Enterprise |
| AI Lab Applied Notebook Packs | Reproducible AI experiment packs. | $79 per pack / $299 bundle / $99/mo subscription | [Product page](products/ai-lab-notebook-packs.md) | |
| AI Character Generator Kit | Fictional character workflow kit for storytelling and RPGs. | $49 one-time | [Product page](products/ai-character-generator-kit.md) | |
| Prompt Engineering Laboratory | Lab-tested prompt templates and iteration workflow. | $39 one-time | [Product page](products/prompt-engineering-laboratory.md) | |
| AI Video Storyboard Studio | Video storyboard assets and pacing guides. | $79 one-time | [Product page](products/ai-video-storyboard-studio.md) | |
| AI Voice Clone Training Kit | Consent-based local voice training workflow kit. | $89 one-time | [Product page](products/ai-voice-clone-training-kit.md) | |
| Research Paper Visualizer | Academic paper visual summary workflow kit. | $59 one-time | [Product page](products/research-paper-visualizer.md) | |
| Defend-Your-AI Legal Kit | AI-use legal, privacy, and risk readiness kit. | $149 one-time | [Product page](products/defend-your-ai-legal-kit.md) | |

Each product links to a description subpage under [products/](/Hardonian/tree/main/products). Buy/checkout links and usage details are on those subpages, keeping this README scannable and professional.

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
