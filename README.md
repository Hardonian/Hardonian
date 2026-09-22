<div align="center">

# HARDONIA

<p><strong>Local compute. Deterministic control. Verifiable outcomes.</strong></p>

**Scott Hardie** · Solutions Architect · AI Systems Builder · Toronto, Canada

[Explore the systems](#platform-monorepos) · [View the storefront](https://www.aiautomatedsystems.ca) · [Connect](https://www.linkedin.com/in/scottrmhardie/)

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

---

## Platform Monorepos

Seven monorepos, each a coherent subsystem. Every monorepo has an [ARCHITECTURE.md](https://github.com/Hardonian/autopilot/blob/main/ARCHITECTURE.md) showing how it fits the platform.

| Monorepo | Purpose | Contents |
|---|---|---|
| [**autopilot**](https://github.com/Hardonian/autopilot) | Runnerless automation | ops · finops · growth · support |
| [**agent-infra**](https://github.com/Hardonian/agent-infra) | Agent execution and governance | control-plane · mission-ledger · agent-mesh · mcpwall |
| [**agent-edge**](https://github.com/Hardonian/agent-edge) | Edge networking and capture | mesh-edge · pcap |
| [**model-tools**](https://github.com/Hardonian/model-tools) | Inference routing and selection | model-forge · inference-api · ollama-router |
| [**consumer-tools**](https://github.com/Hardonian/consumer-tools) | Consumer protection | warranty-weasel · review-radar · inbox-exorcist |
| [**api-tools**](https://github.com/Hardonian/api-tools) | API lifecycle tooling | comfyui-api · webhook-witness · changelog-radar |
| [**ops-tools**](https://github.com/Hardonian/ops-tools) | Operations infrastructure | continuity · drift-inspector · golden-path |

### How they connect

```
autopilot ──→ agent-infra ──→ agent-edge
    │              │
    └──→ model-tools
              │
         ollama-router (GPU fleet: V100 · P40 · RTX 3060)
```

---

## SaaS experiments

Active platform experiments in their own repos:

| Repo | Stack | Purpose |
|---|---|---|
| [**Settler**](https://github.com/Hardonian/Settler) | TypeScript · TigerBeetle | Reconciliation intelligence and audit OS |
| [**Zeo**](https://github.com/Hardonian/Zeo) | TypeScript · Edge | Local-first, signed, composable agent pipelines |
| [**veridag**](https://github.com/Hardonian/veridag) | Rust · Quint | Formally specified distributed trust DAG |
| [**MortgageMatchPro**](https://github.com/Hardonian/MortgageMatchPro) | TypeScript | Mortgage matching platform |
| [**Requiem**](https://github.com/Hardonian/Requiem) | C++ · Native | Native execution and operator-console contracts |
| [**truthcore**](https://github.com/Hardonian/truthcore) | Python · Verification | Verification kernel and evidence reports |
| [**ReadyLayer**](https://github.com/Hardonian/ReadyLayer) | TypeScript · CI | Delivery governance and provenance export |
| [**Reach**](https://github.com/Hardonian/Reach) | Rust · Runtime | Deterministic execution and transcript replay |
| [**Nautilus**](https://github.com/Hardonian/Nautilus) | Docker · Infrastructure | Containerized operational AI infrastructure |
| [**Keys**](https://github.com/Hardonian/Keys) | TypeScript | Auditable mission control for constrained agents |
| [**TokenGoblin**](https://github.com/Hardonian/TokenGoblin) | Go · ClickHouse | AI token-spend observability and routing guardrails |
| [**SawyerCore**](https://github.com/Hardonian/SawyerCore) | Node · Python | Deterministic edge-AI runtime and simulation engine |
| [**World26**](https://github.com/Hardonian/World26) | Python | Open planetary-systems simulator |
| [**WorldForge**](https://github.com/Hardonian/WorldForge) | Rust | Deterministic, moddable simulation operating system |

---

## Infrastructure

| Repo | Purpose |
|---|---|
| [**ai-lab**](https://github.com/Hardonian/ai-lab) | Lab config, scripts, monitoring, GPU fleet management |
| [**agent-governance**](https://github.com/Hardonian/agent-governance) | Agent laws, spec, 159 tests, 35 spec sections |
| [**hardonia-checkout-api**](https://github.com/Hardonian/hardonia-checkout-api) | Stripe checkout + webhook verification |
| [**JupyterNotebooks**](https://github.com/Hardonian/JupyterNotebooks) | Applied AI notebooks: quantization, vision, fine-tuning |

---

## Revenue stack

Commercial systems built on the platform:

| Repo | Purpose |
|---|---|
| [**hardonia-store**](https://github.com/Hardonian/hardonia-store) | Storefront · [aiautomatedsystems.ca](https://www.aiautomatedsystems.ca) |
| [**comfyui-workflow-packs**](https://github.com/Hardonian/comfyui-workflow-packs) | 20+ ComfyUI workflow packs on Gumroad |
| [**content-repo**](https://github.com/Hardonian/content-repo) | 28 SEO blog posts, email sequences, social content |
| [**ai-prompt-templates**](https://github.com/Hardonian/ai-prompt-templates) | 200+ tested prompt templates |
| [**ai-ops-toolkit**](https://github.com/Hardonian/ai-ops-toolkit) | CLI tools for AI lab operations |

---

## Operating principles

| Principle | Working rule |
| --- | --- |
| **Evidence over confidence** | If a run cannot be inspected or replayed, it is not production-ready. |
| **Local-first by design** | Own the compute, data boundary, fallback path, and cost model wherever practical. |
| **Determinism at the edges** | Keep probabilistic intelligence inside explicit policy, schema, and execution constraints. |
| **Boring reliability wins** | Idempotency, RLS, state machines, and observable queues beat clever hidden behavior. |
| **Revenue is a reconciled event** | A dashboard row is not money; provider-correlated settlement evidence is money. |

---

## Working stack

<div align="center">

![Rust](https://img.shields.io/badge/Rust-111827?style=flat-square&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python_3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![NVIDIA](https://img.shields.io/badge/NVIDIA_CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white)
![TypeSafe](https://img.shields.io/badge/TypeSafe_JEV-FF6B00?style=flat-square)

</div>

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