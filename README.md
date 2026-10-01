<div align="center">

<img src="assets/hardonia-system-map.svg" alt="Hardonia production AI systems: observe, control, execute, prove, and reconcile" width="100%" />

# Scott Hardie

## Enterprise Applied AI Architect · AI Agents & Systems Infrastructure · Solutions Architecture

> **Building high-assurance infrastructure around foundation models: deterministic policy boundaries, Model Context Protocol (MCP) gateways, mathematical multi-tenant data isolation, and verified execution.**

[![Focus](https://img.shields.io/badge/Focus-Enterprise_Applied_AI_%7C_Agent_Infrastructure-0A66C2?style=flat-square)](#architecture-focus--systems-philosophy)
[![Role](https://img.shields.io/badge/Role-Solutions_Architect_%40_McGraw_Hill-111827?style=flat-square)](#about)
[![Location](https://img.shields.io/badge/Location-Toronto%2C_Canada-4B5563?style=flat-square)](#about)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-scottrmhardie-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/scottrmhardie/)
[![Email](https://img.shields.io/badge/Email-scottrmhardie%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:scottrmhardie@gmail.com)

[Architecture Focus](#architecture-focus--systems-philosophy) · [Proof-Backed Systems](#proof-backed-systems) · [Production Invariants](#production-invariants-at-a-glance) · [Architecture Matrix](#architectural-capabilities--evidence-matrix) · [Technical Writing](#technical-writing--architecture-guides) · [Platform Topology](#how-the-platform-fits-together) · [Sovereign AI Lab](#sovereign-ai-lab) · [Engineering Stack](#working-stack) · [About & Track Record](#about)

`ENTERPRISE AI ARCHITECTURE` · `MODEL CONTEXT PROTOCOL (MCP)` · `POSTGRESQL RLS` · `AGENT EVALS` · `FINOPS` · `FORMAL VERIFICATION`

</div>

---

## Architecture Focus & Systems Philosophy

AI demos are easy. Production enterprise systems must survive retries, partial failures, hostile inputs, prompt injections, runaway inference spend, model drift, and regulatory scrutiny under strict enterprise boundaries.

I design and build the infrastructure outside and around the model: observable workflows, explicit policy boundaries, capability-gated tool execution, replayable evidence, and mathematically isolated multi-tenant data fabrics.

> **Intelligence can be probabilistic. Infrastructure cannot.**

| Observe | Control | Prove |
| --- | --- | --- |
| Capture model, tool, cost, and transaction events with sub-millisecond telemetry. | Route workloads, enforce capability policies, isolate risk, and recover safely. | Replay decisions, verify state invariants, reconcile transactions, and export audit evidence. |

### Systems Architecture Disciplines

- **Enterprise Applied AI Architecture**: Guiding institutional and enterprise stakeholders through secure agent topologies, governance boundaries, legacy data integrations, and scalable production deployment.
- **Distributed Agent Infrastructure & MCP**: Engineering resilient agent control planes, sandboxed Model Context Protocol (MCP) gateways, policy proxies, and deterministic model failover cascades.
- **Data Boundary & Multi-Tenant Security**: Enforcing mathematical cross-tenant isolation directly in database kernels (PostgreSQL RLS) with automated negative penetration test batteries.
- **Inference FinOps & Execution Observability**: Architecting high-throughput Go ingestion pipelines, real-time token spend quotas, latency/cost routing trade-offs, and continuous evaluation suites.

### Production Invariants at a Glance

| Dimension | Architectural Standard | Verifiable System Proof |
| :--- | :--- | :--- |
| **Tenant Isolation** | Kernel-enforced PostgreSQL Row-Level Security (RLS) | [Settler](https://github.com/Hardonian/Settler) automated cross-tenant penetration test suites |
| **Spend Governance** | Sub-millisecond Go ingestion with hard token quotas | [TokenGoblin](https://github.com/Hardonian/TokenGoblin) ingestion benchmarks & budget cutoff tests |
| **Execution Trust** | Formally verified state machines and DAG ordering | [veridag](https://github.com/Hardonian/veridag) Quint temporal logic models & conformance specs |
| **Tool Authorization** | LLM as unprivileged planner; cryptographic approval tokens | [ReadyLayer](https://github.com/Hardonian/ReadyLayer) CI security gates & policy contracts |
| **Hardware-Informed** | Dedicated 4-tier on-premise GPU/NPU compute lab | [model-tools](https://github.com/Hardonian/model-tools) & [api-tools](https://github.com/Hardonian/api-tools) routing testbeds |

### Choose the shortest path

| If you are… | Start here | What you get |
| --- | --- | --- |
| **Reviewing engineering architecture & code** | **[Inspect the public evidence](#proof-backed-systems)** | 4 canonical open-source systems with benchmarks, test suites, and conservative maturity labels. |
| **Exploring production AI capabilities** | **[Inspect the Architecture Matrix](#architectural-capabilities--evidence-matrix)** | Cross-system mapping of MCP gateways, Postgres RLS multi-tenancy, formal Quint verification, and CI quality gates. |
| **An enterprise or engineering leader** | **[Book a free 30-minute diagnostic](https://calendly.com/scottrmhardie)** | A constraint map, failure-mode assessment, and concrete next steps for brittle AI workflows. |
| **Evaluating private or local AI** | **[Run the free AI lab audit](https://www.aiautomatedsystems.ca/audit)** | A fast readiness signal before spending on infrastructure or local hardware. |

---

## Architectural Capabilities & Evidence Matrix

Field-tested engineering implementations across core production AI competencies, mapped to public repositories, verified test suites, and technical guides:

| Competency Domain | Production Implementation Pattern | Evidence & Repositories |
| --- | --- | --- |
| **Agent Control Planes & MCP Gateways** | Treating the LLM as an unprivileged planner; implementing policy-gated Model Context Protocol (MCP) reverse proxies with dynamic tool discovery, input sanitization, and cryptographic single-use approval tokens for destructive side effects. | [ReadyLayer](https://github.com/Hardonian/ReadyLayer)<br />[agent-infra](https://github.com/Hardonian/agent-infra)<br />[Tool Authorization Guide](OPENAI_CAMPAIGN/content/02_enterprise_tool_calling_authorization_outside_model.md) |
| **Multi-Tenant Security & Relational Isolation** | Enforcing mathematical tenant isolation directly in PostgreSQL Row-Level Security (RLS) policies rather than fragile application-level WHERE filters; verified with automated negative penetration test suites. | [Settler](https://github.com/Hardonian/Settler)<br />[Tenant Isolation Guide](OPENAI_CAMPAIGN/content/01_safe_multi_tenant_ai_agents_postgres_rls.md)<br />[Settler Benchmarks](https://github.com/Hardonian/Settler/blob/main/benchmarks/reconciliationBenchmark.ts) |
| **Inference FinOps & Spend Governance** | High-throughput Go ingestion pipelines measuring cost, usage, latency, and tenant token quotas; automated circuit breakers halting runaway agent loops; budget-governed model cascades (`gpt-4o` → `gpt-4o-mini` → local fallback). | [TokenGoblin](https://github.com/Hardonian/TokenGoblin)<br />[Ingestion Benchmarks](https://github.com/Hardonian/TokenGoblin/blob/main/internal/ingestion/benchmark_test.go)<br />[TokenGoblin Spec](https://github.com/Hardonian/TokenGoblin/blob/main/docs/ARCHITECTURE_AND_SPEC.md) |
| **Formal Verification & Protocol Design** | Specifying distributed execution semantics and capability security using Quint temporal logic formal models, state invariant checks, and cross-language conformance test vectors. | [veridag](https://github.com/Hardonian/veridag)<br />[Quint Formal Models](https://github.com/Hardonian/veridag/blob/main/formal/README.md)<br />[Protocol Architecture](https://github.com/Hardonian/veridag/blob/main/docs/architecture.md) |
| **Continuous Evals & CI/CD Delivery** | Automated evaluation batteries scoring tool selection accuracy, argument schemas, prompt injection refusals, and structured outputs; gating PR merges on deterministic quality thresholds. | [ReadyLayer](https://github.com/Hardonian/ReadyLayer)<br />[Production Agent Guide](OPENAI_CAMPAIGN/content/03_from_prototype_to_production_enterprise_agents.md)<br />[Quality Gates CI](https://github.com/Hardonian/ReadyLayer/actions/workflows/security-gates.yml) |
| **Full-Stack SaaS & Enterprise Integrations** | Modern SaaS delivery with Next.js 16 App Router, Supabase RLS, Prisma, Stripe billing, Kafka messaging, Keycloak OIDC, and enterprise LMS/SIS protocol connectors (LTI, OneRoster). | [ReadyLayer](https://github.com/Hardonian/ReadyLayer)<br />[Settler](https://github.com/Hardonian/Settler)<br />[Enterprise Architecture Record](#about) |

---

## Proof-backed systems

These are the four clearest public examples of the approach. The table is generated from a [versioned manifest](profile-projects.json), checked against GitHub every week, and deliberately separates released, beta, and research work.

<!-- profile-projects:start -->
_Public project metadata last verified **2026-10-01** · [source manifest](profile-projects.json) · [verification policy](CONTRIBUTING.md#project-metadata)_

| Project | Problem | Public evidence |
| --- | --- | --- |
| **[TokenGoblin](https://github.com/Hardonian/TokenGoblin)** · Go<br />Measure · `beta`<br />[![TokenGoblin CI](https://img.shields.io/badge/CI-passing-2ea44f/badge.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/Hardonian/TokenGoblin/actions/workflows/ci.yml) | LLM workloads need cost, usage, and routing data before teams can control inference spend. | Public ingestion benchmarks, cost and routing tests, and a repository-level CI workflow.<br />[Architecture](https://github.com/Hardonian/TokenGoblin/blob/main/docs/ARCHITECTURE_AND_SPEC.md) · [Evidence](https://github.com/Hardonian/TokenGoblin/blob/main/internal/ingestion/benchmark_test.go) |
| **[ReadyLayer](https://github.com/Hardonian/ReadyLayer)** · TypeScript<br />Govern · `beta`<br />[![ReadyLayer CI](https://img.shields.io/badge/CI-passing-2ea44f/badge.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/Hardonian/ReadyLayer/actions/workflows/security-gates.yml) | AI-assisted delivery needs policy, review, and evidence before generated changes reach production. | Public policy contracts, evidence export documentation, test suites, and CI quality gates.<br />[Architecture](https://github.com/Hardonian/ReadyLayer/blob/main/docs/runner/ARCHITECTURE.md) · [Evidence](https://github.com/Hardonian/ReadyLayer/blob/main/docs/EVIDENCE.md) |
| **[veridag](https://github.com/Hardonian/veridag)** · Rust<br />Prove · `research`<br />[![veridag CI](https://img.shields.io/badge/CI-passing-2ea44f/badge.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/Hardonian/veridag/actions/workflows/formal.yml) | Distributed execution needs explicit ordering, capability security, and cross-language conformance. | A public protocol specification, Quint formal models, test vectors, and dedicated conformance workflows.<br />[Architecture](https://github.com/Hardonian/veridag/blob/main/docs/architecture.md) · [Evidence](https://github.com/Hardonian/veridag/blob/main/formal/README.md) |
| **[Settler](https://github.com/Hardonian/Settler)** · TypeScript<br />Reconcile · `beta`<br />[![Settler CI](https://img.shields.io/badge/CI-passing-2ea44f/badge.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/Hardonian/Settler/actions/workflows/security.yml) | Payment, banking, and operational records diverge unless matching and evidence rules are explicit. | Public reconciliation benchmark source and checked-in snapshots, with CI and security-invariant workflows.<br />[Architecture](https://github.com/Hardonian/Settler/blob/main/docs/ARCHITECTURE.md) · [Evidence](https://github.com/Hardonian/Settler/blob/main/benchmarks/reconciliationBenchmark.ts) |
<!-- profile-projects:end -->

<div align="center">

[![Profile evidence checks](https://img.shields.io/badge/profile_checks-passing-2ea44f/badge.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/Hardonian/Hardonian/actions/workflows/profile-ci.yml)

</div>

---

## Technical Writing & Architecture Guides

Field-tested engineering guides grounded in verified production code and open-source infrastructure:

1. **[Building Safe Multi-Tenant AI Agents with Postgres RLS](OPENAI_CAMPAIGN/content/01_safe_multi_tenant_ai_agents_postgres_rls.md)**  
   `POSTGRESQL RLS` · `NEGATIVE PENETRATION TESTING` · `KERNEL-ENFORCED MULTI-TENANCY`  
   _Why application-level filtering fails in autonomous agent workflows, and how to enforce mathematical tenant boundaries via PostgreSQL Row-Level Security with automated negative penetration tests._
2. **[Enterprise Tool Calling: Why Authorization Belongs Outside the Model](OPENAI_CAMPAIGN/content/02_enterprise_tool_calling_authorization_outside_model.md)**  
   `MODEL CONTEXT PROTOCOL (MCP)` · `CRYPTOGRAPHIC HITL TOKENS` · `UNPRIVILEGED PLANNERS`  
   _Treating the LLM as an unprivileged planner; implementing policy-gated MCP reverse proxies with single-use cryptographic approval tokens for privileged side effects._
3. **[From Prototype to Production: Architecture for Enterprise AI Agents](OPENAI_CAMPAIGN/content/03_from_prototype_to_production_enterprise_agents.md)**  
   `THE SIX PRODUCTION PILLARS` · `CONTINUOUS CI EVALS` · `OPENTELEMETRY TRACING`  
   _The six production pillars: model abstraction, tool execution boundaries, continuous CI/CD evaluations, OpenTelemetry observability, and token spend governance._

---

## How I help

| Engagement | Best when | Outcome |
| --- | --- | --- |
| **AI clarity audit** | The opportunity is real, but the workflow and risk boundaries are not yet clear. | A decision-ready map of constraints, ownership, ROI assumptions, and the smallest safe pilot. |
| **Stabilization sprint** | An AI workflow is live but flaky, opaque, or expensive. | Explicit contracts, retries, telemetry, fallbacks, acceptance tests, and an operator runbook. |
| **Governance architecture** | Agents or models can take consequential actions. | Approval boundaries, policy gates, audit trails, incident paths, and evidence you can inspect. |
| **Local AI systems** | Data control, predictable cost, or offline capability matters. | Model and hardware fit, routing, deployment, observability, and a practical operating plan. |

Every engagement starts with the workflow—not a predetermined model or platform. See the [service details](https://www.aiautomatedsystems.ca/services), [case studies](https://www.aiautomatedsystems.ca/case-studies), or [book a diagnostic](https://calendly.com/scottrmhardie).

---

## How the platform fits together

<img src="assets/operating-loop.svg" alt="Architecture, implementation, verification, product delivery, customer surface, and measurement feedback loop" width="100%" />

Seven monorepos keep related systems coherent while preserving clear boundaries:

| Boundary | Public monorepos | Responsibility |
| --- | --- | --- |
| **Observe + control** | [agent-edge](https://github.com/Hardonian/agent-edge) · [agent-infra](https://github.com/Hardonian/agent-infra) | Agent traffic, policy, governance, mission state, and MCP boundaries. |
| **Model + execute** | [model-tools](https://github.com/Hardonian/model-tools) · [autopilot](https://github.com/Hardonian/autopilot) | Inference routing, GPU fit, and runnerless ops, support, growth, and FinOps workflows. |
| **Integrate + operate** | [api-tools](https://github.com/Hardonian/api-tools) · [ops-tools](https://github.com/Hardonian/ops-tools) | APIs, webhooks, continuity, drift inspection, and golden paths. |
| **Consumer outcomes** | [consumer-tools](https://github.com/Hardonian/consumer-tools) | Warranty, review intelligence, and inbox automation. |

<details>
<summary><strong>Open the component map</strong></summary>

```text
signal                     policy                      execution
agent-edge ──────────────► agent-infra ──────────────► autopilot
packet capture             control plane               ops / finops
mesh edge                  agent mesh                  growth / support
                           MCP firewall
      │                          │                          │
      └──────────────────── model-tools ◄───────────────────┘
                          inference / routing
                                  │
                          local GPU testbed
                                  │
                      evidence / reconciliation
```

Each public monorepo includes an `ARCHITECTURE.md` describing its boundary and migration history.

</details>

---

## Sovereign AI lab

Hardonia includes an owned, local testbed for model routing, image and video workflows, and failure-mode testing. It is where local-first claims are exercised before they become architecture advice.

| Lane | Hardware | Primary use |
| --- | --- | --- |
| **Edge orchestration & NPU** | AMD Ryzen AI 9 HX370 · 50 NPU TOPS · 32 GB | Local agent orchestration, low-latency reasoning, and local eval suites. |
| **Heavy inference** | NVIDIA V100 · 16 GB | Larger model and video-generation workloads. |
| **Memory-oriented** | NVIDIA P40 · 24 GB | ComfyUI pipelines, quantized models, and training experiments. |
| **Interactive** | NVIDIA RTX 3060 · 12 GB | Vision, embeddings, and latency-sensitive workflows. |

The lab uses Ollama-compatible routing, ComfyUI, containerized services, and Prometheus/Grafana-style observability. Public implementation lives primarily in [model-tools](https://github.com/Hardonian/model-tools) and [api-tools](https://github.com/Hardonian/api-tools).

<details>
<summary><strong>Decision-layer experiment: where Jev fits</strong></summary>

[TypeSafe Jev](https://typesafe.ai) is being evaluated for low-cost typed classification where a general-purpose LLM is unnecessary—for example intent classification, routing, and tool-selection gates. It complements deterministic policy; it does not replace it. TypeSafe currently lists input pricing at $42 per billion tokens.

</details>

---

## More of the portfolio

<details>
<summary><strong>Trust, execution, and agent systems</strong></summary>

- [Requiem](https://github.com/Hardonian/Requiem) — unified AI control plane and execution contracts.
- [Nautilus](https://github.com/Hardonian/Nautilus) — local AI execution, orchestration, and policy enforcement.
- [Keys](https://github.com/Hardonian/Keys) — auditable mission control for constrained agents.
- [truthcore](https://github.com/Hardonian/truthcore) — verification kernel and offline evidence reports.
- [Zeo](https://github.com/Hardonian/Zeo) — governance, policy enforcement, and deterministic audit trails.
- [agent-governance](https://github.com/Hardonian/agent-governance) — enforceable agent laws and a governance gateway.

</details>

<details>
<summary><strong>Applied systems and simulation</strong></summary>

- [SawyerCore](https://github.com/Hardonian/SawyerCore) — deterministic edge-AI runtime and agent simulation.
- [WorldForge](https://github.com/Hardonian/WorldForge) — deterministic, moddable simulation runtime.
- [World26](https://github.com/Hardonian/World26) — open planetary-systems simulator.
- [FlexibleAccessible](https://github.com/Hardonian/FlexibleAccessible) — accessibility auditing and remediation workflows.
- [MortgageMatchPro](https://github.com/Hardonian/MortgageMatchPro) — mortgage scenario and matching platform.

</details>

<details>
<summary><strong>Productized audits, kits, and workflows</strong></summary>

| Starting point | Intended outcome |
| --- | --- |
| [SaaS repo rescue](products/repo-rescue-saas-audit.md) | Find auth, billing, webhook, RLS, and reliability gaps before they leak revenue. |
| [TokenGoblin cost optimizer](products/tokengoblin-cost-optimizer.md) | Measure and control model-inference spend. |
| [Local AI lab audit](products/local-ai-lab-audit.md) | Review hardware fit, routing, security, and operating posture. |
| [AI command center](products/ai-command-center-setup.md) | Replace operational blind spots with health and priority signals. |
| [ComfyUI workflow packs](products/comfyui-workflow-packs.md) | Run repeatable private image-production workflows on owned compute. |

[Browse the full catalog →](https://www.aiautomatedsystems.ca/catalog)

</details>

---

## Operating principles

| Principle | Working rule |
| --- | --- |
| **Evidence over confidence** | If a run cannot be inspected or replayed, it is not production-ready. |
| **Local-first where it earns its keep** | Own the compute, data boundary, fallback path, and cost model when the trade-off is justified. |
| **Determinism at the edges** | Keep probabilistic intelligence inside explicit policy, schema, and execution constraints. |
| **Boring reliability wins** | Idempotency, row-level security, state machines, and observable queues beat hidden cleverness. |
| **Revenue is a reconciled event** | A dashboard row is not money; provider-correlated settlement evidence is money. |
| **Fix the smallest root cause** | Isolate the failure, repair it surgically, prove the result, then ship. |

---

## Working stack

<div align="center">

**Systems & Core Backend**<br />
![Rust](https://img.shields.io/badge/Rust-111827?style=flat-square&logo=rust&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)

<br /><br />

**Data, Isolation & Security**<br />
![PostgreSQL](https://img.shields.io/badge/PostgreSQL_RLS-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)

<br /><br />

**AI, Agents & Inference**<br />
![Model Context Protocol](https://img.shields.io/badge/MCP-Protocol-6d28d9?style=flat-square)
![NVIDIA CUDA](https://img.shields.io/badge/NVIDIA_CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white)

<br /><br />

**Infrastructure & Cloud**<br />
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=111827)
![Next.js](https://img.shields.io/badge/Next.js_16-000000?style=flat-square&logo=next.js&logoColor=white)

</div>

<details>
<summary><strong>Verify this profile locally</strong></summary>

```bash
git clone https://github.com/Hardonian/Hardonian.git
cd Hardonian
uv run python -m unittest discover tests -v
uv run python scripts/profile-metadata.py --check --verify-remote
uv run python scripts/profile-link-audit.py
```

The checks reject stale project metadata, missing public evidence, broken local assets, and dead links.

</details>

---

## About

I am a Solutions Architect at **McGraw Hill** and build Hardonia independently from Toronto. Alongside that work, I contribute part-time expertise to confidential frontier-AI evaluation and systems initiatives; client, model, dataset, and internal research details remain private.

### Engineering & Enterprise Profile

- **Dual-Discipline Mastery**: Combining high-level enterprise architecture (C-suite technical alignment, procurement, institutional security, FERPA/SOC-2 compliance) with low-level systems implementation (Go distributed control planes, Rust formal models, TypeScript/Next.js production apps, and PostgreSQL kernel-level isolation).
- **Enterprise Integrations at Scale**: Deep experience architecting mission-critical data exchanges across large-scale distributed systems, identity providers (Keycloak, SAML, OIDC), message buses, and legacy institutional platforms (LMS, SIS, ERP).
- **Commercial & Delivery Track Record**: Winner of the President's Award for Sales Excellence; proven ability to bridge frontier AI research into reliable, revenue-generating enterprise customer outcomes.
- **Sovereign Infrastructure**: Hands-on hardware engineering operating an owned GPU/NPU inference cluster for local model evaluations, quantized inference, and private agent pipelines.

---

## Bring the bottleneck

If you have an AI workflow that is expensive, unreliable, hard to govern, or stuck between prototype and production—or want to connect on high-assurance AI systems architecture and enterprise engineering—reach out directly:

<div align="center">

[![Book](https://img.shields.io/badge/BOOK-30_MIN_DIAGNOSTIC-f97316?style=for-the-badge)](https://calendly.com/scottrmhardie)
[![Email](https://img.shields.io/badge/EMAIL-DIRECT-6d28d9?style=for-the-badge&logo=gmail&logoColor=white)](mailto:scottrmhardie@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LINKEDIN-SCOTT_HARDIE-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/scottrmhardie/)
[![Website](https://img.shields.io/badge/WEBSITE-AI_AUTOMATED_SYSTEMS-0f766e?style=for-the-badge)](https://www.aiautomatedsystems.ca)

<br />

<sub>Hardonia · local compute · deterministic control · verifiable outcomes</sub>

</div>
