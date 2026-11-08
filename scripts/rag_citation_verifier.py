#!/usr/bin/env python3
"""Permission-aware hybrid RAG retrieval (RRF) and cryptographic citation provenance verifier."""

from __future__ import annotations

import hashlib
import math
import re
from dataclasses import dataclass
from typing import Sequence

CITATION_PATTERN = re.compile(r"\[cite:([a-zA-Z0-9_-]+)@([0-9a-f]{12})\]")
TOKEN_PATTERN = re.compile(r"[a-z0-9]+")


class ProvenanceError(ValueError):
    """Raised when a retrieval or citation provenance invariant is violated."""


@dataclass(frozen=True)
class SessionClaims:
    tenant_id: str
    roles: frozenset[str]

    def __post_init__(self) -> None:
        if not self.tenant_id.strip():
            raise ProvenanceError("session tenant_id must be non-empty")


@dataclass(frozen=True)
class DocumentChunk:
    chunk_id: str
    tenant_id: str
    allowed_roles: frozenset[str]
    text: str
    embedding: tuple[float, ...]

    @property
    def sha256_hex(self) -> str:
        payload = f"{self.tenant_id}:{self.chunk_id}:{self.text}".encode("utf-8")
        return hashlib.sha256(payload).hexdigest()

    @property
    def digest_prefix(self) -> str:
        return self.sha256_hex[:12]


@dataclass(frozen=True)
class ScoredChunk:
    chunk: DocumentChunk
    dense_rank: int
    lexical_rank: int
    rrf_score: float


@dataclass(frozen=True)
class CitationReceipt:
    tenant_id: str
    verified_citations: tuple[str, ...]
    grounded_claim_count: int
    receipt_sha256: str


def tokenize(text: str) -> list[str]:
    return TOKEN_PATTERN.findall(text.lower())


def cosine_similarity(vec_a: Sequence[float], vec_b: Sequence[float]) -> float:
    if len(vec_a) != len(vec_b) or not vec_a:
        raise ProvenanceError("embedding vectors must have identical non-zero dimension")
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return dot / (norm_a * norm_b)


def bm25_score(
    query_tokens: Sequence[str],
    doc_tokens: Sequence[str],
    *,
    avg_doc_len: float,
    doc_count: int,
    doc_freqs: dict[str, int],
    k1: float = 1.5,
    b: float = 0.75,
) -> float:
    if not doc_tokens or not query_tokens or avg_doc_len <= 0.0:
        return 0.0
    counts: dict[str, int] = {}
    for tok in doc_tokens:
        counts[tok] = counts.get(tok, 0) + 1
    doc_len = float(len(doc_tokens))
    score = 0.0
    for term in dict.fromkeys(query_tokens):
        tf = counts.get(term, 0)
        if tf == 0:
            continue
        df = doc_freqs.get(term, 0)
        idf = math.log(1.0 + (doc_count - df + 0.5) / (df + 0.5))
        denom = tf + k1 * (1.0 - b + b * (doc_len / avg_doc_len))
        score += idf * ((tf * (k1 + 1.0)) / denom)
    return score


def retrieve_hybrid_rrf(
    claims: SessionClaims,
    corpus: Sequence[DocumentChunk],
    query_text: str,
    query_embedding: Sequence[float],
    *,
    top_k: int = 5,
    rrf_k: int = 60,
) -> list[ScoredChunk]:
    """Filter corpus strictly by tenant + RBAC claims BEFORE ranking, then fuse via RRF."""
    if top_k < 1 or rrf_k < 1:
        raise ProvenanceError("top_k and rrf_k must be positive integers")

    # Kernel/pre-index invariant: unauthorized chunks are invisible before scoring
    authorized = [
        chunk
        for chunk in corpus
        if chunk.tenant_id == claims.tenant_id and bool(chunk.allowed_roles & claims.roles)
    ]
    if not authorized:
        return []

    query_tokens = tokenize(query_text)
    tokenized_docs = {chunk.chunk_id: tokenize(chunk.text) for chunk in authorized}
    avg_len = sum(len(tokens) for tokens in tokenized_docs.values()) / len(authorized)

    doc_freqs: dict[str, int] = {}
    for tokens in tokenized_docs.values():
        for term in set(tokens):
            doc_freqs[term] = doc_freqs.get(term, 0) + 1

    dense_Order = sorted(
        authorized,
        key=lambda c: (cosine_similarity(query_embedding, c.embedding), c.chunk_id),
        reverse=True,
    )
    lexical_order = sorted(
        authorized,
        key=lambda c: (
            bm25_score(
                query_tokens,
                tokenized_docs[c.chunk_id],
                avg_doc_len=avg_len,
                doc_count=len(authorized),
                doc_freqs=doc_freqs,
            ),
            c.chunk_id,
        ),
        reverse=True,
    )

    dense_ranks = {chunk.chunk_id: idx + 1 for idx, chunk in enumerate(dense_Order)}
    lexical_ranks = {chunk.chunk_id: idx + 1 for idx, chunk in enumerate(lexical_order)}

    scored: list[ScoredChunk] = []
    for chunk in authorized:
        d_rank = dense_ranks[chunk.chunk_id]
        l_rank = lexical_ranks[chunk.chunk_id]
        rrf = (1.0 / (rrf_k + d_rank)) + (1.0 / (rrf_k + l_rank))
        scored.append(
            ScoredChunk(
                chunk=chunk,
                dense_rank=d_rank,
                lexical_rank=l_rank,
                rrf_score=round(rrf, 8),
            )
        )

    scored.sort(key=lambda item: (-item.rrf_score, item.dense_rank, item.chunk.chunk_id))
    return scored[:top_k]


def verify_response_citations(
    claims: SessionClaims,
    retrieved: Sequence[ScoredChunk],
    response_sentences: Sequence[str],
    *,
    min_token_overlap: int = 2,
) -> CitationReceipt:
    """Verify every sentence carries a valid cryptographic citation grounded in authorized chunks."""
    if not response_sentences:
        raise ProvenanceError("response_sentences cannot be empty")

    authorized_map = {
        item.chunk.chunk_id: item.chunk
        for item in retrieved
        if item.chunk.tenant_id == claims.tenant_id
        and bool(item.chunk.allowed_roles & claims.roles)
    }

    verified_ids: list[str] = []
    for sentence in response_sentences:
        matches = CITATION_PATTERN.findall(sentence)
        if not matches:
            raise ProvenanceError(f"ungrounded claim missing citation tag: {sentence!r}")

        clean_sentence = CITATION_PATTERN.sub("", sentence)
        sentence_tokens = set(tokenize(clean_sentence))

        for chunk_id, digest_prefix in matches:
            chunk = authorized_map.get(chunk_id)
            if chunk is None:
                raise ProvenanceError(
                    f"citation references unauthorized or unretrieved chunk: {chunk_id}"
                )
            if chunk.digest_prefix != digest_prefix:
                raise ProvenanceError(
                    f"cryptographic digest mismatch for {chunk_id}: "
                    f"expected {chunk.digest_prefix}, got {digest_prefix}"
                )
            chunk_tokens = set(tokenize(chunk.text))
            if len(sentence_tokens & chunk_tokens) < min_token_overlap:
                raise ProvenanceError(
                    f"claim tokens insufficiently grounded in cited chunk {chunk_id}"
                )
            verified_ids.append(f"{chunk_id}@{digest_prefix}")

    canonical = "|".join(
        [claims.tenant_id, str(len(response_sentences)), *verified_ids]
    ).encode("utf-8")
    receipt_hash = hashlib.sha256(canonical).hexdigest()
    return CitationReceipt(
        tenant_id=claims.tenant_id,
        verified_citations=tuple(verified_ids),
        grounded_claim_count=len(response_sentences),
        receipt_sha256=receipt_hash,
    )

