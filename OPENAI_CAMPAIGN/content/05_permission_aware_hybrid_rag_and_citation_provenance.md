# 05 // Permission-Aware Hybrid RAG & Cryptographic Citation Provenance

**Author**: Scott Hardie  
**Technical Domain**: Retrieval-Augmented Generation (RAG), Sub-Document RBAC/ABAC, Reciprocal Rank Fusion (RRF), Citation Verification  
**Repository Reference**: [`Hardonian/Settler` (`v1.8.0`)](https://github.com/Hardonian/Settler), [`Hardonian/AgentAxiom`](https://github.com/Hardonian/AgentAxiom) & [`scripts/rag_citation_verifier.py`](../../scripts/rag_citation_verifier.py)  
**Series Navigation**: [**Profile README**](../../README.md) · [01: Postgres RLS](01_safe_multi_tenant_ai_agents_postgres_rls.md) · [02: MCP Authorization](02_enterprise_tool_calling_authorization_outside_model.md) · [03: Prototype to Production](03_from_prototype_to_production_enterprise_agents.md) · [04: ZK eBPF & Causal DAGs](04_zero_knowledge_ebpf_sandboxing_and_causal_dags.md) · **05: Hybrid RAG & Provenance** · [06: GPU Roofline & KV-Cache](06_gpu_kv_cache_roofline_and_serving_topology.md)

---

## 1. Two Structural Failures in Production RAG

Enterprise retrieval systems routinely fail security and audit reviews for two reasons:

1. **Post-Filtering Vector Leakage & HNSW Recall Collapse**: Many pipelines run an Approximate Nearest Neighbor (ANN) `pgvector` HNSW search across a global index first and apply application-level role filters afterward. If a low-privilege user's top-$k$ nearest neighbors belong to restricted executive documents, post-filtering either leaks existence timing or returns zero results (`recall collapse`), while any bug in the post-filter leaks restricted chunks across roles.
2. **Unverified Hallucinated Citations**: Prompting a model to *"cite your sources as [1], [2]"* does not prove that the cited chunk was actually retrieved in the current session, that the user was authorized to read it, or that the generated claim shares lexical/semantic support with the cited span.

---

## 2. Pre-Filtered Hybrid Retrieval (`FORCE RLS` + BM25 + `pgvector` RRF)

To guarantee zero cross-tenant or cross-role leakage, access control must execute as a **relational predicate inside PostgreSQL before score fusion**:

```sql
CREATE TABLE knowledge_chunks (
    chunk_id        TEXT PRIMARY KEY,
    tenant_id       UUID NOT NULL,
    allowed_roles   TEXT[] NOT NULL,
    content         TEXT NOT NULL,
    content_tsv     TSVECTOR GENERATED ALWAYS AS (to_tsvector('english', content)) STORED,
    embedding       vector(1536) NOT NULL,
    chunk_sha256    CHAR(64) NOT NULL
);

ALTER TABLE knowledge_chunks ENABLE ROW LEVEL SECURITY;
ALTER TABLE knowledge_chunks FORCE ROW LEVEL SECURITY;

-- Enforce BOTH tenant boundary AND sub-document role intersection in the kernel
CREATE POLICY chunk_tenant_and_rbac_isolation ON knowledge_chunks
    FOR SELECT
    TO authenticated_role
    USING (
        tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::UUID
        AND allowed_roles && string_to_array(
            NULLIF(current_setting('app.current_user_roles', true), ''), ','
        )
    );
```

### Reciprocal Rank Fusion (RRF) Over Authorized Tuples

Within the RLS-scoped transaction, dense cosine similarity (`embedding <=> $1`) and lexical BM25/ts_rank (`content_tsv @@ plainto_tsquery($2)`) are combined via Reciprocal Rank Fusion ($k = 60$):

$$\text{RRF}(d) = \frac{1}{k + \text{rank}_{\text{dense}}(d)} + \frac{1}{k + \text{rank}_{\text{lexical}}(d)}$$

---

## 3. Cryptographic Span-Level Citation Verification

Every authorized chunk injected into the model's context carries a deterministic 12-character SHA-256 commitment prefix computed over `tenant_id : chunk_id : content`:

```text
[Context Chunk: chk_01@8f4a2c91b03e]
Quarterly settlement reconciliation requires SHA256 ledger verification.
```

Before returning a model response to the caller, the deterministic verifier in [`scripts/rag_citation_verifier.py`](../../scripts/rag_citation_verifier.py) enforces four invariants on every emitted sentence:

1. **Citation Presence**: Every factual sentence must contain at least one `[cite:<chunk_id>@<sha256_prefix>]` tag.
2. **Session Authorization Membership**: `<chunk_id>` must exist in the current session's RLS-filtered retrieval set.
3. **Cryptographic Digest Integrity**: `<sha256_prefix>` must match `SHA256(tenant_id : chunk_id : text)[:12]`, preventing prompt-injected or fabricated chunk IDs.
4. **Lexical Grounding Overlap**: The non-stopword token intersection between the sentence and the cited chunk must meet the minimum grounding threshold (`min_token_overlap`).

---

## 4. Executable Verification in This Repository

The reference implementation ([`scripts/rag_citation_verifier.py`](../../scripts/rag_citation_verifier.py)) and its test suite ([`tests/test_rag_citation_verifier.py`](../../tests/test_rag_citation_verifier.py)) run as part of the standard repository test suite:

```bash
python -m unittest tests/test_rag_citation_verifier.py -v
```

---

**Next in the Hardonia Architecture Series →** [06 // GPU KV-Cache Roofline Modeling & Deterministic Serving Topology](06_gpu_kv_cache_roofline_and_serving_topology.md) · [Return to Profile README](../../README.md)

