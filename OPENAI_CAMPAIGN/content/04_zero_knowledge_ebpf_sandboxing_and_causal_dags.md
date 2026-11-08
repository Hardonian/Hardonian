# 04 // Zero-Knowledge eBPF Sandboxing & Causal DAG Execution for Autonomous Systems

**Author**: Scott Hardie  
**Technical Domain**: Kernel Isolation, Formal State Machines (Quint), Zero-Knowledge Proofs, Distributed Control Planes  
**Repository Reference**: [`Hardonian/zerokernel` (`v1.0.0`)](https://github.com/Hardonian/zerokernel), [`Hardonian/veridag`](https://github.com/Hardonian/veridag), [`Hardonian/ControlPlane` (`v1.0.0`)](https://github.com/Hardonian/ControlPlane) & [`Hardonian/Settler` (`v1.8.0`)](https://github.com/Hardonian/Settler)  
**Series Navigation**: [**Profile README**](../../README.md) · [01: Postgres RLS](01_safe_multi_tenant_ai_agents_postgres_rls.md) · [02: MCP Authorization](02_enterprise_tool_calling_authorization_outside_model.md) · [03: Prototype to Production](03_from_prototype_to_production_enterprise_agents.md) · **04: ZK eBPF & Causal DAGs** · [Architecture Playbook](../../architecture-playbook/README.md)

---

## 1. Beyond Prompt Guards and Container Namespaces

Even after isolating tenant rows with [PostgreSQL `FORCE ROW LEVEL SECURITY`](01_safe_multi_tenant_ai_agents_postgres_rls.md) and moving tool authorization into an [external MCP policy gateway](02_enterprise_tool_calling_authorization_outside_model.md), two critical execution vulnerabilities remain when autonomous agents run multi-step workflows or untrusted code:

1. **Out-of-Order Distributed Mutation**: Concurrent workers, network retries, and speculative agent branches can apply side effects out of causal order—executing a downstream reconciliation or payout step before upstream preconditions have converged.
2. **Untrusted Compute & Unverifiable Execution**: Standard Linux containers share the host kernel syscall interface. When an autonomous workflow executes untrusted plugins, synthesized filters, or third-party transforms, a container exit code (`0`) does not cryptographically prove *which* bytecode ran or that execution stayed within instruction and memory bounds.

To close both gaps, the Hardonian architecture pairs **Quint-verified causal DAG state machines** (`veridag` / `ControlPlane`) with **zero-knowledge eBPF sandboxes** (`zerokernel`) and commits the resulting proof envelope to an **immutable reconciliation ledger** (`Settler`).

---

## 2. The Four-Plane Deterministic Execution Loop

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ 01 // HARDONIAN CONTROL PLANE (ControlPlane v1.0.0 · ReadyLayer)             │
│   • Evaluates MCP capability scope & TokenGoblin hard quota ceiling          │
│   • Mints single-use capability token bound to SHA-256 argument digest       │
└───────────────────┬──────────────────────────────────────┬───────────────────┘
                    │                                      │
                    ▼                                      ▼
┌───────────────────────────────────────┐  ┌───────────────────────────────────┐
│ 02A // CAUSAL DAG ENGINE (veridag)    │  │ 02B // ZK-eBPF SANDBOX            │
│   • Verifies parent node hashes       │  │   (zerokernel v1.0.0)             │
│   • Checks Quint state invariants     │  │   • Deterministic eBPF VM         │
│   • Enforces idempotent transition    │  │   • Strict instruction metering   │
│     ordering across workers           │  │   • Emits ZK execution receipt    │
└───────────────────┬───────────────────┘  └───────────────┬───────────────────┘
                    │                                      │
                    └───────────────────┬──────────────────┘
                                        ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ 03 // SETTLER AUDIT & RECONCILIATION LEDGER (Settler v1.8.0)                 │
│   • Verifies ZK receipt + causal DAG parent chain + PostgreSQL RLS context   │
│   • Appends SHA-256 Merkle trace leaf for deterministic replay               │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Formalizing Causal DAG Preconditions in Quint (`veridag`)

Before writing Rust worker code, state transitions are specified in [Quint](https://github.com/informalsystems/quint) so model checking can exhaustively search for invariant violations (such as executing a node before all causal parents are `Committed`, or double-applying a non-idempotent side effect):

```quint
module VeridagCausalExecution {
  type NodeState = Pending | Authorized | Executing | Committed | Aborted

  type DagNode = {
    id: str,
    parents: Set[str],
    state: NodeState,
    capability_digest: str
  }

  var nodes: str -> DagNode
  var consumed_tokens: Set[str]

  // Invariant 1: No node can be Executing or Committed unless all parents are Committed
  val causalOrderingInvariant = nodes.keys().forall(id => {
    val node = nodes.get(id)
    (node.state == Executing or node.state == Committed) implies
      node.parents.forall(p => nodes.get(p).state == Committed)
  })

  // Action: Transition an Authorized node to Executing by consuming its single-use token
  action startExecution(nodeId: str, tokenDigest: str): bool = all {
    nodes.keys().contains(nodeId),
    val node = nodes.get(nodeId)
    node.state == Authorized,
    node.capability_digest == tokenDigest,
    not(consumed_tokens.contains(tokenDigest)),
    node.parents.forall(p => nodes.get(p).state == Committed),
    nodes' = nodes.set(nodeId, { ...node, state: Executing }),
    consumed_tokens' = consumed_tokens.union(Set(tokenDigest))
  }
}
```

---

## 4. Zero-Panic Rust Enforcement in `ControlPlane` & `veridag`

In production Rust (`ControlPlane` `v1.0.0` and `veridag`), every state transition enforces the Quint preconditions using explicit `Result<T, E>` types—forbidding `.unwrap()` and `.expect()` in runtime paths:

```rust
use sha2::{Digest, Sha256};
use std::collections::{BTreeMap, BTreeSet};

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum NodeState {
    Pending,
    Authorized,
    Executing,
    Committed,
    Aborted,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum TransitionError {
    NodeNotFound(String),
    InvalidPredecessorState { node_id: String, parent_id: String, actual: NodeState },
    InvalidCurrentState { expected: NodeState, actual: NodeState },
    CapabilityDigestMismatch,
    TokenAlreadyConsumed,
}

#[derive(Debug, Clone)]
pub struct DagNode {
    pub id: String,
    pub parents: BTreeSet<String>,
    pub state: NodeState,
    pub capability_digest: [u8; 32],
}

pub struct CausalGraph {
    nodes: BTreeMap<String, DagNode>,
    consumed_tokens: BTreeSet<[u8; 32]>,
}

impl CausalGraph {
    pub fn authorize_and_begin(
        &mut self,
        node_id: &str,
        presented_token: &[u8],
    ) -> Result<[u8; 32], TransitionError> {
        let token_digest: [u8; 32] = Sha256::digest(presented_token).into();

        if self.consumed_tokens.contains(&token_digest) {
            return Err(TransitionError::TokenAlreadyConsumed);
        }

        let parent_ids = {
            let node = self
                .nodes
                .get(node_id)
                .ok_or_else(|| TransitionError::NodeNotFound(node_id.to_owned()))?;

            if node.state != NodeState::Authorized {
                return Err(TransitionError::InvalidCurrentState {
                    expected: NodeState::Authorized,
                    actual: node.state,
                });
            }
            if node.capability_digest != token_digest {
                return Err(TransitionError::CapabilityDigestMismatch);
            }
            node.parents.clone()
        };

        for parent_id in &parent_ids {
            let parent = self
                .nodes
                .get(parent_id)
                .ok_or_else(|| TransitionError::NodeNotFound(parent_id.clone()))?;
            if parent.state != NodeState::Committed {
                return Err(TransitionError::InvalidPredecessorState {
                    node_id: node_id.to_owned(),
                    parent_id: parent_id.clone(),
                    actual: parent.state,
                });
            }
        }

        if let Some(node) = self.nodes.get_mut(node_id) {
            node.state = NodeState::Executing;
            self.consumed_tokens.insert(token_digest);
            Ok(token_digest)
        } else {
            Err(TransitionError::NodeNotFound(node_id.to_owned()))
        }
    }
}
```

---

## 5. Zero-Knowledge eBPF Isolation (`zerokernel v1.0.0`)

When a DAG node requires executing untrusted bytecode (such as a tenant-supplied reconciliation rule or dynamic data filter), [`zerokernel`](https://github.com/Hardonian/zerokernel) executes the program inside a deterministic eBPF virtual machine with a zero-knowledge prover:

| Isolation Property | Conventional Container | `zerokernel` (`v1.0.0`) eBPF ZK-VM |
| :--- | :--- | :--- |
| **Syscall Surface** | 300+ Linux host syscalls (filtered via `seccomp`) | Zero ambient syscalls; strictly whitelisted deterministic host helpers |
| **Termination Guarantee** | Relies on external wall-clock SIGKILL | Verifier-enforced bounded loops + deterministic instruction gas meter |
| **Memory Isolation** | Virtual address space + cgroups | Linearly bounded stack/packet buffer with static bounds checking |
| **Execution Evidence** | Unverified process exit code & stdout | Cryptographic ZK receipt attesting `H(program_elf \|\| input_slice \|\| output_slice \|\| insn_count)` |

---

## 6. End-to-End Reproducible Trace Envelope

Every completed operation produces a canonical, machine-verifiable JSON evidence envelope committed to [`Settler`](https://github.com/Hardonian/Settler):

```json
{
  "schema": "https://hardonia.dev/schemas/evidence-envelope/v1.json",
  "trace_id": "tr_01j9z8k4m2p8x7q5r3v6n1w0y9",
  "tenant_context": {
    "tenant_id": "ef47a890-3b12-4c88-9a10-7712d4b091ac",
    "postgres_rls_enforced": true,
    "tx_isolation": "SERIALIZABLE"
  },
  "control_plane": {
    "engine": "Hardonian/ControlPlane@v1.0.0",
    "policy_gateway": "Hardonian/ReadyLayer",
    "capability_token_sha256": "8f434346648f6b96df89dda901c5176b10a6d83961dd3c1ac88b59b2dc327aa4",
    "quota_governor": {
      "tracker": "Hardonian/TokenGoblin",
      "prompt_tokens": 1420,
      "completion_tokens": 318,
      "latency_ms": 0.41,
      "budget_status": "WITHIN_HARD_CAP"
    }
  },
  "causal_dag": {
    "engine": "Hardonian/veridag",
    "node_id": "step_04_reconcile_settlement",
    "verified_parents": [
      "step_01_ingest_bank_feed",
      "step_02_normalize_currency",
      "step_03_policy_approval"
    ],
    "quint_invariant_check": "PASS"
  },
  "sandbox_attestation": {
    "engine": "Hardonian/zerokernel@v1.0.0",
    "elf_sha256": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae",
    "instructions_executed": 1842,
    "instruction_limit": 65536,
    "zk_receipt_verified": true
  },
  "reconciliation_ledger": {
    "engine": "Hardonian/Settler@v1.8.0",
    "merkle_leaf_sha256": "4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a",
    "replay_deterministic": true
  }
}
```

---

**Next in the Hardonia Architecture Series →** [05 // Permission-Aware Hybrid RAG & Cryptographic Citation Provenance](05_permission_aware_hybrid_rag_and_citation_provenance.md) · [Return to Profile README](../../README.md)

