<div align="center">

<img src="assets/hardonia-system-map.svg" alt="Hardonia Sovereign AI Systems: Observe, Control, Execute, Prove, and Reconcile" width="100%" />

<br />

[![Focus: Applied AI & Platform Infrastructure](https://img.shields.io/badge/FOCUS-APPLIED_AI_%7C_PLATFORM_INFRA-0369a1?style=for-the-badge&labelColor=0f172a)](#what-i-build)
[![Isolation: Postgres RLS & eBPF](https://img.shields.io/badge/ISOLATION-POSTGRES_RLS_%7C_eBPF-047857?style=for-the-badge&labelColor=0f172a)](#architecture-at-a-glance)
[![Role: Solutions Architect at McGraw Hill](https://img.shields.io/badge/MCGRAW_HILL-SOLUTIONS_ARCHITECT-3730a3?style=for-the-badge&labelColor=0f172a)](#about)
[![Profile Checks Passing](https://img.shields.io/badge/CI_PROOF_GATES-PASSING-065f46?style=for-the-badge&labelColor=0f172a&logo=githubactions&logoColor=white)](https://github.com/Hardonian/Hardonian/actions/workflows/profile-ci.yml)
[![Connect with Scott Hardie on LinkedIn](https://img.shields.io/badge/LINKEDIN-SCOTTRMHARDIE-0A66C2?style=for-the-badge&labelColor=0f172a&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/scottrmhardie/)

# Scott Hardie

## Senior / Staff Applied AI & Platform Engineer · Distributed Systems · Enterprise Architecture

**Toronto, Canada** · [Executive Brief](EXECUTIVE_BRIEF.md) · [Architecture Playbook](architecture-playbook/README.md) · [LinkedIn](https://www.linkedin.com/in/scottrmhardie/) · [Email](mailto:scottrmhardie@gmail.com?subject=Role%20or%20systems%20conversation)

<p align="center">
  <strong>I build the deterministic infrastructure around foundation models that makes them safe to run in production:</strong><br />
  policy-gated tool execution, database-kernel tenant isolation, bounded inference economics, formal state verification, and cryptographically replayable audit trails.
</p>

[**Executive Brief**](EXECUTIVE_BRIEF.md) · [**Flagship Systems**](#what-i-build) · [**Control Plane Architecture**](#architecture-at-a-glance) · [**Failure Modes & Mitigations**](#production-failure-modes--kernel-mitigations) · [**Verified Proof Matrix**](#proof-backed-systems) · [**Technical Writing**](#technical-writing) · [**About & Contact**](#about)

</div>

---

## Why teams bring me in

| Engineering Pillar | How I Execute It in Practice | Shipped Public Proof |
| :--- | :--- | :--- |
| **Architecture ↔ Implementation** | Align executives, security, and product teams on system boundaries, then write the Rust, Go, C++, TypeScript, Python, SQL, and CI gates that enforce those boundaries in code. | [ControlPlane (`v1.0.0`)](https://github.com/Hardonian/ControlPlane) · [FORGE (`v1.0.0`)](https://github.com/Hardonian/FORGE) · [Requiem (`C++/TS`)](https://github.com/Hardonian/Requiem) |
| **Probabilistic AI, Deterministic Kernels** | Treat the model as an unprivileged planner; enforce capability authorization in out-of-band MCP gateways, tenant isolation via PostgreSQL `FORCE ROW LEVEL SECURITY`, and untrusted execution in ZK-eBPF and Wasmtime sandboxes. | [ReadyLayer](https://github.com/Hardonian/ReadyLayer) · [Settler (`v1.8.0`)](https://github.com/Hardonian/Settler) · [zerokernel (`v1.0.0`)](https://github.com/Hardonian/zerokernel) · [WorldVM (`WASM`)](https://github.com/Hardonian/WorldVM) |
| **Machine-Checkable Proof Over Demos** | Back architectural claims with executable specifications, Quint state-machine models, Lean 4 kernel-checked proof witnesses (`Zero Axioms`), Vertex AI/Gemini regression contracts, and HLO compiler delta-minimizers. | [veridag](https://github.com/Hardonian/veridag) · [GRAPH-Lab](https://github.com/Hardonian/GRAPH-Lab) · [UNIFORM](https://github.com/Hardonian/UNIFORM) · [AgentAxiom](https://github.com/Hardonian/AgentAxiom) · [XLAxiom](https://github.com/Hardonian/XLAxiom) |
| **Enterprise Delivery & Inference FinOps** | Combine enterprise identity/compliance expertise (`OAuth 2.0`, `OIDC`, `SCIM`, `LTI 1.3`, `CASE`, `SOC 2`, `FERPA`) and commercial execution (**McGraw Hill Solutions Architect · President's Award**) with sub-millisecond token telemetry and GPU roofline modeling. | [TokenGoblin](https://github.com/Hardonian/TokenGoblin) · [TokPulse (`v3.0.0`)](https://github.com/Hardonian/TokPulse) · [Cred-bridge](https://github.com/Hardonian/Cred-bridge) · [Executive Brief](EXECUTIVE_BRIEF.md) |

| `< 1 ms` | `FORCE RLS` | `0 Syscalls` | `Zero Axioms` | `6 Releases` |
| :---: | :---: | :---: | :---: | :---: |
| **Token Telemetry & Quota Gate**<br />Sub-ms stream ingestion in Go ([TokenGoblin](https://github.com/Hardonian/TokenGoblin) · [TokPulse](https://github.com/Hardonian/TokPulse)) | **Kernel Tenant Isolation**<br />Session JWTs bound in PostgreSQL ([Settler `v1.8.0`](https://github.com/Hardonian/Settler)) | **Ambient Host Surface**<br />Deterministic eBPF ZK-VM sandboxing ([zerokernel `v1.0.0`](https://github.com/Hardonian/zerokernel)) | **Formal Verification**<br />Lean 4 kernel proofs & Quint specs ([GRAPH-Lab](https://github.com/Hardonian/GRAPH-Lab) · [veridag](https://github.com/Hardonian/veridag)) | **CI-Gated Production Tags**<br />`Settler`, `FORGE`, `zerokernel`, `ControlPlane`, `TokPulse`, `SAT-Frontier` |

---

## What I build

| System Domain | Architectural Approach & Enforced Invariants | Shipped Repositories & Releases |
| :--- | :--- | :--- |
| **AI Platform, Evals & Agent Governance** | Keep foundation models unprivileged; enforce MCP capability contracts, offline regression/grounding assertions (`Context Caching` & `Thinking Tokens`), and policy-gated delivery. | **[ReadyLayer](https://github.com/Hardonian/ReadyLayer)** `TS` · **[FORGE](https://github.com/Hardonian/FORGE)** `v1.0.0` · **[AgentAxiom](https://github.com/Hardonian/AgentAxiom)** `Py · Vertex/Gemini` · **[agent-infra](https://github.com/Hardonian/agent-infra)** |
| **Multi-Tenant Data, RAG & Kernel Isolation** | Enforce tenant and sub-document RBAC boundaries in PostgreSQL (`FORCE RLS`), verify SHA-256 RAG citation provenance, and isolate untrusted code in ZK-eBPF and WASM sandboxes. | **[Settler](https://github.com/Hardonian/Settler)** `v1.8.0 · TS` · **[zerokernel](https://github.com/Hardonian/zerokernel)** `v1.0.0 · Rust/eBPF` · **[WorldVM](https://github.com/Hardonian/WorldVM)** `Rust/Wasmtime` · **[RAG Verifier](scripts/rag_citation_verifier.py)** |
| **Inference Economics, FinOps & GPU Roofline** | Measure token throughput, tail latency, and spend in sub-millisecond streams; compile PagedAttention KV-cache & quantization topologies against hardware rooflines. | **[TokenGoblin](https://github.com/Hardonian/TokenGoblin)** `Go` · **[TokPulse](https://github.com/Hardonian/TokPulse)** `v3.0.0 · Go` · **[KV Roofline Compiler](scripts/kv_roofline_compiler.py)** `Py/Triton` |
| **Deterministic Distributed & Native Execution** | Specify causal state transitions, PostgreSQL exactly-once RPC queues, and native C++/Rust runtimes validated against Quint formal models. | **[veridag](https://github.com/Hardonian/veridag)** `Rust/Quint` · **[ControlPlane](https://github.com/Hardonian/ControlPlane)** `v1.0.0 · Rust` · **[Requiem](https://github.com/Hardonian/Requiem)** `C++/TS` · **[JobForge](https://github.com/Hardonian/JobForge)** `Postgres/RPC` |
| **ML Compilers & Numerical Fidelity** | Turn silent floating-point discrepancies across large JAX/OpenXLA computation graphs into minimal, portable, deterministic reproducers. | **[XLAxiom](https://github.com/Hardonian/XLAxiom)** `Python · JAX/OpenXLA` |
| **Formal Methods, SMT & Enterprise Standards** | Pair exact rational/combinatorial search, `QF_NRA` SMT campaigns, and SAT solving with Lean 4 kernel witnesses (`Zero Axioms`) and signed EdTech (`CASE`) ledgers. | **[GRAPH-Lab](https://github.com/Hardonian/GRAPH-Lab)** `Lean 4/Py` · **[UNIFORM](https://github.com/Hardonian/UNIFORM)** `Rust/Lean 4` · **[SAT-Frontier](https://github.com/Hardonian/SAT-Frontier)** `v0.2.9` · **[Cred-bridge](https://github.com/Hardonian/Cred-bridge)** `CASE` |

---

## Architecture at a glance

Production AI requires strict deterministic boundaries around probabilistic models. The model proposes candidate intent; typed policy services authorize what may happen; isolated kernels execute only approved work; cryptographic ledgers make every outcome inspectable and replayable.

<div align="center">

<img src="assets/hardonian-control-plane.svg" alt="Hardonian Control Plane Architecture" width="100%" />

</div>

### Production failure modes & kernel mitigations

| Production Failure Mode | Why Naïve Agent Wrappers Fail | Hardonian Kernel / Protocol Mitigation | Verified Implementation |
| :--- | :--- | :--- | :--- |
| **Prompt-injected cross-tenant read/write** | Application-layer `WHERE tenant_id = ?` filters are easily omitted by generated queries or bypassed by ORM bugs. | Session-scoped JWT claims bound directly in the PostgreSQL kernel via `FORCE ROW LEVEL SECURITY`, verified by automated negative tests. | [Settler (`v1.8.0`)](https://github.com/Hardonian/Settler) · [RLS Architecture Note](OPENAI_CAMPAIGN/content/01_safe_multi_tenant_ai_agents_postgres_rls.md) |
| **Unauthorized tool execution & privilege creep** | Passing raw API credentials or broad tool schemas to a model lets an injected prompt trigger destructive side effects. | Unprivileged planner emits typed intent; an external MCP policy gateway validates capability scope and mints single-use approval tokens. | [ReadyLayer](https://github.com/Hardonian/ReadyLayer) · [MCP Authorization Note](OPENAI_CAMPAIGN/content/02_enterprise_tool_calling_authorization_outside_model.md) |
| **Runaway agent loops & unmeasured token spend** | Multi-step retries and recursive tool calls compound tail latency and exhaust budgets long before billing alerts fire. | Sub-millisecond token stream ingestion, tenant-level hard quota circuit breakers, and deterministic fallback model routing. | [TokenGoblin](https://github.com/Hardonian/TokenGoblin) · [TokPulse (`v3.0.0`)](https://github.com/Hardonian/TokPulse) |
| **Out-of-order distributed state mutation** | Concurrent workers and network retries violate causal ordering when state transitions are implicit. | Quint state-machine specifications, capability-checked causal DAG transitions, and ZK-proved eBPF sandboxes. | [veridag](https://github.com/Hardonian/veridag) · [zerokernel (`v1.0.0`)](https://github.com/Hardonian/zerokernel) · [ZK eBPF & DAG Note](OPENAI_CAMPAIGN/content/04_zero_knowledge_ebpf_sandboxing_and_causal_dags.md) |
| **Silent compiler numerical divergence** | Floating-point discrepancies inside multi-thousand-node JAX/OpenXLA graphs are intractable to isolate by hand. | Automated HLO graph delta-minimization that bisects and extracts minimal, portable numerical reproducers. | [XLAxiom](https://github.com/Hardonian/XLAxiom) · [GPU Roofline Note](OPENAI_CAMPAIGN/content/06_gpu_kv_cache_roofline_and_serving_topology.md) |
| **RAG role leakage & hallucinated citations** | Post-filtering ANN vector search leaks restricted chunks across roles, and prompt-level citations can be fabricated. | Pre-filtered `FORCE RLS` + BM25/`pgvector` RRF fusion paired with cryptographic `[cite:id@sha256]` span verification. | [AgentAxiom](https://github.com/Hardonian/AgentAxiom) · [RAG Verifier](scripts/rag_citation_verifier.py) · [RAG Provenance Note](OPENAI_CAMPAIGN/content/05_permission_aware_hybrid_rag_and_citation_provenance.md) |
| **Unverified algorithmic or mathematical bounds** | Heuristic search scripts can misreport extremal counterexamples without machine-checked proof obligations. | Exact rational/SMT search and SAT solving paired with Lean 4 kernel-verified proof witnesses (`Zero Axioms`). | [GRAPH-Lab](https://github.com/Hardonian/GRAPH-Lab) · [UNIFORM](https://github.com/Hardonian/UNIFORM) · [SAT-Frontier (`v0.2.9`)](https://github.com/Hardonian/SAT-Frontier) |

---

## Proof-backed systems

These four canonical repositories represent how I design, test, and verify software. The table below is generated from a [versioned manifest](profile-projects.json), audited against live GitHub endpoints in CI, and separates `stable`, `beta`, and `research` maturity tiers.

<!-- profile-projects:start -->
_Public project metadata last verified **2026-11-07** · [source manifest](profile-projects.json) · [verification policy](CONTRIBUTING.md#project-metadata)_

| Project | Problem | Public evidence |
| --- | --- | --- |
| **[TokenGoblin](https://github.com/Hardonian/TokenGoblin)** · Go<br />Measure · `beta`<br />[![View TokenGoblin GitHub Actions CI workflow](https://img.shields.io/badge/CI-passing-2ea44f/badge.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/Hardonian/TokenGoblin/actions/workflows/ci.yml) | LLM workloads need cost, usage, and routing data before teams can control inference spend. | Public ingestion benchmarks, cost and routing tests, and a repository-level CI workflow.<br />[Architecture](https://github.com/Hardonian/TokenGoblin/blob/main/docs/ARCHITECTURE_AND_SPEC.md) · [Evidence](https://github.com/Hardonian/TokenGoblin/blob/main/internal/ingestion/benchmark_test.go) |
| **[ReadyLayer](https://github.com/Hardonian/ReadyLayer)** · TypeScript<br />Govern · `beta`<br />[![View ReadyLayer GitHub Actions CI workflow](https://img.shields.io/badge/CI-passing-2ea44f/badge.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/Hardonian/ReadyLayer/actions/workflows/security-gates.yml) | AI-assisted delivery needs policy, review, and evidence before generated changes reach production. | Public policy contracts, evidence export documentation, test suites, and CI quality gates.<br />[Architecture](https://github.com/Hardonian/ReadyLayer/blob/main/docs/runner/ARCHITECTURE.md) · [Evidence](https://github.com/Hardonian/ReadyLayer/blob/main/docs/EVIDENCE.md) |
| **[veridag](https://github.com/Hardonian/veridag)** · Rust<br />Prove · `research`<br />[![View veridag GitHub Actions CI workflow](https://img.shields.io/badge/CI-passing-2ea44f/badge.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/Hardonian/veridag/actions/workflows/formal.yml) | Distributed execution needs explicit ordering, capability security, and cross-language conformance. | A public protocol specification, Quint formal models, test vectors, and dedicated conformance workflows.<br />[Architecture](https://github.com/Hardonian/veridag/blob/main/docs/architecture.md) · [Evidence](https://github.com/Hardonian/veridag/blob/main/formal/README.md) |
| **[Settler](https://github.com/Hardonian/Settler)** · TypeScript<br />Reconcile · `stable` · [`v1.8.0`](https://github.com/Hardonian/Settler/releases/tag/v1.8.0)<br />[![View Settler GitHub Actions CI workflow](https://img.shields.io/badge/CI-passing-2ea44f/badge.svg?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/Hardonian/Settler/actions/workflows/security.yml) | Payment, banking, and operational records diverge unless matching and evidence rules are explicit. | Multi-tenant reconciliation engine v1.8.0, 20+ CI gates, public benchmark suite, and cryptographically verified release artifacts.<br />[Architecture](https://github.com/Hardonian/Settler/blob/main/docs/ARCHITECTURE.md) · [Evidence](https://github.com/Hardonian/Settler/blob/main/benchmarks/reconciliationBenchmark.ts) |
<!-- profile-projects:end -->

---

## Technical writing

Architecture monographs and reference specifications grounded directly in the production systems above:

| Monograph / Specification | Core Architectural Thesis | Companion Codebase |
| :--- | :--- | :--- |
| **[01 // Building Safe Multi-Tenant AI Agents with Postgres RLS](OPENAI_CAMPAIGN/content/01_safe_multi_tenant_ai_agents_postgres_rls.md)** | Why application-layer `WHERE` filtering fails in autonomous workflows, and how to bind session-scoped JWT tenant claims directly to PostgreSQL `FORCE ROW LEVEL SECURITY`. | [Settler (`v1.8.0`)](https://github.com/Hardonian/Settler) |
| **[02 // Enterprise Tool Calling: Authorization Outside the Model](OPENAI_CAMPAIGN/content/02_enterprise_tool_calling_authorization_outside_model.md)** | Decoupling probabilistic planning from privileged execution via policy-gated MCP reverse proxies and single-use cryptographic approval tokens. | [ReadyLayer](https://github.com/Hardonian/ReadyLayer) · [FORGE (`v1.0.0`)](https://github.com/Hardonian/FORGE) |
| **[03 // From Prototype to Production: Enterprise AI Agents](OPENAI_CAMPAIGN/content/03_from_prototype_to_production_enterprise_agents.md)** | End-to-end production hardening across model routing abstractions, deterministic state boundaries, CI evaluation gates, OpenTelemetry tracing, and FinOps circuit breakers. | [TokenGoblin](https://github.com/Hardonian/TokenGoblin) · [TokPulse (`v3.0.0`)](https://github.com/Hardonian/TokPulse) |
| **[04 // Zero-Knowledge eBPF Sandboxing & Causal DAG Execution](OPENAI_CAMPAIGN/content/04_zero_knowledge_ebpf_sandboxing_and_causal_dags.md)** | Formalizing causal state-machine preconditions in Quint, isolating untrusted execution inside deterministic eBPF ZK-VMs, and emitting replayable SHA-256 evidence envelopes. | [zerokernel (`v1.0.0`)](https://github.com/Hardonian/zerokernel) · [veridag](https://github.com/Hardonian/veridag) · [ControlPlane (`v1.0.0`)](https://github.com/Hardonian/ControlPlane) |
| **[05 // Permission-Aware Hybrid RAG & Cryptographic Citation Provenance](OPENAI_CAMPAIGN/content/05_permission_aware_hybrid_rag_and_citation_provenance.md)** | Pre-filtered PostgreSQL `FORCE RLS` + BM25/`pgvector` Reciprocal Rank Fusion (RRF) and deterministic `[cite:chunk@sha256]` claim grounding verification. | [RAG Verifier](scripts/rag_citation_verifier.py) · [AgentAxiom](https://github.com/Hardonian/AgentAxiom) · [Settler (`v1.8.0`)](https://github.com/Hardonian/Settler) |
| **[06 // GPU KV-Cache Roofline Modeling & Deterministic Serving Topology](OPENAI_CAMPAIGN/content/06_gpu_kv_cache_roofline_and_serving_topology.md)** | Modeling GQA PagedAttention KV-cache footprints, memory-bandwidth vs. compute rooflines, and Triton fused `INT4` dequant-GEMV kernels across heterogeneous GPUs. | [KV Roofline Compiler](scripts/kv_roofline_compiler.py) · [XLAxiom](https://github.com/Hardonian/XLAxiom) · [TokenGoblin](https://github.com/Hardonian/TokenGoblin) |
| **[07 // Hardonia Sovereign AI Architecture Playbook](architecture-playbook/README.md)** | System topology, bounded contexts (`Observe → Control → Operate → Prove → Reconcile`), verified release tags, and cryptographic evidence boundaries. | [Hardonian](https://github.com/Hardonian/Hardonian) · [Executive Brief](EXECUTIVE_BRIEF.md) |

---

## Working stack

<div align="center">

![Rust](https://img.shields.io/badge/Rust-111827?style=for-the-badge&logo=rust&logoColor=white)
![Go](https://img.shields.io/badge/Go-0369a1?style=for-the-badge&logo=go&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-1e3a8a?style=for-the-badge&logo=cplusplus&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-1e40af?style=for-the-badge&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-1d4ed8?style=for-the-badge&logo=python&logoColor=white)
![Lean 4 & Quint](https://img.shields.io/badge/Lean_4_%7C_Quint-3730a3?style=for-the-badge)

![PostgreSQL RLS](https://img.shields.io/badge/PostgreSQL_RLS-1e3a8a?style=for-the-badge&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-065f46?style=for-the-badge&logo=supabase&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-991b1b?style=for-the-badge&logo=redis&logoColor=white)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-111827?style=for-the-badge&logo=opentelemetry&logoColor=white)
![MCP Protocol](https://img.shields.io/badge/MCP_Gateway-4338ca?style=for-the-badge)
![WebAssembly](https://img.shields.io/badge/Wasmtime_%7C_WASM-3730a3?style=for-the-badge&logo=webassembly&logoColor=white)

![NVIDIA CUDA](https://img.shields.io/badge/NVIDIA_CUDA_%7C_Triton-15803d?style=for-the-badge&logo=nvidia&logoColor=white)
![PyTorch & JAX](https://img.shields.io/badge/PyTorch_%7C_OpenXLA-9a3412?style=for-the-badge&logo=pytorch&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-0369a1?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-1d4ed8?style=for-the-badge&logo=kubernetes&logoColor=white)
![Linux & eBPF](https://img.shields.io/badge/Linux_%7C_eBPF-111827?style=for-the-badge&logo=linux&logoColor=white)

</div>

### Owned local compute & inference testbed

I operate a dedicated hardware lab for local model routing, quantized inference benchmarking, multi-GPU failure-mode injection, and telemetry soak testing:

| Compute Tier | Hardware / Runtime Specification | Public Tooling & Workloads |
| :--- | :--- | :--- |
| **Server & Accelerator Rack** | **AMD EPYC 7452** (32C/64T server host) · **NVIDIA Tesla V100 / P40 / RTX 3060** multi-GPU array | Quantized LLM serving, OpenXLA compiler bisecting, [KV Roofline Compiler](scripts/kv_roofline_compiler.py) |
| **Edge & NPU Workstation** | **AMD Ryzen AI 9 HX370** (XDNA 2 NPU + Radeon 890M) · `aarch64` / Linux container parity | Local agent control loops, low-latency MCP gateway testing, [RAG Citation Verifier](scripts/rag_citation_verifier.py) |
| **Routing & Observability Plane** | Ollama-compatible model routers · Docker/OCI · Prometheus & OpenTelemetry collectors | [model-tools](https://github.com/Hardonian/model-tools) · [autopilot](https://github.com/Hardonian/autopilot) · [api-tools](https://github.com/Hardonian/api-tools) |

<details>
<summary><strong>Reproduce &amp; verify this profile locally</strong></summary>

<br />

Every project claim, live CI workflow badge, local SVG asset, and external link in this README is continuously verified by automated test suites:

```bash
git clone https://github.com/Hardonian/Hardonian.git
cd Hardonian
python -m unittest discover -s tests -v
python scripts/profile-metadata.py --check --verify-remote
python scripts/profile-link-audit.py
```

</details>

---

## About

I am a **Solutions Architect at McGraw Hill** and build the Hardonia ecosystem independently from Toronto. My career combines enterprise-scale technical strategy with hands-on systems engineering: designing distributed control planes, formal state models, multi-tenant TypeScript/Rust/Go services, and database-kernel security boundaries.

I also contribute specialized part-time expertise to confidential frontier-AI evaluation and systems initiatives (client, model, dataset, and internal research details remain strictly private).

- **Enterprise Architecture & Integration:** Deep field experience integrating identity providers, event buses, and institutional platforms (`OAuth 2.0`, `Keycloak OIDC`, `SCIM`, `LTI 1.3 Advantage`, `OneRoster 1.2`, `MCP`, and `OpenTelemetry`).
- **Security & Governance:** Proven track record leading institutional security, data residency, `SOC 2`, and `FERPA` compliance architecture reviews.
- **Commercial Impact:** Recipient of the **President's Award for Sales Excellence**, reflecting the ability to translate rigorous systems engineering into customer trust and enterprise revenue.
- **Target Roles:** Senior / Staff Applied AI Engineer · AI Platform Engineer · Distributed Systems Engineer · Principal / Solutions Architect.

---

## Let’s talk

| Audience | Scope & Focus | Direct Channel |
| :--- | :--- | :--- |
| **Hiring Leaders & Executive Recruiters** | Senior / Staff / Principal Applied AI Engineer · AI Platform Engineer · Distributed Systems Engineer · Principal Solutions Architect | [LinkedIn](https://www.linkedin.com/in/scottrmhardie/) · [Email](mailto:scottrmhardie@gmail.com?subject=Engineering%20or%20Architecture%20Role) · [Executive Brief](EXECUTIVE_BRIEF.md) |
| **Founders, Investors & Technical Advisory** | AI control-plane architecture reviews, multi-tenant database isolation audits, LLM FinOps governance, and technical due diligence | [LinkedIn](https://www.linkedin.com/in/scottrmhardie/) · [Email](mailto:scottrmhardie@gmail.com?subject=Architecture%20Advisory%20or%20Due%20Diligence) · [Architecture Playbook](architecture-playbook/README.md) |

<div align="center">

[![Read the Executive Brief](https://img.shields.io/badge/DOSSIER-EXECUTIVE_BRIEF-0369a1?style=for-the-badge&labelColor=0f172a)](EXECUTIVE_BRIEF.md)
[![Explore the Architecture Playbook](https://img.shields.io/badge/PLAYBOOK-SYSTEM_ARCHITECTURE-047857?style=for-the-badge&labelColor=0f172a)](architecture-playbook/README.md)
[![Connect with Scott Hardie on LinkedIn](https://img.shields.io/badge/LINKEDIN-SCOTT_HARDIE-0A66C2?style=for-the-badge&labelColor=0f172a&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/scottrmhardie/)
[![Send an email to Scott Hardie](https://img.shields.io/badge/EMAIL-SCOTTRMHARDIE%40GMAIL.COM-4338ca?style=for-the-badge&labelColor=0f172a&logo=gmail&logoColor=white)](mailto:scottrmhardie@gmail.com?subject=Role%20or%20systems%20conversation)

<br />

<sub><strong>Hardonia</strong> · Local Compute · Deterministic Control · Kernel Isolation · Verifiable Outcomes</sub>

</div>
