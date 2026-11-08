import importlib.util
import sys
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "rag_citation_verifier", Path(__file__).parents[1] / "scripts/rag_citation_verifier.py"
)
rag = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = rag
SPEC.loader.exec_module(rag)


class RagCitationVerifierTests(unittest.TestCase):
    def setUp(self):
        self.chunk_alpha_finance = rag.DocumentChunk(
            chunk_id="chk_01",
            tenant_id="tenant_alpha",
            allowed_roles=frozenset({"finance_auditor", "admin"}),
            text="Quarterly settlement reconciliation requires SHA256 ledger verification.",
            embedding=(0.9, 0.1, 0.0),
        )
        self.chunk_alpha_support = rag.DocumentChunk(
            chunk_id="chk_02",
            tenant_id="tenant_alpha",
            allowed_roles=frozenset({"support_agent", "finance_auditor"}),
            text="Customer support tickets escalate after forty eight hours.",
            embedding=(0.1, 0.9, 0.0),
        )
        self.chunk_beta_secret = rag.DocumentChunk(
            chunk_id="chk_99",
            tenant_id="tenant_beta",
            allowed_roles=frozenset({"finance_auditor", "admin"}),
            text="Tenant beta confidential wire transfer settlement ledger.",
            embedding=(0.95, 0.05, 0.0),
        )
        self.corpus = [
            self.chunk_alpha_finance,
            self.chunk_alpha_support,
            self.chunk_beta_secret,
        ]

    def test_blocks_cross_tenant_and_unauthorized_role_chunks_prior_to_rrf(self):
        # Support agent in tenant_alpha must never see chk_01 (finance only) or chk_99 (tenant_beta)
        claims = rag.SessionClaims(
            tenant_id="tenant_alpha",
            roles=frozenset({"support_agent"}),
        )
        results = rag.retrieve_hybrid_rrf(
            claims,
            self.corpus,
            "settlement ledger reconciliation",
            (0.95, 0.05, 0.0),
        )
        self.assertEqual([r.chunk.chunk_id for r in results], ["chk_02"])

    def test_hybrid_rrf_ranks_matching_authorized_chunk_first(self):
        claims = rag.SessionClaims(
            tenant_id="tenant_alpha",
            roles=frozenset({"finance_auditor"}),
        )
        results = rag.retrieve_hybrid_rrf(
            claims,
            self.corpus,
            "settlement reconciliation SHA256 ledger",
            (0.92, 0.08, 0.0),
        )
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].chunk.chunk_id, "chk_01")
        self.assertGreater(results[0].rrf_score, results[1].rrf_score)

    def test_verifies_cryptographically_grounded_citations(self):
        claims = rag.SessionClaims(
            tenant_id="tenant_alpha",
            roles=frozenset({"finance_auditor"}),
        )
        retrieved = rag.retrieve_hybrid_rrf(
            claims,
            self.corpus,
            "settlement reconciliation ledger",
            (0.92, 0.08, 0.0),
        )
        tag = f"[cite:chk_01@{self.chunk_alpha_finance.digest_prefix}]"
        sentences = [f"Settlement reconciliation enforces SHA256 ledger checks {tag}."]
        receipt = rag.verify_response_citations(claims, retrieved, sentences)
        self.assertEqual(receipt.grounded_claim_count, 1)
        self.assertEqual(len(receipt.receipt_sha256), 64)

    def test_rejects_tampered_digest_or_missing_citation(self):
        claims = rag.SessionClaims(
            tenant_id="tenant_alpha",
            roles=frozenset({"finance_auditor"}),
        )
        retrieved = rag.retrieve_hybrid_rrf(
            claims,
            self.corpus,
            "settlement reconciliation ledger",
            (0.92, 0.08, 0.0),
        )
        with self.assertRaisesRegex(rag.ProvenanceError, "missing citation"):
            rag.verify_response_citations(claims, retrieved, ["Uncited settlement claim."])

        with self.assertRaisesRegex(rag.ProvenanceError, "digest mismatch"):
            rag.verify_response_citations(
                claims,
                retrieved,
                ["Settlement reconciliation ledger [cite:chk_01@000000000000]."],
            )


if __name__ == "__main__":
    unittest.main()
