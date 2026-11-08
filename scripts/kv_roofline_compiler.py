#!/usr/bin/env python3
"""Deterministic GPU Roofline and PagedAttention KV-cache serving topology compiler."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Sequence

BYTES_PER_GIB = 1024**3
PAGED_BLOCK_TOKENS = 16


class TopologyCompileError(ValueError):
    """Raised when no hardware topology satisfies memory, latency, or budget constraints."""


@dataclass(frozen=True)
class AcceleratorSpec:
    name: str
    architecture: str
    vram_gib: float
    mem_bandwidth_gbps: float
    fp16_tflops: float
    int8_tops: float
    hourly_cost_usd: float

    @property
    def ridge_point_ops_per_byte(self) -> float:
        """Arithmetic intensity (FLOP/byte) separating memory-bound vs compute-bound regimes."""
        return (self.fp16_tflops * 1e12) / (self.mem_bandwidth_gbps * 1e9)


@dataclass(frozen=True)
class ModelArchitectureSpec:
    name: str
    params_billions: float
    num_layers: int
    num_qo_heads: int
    num_kv_heads: int
    head_dim: int


@dataclass(frozen=True)
class WorkloadSLO:
    batch_size: int
    prompt_tokens: int
    output_tokens: int
    max_ttft_ms: float
    max_itl_ms: float


@dataclass(frozen=True)
class CompiledTopology:
    accelerator: str
    tensor_parallel_degree: int
    weight_bits: int
    kv_cache_bits: int
    weights_gib: float
    kv_cache_gib: float
    paged_blocks_allocated: int
    prefill_regime: str
    decode_regime: str
    estimated_ttft_ms: float
    estimated_itl_ms: float
    hourly_cost_usd: float


LAB_ACCELERATORS: tuple[AcceleratorSpec, ...] = (
    AcceleratorSpec(
        name="NVIDIA Tesla V100-SXM2-32GB",
        architecture="Volta (SM70 · HBM2)",
        vram_gib=32.0,
        mem_bandwidth_gbps=900.0,
        fp16_tflops=125.0,
        int8_tops=62.0,
        hourly_cost_usd=0.95,
    ),
    AcceleratorSpec(
        name="NVIDIA GeForce RTX 3060-12GB",
        architecture="Ampere (SM86 · GDDR6)",
        vram_gib=12.0,
        mem_bandwidth_gbps=360.0,
        fp16_tflops=51.0,
        int8_tops=102.0,
        hourly_cost_usd=0.35,
    ),
    AcceleratorSpec(
        name="NVIDIA Tesla P40-24GB",
        architecture="Pascal (SM61 · GDDR5)",
        vram_gib=24.0,
        mem_bandwidth_gbps=346.0,
        fp16_tflops=12.0,
        int8_tops=47.0,
        hourly_cost_usd=0.40,
    ),
    AcceleratorSpec(
        name="AMD Ryzen AI 9 HX370-Unified",
        architecture="XDNA 2 + RDNA 3.5 (LPDDR5X)",
        vram_gib=24.0,
        mem_bandwidth_gbps=120.0,
        fp16_tflops=32.0,
        int8_tops=80.0,
        hourly_cost_usd=0.20,
    ),
)


def kv_bytes_per_token(model: ModelArchitectureSpec, kv_bits: int) -> float:
    """Compute exact KV-cache footprint per token across all GQA/MHA layers:
    2 (K and V) * num_layers * num_kv_heads * head_dim * (kv_bits / 8).
    """
    if kv_bits not in {4, 8, 16}:
        raise TopologyCompileError(f"unsupported kv_bits: {kv_bits}")
    bytes_per_elem = kv_bits / 8.0
    return 2.0 * model.num_layers * model.num_kv_heads * model.head_dim * bytes_per_elem


def compile_serving_topology(
    model: ModelArchitectureSpec,
    slo: WorkloadSLO,
    accelerators: Sequence[AcceleratorSpec] = LAB_ACCELERATORS,
    *,
    vram_headroom_ratio: float = 0.88,
) -> CompiledTopology:
    """Select the lowest-cost (accelerator, TP, quantization) tuple meeting VRAM and latency SLOs."""
    if slo.batch_size < 1 or slo.prompt_tokens < 1 or slo.output_tokens < 1:
        raise TopologyCompileError("batch_size, prompt_tokens, and output_tokens must be >= 1")

    seq_len = slo.prompt_tokens + slo.output_tokens
    blocks_per_seq = math.ceil(seq_len / PAGED_BLOCK_TOKENS)
    total_paged_blocks = slo.batch_size * blocks_per_seq
    padded_tokens = total_paged_blocks * PAGED_BLOCK_TOKENS

    candidates: list[CompiledTopology] = []

    for accel in accelerators:
        for tp in (1, 2):
            for weight_bits, kv_bits in ((16, 16), (8, 8), (4, 8), (4, 4)):
                weights_bytes = model.params_billions * 1e9 * (weight_bits / 8.0) * 1.05
                kv_bytes = padded_tokens * kv_bytes_per_token(model, kv_bits)
                total_gib = (weights_bytes + kv_bytes) / BYTES_PER_GIB
                usable_vram_gib = accel.vram_gib * tp * vram_headroom_ratio

                if total_gib > usable_vram_gib:
                    continue

                eff_bw_gbps = accel.mem_bandwidth_gbps * tp * (0.92 if tp == 1 else 0.84)
                eff_tflops = accel.fp16_tflops * tp * (0.90 if tp == 1 else 0.82)

                # Prefill arithmetic intensity: ~2 * P * B * S FLOPs vs weights + KV read/write
                prefill_flops = 2.0 * (model.params_billions * 1e9) * slo.batch_size * slo.prompt_tokens
                prefill_bytes = weights_bytes + (slo.batch_size * slo.prompt_tokens * kv_bytes_per_token(model, kv_bits))
                prefill_ai = prefill_flops / prefill_bytes
                prefill_regime = (
                    "compute-bound" if prefill_ai >= accel.ridge_point_ops_per_byte else "memory-bound"
                )
                ttft_compute_s = prefill_flops / (eff_tflops * 1e12)
                ttft_mem_s = prefill_bytes / (eff_bw_gbps * 1e9)
                ttft_ms = max(ttft_compute_s, ttft_mem_s) * 1000.0

                # Autoregressive decode step: memory-bandwidth-bound reading weights + active KV cache
                decode_flops = 2.0 * (model.params_billions * 1e9) * slo.batch_size
                decode_bytes = weights_bytes + kv_bytes
                decode_ai = decode_flops / decode_bytes
                decode_regime = (
                    "compute-bound" if decode_ai >= accel.ridge_point_ops_per_byte else "memory-bound"
                )
                itl_compute_s = decode_flops / (eff_tflops * 1e12)
                itl_mem_s = decode_bytes / (eff_bw_gbps * 1e9)
                itl_ms = max(itl_compute_s, itl_mem_s) * 1000.0

                if ttft_ms <= slo.max_ttft_ms and itl_ms <= slo.max_itl_ms:
                    candidates.append(
                        CompiledTopology(
                            accelerator=accel.name,
                            tensor_parallel_degree=tp,
                            weight_bits=weight_bits,
                            kv_cache_bits=kv_bits,
                            weights_gib=round(weights_bytes / BYTES_PER_GIB, 3),
                            kv_cache_gib=round(kv_bytes / BYTES_PER_GIB, 3),
                            paged_blocks_allocated=total_paged_blocks,
                            prefill_regime=prefill_regime,
                            decode_regime=decode_regime,
                            estimated_ttft_ms=round(ttft_ms, 2),
                            estimated_itl_ms=round(itl_ms, 2),
                            hourly_cost_usd=round(accel.hourly_cost_usd * tp, 2),
                        )
                    )

    if not candidates:
        raise TopologyCompileError("no hardware topology satisfies the requested VRAM and latency SLOs")

    # Prefer lowest hourly cost, then highest precision (weight_bits + kv_bits), then lowest ITL
    candidates.sort(
        key=lambda c: (c.hourly_cost_usd, -(c.weight_bits + c.kv_cache_bits), c.estimated_itl_ms)
    )
    return candidates[0]
