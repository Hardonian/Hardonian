<h1 align="center">Scott Hardie</h1>

<h3 align="center">
Solutions Architect • AI Systems Operator • Platform Builder
</h3>

<p align="center">
Solutions Architect @ <strong>McGraw Hill</strong><br>
Ontario, Canada • SaaS Architecture • Local-First AI Infrastructure • Revenue Automation
</p>

<p align="center">
  <a href="https://github.com/Hardonian">
    <img src="https://github-readme-stats.vercel.app/api?username=Hardonian&show_icons=true&count_private=true&hide_border=true&theme=radical" alt="GitHub Stats" height="180"/>
  </a>
  <a href="https://github.com/Hardonian">
    <img src="https://github-readme-streak-stats.herokuapp.com/?user=Hardonian&hide_border=true&theme=radical" alt="GitHub Streak" height="180"/>
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/System-Local--First-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Revenue-Stripe%20Integrated-blueviolet?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/AI-Ollama%20%2F%20ComfyUI-8A05FF?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Stack-Python%20%2F%20TS%20%2F%20SQL-3c873a?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Automation-systemd%20%2F%20Docker%20%2F%20n8n-orange?style=for-the-badge"/>
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

## Architecture Portfolio & Playbook

I also maintain a reusable architecture delivery kit under [architecture-playbook](/Hardonian/tree/main/architecture-playbook). It covers current-state assessment, target-state architecture, ADRs, migration planning, rollout risk, and executive briefs.

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
| [ai-lab-audit-api](https://github.com/Hardonian/ai-lab-audit-api) | Local-first AI-lab audit API with reports, metrics, and checkout integration | Live-ready | FastAPI, Python, Stripe |

### Webhook / Infra / Platform Tooling

| Repo | What It Does | Status | Stack |
|------|--------------|--------|-------|
| [webhook-witness](https://github.com/Hardonian/webhook-witness) | Capture, inspect, and replay webhook traffic | Deployed / phase 2 | Cloudflare Workers, D1 |
| [api-changelog-radar](https://github.com/Hardonian/api-changelog-radar) | API changelog monitoring scaffold | Proof-of-concept | Cloudflare Workers, D1 |
| [tfstate-drift-inspector](https://github.com/Hardonian/tfstate-drift-inspector) | Terraform drift scanning and alerting | Experimental | Python, Docker |
| [cloudflare-app-ops-dashboard](https://github.com/Hardonian/cloudflare-app-ops-dashboard) | Portfolio status board for Cloudflare services | Deployed | TypeScript, Workers |

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

## Live Operator-Managed Products

These are managed through the **AI Lab Command Center / Revenue OS** dashboard and listed here for visibility. This README stays scannable and secure: pricing, checkout, and purchase links live on each product subpage, not in the README itself.

| Product | Headline | Track / Buyer | Product Page | Notes |
|---------|----------|---------------|--------------|-------|
| Local AI Lab Audit | Find and fix the bottlenecks in your local AI lab. | Direct sale | [Product page](products/local-ai-lab-audit.md) | Audit-first |
| AI Command Center Setup | Local control plane template with managed checks. | Template / services | [Product page](products/ai-command-center-setup.md) | Flagship |
| APVA AI ROI Benchmark | Reliability-adjusted AI workflow ROI scoring. | Direct sale | [Product page](products/apva-roi-benchmark.md) | Benchmark |
| SaaS Repo Rescue Audit | Audit and fix auth, billing, RLS, webhooks, deployment. | Audit + sprint | [Product page](products/repo-rescue-saas-audit.md) | Repo buyer |
| Local Automation Retainer | Recurring automation and operator support. | Retainer | [Product page](products/automation-retainer.md) | Recurring revenue |
| ComfyUI Node Starter Kit | Starter scaffold for custom ComfyUI node packs. | Creator tooling | [Product page](products/comfyui-node-starter-kit.md) | Creator |
| ComfyUI Product Photo Kit | Repeatable local ecommerce product image workflow. | Commerce creator | [Product page](products/comfyui-product-photo-kit.md) | Commerce |
| ComfyUI Fashion Lookbook Kit | Fictional editorial lookbook workflow pack. | Fashion / editorial | [Product page](products/comfyui-fashion-lookbook-kit.md) | Editorial |
| ComfyUI Thumbnail Creator Kit | Local thumbnail generation workflow for creators. | Creator / channel | [Product page](products/comfyui-thumbnail-creator-kit.md) | Channel |
| ComfyUI Workflow Pack Shop | Productized private ComfyUI workflow packs. | Workflow buyer | [Product page](products/comfyui-workflow-packs.md) | Shop catalog |
| Floyo Workflow Radar | Workflow-pattern audit, setup, and monitoring. | Operator / founder | [Product page](products/floyo-workflow-radar.md) | Monitor |
| Settler FinOps Reconciliation Engine | Payment reconciliation with deterministic matching. | Enterprise finance | [Product page](products/settler-finops-platform.md) | Enterprise |
| TokenGoblin LLM Cost Optimizer | Token measurement, smart routing, cost optimization. | Enterprise AI | [Product page](products/tokengoblin-cost-optimizer.md) | Enterprise |
| AI Lab Applied Notebook Packs | Reproducible AI experiment packs. | Researcher / learner | [Product page](products/ai-lab-notebook-packs.md) | Subscription |
| AI Character Generator Kit | Fictional character workflow kit for storytelling. | Hobbyist / creator | [Product page](products/ai-character-generator-kit.md) | Creator |
| Prompt Engineering Laboratory | Lab-tested prompt templates and iteration workflow. | Operator / learner | [Product page](products/prompt-engineering-laboratory.md) | Learning |
| AI Video Storyboard Studio | Video storyboard assets and pacing guides. | Creator / studio | [Product page](products/ai-video-storyboard-studio.md) | Creator |
| AI Voice Clone Training Kit | Consent-based local voice training workflow kit. | Voice creator | [Product page](products/ai-voice-clone-training-kit.md) | Consent-first |
| Research Paper Visualizer | Academic paper visual summary workflow kit. | Researcher / student | [Product page](products/research-paper-visualizer.md) | Research |
| Defend-Your-AI Legal Kit | AI-use legal, privacy, and risk readiness kit. | Operator / org | [Product page](products/defend-your-ai-legal-kit.md) | Risk-first |

Each product links to a description subpage under [products/](/Hardonian/tree/main/products). Checkout and usage details are on those subpages, keeping this README scannable and professional.

## Verified Leverage

What is actually running, tested, and enforced in this environment:

| Layer | Verified State |
|-------|----------------|
| Checkout | ✅ Stripe checkout sessions, Canadian tax by province, EU VAT estimates, subscriptions, refunds, coupons, affiliate tracking |
| Compute | ✅ FastAPI job dispatch with real Ollama/ComfyUI runners, 10/10 tests passing |
| Storefront | ✅ Dynamic markdown→HTML product pages, legal routes, age-gate middleware |
| Command Center | ✅ Health aggregation, metering, backup status, service watchdog |
| Security | ✅ HSTS, CSP, rate limiting, audit logging, webhook signature verification, TrustedHostMiddleware |
| Backups | ✅ Daily compressed backups, 30-day retention, offsite sync script, SHA-256 integrity |
| CI/CD | ✅ Dependency Review passing on PRs, GitHub Actions enabled |
| Hardware | ✅ EPYC host, V100 16GB, P40 23GB, RTX 3060 12GB, Docker, NVIDIA CUDA |
| Automation | ✅ systemd user services, timers, Telegram alerts, smoke tests |

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

## Contact & Credentials

- **Location:** Toronto, Ontario, Canada
- **LinkedIn:** [scottrmhardie](https://www.linkedin.com/in/scottrmhardie/)
- **Email:** scottrmhardie@gmail.com
- **GitHub:** [@Hardonian](https://github.com/Hardonian)
- **Role:** Solutions Architect @ McGraw Hill
- **Experience:** 15+ years at McGraw Hill and Pearson
- **Focus:** Local-first AI infrastructure, revenue automation, SaaS architecture

### Credentials & Certifications

- **AWS Certified Solutions Architect** – Professional level
- **Cloudflare Developer Certification** – Edge runtime, Workers, D1
- **Terraform Associate** – Infrastructure as code, state management
- **GitHub Advanced Security** – Secret scanning, dependency review
- **Stripe Payments** – Checkout, tax, subscriptions, webhooks, refunds
- **Open WebUI / Ollama** – Production local inference operator
- **FastAPI / Pydantic** – Production API design, validation, security middleware
- **PostgreSQL / Redis / SQLite** – Multi-model data architecture
- **Docker / n8n / systemd** – Container ops, workflow automation, service hardening

---

## Background

- Solutions Architect at **McGraw Hill**
- 15+ years across **McGraw Hill** and **Pearson**
- Strong mix of technical architecture, commercial execution, and operator thinking
- Recent focus: building systems that connect internal tooling to revenue, not just demos

---

*If you want to collaborate, the best starting points are [Settler](https://github.com/Hardonian/Settler) and [ai-lab-command-center](https://github.com/Hardonian/ai-lab-command-center).*
