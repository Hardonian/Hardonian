# From Prototype to Production: Architecture for Enterprise AI Agents

**Author**: Scott Hardie  
**Technical Domain**: Enterprise AI Systems, Applied AI Architecture, Platform Engineering  
**Repository Reference**: [`Hardonian/AgentMesh`](https://github.com/Hardonian/AgentMesh) & [`Hardonian/Settler`](https://github.com/Hardonian/Settler)  

---

## 1. The Production Chasm in Enterprise AI

Building an AI agent prototype is deceptively fast: twenty lines of Python calling an LLM with tool definitions can produce an impressive demonstration in an afternoon. 

However, taking that prototype into an enterprise environment—where it must handle millions of dollars in transactions, process sensitive PII, integrate with complex enterprise systems, survive model provider outages, and comply with institutional audits—reveals a massive architectural chasm:

```text
PROTOTYPE REALITY                                  PRODUCTION REALITY
─────────────────                                  ──────────────────
• Single API key in .env                           • Strict tenant isolation & PostgreSQL RLS
• Model directly executes Python/bash              • Sandboxed MCP gateway with least privilege
• Assumes 100% provider uptime                     • Resilient model fallback (gpt-4o → mini → local)
• Unmonitored token spend                          • Real-time token budgeting & cost caps
• "Looks good" manual evaluation                   • Deterministic CI/CD evaluation harness
• Hardcoded prompt strings                         • Versioned prompts, audit trails, and CAS
```

This guide details the architectural blueprint required to bridge this chasm.

---

## 2. The Six Production Pillars

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ENTERPRISE AGENT ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [1. USER CONTEXT] ────► [2. GATEWAY & AUTH] ────► [3. MODEL ROUTER]        │
│    Tenant Identity          Least-Privilege Policy    Provider Abstraction  │
│    RBAC / OIDC Claims       MCP Tool Registry         Health & Fallback     │
│                                                                             │
│                                      │                                      │
│                                      ▼                                      │
│                                                                             │
│  [4. OBSERVABILITY] ◄─── [5. TOOL RUNTIME]   ────► [6. GOVERNANCE & FINOPS] │
│    OpenTelemetry Spans      HITL Approval Gate        Daily Spend Ceilings  │
│    Redacted Audit Logs      Secret Scrubbing          Eval Regression Suite │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Pillar 1: Model Abstraction & Dynamic Routing

Never couple your application logic directly to a single vendor SDK or specific model version. Upstream APIs experience regional outages, rate limiting, and pricing adjustments.

### Production Pattern:
Implement a vendor-neutral provider interface with policy-governed fallback:

```go
type ModelTarget struct {
    ModelID      string    `json:"modelId"`      // "gpt-4o", "gpt-4o-mini"
    Provider     string    `json:"provider"`     // "openai", "gemini"
    HealthStatus string    `json:"healthStatus"` // "HEALTHY", "DEGRADED", "UNAVAILABLE"
    CostPer1kIn  float64   `json:"costPer1kIn"`
    CostPer1kOut float64   `json:"costPer1kOut"`
}

// GenerateWithFallback dispatches to secondary target only if permitted by tenant policy
func (mr *ModelRouter) GenerateWithFallback(ctx context.Context, primary, fallback string, allowed []string, req *GenerateRequest) (*GenerateResponse, *FallbackEvent, error)
```

If `gpt-4o` returns an HTTP 429 (Rate Limit) or consecutive timeouts, the router records a `FallbackEvent` in telemetry and transparently routes the prompt to `gpt-4o-mini`, preserving the user's workflow without throwing a 500 error.

---

## 4. Pillar 2: Governed Tool Execution via Model Context Protocol (MCP)

In production, agents must not have raw access to database drivers or private network endpoints. All capabilities should be registered as **Model Context Protocol (MCP)** tools behind an authorizing gateway.

1. **Tool Discovery Filtering**: When the client requests `tools/list`, the gateway filters the catalog based on the caller's verified tenant and RBAC role. The model never sees tool schemas it is unauthorized to invoke.
2. **Execution Boundary**: Invocations of destructive or high-risk tools (e.g., refunds, database mutations) return an `MCPApprovalRequired` error with a unique request ID, halting execution until an authorized human signs off.

---

## 5. Pillar 3: FinOps & Token Budget Governance

Unchecked autonomous agents can enter recursive retry loops or ingest enormous documents, resulting in catastrophic billing spikes.

### The Budget State Machine
```
   [Task Initiated]
          │
          ▼
   CheckDailySpend(TenantID)
          ├── Spend > Limit ──► REJECT (-32003: MCPBudgetExceeded)
          │
          └── Spend <= Limit ──► Execute Model & Tools
                                        │
                                        ▼
                                 RecordUsage(Tokens, USD)
                                        │
                                        ▼
                                 Update Daily Aggregates
```

Every model invocation must report exact token consumption (`PromptTokens`, `CompletionTokens`, `CachedTokens`). The platform computes estimated costs per request and halts execution the moment a tenant threshold is reached.

---

## 6. Pillar 4: Automated Continuous Evaluation (Evals in CI/CD)

You cannot deploy changes to prompts, model versions, or tools without automated quality gates. In `AgentMesh`, evaluations are treated like integration tests in CI:

```bash
# Executable Evaluation Battery
go test -v ./internal/evaluation -run TestOpenAI_EnterpriseAgentEvaluation
```

### Essential Evaluation Scenarios:
1. **Tool Selection Accuracy**: Given an ambiguous prompt, does the model select the exact correct tool?
2. **Parameter Grounding**: Are all arguments strictly grounded in the user's prompt or context, rather than hallucinated?
3. **Authorization Refusal**: Does the agent refuse to execute tools outside its role?
4. **Adversarial Resilience**: Can the agent resist prompt injection attempts attempting to bypass human approval gates?

---

## 7. Pillar 5: Secret-Scrubbed Observability

Enterprise compliance (SOC2, HIPAA, GDPR) prohibits logging raw PII, auth headers, or proprietary customer documents in telemetry traces.

- **Trace Propagation**: Every user interaction assigns a root `trace_id` propagated through HTTP headers into the agent runtime and MCP tool calls.
- **Secret Scrubbing**: All error messages and tool responses pass through automated sanitization filters (`telemetry.ScrubSecrets`) before being emitted to OpenTelemetry collectors.

---

## 8. Summary Checklist for Production Deployment

- [x] **Tenant Context**: Passed via cryptographic JWT claims, not user-supplied prompt strings.
- [x] **Data Isolation**: PostgreSQL Row-Level Security (RLS) enabled on 100% of tenant-bound tables.
- [x] **Least Privilege**: Read tools automated; destructive actions gated behind human approvals.
- [x] **Model Redundancy**: Provider abstraction with automatic retry and policy-checked fallback.
- [x] **Cost Controls**: Hard token and dollar budgets enforced before tool dispatch.
- [x] **Continuous Evals**: Quality, safety, and tool accuracy scored automatically on every pull request.
