import importlib.util
import sys
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "kv_roofline_compiler", Path(__file__).parents[1] / "scripts/kv_roofline_compiler.py"
)
roofline = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = roofline
SPEC.loader.exec_module(roofline)


class KvRooflineCompilerTests(unittest.TestCase):
    def setUp(self):
        # Llama-3-8B GQA architecture (32 layers, 32 Q heads, 8 KV heads, 128 head_dim)
        self.llama_8b = roofline.ModelArchitectureSpec(
            name="Llama-3-8B-Instruct",
            params_billions=8.03,
            num_layers=32,
            num_qo_heads=32,
            num_kv_heads=8,
            head_dim=128,
        )

    def test_computes_exact_gqa_kv_bytes_per_token(self):
        # 2 * 32 * 8 * 128 * 2 bytes (FP16) = 131,072 bytes (128 KiB) per token
        self.assertEqual(roofline.kv_bytes_per_token(self.llama_8b, 16), 131072.0)
        # INT8 KV cache halves footprint to 65,536 bytes (64 KiB) per token
        self.assertEqual(roofline.kv_bytes_per_token(self.llama_8b, 8), 65536.0)

    def test_prefill_is_compute_bound_and_decode_is_memory_bound(self):
        slo = roofline.WorkloadSLO(
            batch_size=4,
            prompt_tokens=1024,
            output_tokens=256,
            max_ttft_ms=1500.0,
            max_itl_ms=45.0,
        )
        compiled = roofline.compile_serving_topology(self.llama_8b, slo)
        self.assertEqual(compiled.prefill_regime, "compute-bound")
        self.assertEqual(compiled.decode_regime, "memory-bound")
        self.assertLessEqual(compiled.estimated_ttft_ms, slo.max_ttft_ms)
        self.assertLessEqual(compiled.estimated_itl_ms, slo.max_itl_ms)

    def test_raises_when_slo_impossible(self):
        impossible_slo = roofline.WorkloadSLO(
            batch_size=64,
            prompt_tokens=32768,
            output_tokens=4096,
            max_ttft_ms=1.0,
            max_itl_ms=0.1,
        )
        with self.assertRaises(roofline.TopologyCompileError):
            roofline.compile_serving_topology(self.llama_8b, impossible_slo)


if __name__ == "__main__":
    unittest.main()
