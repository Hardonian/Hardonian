<div align="center">

<img src="assets/hardonia-system-map.svg" alt="Hardonia system map: observe, control, execute, prove, and reconcile" width="100%" />

# HARDONIA

### Local compute. Deterministic control. Verifiable outcomes.

**Scott Hardie** · Solutions Architect · AI Systems Builder · Toronto, Canada

[Explore the systems](#flagship-systems) · [Read the architecture](#the-platform) · [View the storefront](https://www.aiautomatedsystems.ca) · [Connect](https://www.linkedin.com/in/scottrmhardie/)

<br />

`LOCAL-FIRST AI` · `CONTROL PLANES` · `DETERMINISTIC BACKENDS` · `FINOPS` · `VERIFICATION`

</div>

---

## Built for the moment after the demo

AI demos are easy. Production systems must survive retries, partial failure, hostile inputs, runaway spend, model drift, and an auditor asking exactly what happened.

Hardonia is a working portfolio of control planes, runtimes, security boundaries, and commercial systems designed around one idea:

> **Intelligence can be probabilistic. Infrastructure cannot.**

| **Observe** | **Control** | **Prove** |
| :--- | :--- | :--- |
| Capture agent, model, tool, cost, and transaction events. | Route workloads, enforce policy, isolate tenants, and recover safely. | Replay decisions, verify state, reconcile money, and export evidence. |

<p align="center">
  <a href="#start-here"><kbd>Start here</kbd></a>&nbsp;&nbsp;
  <a href="#the-platform"><kbd>Platform</kbd></a>&nbsp;&nbsp;
  <a href="#flagship-systems"><kbd>Flagships</kbd></a>&nbsp;&nbsp;
  <a href="#engineering-vault"><kbd>All projects</kbd></a>&nbsp;&nbsp;
  <a href="#productized-systems"><kbd>Products</kbd></a>&nbsp;&nbsp;
  <a href="#lets-build"><kbd>Contact</kbd></a>
</p>

---

## Start here

Six systems tell the story fastest.

| System | The hard problem | What it does |
| --- | --- | --- |
| **[AgentPCAP](https://github.com/Hardonian/AgentPCAP)** | Agents fail across invisible protocol boundaries. | Captures A2A, MCP, model, and tool traffic into one replayable timeline. |
| **[mcpwall](https://github.com/Hardonian/mcpwall)** | Tool-capable models need an enforceable security perimeter. | Applies local, fail-closed policy and signed approval gates to MCP execution. |
| **[ModelForge](https://github.com/Hardonian/ModelForge)** | Model deployment is still trial-and-OOM. | Compiles model, VRAM, quantization, batch, and latency constraints into a deployment plan. |
| **[nlsqlc](https://github.com/Hardonian/nlsqlc)** | Natural-language database access can leak tenant data. | Converts requests to a deterministic Query IR with fail-closed tenant isolation. |
| **[Settler](https://github.com/Hardonian/Settler)** | Financial truth gets fragmented across gateways and exports. | Reconciles transaction streams into hash-linked, audit-ready evidence. |
| **[continuityos](https://github.com/Hardonian/continuityos)** | Critical operations need more than a disaster-recovery PDF. | Turns continuity policy into executable, testable resilience contracts. |

---

## The platform

Hardonia spans the complete path from physical compute to verified commercial outcome.

```mermaid
flowchart TB
    L5["05 · FINANCIAL PROOF<br/>Settler · webhook-witness · immutable revenue ledger"]
    L4["04 · TRUST & RESILIENCE<br/>veridag · mcpwall · continuityos · ReadyLayer"]
    L3["03 · AGENT CONTROL<br/>AgentMesh · AgentPCAP · JobForge · MissionLedger"]
    L2["02 · COMPUTE COMPILATION<br/>ModelForge · nlsqlc · SawyerCore"]
    L1["01 · SOVEREIGN COMPUTE<br/>V100 16 GB · P40 24 GB · RTX 3060 12 GB"]

    L1 --> L2 --> L3 --> L4 --> L5
```

<div align="center">

![System health](https://img.shields.io/badge/SYSTEMS-10%2F10_NOMINAL-0f766e?style=flat-square)
![GPU lanes](https://img.shields.io/badge/GPU_LANES-3_ACTIVE-0891b2?style=flat-square)
![Models](https://img.shields.io/badge/MODELS-13_LOADED-7c3aed?style=flat-square)
![Products](https://img.shields.io/badge/PRODUCTS-28_READY-ea580c?style=flat-square)
![Profile CI](https://github.com/Hardonian/Hardonian/actions/workflows/profile-ci.yml/badge.svg)

</div>

<details>
<summary><strong>Open the live hardware and operating envelope</strong></summary>

<br />

| Lane | Hardware | Workload | Operating target |
| --- | --- | --- | --- |
| **Alpha · Throughput** | NVIDIA Tesla V100 · 16 GB HBM2 | Batch inference, embeddings, code generation, evaluation | `<45 ms` TTFT target |
| **Beta · Context** | NVIDIA Tesla P40 · 24 GB GDDR5 | Long-context reasoning, larger quantized models, MoE workloads | `<120 ms` TTFT target |
| **Gamma · Latency** | NVIDIA RTX 3060 · 12 GB GDDR6 | Interactive inference, agent routing, SDXL / Flux | `<25 ms` TTFT target |
| **Router mesh** | Local Linux services · Ollama-compatible API | Health probing, batching, fallback, thermal and memory supervision | `99.98%` uptime target |

The current operator layer supervises ten core services, three local GPU lanes, model routing, agent traffic capture, image workflows, policy enforcement, reconciliation, and the commercial storefront. Public health is treated as operational telemetry—not proof of revenue. Revenue claims require provider-correlated payment evidence.

</details>

---

## Flagship systems

### Control, security, and trust

| | |
| --- | --- |
| **[mcpwall](https://github.com/Hardonian/mcpwall) · Rust**<br />A zero-cloud security firewall for MCP servers. Stdio interception, inspectable TOML policy, cryptographic approval tokens, and fail-closed defaults. | **[veridag](https://github.com/Hardonian/veridag) · Rust + Quint**<br />A formally specified trust fabric for agents and edge swarms using a distributed DAG, QUIC, TLS 1.3, and embedded storage. |
| **[AgentPCAP](https://github.com/Hardonian/AgentPCAP) · Python**<br />Wire-level observability for agentic systems. Capture, normalize, inspect, and replay cross-protocol execution without vendor instrumentation. | **[AgentMesh](https://github.com/Hardonian/AgentMesh) · Go**<br />An open control plane for A2A and MCP agents: identity, policy, routing, reliability, circuit breaking, and progressive delivery. |

### Compute, data, and money

| | |
| --- | --- |
| **[ModelForge](https://github.com/Hardonian/ModelForge) · Python**<br />A compute compiler that resolves model metadata, VRAM limits, quantization, latency targets, and batch bounds before deployment. | **[nlsqlc](https://github.com/Hardonian/nlsqlc) · Rust**<br />A deterministic multi-tenant Query IR compiler with five SQL dialects, fail-closed isolation, and a benchmarked core above 62k QPS. |
| **[Settler](https://github.com/Hardonian/Settler) · TigerBeetle + Next.js**<br />Reconciliation intelligence for payment, banking, and inventory events with deterministic matching and hash-linked audit evidence. | **[TokenGoblin](https://github.com/Hardonian/TokenGoblin) · Go + ClickHouse**<br />Real-time token-cost telemetry, budget enforcement, and intelligent model routing for production AI workloads. |

### Execution and continuity

| | |
| --- | --- |
| **[JobForge](https://github.com/Hardonian/JobForge) · PostgreSQL**<br />Idempotent jobs, exponential backoff, and row-level execution boundaries without adding a separate queueing stack. | **[continuityos](https://github.com/Hardonian/continuityos) · Go + OPA**<br />Resilience-as-Code for critical supply chains, infrastructure, and cyber-physical operations. |
| **[Reach](https://github.com/Hardonian/Reach) · Rust**<br />A deterministic execution runtime with transcript replay and cryptographic evidence contracts. | **[ReadyLayer](https://github.com/Hardonian/ReadyLayer) · TypeScript**<br />Software-delivery governance with automated policy checks, provenance, and portable evidence export. |

---

## How the systems fit together

```text
  SIGNAL                 DECISION                 EXECUTION                PROOF
  ──────                 ────────                 ─────────                ─────
  AgentPCAP  ───────►    AgentMesh   ─────────►   JobForge   ─────────►   truthcore
  Telemetry              mcpwall                  Reach                    veridag
  Cost events            ModelForge               Local inference          Settler
       ▲                                                                      │
       └────────────────────── measurable feedback loop ◄─────────────────────┘
```

1. **Observe the real system.** Capture traffic, latency, spend, tool calls, and business events.
2. **Make policy explicit.** Compile constraints before allowing models or agents to act.
3. **Execute inside boundaries.** Use idempotency, tenant isolation, signed artifacts, and controlled fallback.
4. **Produce evidence.** Every meaningful run should leave enough context to inspect, replay, and reconcile.
5. **Feed reality back in.** Operational and commercial results—not demos—drive the next architecture decision.

---

## Engineering vault

The portfolio covers AI infrastructure, enterprise reliability, financial systems, simulation, commerce, and applied tooling. The short list above is curated; the complete map lives here.

<details>
<summary><strong>AI systems, agent control planes, and inference runtimes</strong></summary>

- **[AgentPCAP](https://github.com/Hardonian/AgentPCAP)** `[Python · CLI]` — Protocol capture and deterministic replay for AI agents.
- **[AgentMesh](https://github.com/Hardonian/AgentMesh)** `[Go · Distributed]` — Identity, policy, routing, reliability, and progressive delivery for A2A and MCP.
- **[ModelForge](https://github.com/Hardonian/ModelForge)** `[Python · AI]` — Constraint-driven model deployment planning.
- **[mcpwall](https://github.com/Hardonian/mcpwall)** `[Rust · Security]` — Local-first MCP firewall and audit proxy.
- **[veridag](https://github.com/Hardonian/veridag)** `[Rust · Quint]` — Formally specified distributed trust DAG.
- **[nlsqlc](https://github.com/Hardonian/nlsqlc)** `[Rust · Compiler]` — Multi-tenant natural-language Query IR compiler.
- **[SawyerCore](https://github.com/Hardonian/SawyerCore)** `[Node · Python]` — Deterministic edge-AI runtime and simulation engine.
- **[llm-inference-api](https://github.com/Hardonian/llm-inference-api)** `[FastAPI]` — OpenAI-compatible local inference gateway.
- **[ollama-router](https://github.com/Hardonian/ollama-router)** `[Python · Daemon]` — Multi-lane model routing, health checks, and fallback.
- **[comfyui-api](https://github.com/Hardonian/comfyui-api)** `[Cloudflare · TypeScript]` — Headless ComfyUI automation and queue management.
- **[Nautilus](https://github.com/Hardonian/Nautilus)** `[Docker · Infrastructure]` — Containerized operational AI infrastructure.
- **[Keys](https://github.com/Hardonian/Keys)** `[TypeScript]` — Auditable mission control for constrained agents.
- **[ControlPlane](https://github.com/Hardonian/ControlPlane)** `[Python · Systems]` — Service supervision and operator architecture.
- **[AI-Agent-Portfolio](https://github.com/Hardonian/AI-Agent-Portfolio)** `[Python · Agents]` — Agent patterns, tool boundaries, and evaluations.
- **[JupyterNotebooks](https://github.com/Hardonian/JupyterNotebooks)** `[Jupyter · PyTorch]` — Quantization, vision, and fine-tuning research.

</details>

<details>
<summary><strong>Governance, verification, and resilience</strong></summary>

- **[continuityos](https://github.com/Hardonian/continuityos)** `[Go · OPA]` — Sovereign Resilience-as-Code.
- **[FlexibleAccessible](https://github.com/Hardonian/FlexibleAccessible)** `[TypeScript · SaaS]` — Continuous accessibility discovery and remediation operations.
- **[ReadyLayer](https://github.com/Hardonian/ReadyLayer)** `[TypeScript · CI]` — Delivery governance, provenance, and evidence export.
- **[truthcore](https://github.com/Hardonian/truthcore)** `[Python · Verification]` — Verification kernel, content-addressed cache, and evidence reports.
- **[Reach](https://github.com/Hardonian/Reach)** `[Rust · Runtime]` — Deterministic execution and transcript replay.
- **[Requiem](https://github.com/Hardonian/Requiem)** `[C++ · Native]` — Native execution and operator-console contracts.
- **[JobForge](https://github.com/Hardonian/JobForge)** `[PostgreSQL · TypeScript]` — Idempotent, RLS-isolated job execution.
- **[MissionLedger](https://github.com/Hardonian/MissionLedger)** `[TypeScript · Policy]` — Governed missions, budgets, and proofpacks.
- **[hardonia-compliance-agent](https://github.com/Hardonian/hardonia-compliance-agent)** `[Rust · Workspace]` — Autonomous regulatory-compliance tooling.
- **[hardonia-audit-pack](https://github.com/Hardonian/hardonia-audit-pack)** `[Python · Evidence]` — Deterministic reconciliation evidence bundles.

</details>

<details>
<summary><strong>FinOps, ledger infrastructure, and commercial engines</strong></summary>

- **[Settler](https://github.com/Hardonian/Settler)** `[TigerBeetle · Next.js]` — Reconciliation intelligence and audit OS.
- **[WhatsForDinner](https://github.com/Hardonian/WhatsForDinner)** `[React · Stripe]` — Consumer AI SaaS with subscriptions, credits, marketplace, and vision workflows.
- **[TokenGoblin](https://github.com/Hardonian/TokenGoblin)** `[Go · ClickHouse]` — AI token-spend observability and routing guardrails.
- **[apva-framework](https://github.com/Hardonian/apva-framework)** `[Python · Telemetry]` — Reliability-adjusted AI ROI measurement.
- **[finops-autopilot](https://github.com/Hardonian/finops-autopilot)** `[Python · FinOps]` — Cost anomaly detection and rightsizing policies.
- **[webhook-witness](https://github.com/Hardonian/webhook-witness)** `[Rust · Cryptography]` — Signed, tamper-evident webhook ingestion and replay.
- **[commercial-architecture-simulator](https://github.com/Hardonian/commercial-architecture-simulator)** `[Python · Monte Carlo]` — SaaS pricing, churn, and unit-economics simulation.
- **[prompt-ops-hardonia-packs](https://github.com/Hardonian/prompt-ops-hardonia-packs)** `[Prompt Ops]` — Operator packs for GTM, outreach, and verification.
- **[TokPulse](https://github.com/Hardonian/TokPulse)** `[Turborepo · Remix]` — Multi-store creator-commerce operating system.
- **[storefront](https://github.com/Hardonian/storefront)** `[HTML · Edge]` — Edge-rendered commerce and digital fulfillment.

</details>

<details>
<summary><strong>Simulation, game runtimes, platforms, and micro-tools</strong></summary>

- **[CEO-G Canada Opportunity Graph](https://github.com/Hardonian/CEO-G-Canada-Economic-Opportunity-Graph)** `[Python · Graph]` — Sovereign infrastructure opportunity modeling.
- **[World26](https://github.com/Hardonian/World26)** `[Python · Simulation]` — Open planetary-systems simulator.
- **[WorldVM](https://github.com/Hardonian/WorldVM)** `[Rust · WASM]` — Sandboxed creator-built gameplay for major game engines.
- **[ReachRadar](https://github.com/Hardonian/ReachRadar)** `[Next.js · Analytics]` — Recommendation-algorithm observability.
- **[Zeo](https://github.com/Hardonian/Zeo)** `[TypeScript · Edge]` — Local-first, signed, composable agent pipelines.
- **[AI Automated Systems](https://github.com/Hardonian/AI-Automated-Systems_AIAS)** `[Astro · Static]` — Automation consulting and diagnostic surface.
- **[enterprise-integration-fabric](https://github.com/Hardonian/enterprise-integration-fabric)** `[Kotlin · Spring]` — Governed event-driven integration architecture.
- **[identity-entitlement-broker](https://github.com/Hardonian/identity-entitlement-broker)** `[Go · Zero Trust]` — Identity brokering and fine-grained entitlements.
- **[api-changelog-radar](https://github.com/Hardonian/api-changelog-radar)** `[Cloudflare Worker]` — Breaking-change detection for vendor APIs.
- **[reliability-platform](https://github.com/Hardonian/reliability-platform)** `[Go]` — Circuit breakers and automated disaster recovery.
- **[golden-path-platform](https://github.com/Hardonian/golden-path-platform)** `[Terraform · CI/CD]` — Compliant internal developer-platform templates.
- **[support-autopilot](https://github.com/Hardonian/support-autopilot)** `[Node.js · CLI]` — Autonomous support triage and diagnosis.
- **[ops-autopilot](https://github.com/Hardonian/ops-autopilot)** `[Python]` — Telemetry-driven reliability proposals through JobForge.
- **[growth-autopilot](https://github.com/Hardonian/growth-autopilot)** `[Python]` — SEO experiment and content proposals through JobForge.
- **[InboxExorcist](https://github.com/Hardonian/InboxExorcist)** `[Python · Gmail]` — Reversible inbox decluttering and filter automation.
- **[floyo](https://github.com/Hardonian/floyo)** `[Rust · Telemetry]` — Local workflow-opportunity detection.
- **[tfstate-drift-inspector](https://github.com/Hardonian/tfstate-drift-inspector)** `[Go · Terraform]` — Infrastructure drift inspection before apply.
- **[Architecture Playbook](architecture-playbook/README.md)** `[Documentation]` — Public patterns, controls, and evidence boundaries.

</details>

---

## Productized systems

The same architecture patterns are packaged as deployable kits, audits, and operator workflows.

| Product | Outcome | Explore |
| --- | --- | :---: |
| **AI Command Center** | Replace operational blind spots with health history, priorities, and revenue-aware triage. | [Open](products/ai-command-center-setup.md) |
| **SaaS Repo Rescue** | Audit auth, billing, webhooks, RLS, security boundaries, and revenue-leaking edge cases. | [Open](products/repo-rescue-saas-audit.md) |
| **Settler FinOps Engine** | Normalize and reconcile payment streams into deterministic evidence packs. | [Open](products/settler-finops-platform.md) |
| **TokenGoblin Optimizer** | Measure, route, budget, and reduce model inference spend. | [Open](products/tokengoblin-cost-optimizer.md) |
| **APVA ROI Benchmark** | Calculate reliability-adjusted value before scaling an AI workflow. | [Open](products/apva-roi-benchmark.md) |
| **Local AI Lab Audit** | Review GPU utilization, routing, model fit, security, and operating posture. | [Open](products/local-ai-lab-audit.md) |
| **ComfyUI Pro Workflows** | Run repeatable, private image-production pipelines on owned compute. | [Open](products/comfyui-workflow-packs.md) |
| **Automation Retainer** | Add senior architecture and workflow improvement without a full-time hire. | [Open](products/automation-retainer.md) |

<details>
<summary><strong>Explore the complete 28-product catalog</strong></summary>

### Creative and generative production

- [8K upscaling and facial restoration](products/advanced-upscale-restoration.md)
- [Architectural and interior visualization](products/architectural-interior-design.md)
- [E-commerce product relighting](products/ecommerce-product-relighting.md)
- [Flux inpainting and outpainting](products/flux-inpaint-outpaint-pro.md)
- [Flux portrait studio](products/flux-ultra-portrait-studio.md)
- [Game asset and PBR texture generation](products/game-asset-3d-generator.md)
- [Cinematic AI video production](products/video-production-cinema.md)
- [Voice-to-avatar lip sync](products/voice-to-avatar-lip-sync.md)
- [AI character generator](products/ai-character-generator-kit.md)
- [AI video storyboard studio](products/ai-video-storyboard-studio.md)
- [Consent-based voice cloning](products/ai-voice-clone-training-kit.md)
- [ComfyUI fashion lookbooks](products/comfyui-fashion-lookbook-kit.md)
- [ComfyUI product photography](products/comfyui-product-photo-kit.md)
- [ComfyUI thumbnail creation](products/comfyui-thumbnail-creator-kit.md)
- [ComfyUI custom-node starter](products/comfyui-node-starter-kit.md)

### Operations, research, and governance

- [Prompt engineering laboratory](products/prompt-engineering-laboratory.md)
- [Defend Your AI legal kit](products/defend-your-ai-legal-kit.md)
- [Floyo workflow radar](products/floyo-workflow-radar.md)
- [Research paper visualizer](products/research-paper-visualizer.md)
- [AI lab notebook packs](products/ai-lab-notebook-packs.md)

</details>

---

## Operating principles

| Principle | Working rule |
| --- | --- |
| **Evidence over confidence** | If a run cannot be inspected or replayed, it is not production-ready. |
| **Local-first by design** | Own the compute, data boundary, fallback path, and cost model wherever practical. |
| **Determinism at the edges** | Keep probabilistic intelligence inside explicit policy, schema, and execution constraints. |
| **Boring reliability wins** | Idempotency, RLS, state machines, and observable queues beat clever hidden behavior. |
| **Revenue is a reconciled event** | A dashboard row is not money; provider-correlated settlement evidence is money. |
| **Fix the smallest root cause** | Isolate the failure, repair it surgically, prove the result, then ship. |

---

## Working stack

<div align="center">

![Rust](https://img.shields.io/badge/Rust-111827?style=flat-square&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python_3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![TigerBeetle](https://img.shields.io/badge/TigerBeetle-F59E0B?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-111827?style=flat-square&logo=nextdotjs&logoColor=white)
![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=flat-square&logo=cloudflare&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=111827)
![NVIDIA](https://img.shields.io/badge/NVIDIA_CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white)

</div>

<details>
<summary><strong>Run this profile's validation locally</strong></summary>

```bash
git clone https://github.com/Hardonian/Hardonian.git
cd Hardonian
just bootstrap
cp .env.example .env
just test
```

The test harness validates local assets, product-page structure, workflow syntax, and README links.

</details>

---

## Frontier AI work

Alongside full-time solutions architecture work at **McGraw Hill**, I contribute independent, part-time expertise to confidential frontier-AI evaluation and systems initiatives.

The work spans complex technical reasoning, multi-step real-world evaluation design, failure-mode analysis, agent protocol governance, tool-execution boundaries, and structured feedback for enterprise-grade model behavior. Client, model, dataset, and internal research details remain confidential.

---

## Let's build

If you are working on a serious AI, SaaS, integration, reliability, or revenue system, start with a specific bottleneck, a measurable outcome, and a verifiable path to production.

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LINKEDIN-CONNECT_WITH_SCOTT-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/scottrmhardie/)
[![Storefront](https://img.shields.io/badge/STOREFRONT-EXPLORE_SYSTEMS-0f766e?style=for-the-badge&logo=cloudflare&logoColor=white)](https://www.aiautomatedsystems.ca)
[![Email](https://img.shields.io/badge/EMAIL-START_A_CONVERSATION-6d28d9?style=for-the-badge&logo=gmail&logoColor=white)](mailto:scottrmhardie@gmail.com?subject=Hardonia%20systems%20inquiry)

<br />

<sub>© Scott Hardie · Hardonia Sovereign Systems · Toronto, Canada</sub>

</div>
