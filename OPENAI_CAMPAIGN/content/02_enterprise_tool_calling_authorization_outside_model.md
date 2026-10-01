# Enterprise Tool Calling: Why Authorization Belongs Outside the Model

**Author**: Scott Hardie  
**Technical Domain**: AI Agent Governance, Model Context Protocol (MCP), Security Architecture  
**Repository Reference**: [`Hardonian/AgentMesh`](https://github.com/Hardonian/AgentMesh)  

---

## 1. The Prompt-Level Authorization Fallacy

As enterprises connect foundation models (such as OpenAI `gpt-4o`) to live internal systems via tool calling and the Model Context Protocol (MCP), a widespread anti-pattern has emerged: **delegating authorization logic to the prompt**.

```markdown
<!-- FRAGILE PROMPT-LEVEL AUTHORIZATION -->
You are an enterprise support assistant.
Only invoke the `issue_refund` tool if the user's role is "billing_admin".
Never issue a refund greater than $50 without explicit manager approval.
```

In production, relying on an LLM to self-police authorization is an immediate security vulnerability:
1. **Direct & Indirect Prompt Injection**: An adversarial prompt or malicious document retrieved via RAG can instruct the model to ignore prior instructions and execute the privileged tool.
2. **Context Window Degradation**: As conversations extend and system prompts are compressed, negative constraints ("never do X") suffer higher failure rates.
3. **The Confused Deputy Problem**: The model acts on behalf of the end user, but executes tools with the system's ambient service credentials, inadvertently allowing privilege escalation.

### The Fundamental Rule
> **A foundation model proposes intent. A deterministic control plane enforces authorization.**

No tool should ever execute simply because a model generated a valid JSON function call. Authorization checks must occur in a hardened software boundary *between* the model's output and the upstream system.

---

## 2. The Tool Authorization Boundary Architecture

```
┌─────────────────┐       1. Prompt + Tools Schema
│ Enterprise User ├──────────────────────────────────────────┐
└────────┬────────┘                                          │
         │                                                   ▼
         │                                       ┌───────────────────────┐
         │                                       │   OpenAI API / LLM    │
         │                                       │       (gpt-4o)        │
         │                                       └───────────┬───────────┘
         │                                                   │ 2. ToolCall Proposed
         │                                                   │    ("billing.refund", $500)
         │                                                   ▼
         │                              ┌────────────────────────────────────────┐
         │                              │       AGENTMESH MCP GATEWAY            │
         │                              │                                        │
         │                              │  3. Policy Authorization Check         │
         │                              │     [Effect: RequireApproval]          │
         │                              │                                        │
         │    4. Review Notification    │  4. Halt Side Effect                   │
         │◄─────────────────────────────┤     Generate Approval Request ID       │
         │                              └────────────────────────────────────────┘
         │
         │ 5. Cryptographic Signoff
         ▼
┌─────────────────┐ 6. Resolved with Token
│ Human Approver  ├─────────────────────────────┐
└─────────────────┘                             │
                                                ▼
                                ┌────────────────────────────────────────┐
                                │       AGENTMESH MCP GATEWAY            │
                                │                                        │
                                │  7. Validate Token & Arg Hash          │
                                │  8. Execute Privileged Action          │
                                └───────────────────┬────────────────────┘
                                                    │ 9. Mutate State
                                                    ▼
                                        ┌───────────────────────┐
                                        │ Enterprise Billing DB │
                                        └───────────────────────┘
```

---

## 3. Tool Classification Matrix

Enterprise tools must be explicitly categorized by side-effect risk:

| Classification | Side Effect Risk | Example Operations | Enforcement Policy |
| :--- | :--- | :--- | :--- |
| **READ** | Zero mutation / Low risk | `crm.get_account`, `docs.search` | Auto-allowed if caller has tenant permissions. Rate-limited. |
| **WRITE (Idempotent)** | Low-to-Medium mutation | `ticket.add_comment`, `user.update_theme` | Auto-allowed with audit event logging and parameter validation. |
| **PRIVILEGED / DESTRUCTIVE** | High financial, legal, or data risk | `billing.issue_refund`, `db.drop_table`, `git.push_force` | **Hard Block** until Human-in-the-Loop (HITL) cryptographic approval token is verified. |

---

## 4. Implementation: The Go MCP Gateway Guard

As implemented in `AgentMesh` (`internal/mcp/gateway.go`), the gateway intercepts every `tools/call` JSON-RPC message before delegating to the tool driver.

### 4.1 Policy Evaluation & Approval Gating

```go
func (g *Gateway) executeToolCall(ctx context.Context, reqID any, tenantID, agentID string, params *protocol.MCPCallToolParams) *protocol.JSONRPCResponse {
    // 1. Policy Authorization Check
    if g.policyEngine != nil {
        dec := g.policyEngine.Evaluate(ctx, &policy.EvaluationRequest{
            TenantID:       tenantID,
            SubjectAgentID: agentID,
            Tool:           params.Name,
            Action:         "execute",
        })

        switch dec.Effect {
        case policy.EffectDeny:
            // Fail closed immediately
            return &protocol.JSONRPCResponse{
                JSONRPC: "2.0",
                ID:      reqID,
                Error: &protocol.JSONRPCError{
                    Code:    protocol.MCPPolicyDenied,
                    Message: fmt.Sprintf("tool execution denied by policy: %s", dec.Reason),
                },
            }

        case policy.EffectRequireApproval:
            // Check for valid, signed approval token
            approvalToken, _ := params.Arguments["_approvalToken"].(string)
            requestID, _ := params.Arguments["_approvalRequestId"].(string)

            // Extract clean payload without governance metadata
            cleanArgs := extractCleanArguments(params.Arguments)

            if approvalToken == "" || requestID == "" {
                // Halt side effect: generate pending approval request
                appReq, _ := g.approvalSvc.CreateRequest(
                    tenantID, agentID, params.Name, "execute",
                    cleanArgs, dec.PolicyID, dec.DecisionVersion, dec.Reason,
                    15*time.Minute,
                )
                return &protocol.JSONRPCResponse{
                    JSONRPC: "2.0",
                    ID:      reqID,
                    Error: &protocol.JSONRPCError{
                        Code:    protocol.MCPApprovalRequired,
                        Message: fmt.Sprintf("human approval required for tool %q: %s", params.Name, dec.Reason),
                        Data:    appReq,
                    },
                }
            }

            // Validate that token matches exact argument hash and tenant
            if err := g.approvalSvc.ConsumeApproval(requestID, tenantID, agentID, params.Name, cleanArgs, approvalToken); err != nil {
                return &protocol.JSONRPCResponse{
                    JSONRPC: "2.0",
                    ID:      reqID,
                    Error: &protocol.JSONRPCError{
                        Code:    protocol.MCPApprovalRequired,
                        Message: fmt.Sprintf("approval validation failed: %v", err),
                    },
                }
            }
            // Approved and single-use token consumed! Fall through to execution
        }
    }

    // 2. Execute Upstream Tool with Secret Scrubbing
    res, err := g.upstreamHandler(ctx, params.Name, params.Arguments)
    if err != nil {
        return &protocol.JSONRPCResponse{
            JSONRPC: "2.0",
            ID:      reqID,
            Error: &protocol.JSONRPCError{
                Code:    protocol.MCPInternalError,
                Message: telemetry.ScrubSecrets(err.Error()),
            },
        }
    }

    return &protocol.JSONRPCResponse{
        JSONRPC: "2.0",
        ID:      reqID,
        Result:  res,
    }
}
```

---

## 5. Preventing Parameter Tampering with Cryptographic Hashes

A subtle vulnerability in approval systems is **parameter tampering**:
1. Agent requests approval for `billing.issue_refund` with `{ "amount": 10.00 }`.
2. Supervisor reviews and approves the $10.00 refund.
3. Attacker alters the payload to `{ "amount": 10000.00 }` and re-submits the approval token.

In `AgentMesh` (`internal/approval/approval.go`), the approval request computes a canonical SHA-256 hash over the sorted JSON representation of the arguments:

```go
func computeParametersHash(params map[string]any) string {
    canonicalJSON, _ := json.Marshal(params)
    hash := sha256.Sum256(canonicalJSON)
    return hex.EncodeToString(hash[:])
}

func (s *Service) ConsumeApproval(requestID, tenantID, agentID, tool string, params map[string]any, token string) error {
    s.mu.Lock()
    defer s.mu.Unlock()

    req, ok := s.requests[requestID]
    if !ok || req.Consumed {
        return ErrApprovalConsumed
    }

    // Assert argument integrity
    currentHash := computeParametersHash(params)
    if subtle.ConstantTimeCompare([]byte(currentHash), []byte(req.ParametersHash)) != 1 {
        return ErrApprovalTampered // Parameter values were altered!
    }

    req.Consumed = true
    return nil
}
```

---

## 6. Enterprise Takeaways

1. **Defense-in-Depth**: Treat LLM tool calls as untrusted user input from the public internet. Apply input sanitization, schema validation, and authorization checks.
2. **Single-Use Tokens**: High-risk operations must require nonces that expire quickly and cannot be replayed.
3. **Decoupled Policies**: Policies must be declaratively version-controlled, auditable by compliance officers, and independent of model prompts.
