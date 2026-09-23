<div align="center">

<img src="assets/hardonia-system-map.svg" alt="Hardonia sovereign systems — JEV-powered decision layer across observe, control, execute, prove, and reconcile" width="100%" />

# HARDONIA

<p><strong>Local compute. Deterministic control. Verifiable outcomes.</strong></p>

**Scott Hardie** · Solutions Architect · AI Systems Builder · Toronto, Canada

[Explore the platform](#-platform-monorepos) · [View the storefront](https://www.aiautomatedsystems.ca) · [Connect](https://www.linkedin.com/in/scottrmhardie/)

<br />

![Rust](https://img.shields.io/badge/Rust-111827?style=flat-square&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![NVIDIA](https://img.shields.io/badge/NVIDIA_CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white)
![TypeSafe](https://img.shields.io/badge/%E2%9A%A1_JEV-FF6B00?style=flat-square)

</div>

---

## Built for the moment after the demo

AI demos are easy. Production systems must survive retries, partial failure, hostile inputs, runaway spend, model drift, and an auditor asking exactly what happened.

Hardonia is a working portfolio of control planes, runtimes, security boundaries, and commercial systems designed around one idea:

> **Intelligence can be probabilistic. Infrastructure cannot.**

Every decision in the platform flows through **[TypeSafe JEV](https://typesafe.ai)** — a deterministic decision engine that classifies intent, routes workloads, gates tool calls, and verifies outcomes at $0.042 per million tokens. No black boxes. No vibes-based routing.

<img src="assets/operating-loop.svg" alt="Architecture → Implementation → Verification → Product → Customer Surface → Support + Measurement → feedback loop" width="100%" />

---

## ⚡ JEV Decision Layer

JEV runs between every layer of the Hardonia platform:

| Layer | What JEV does | Cost |
|---|---|---|
| **Chat widget** | Classifies visitor intent in 300ms — canned response or deep inference | $0.00002/msg |
| **Context engine** | Decides which tool calls to keep or drop during compaction | $0.001/compaction |
| **Tool gating** | Gates every MCP tool call through allowlist + hard rules before execution | $0.00001/call |
| **Caveman compression** | 62% token reduction on long sessions | Auto-triggered |
| **GPU routing** | Routes inference to the right GPU lane (V100 · P40 · RTX 3060) | Zero cost |

> *The chat widget on [aiautomatedsystems.ca](https://www.aiautomatedsystems.ca) classifies every visitor message through JEV before deciding whether to serve a canned response or route to local Ollama inference. Zero cloud API costs.*

---

## 🏗️ Platform Monorepos

Seven monorepos, each a coherent subsystem. Every monorepo has an [ARCHITECTURE.md](https://github.com/Hardonian/autopilot/blob/main/ARCHITECTURE.md) showing how it fits the platform.

<table>
<tr>
<td width="50%">

**Automation**

| Monorepo | Purpose |
|---|---|
| [**autopilot**](https://github.com/Hardonian/autopilot) | Runnerless ops · finops · growth · support |
| [**consumer-tools**](https://github.com/Hardonian/consumer-tools) | Warranty · review intel · inbox cleanup |
| [**api-tools**](https://github.com/Hardonian/api-tools) | ComfyUI API · webhooks · changelog tracking |

</td>
<td width="50%">

**Infrastructure**

| Monorepo | Purpose |
|---|---|
| [**agent-infra**](https://github.com/Hardonian/agent-infra) | Control plane · governance · mesh · firewall |
| [**agent-edge**](https://github.com/Hardonian/agent-edge) | Edge networking · packet capture |
| [**model-tools**](https://github.com/Hardonian/model-tools) | Inference routing · GPU management |
| [**ops-tools**](https://github.com/Hardonian/ops-tools) | Continuity · drift inspection · golden paths |

</td>
</tr>
</table>

```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  autopilot   │  │ agent-infra  │  │ agent-edge   │
│  ops/finops/ │──│ control-     │──│ mesh-edge/   │
│  growth/     │  │  plane/      │  │ pcap/        │
│  support/    │  │ mission-     │  └──────────────┘
└──────┬───────┘  │  ledger/     │
       │          │ agent-mesh/  │
       └──────────│ mcpwall/     │
                  └──────┬───────┘
                         │
                   ┌─────▼──────┐
                   │ model-tools │
                   │ inference/  │
                   │ ollama/     │
                   └──────┬──────┘
                          │
                    ⚡ JEV decides
                          │
                   ┌──────▼──────┐
                   │  GPU FLEET   │
                   │ V100 · P40   │
                   │  RTX 3060    │
                   └──────────────┘
```

---

## 🧪 SaaS Experiments

| Repo | Stack | What it does |
|---|---|---|
| [**Settler**](https://github.com/Hardonian/Settler) | TS · TigerBeetle | Reconciliation intelligence and audit OS |
| [**veridag**](https://github.com/Hardonian/veridag) | Rust · Quint | Formally specified distributed trust DAG |
| [**Zeo**](https://github.com/Hardonian/Zeo) | TS · Edge | Local-first, signed, composable agent pipelines |
| [**Reach**](https://github.com/Hardonian/Reach) | Rust · Runtime | Deterministic execution and transcript replay |
| [**Requiem**](https://github.com/Hardonian/Requiem) | C++ · Native | Native execution and operator-console contracts |
| [**truthcore**](https://github.com/Hardonian/truthcore) | Python | Verification kernel and evidence reports |
| [**ReadyLayer**](https://github.com/Hardonian/ReadyLayer) | TS · CI | Delivery governance and provenance export |
| [**MortgageMatchPro**](https://github.com/Hardonian/MortgageMatchPro) | TypeScript | Mortgage matching platform |
| [**Keys**](https://github.com/Hardonian/Keys) | TypeScript | Auditable mission control for constrained agents |
| [**Nautilus**](https://github.com/Hardonian/Nautilus) | Docker | Containerized operational AI infrastructure |
| [**TokenGoblin**](https://github.com/Hardonian/TokenGoblin) | Go · ClickHouse | AI token-spend observability and routing guardrails |
| [**SawyerCore**](https://github.com/Hardonian/SawyerCore) | Node · Python | Deterministic edge-AI runtime and simulation engine |
| [**WorldForge**](https://github.com/Hardonian/WorldForge) | Rust | Deterministic, moddable simulation operating system |
| [**World26**](https://github.com/Hardonian/World26) | Python | Open planetary-systems simulator |
| [**FlexibleAccessible**](https://github.com/Hardonian/FlexibleAccessible) | TypeScript | WCAG accessibility compliance |

---

## 🛠️ Infrastructure

| Repo | What it does |
|---|---|
| [**ai-lab**](https://github.com/Hardonian/ai-lab) | Lab config, scripts, monitoring, GPU fleet management |
| [**agent-governance**](https://github.com/Hardonian/agent-governance) | Agent laws, spec, 159 tests, 35 spec sections |
| [**hardonia-checkout-api**](https://github.com/Hardonian/hardonia-checkout-api) | Stripe checkout + webhook verification |
| [**JupyterNotebooks**](https://github.com/Hardonian/JupyterNotebooks) | Applied AI notebooks: quantization, vision, fine-tuning |

---

## 💰 Revenue Stack

| Repo | What it does |
|---|---|
| [**hardonia-store**](https://github.com/Hardonian/hardonia-store) | Storefront · [aiautomatedsystems.ca](https://www.aiautomatedsystems.ca) |
| [**comfyui-workflow-packs**](https://github.com/Hardonian/comfyui-workflow-packs) | 20+ ComfyUI workflow packs on Gumroad |
| [**content-repo**](https://github.com/Hardonian/content-repo) | 28 SEO blog posts, email sequences, social content |
| [**ai-prompt-templates**](https://github.com/Hardonian/ai-prompt-templates) | 200+ tested prompt templates |
| [**ai-ops-toolkit**](https://github.com/Hardonian/ai-ops-toolkit) | CLI tools for AI lab operations |

---

## 🎬 Sovereign AI Lab — Local Video Generation

The Hardonia AI lab runs a 3-GPU sovereign stack with **2,354 ComfyUI nodes** across video generation, image processing, and audio synthesis — all running locally with zero cloud API costs.

| GPU | VRAM | Role | Model Capacity |
|---|---|---|---|
| **NVIDIA V100** | 32 GB | Heavy inference · Wan 2.2 14B video | 14B params |
| **NVIDIA P40** | 24 GB | ComfyUI primary · HunyuanVideo · LoRA training | 8.3B params |
| **NVIDIA RTX 3060** | 12 GB | Vision models · embeddings · LTX 2.3 | 5B params |

**Live capabilities:**

| Capability | Model | Nodes | Output |
|---|---|---|---|
| Product photo → video | [Wan 2.2](https://github.com/Wan-AI/Wan2.2) | 168 nodes | 5-sec rotating product demo |
| Text → video + audio | [LTX 2.3](https://github.com/Lightricks/ComfyUI-LTXVideo) | 111 nodes | Synced video + narration |
| Photo → cinematic video | [HunyuanVideo 1.5](https://github.com/Tencent/HunyuanVideo) | 19 nodes | 1080p with super-resolution |
| Image → portrait | SDXL + ControlNet | 400+ nodes | Professional headshots |
| Batch product photos | ComfyUI + IP-Adapter | 300+ nodes | 100+ images/hour |

**Infrastructure:** Ollama 4-lane inference · LiteLLM routing · Prometheus + Grafana monitoring · NATS event mesh · n8n automation · Agent governance (159 tests, 35 spec sections)

> The [Video Gen API](https://github.com/Hardonian/ai-lab) on `:8085` wraps all video models behind a single REST endpoint. Upload a product photo, pick a style, get a video.

---

## Operating Principles

| | Principle | Working rule |
|---|---|---|
| 🔍 | **Evidence over confidence** | If a run cannot be inspected or replayed, it is not production-ready. |
| 🏠 | **Local-first by design** | Own the compute, data boundary, fallback path, and cost model wherever practical. |
| 🔒 | **Determinism at the edges** | Keep probabilistic intelligence inside explicit policy, schema, and execution constraints. |
| ⚙️ | **Boring reliability wins** | Idempotency, RLS, state machines, and observable queues beat clever hidden behavior. |
| 💵 | **Revenue is a reconciled event** | A dashboard row is not money; provider-correlated settlement evidence is money. |
| ⚡ | **JEV before vibes** | Every decision is classified, routed, and verified — not guessed. |

---

## Let's build

If you are working on a serious AI, SaaS, integration, reliability, or revenue system, start with a specific bottleneck, a measurable outcome, and a verifiable path to production.

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LINKEDIN-CONNECT-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/scottrmhardie/)
[![Storefront](https://img.shields.io/badge/STOREFRONT-EXPLORE-0f766e?style=for-the-badge&logo=cloudflare&logoColor=white)](https://www.aiautomatedsystems.ca)
[![Email](https://img.shields.io/badge/EMAIL-START_A_CONVERSATION-6d28d9?style=for-the-badge&logo=gmail&logoColor=white)](mailto:scottrmhardie@gmail.com?subject=Hardonia%20systems%20inquiry)

<br />
<br />

![Visitors](https://api.visitorbadge.io/api/visitors?path=Hardonian%2FHardonian&countColor=%23373737&style=flat-square)
![Repos](https://img.shields.io/badge/repos-39-blue?style=flat-square)
![Monorepos](https://img.shields.io/badge/monorepos-7-orange?style=flat-square)
![JEV](https://img.shields.io/badge/JEV-decisions-FF6B00?style=flat-square)

<sub>© Scott Hardie · Hardonia Sovereign Systems · Toronto, Canada</sub>

</div>