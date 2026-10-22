<div align="center">

<img src="assets/hardonia-system-map.svg" alt="Hardonia production AI systems: observe, control, execute, prove, and reconcile" width="100%" />

# Scott Hardie

### Senior Applied AI / Platform Engineer · Distributed Systems · Enterprise Architecture

Toronto, Canada · [LinkedIn](https://www.linkedin.com/in/scottrmhardie/) · [Email](mailto:scottrmhardie@gmail.com?subject=Role%20or%20systems%20conversation)

> I build the systems around foundation models that make them safe to operate: policy-gated tool execution, tenant-isolated data, measurable inference cost, observable workflows, and evidence you can replay.

**Target roles:** Senior/Staff Applied AI Engineer · AI Platform Engineer · Distributed Systems Engineer · Solutions Architect

**Interested in:** teams shipping high-assurance AI, developer platforms, agent infrastructure, and enterprise-scale systems.

[![Focus: Applied AI and platform infrastructure](https://img.shields.io/badge/Focus-Applied_AI_%7C_Platform_Infrastructure-0A66C2?style=flat-square)](#what-i-build)
[![Solutions Architect at McGraw Hill](https://img.shields.io/badge/McGraw_Hill-Solutions_Architect-111827?style=flat-square)](#about)
[![Location: Toronto, Canada](https://img.shields.io/badge/Location-Toronto%2C_Canada-4B5563?style=flat-square)](#about)
[![Connect with Scott Hardie on LinkedIn](https://img.shields.io/badge/LinkedIn-scottrmhardie-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/scottrmhardie/)

`APPLIED AI` · `DISTRIBUTED SYSTEMS` · `MCP` · `POSTGRESQL RLS` · `AGENT EVALS` · `FORMAL VERIFICATION`

</div>

---

## Why I am a strong engineering hire

- **I bridge architecture and implementation.** I can align stakeholders on a system boundary, then build the Go, Rust, TypeScript, Python, database, and CI pieces that make the boundary real.
- **I treat AI as a production systems problem.** Models are useful; the surrounding controls determine whether a system is reliable, secure, affordable, and supportable.
- **I make claims inspectable.** My public work includes specifications, benchmarks, negative security tests, formal models, conformance vectors, and CI quality gates—not just screenshots or demos.
- **I understand enterprise delivery.** My work spans customer-facing architecture, identity and data integrations, institutional security, procurement conversations, and the operational constraints that decide whether a system ships.

## What I build

| Area | How I approach it | Public proof |
| --- | --- | --- |
| **AI platform and agent infrastructure** | Keep the model unprivileged; put capability discovery, authorization, retries, budgets, and side effects behind explicit services. | [ReadyLayer](https://github.com/Hardonian/ReadyLayer) · [agent-infra](https://github.com/Hardonian/agent-infra) |
| **Secure multi-tenant systems** | Enforce tenant boundaries in the database kernel with PostgreSQL RLS and test the negative cases automatically. | [Settler](https://github.com/Hardonian/Settler) |
| **Inference economics and operations** | Measure tokens, latency, routing, and spend; use hard quotas and fallbacks to keep inference predictable. | [TokenGoblin](https://github.com/Hardonian/TokenGoblin) |
| **Reliable distributed execution** | Specify state transitions, ordering, and capability rules; validate implementations against formal models and conformance vectors. | [veridag](https://github.com/Hardonian/veridag) |

## Start here

If you are reviewing this profile for a role, these are the fastest paths to signal:

- **[Four canonical systems](#proof-backed-systems)** — the clearest portfolio of measurable, governed, and verifiable AI infrastructure.
- **[Architecture and technical writing](#technical-writing)** — how I reason about production AI beyond model selection.
- **[Working stack](#working-stack)** — the languages, data systems, inference tooling, and infrastructure I use.
- **[About and contact](#about)** — current role, enterprise background, and the best way to reach me.

---

## Architecture at a glance

Production AI needs deterministic boundaries around probabilistic components. The model proposes; typed policy services decide what may happen; execution systems perform only authorized work; evidence makes the result inspectable.

```text
untrusted input / event
          │
          ▼
┌──────────────────────────────────────────────────────────────┐
│ Observe: ingress, token spend, latency, traces, tenant scope │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ Plan: unprivileged model emits typed candidate tool intent    │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ Control: MCP policy gateway authorizes reads, writes, and HITL│
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ Execute: isolated services, RLS data access, idempotent jobs │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ Prove: audit chain, invariants, reconciliation, replayable log│
└──────────────────────────────────────────────────────────────┘
```

> **Intelligence can be probabilistic. Infrastructure cannot.**

### Engineering principles

- **Evidence over confidence:** if a run cannot be inspected or replayed, it is not production-ready.
- **Determinism at the edges:** keep probabilistic behavior inside explicit schemas, policies, state machines, and execution limits.
- **Security in the kernel:** enforce tenant isolation and authorization where a missed application check cannot bypass them.
- **Boring reliability wins:** idempotency, retries, observable queues, and clear failure paths beat hidden cleverness.
- **Cost is a correctness constraint:** runaway inference spend is an operational failure, not merely a finance problem.

---

## Proof-backed systems

These four repositories are the most representative public evidence of how I work. The table is generated from a [versioned manifest](profile-projects.json), checked against GitHub weekly, and separates released, beta, and research work.

<!-- profile-projects:start -->
_Public project metadata last verified **2026-10-14** · [source manifest](profile-projects.json) · [verification policy](CONTRIBUTING.md#project-metadata)_

| Project | Problem | Public evidence |
| --- | --- | --- |
| **[TokenGoblin](https://github.com/Hardonian/TokenGoblin)** · Go<br />Measure · `beta`<br />[![View TokenGoblin GitHub Actions CI workflow](https://img.shields.io/badge/CI-passing-2ea44f/badge.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/Hardonian/TokenGoblin/actions/workflows/ci.yml) | LLM workloads need cost, usage, and routing data before teams can control inference spend. | Public ingestion benchmarks, cost and routing tests, and a repository-level CI workflow.<br />[Architecture](https://github.com/Hardonian/TokenGoblin/blob/main/docs/ARCHITECTURE_AND_SPEC.md) · [Evidence](https://github.com/Hardonian/TokenGoblin/blob/main/internal/ingestion/benchmark_test.go) |
| **[ReadyLayer](https://github.com/Hardonian/ReadyLayer)** · TypeScript<br />Govern · `beta`<br />[![View ReadyLayer GitHub Actions CI workflow](https://img.shields.io/badge/CI-passing-2ea44f/badge.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/Hardonian/ReadyLayer/actions/workflows/security-gates.yml) | AI-assisted delivery needs policy, review, and evidence before generated changes reach production. | Public policy contracts, evidence export documentation, test suites, and CI quality gates.<br />[Architecture](https://github.com/Hardonian/ReadyLayer/blob/main/docs/runner/ARCHITECTURE.md) · [Evidence](https://github.com/Hardonian/ReadyLayer/blob/main/docs/EVIDENCE.md) |
| **[veridag](https://github.com/Hardonian/veridag)** · Rust<br />Prove · `research`<br />[![View veridag GitHub Actions CI workflow](https://img.shields.io/badge/CI-passing-2ea44f/badge.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/Hardonian/veridag/actions/workflows/formal.yml) | Distributed execution needs explicit ordering, capability security, and cross-language conformance. | A public protocol specification, Quint formal models, test vectors, and dedicated conformance workflows.<br />[Architecture](https://github.com/Hardonian/veridag/blob/main/docs/architecture.md) · [Evidence](https://github.com/Hardonian/veridag/blob/main/formal/README.md) |
| **[Settler](https://github.com/Hardonian/Settler)** · TypeScript<br />Reconcile · `beta`<br />[![View Settler GitHub Actions CI workflow](https://img.shields.io/badge/CI-passing-2ea44f/badge.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/Hardonian/Settler/actions/workflows/security.yml) | Payment, banking, and operational records diverge unless matching and evidence rules are explicit. | Public reconciliation benchmark source and checked-in snapshots, with CI and security-invariant workflows.<br />[Architecture](https://github.com/Hardonian/Settler/blob/main/docs/ARCHITECTURE.md) · [Evidence](https://github.com/Hardonian/Settler/blob/main/benchmarks/reconciliationBenchmark.ts) |
<!-- profile-projects:end -->

<div align="center">

[![View Profile evidence checks GitHub Actions workflow](https://img.shields.io/badge/profile_checks-passing-2ea44f/badge.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/Hardonian/Hardonian/actions/workflows/profile-ci.yml)

</div>

---

## Technical writing

I publish architecture notes that are grounded in the systems above:

1. **[Building Safe Multi-Tenant AI Agents with Postgres RLS](OPENAI_CAMPAIGN/content/01_safe_multi_tenant_ai_agents_postgres_rls.md)** — why application-level filtering fails in autonomous workflows, and how to enforce tenant boundaries in PostgreSQL.
2. **[Enterprise Tool Calling: Why Authorization Belongs Outside the Model](OPENAI_CAMPAIGN/content/02_enterprise_tool_calling_authorization_outside_model.md)** — policy-gated MCP reverse proxies, unprivileged planners, and single-use approval tokens.
3. **[From Prototype to Production: Architecture for Enterprise AI Agents](OPENAI_CAMPAIGN/content/03_from_prototype_to_production_enterprise_agents.md)** — model abstraction, execution boundaries, CI evaluations, observability, and token-spend governance.
4. **[Hardonia Architecture Playbook](architecture-playbook/README.md)** — system topology, bounded contexts, operating loops, and evidence verification.

---

## Working stack

<div align="center">

**Languages & systems**<br />
![Rust](https://img.shields.io/badge/Rust-111827?style=flat-square&logo=rust&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)

<br /><br />

**Data, security & observability**<br />
![PostgreSQL RLS](https://img.shields.io/badge/PostgreSQL_RLS-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white)

<br /><br />

**AI, agents & infrastructure**<br />
![Model Context Protocol](https://img.shields.io/badge/MCP-Protocol-6d28d9?style=flat-square)
![NVIDIA CUDA](https://img.shields.io/badge/NVIDIA_CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=111827)

</div>

<details>
<summary><strong>Local compute and inference lab</strong></summary>

I run a private, owned testbed for local model routing, quantized inference, image/video workflows, and failure-mode testing. The hardware includes an AMD EPYC 7452 server, AMD Ryzen AI 9 HX370 NPU/GPU compute, NVIDIA V100/P40/RTX 3060 accelerators, Ollama-compatible routing, ComfyUI, containers, and Prometheus/Grafana-style observability.

Public implementation lives primarily in [model-tools](https://github.com/Hardonian/model-tools), [autopilot](https://github.com/Hardonian/autopilot), and [api-tools](https://github.com/Hardonian/api-tools).

</details>

<details>
<summary><strong>Verify the profile locally</strong></summary>

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

I am a **Solutions Architect at McGraw Hill** and build Hardonia independently from Toronto. My work combines enterprise architecture and hands-on systems implementation: customer-facing technical strategy, distributed control planes, formal models, production TypeScript applications, and PostgreSQL isolation.

I also contribute part-time expertise to confidential frontier-AI evaluation and systems initiatives; client, model, dataset, and internal research details remain private.

Selected background:

- Enterprise integrations across identity providers, message buses, LMS/SIS/ERP platforms, and legacy data exchanges.
- Working knowledge of LTI 1.3 Advantage, OneRoster 1.2, OAuth 2.0, Keycloak OIDC, SCIM, MCP, and OpenTelemetry trace propagation.
- Institutional security and compliance conversations, including FERPA and SOC 2 requirements.
- President's Award for Sales Excellence, reflecting the ability to turn difficult technical work into customer and business outcomes.

---

## Let’s talk

Hiring managers and recruiting teams: the best way to reach me is [LinkedIn](https://www.linkedin.com/in/scottrmhardie/) or [email](mailto:scottrmhardie@gmail.com?subject=Role%20or%20systems%20conversation). I am especially interested in roles where I can help turn ambitious AI capabilities into reliable platform primitives and shipped products.

If you are evaluating the engineering work first, start with [TokenGoblin](https://github.com/Hardonian/TokenGoblin), [ReadyLayer](https://github.com/Hardonian/ReadyLayer), [veridag](https://github.com/Hardonian/veridag), or [Settler](https://github.com/Hardonian/Settler), then follow the architecture links in each project.

<div align="center">

[![Connect with Scott Hardie on LinkedIn](https://img.shields.io/badge/LINKEDIN-SCOTT_HARDIE-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/scottrmhardie/)
[![Send an email to Scott Hardie](https://img.shields.io/badge/EMAIL-DIRECT-6d28d9?style=for-the-badge&logo=gmail&logoColor=white)](mailto:scottrmhardie@gmail.com?subject=Role%20or%20systems%20conversation)

<br />

<sub>Hardonia · local compute · deterministic control · verifiable outcomes</sub>

</div>
