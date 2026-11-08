# 06 // GPU KV-Cache Roofline Modeling & Deterministic Serving Topology

**Author**: Scott Hardie  
**Technical Domain**: GPU Kernel Engineering, Roofline Performance Modeling, PagedAttention KV-Cache, Quantized LLM Serving  
**Repository Reference**: [`Hardonian/XLAxiom`](https://github.com/Hardonian/XLAxiom), [`Hardonian/TokenGoblin`](https://github.com/Hardonian/TokenGoblin) & [`scripts/kv_roofline_compiler.py`](../../scripts/kv_roofline_compiler.py)  
**Series Navigation**: [**Profile README**](../../README.md) · [01: Postgres RLS](01_safe_multi_tenant_ai_agents_postgres_rls.md) · [02: MCP Authorization](02_enterprise_tool_calling_authorization_outside_model.md) · [03: Prototype to Production](03_from_prototype_to_production_enterprise_agents.md) · [04: ZK eBPF & Causal DAGs](04_zero_knowledge_ebpf_sandboxing_and_causal_dags.md) · [05: Hybrid RAG & Provenance](05_permission_aware_hybrid_rag_and_citation_provenance.md) · **06: GPU Roofline & KV-Cache**

---

## 1. Why Inference Economics Starts at the Memory Bus

Treating LLM inference purely as an API billing problem misses the underlying hardware physics. Transformer inference consists of two distinct hardware regimes separated by the accelerator's **Roofline Ridge Point** ($\mathcal{I}_{\text{ridge}} = \text{Peak FLOP/s} \div \text{Peak Memory Bandwidth}$):

1. **Prefill Phase (Compute-Bound, High Arithmetic Intensity)**: Processing $B \times S_{\text{prompt}}$ tokens in parallel performs $\approx 2 \cdot P \cdot B \cdot S_{\text{prompt}}$ FLOPs per weight read. Latency (Time-To-First-Token, `TTFT`) is governed by tensor-core throughput (`TFLOP/s`).
2. **Autoregressive Decode Phase (Memory-Bandwidth-Bound, Low Arithmetic Intensity)**: Generating 1 token per sequence streams the entire quantized weight matrix plus the active Key-Value (`KV`) cache across HBM/GDDR memory for only $2 \cdot P \cdot B$ FLOPs. Inter-Token Latency (`ITL`) is strictly lower-bounded by memory bandwidth:

$$\text{ITL}_{\min} = \frac{\text{Bytes}_{\text{weights}} + \text{Bytes}_{\text{KV}}(B, S_{\text{ctx}})}{\text{Bandwidth}_{\text{effective}}}$$

---

## 2. Exact Grouped-Query Attention (GQA) KV-Cache Footprint

For a model with $L$ layers, $H_{kv}$ key-value heads, head dimension $D_h$, and KV precision $b_{kv} \in \{4, 8, 16\}$ bits, the exact KV-cache memory per token is:

$$\text{Bytes}_{\text{KV/token}} = 2 \times L \times H_{kv} \times D_h \times \left(\frac{b_{kv}}{8}\right)$$

With **PagedAttention** block size $B_{\text{page}} = 16$ tokens, a batch of $B$ sequences of length $S = S_{\text{prompt}} + S_{\text{out}}$ allocates:

$$N_{\text{blocks}} = B \times \left\lceil \frac{S}{16} \right\rceil, \qquad \text{Bytes}_{\text{KV\_total}} = 16 \cdot N_{\text{blocks}} \cdot \text{Bytes}_{\text{KV/token}}$$

| Model Architecture | Layers ($L$) | $H_q / H_{kv}$ | $D_h$ | `FP16` KV / Token | `INT8` KV / Token | `INT4` KV / Token |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Llama-3-8B-Instruct** (GQA) | 32 | `32 / 8` | 128 | `128 KiB` | `64 KiB` | `32 KiB` |
| **Llama-3-70B-Instruct** (GQA) | 80 | `64 / 8` | 128 | `320 KiB` | `160 KiB` | `80 KiB` |

---

## 3. Hardware Lab Roofline Profile

The topology compiler in [`scripts/kv_roofline_compiler.py`](../../scripts/kv_roofline_compiler.py) models the four accelerator tiers in the Hardonia local hardware testbed:

| Accelerator | Architecture | VRAM | Memory Bandwidth | Peak FP16 / INT8 | Ridge Point ($\text{FLOP/Byte}$) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **NVIDIA Tesla V100-SXM2** | Volta (`SM70` · HBM2) | `32 GiB` | `900 GB/s` | `125 TFLOPS` | `138.9` |
| **NVIDIA GeForce RTX 3060** | Ampere (`SM86` · GDDR6) | `12 GiB` | `360 GB/s` | `51 TFLOPS` / `102 TOPS` | `141.7` |
| **NVIDIA Tesla P40** | Pascal (`SM61` · GDDR5) | `24 GiB` | `346 GB/s` | `12 TFLOPS` / `47 TOPS` | `34.7` |
| **AMD Ryzen AI 9 HX370** | XDNA 2 + RDNA 3.5 | `24 GiB` | `120 GB/s` | `32 TFLOPS` / `80 TOPS` | `266.7` |

---

## 4. Fused INT4 Dequant-GEMV Kernel Pattern (OpenAI Triton)

Because autoregressive decode is memory-bandwidth-bound ($\mathcal{I} \ll \mathcal{I}_{\text{ridge}}$), storing weights in `INT4` (2 weights packed per `uint8` byte with group size $G = 128$ `FP16` scales/zeros) and dequantizing inside registers **cuts HBM/GDDR traffic by ~3.5x**, directly accelerating `ITL`:

```python
import triton
import triton.language as tl

@triton.jit
def fused_int4_dequant_gemv_kernel(
    x_ptr,          # [K] FP16 activation vector
    qweight_ptr,    # [N, K // 2] uint8 packed INT4 weights
    scales_ptr,     # [N, K // 128] FP16 group scales
    out_ptr,        # [N] FP16 output vector
    N: tl.constexpr,
    K: tl.constexpr,
    BLOCK_K: tl.constexpr,
):
    row_idx = tl.program_id(0)
    acc = tl.zeros((BLOCK_K,), dtype=tl.float32)

    for k_offset in range(0, K, BLOCK_K):
        k_indices = k_offset + tl.arange(0, BLOCK_K)
        packed_idx = row_idx * (K // 2) + (k_indices // 2)
        packed_byte = tl.load(qweight_ptr + packed_idx)

        # Unpack low/high 4-bit nibbles in registers (zero extra global memory reads)
        shift = (k_indices % 2) * 4
        int4_val = ((packed_byte >> shift) & 0x0F).to(tl.int8) - 8

        scale_idx = row_idx * (K // 128) + (k_indices // 128)
        scale = tl.load(scales_ptr + scale_idx).to(tl.float32)

        w_fp32 = int4_val.to(tl.float32) * scale
        x_fp32 = tl.load(x_ptr + k_indices).to(tl.float32)
        acc += w_fp32 * x_fp32

    tl.store(out_ptr + row_idx, tl.sum(acc, axis=0).to(tl.float16))
```

---

## 5. Executable Topology Compiler Verification

The deterministic compiler in [`scripts/kv_roofline_compiler.py`](../../scripts/kv_roofline_compiler.py) evaluates `(accelerator, tensor_parallel_degree, weight_bits, kv_cache_bits)` combinations against VRAM headroom (`88%`), PagedAttention block allocation, `TTFT`, and `ITL` SLOs:

```bash
python -m unittest tests/test_kv_roofline_compiler.py -v
```

---

**Series Complete · Explore Further →** [Hardonia Architecture Playbook](../../architecture-playbook/README.md) · [Executive & Technical Brief](../../EXECUTIVE_BRIEF.md) · [Return to Profile README](../../README.md)
