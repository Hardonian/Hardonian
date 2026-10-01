# Building Safe Multi-Tenant AI Agents with Postgres Row-Level Security (RLS)

**Author**: Scott Hardie  
**Technical Domain**: Enterprise AI Systems, Multi-Tenant Architecture, Database Security  
**Repository Reference**: [`Hardonian/Settler`](https://github.com/Hardonian/Settler) & [`Hardonian/ReadyLayer`](https://github.com/Hardonian/ReadyLayer)  

---

## 1. The Core Enterprise Vulnerability

When enterprises deploy autonomous AI agents or retrieval-augmented generation (RAG) pipelines, the most dangerous failure mode is not a hallucinated summary—it is **cross-tenant data contamination**. 

In conventional web applications, developers rely on application-level filtering:
```typescript
// INSECURE CONVENTIONAL PATTERN: Vulnerable to developer error and agent manipulation
const documents = await db.query(
  `SELECT * FROM documents WHERE tenant_id = $1 AND content ILIKE $2`,
  [tenantId, query]
);
```

In an agentic ecosystem, this pattern breaks down catastrophically:
1. **Tool Argument Drift**: When an LLM generates SQL queries (e.g., via NL-to-SQL or dynamic query tools), a prompt injection or hallucination can easily omit or alter the `WHERE tenant_id = ...` clause.
2. **Context Bleed**: If connection pooling or agent session memory retains state across requests, query parameters can inadvertently bind to another tenant's workspace.
3. **Application Layer Bypass**: A single forgotten filter in a secondary service or background queue leaks private customer data across tenants.

To build trustworthy enterprise AI systems, **tenant isolation must be enforced cryptographically and relationally at the database engine level**, independent of the LLM and independent of application code.

---

## 2. The Architectural Solution: Invariant Row-Level Security

PostgreSQL Row-Level Security (RLS) shifts the boundary of isolation from application code to the database kernel. Even if an AI agent is tricked into running `SELECT * FROM internal_financial_records;`, PostgreSQL will physically filter the returned tuples to only those matching the current tenant session context.

```
┌────────────────────────────────────────────────────────┐
│                   ENTERPRISE USER                      │
└───────────────────────────┬────────────────────────────┘
                            │ Bearer JWT (claims: tenant_id = "tenant_acme")
                            ▼
┌────────────────────────────────────────────────────────┐
│                 NEXT.JS APP GATEWAY                    │
│   • Authenticates JWT                                  │
│   • Extracts tenant_id claim                           │
│   • Acquires connection from pool                      │
└───────────────────────────┬────────────────────────────┘
                            │ SET LOCAL app.current_tenant_id = 'tenant_acme';
                            ▼
┌────────────────────────────────────────────────────────┐
│           POSTGRESQL KERNEL WITH RLS ENFORCED          │
│                                                        │
│  TABLE: agent_runs                                     │
│  POLICY: tenant_isolation_policy                       │
│  USING (tenant_id = current_setting('app.tenant_id'))   │
│                                                        │
│  ┌─────────────────────────┐  ┌─────────────────────┐  │
│  │   Tenant ACME Records   │  │ Tenant BETA Records │  │
│  │   [VISIBLE TO AGENT]    │  │   [ZERO LEAKAGE]    │  │
│  └─────────────────────────┘  └─────────────────────┘  │
└────────────────────────────────────────────────────────┘
```

---

## 3. Production Database Implementation

### 3.1 Migration Schema with Tenant Invariants

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Base Organizations / Tenants Table
CREATE TABLE organizations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    slug VARCHAR(64) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Agent Execution Sessions Table
CREATE TABLE agent_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    agent_id VARCHAR(128) NOT NULL,
    session_title VARCHAR(255),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Agent Knowledge / Memory Table
CREATE TABLE agent_memories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    session_id UUID REFERENCES agent_sessions(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    embedding VECTOR(1536), -- pgvector embeddings
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 1. ENABLE RLS ON ALL TENANT-BOUND TABLES
ALTER TABLE organizations ENABLE ROW LEVEL SECURITY;
ALTER TABLE agent_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE agent_memories ENABLE ROW LEVEL SECURITY;

-- FORCE RLS FOR TABLE OWNERS AS WELL (Prevents superuser bypass in pool)
ALTER TABLE agent_sessions FORCE ROW LEVEL SECURITY;
ALTER TABLE agent_memories FORCE ROW LEVEL SECURITY;
```

### 3.2 Defining Strict Security Policies

```sql
-- RLS Policy using session configuration variable
CREATE POLICY tenant_isolation_agent_sessions ON agent_sessions
    FOR ALL
    TO authenticated_role
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::UUID)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::UUID);

CREATE POLICY tenant_isolation_agent_memories ON agent_memories
    FOR ALL
    TO authenticated_role
    USING (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::UUID)
    WITH CHECK (tenant_id = NULLIF(current_setting('app.current_tenant_id', true), '')::UUID);
```

---

## 4. Application Layer Context Binding in TypeScript / Next.js

When dispatching an AI agent task, wrap the database transaction in an explicit tenant boundary session:

```typescript
import { Pool, PoolClient } from 'pg';

export class TenantContextDatabase {
  constructor(private pool: Pool) {}

  /**
   * Executes a database operation within an unbreakable tenant boundary.
   */
  async withTenant<T>(
    tenantId: string,
    operation: (client: PoolClient) => Promise<T>
  ): Promise<T> {
    const client = await this.pool.connect();
    try {
      await client.query('BEGIN');
      
      // Bind session context to current transaction only
      await client.query(
        `SELECT set_config('app.current_tenant_id', $1, true)`,
        [tenantId]
      );

      const result = await operation(client);

      await client.query('COMMIT');
      return result;
    } catch (error) {
      await client.query('ROLLBACK');
      throw error;
    } finally {
      client.release();
    }
  }
}
```

---

## 5. Automated Negative Penetration Testing

A security policy is only as good as the tests proving it cannot be bypassed. As implemented in `Settler` (`scripts/validate:tenant-isolation`), automated tests must actively attempt cross-tenant theft:

```typescript
import { describe, it, expect, beforeAll } from 'vitest';
import { db, createTestTenant, seedAgentMemory } from './test-harness';

describe('Postgres RLS Multi-Tenant Invariants', () => {
  let tenantAlpha: string;
  let tenantBeta: string;
  let alphaSecretDocId: string;

  beforeAll(async () => {
    tenantAlpha = await createTestTenant('alpha-corp');
    tenantBeta = await createTestTenant('beta-corp');

    alphaSecretDocId = await seedAgentMemory(
      tenantAlpha,
      'Classified Project Blueprint: Alpha Secrets'
    );
  });

  it('PREVENTS Tenant Beta from reading Tenant Alpha records via direct query', async () => {
    await db.withTenant(tenantBeta, async (client) => {
      // Malicious or hallucinated agent queries by exact primary key of Tenant Alpha
      const res = await client.query(
        `SELECT * FROM agent_memories WHERE id = $1`,
        [alphaSecretDocId]
      );

      // Must return 0 rows — NOT an error, but complete invisibility
      expect(res.rows.length).toBe(0);
    });
  });

  it('PREVENTS Tenant Beta from mutating or deleting Tenant Alpha records', async () => {
    await db.withTenant(tenantBeta, async (client) => {
      const res = await client.query(
        `DELETE FROM agent_memories WHERE id = $1`,
        [alphaSecretDocId]
      );

      expect(res.rowCount).toBe(0);
    });

    // Verify record still exists in Tenant Alpha
    await db.withTenant(tenantAlpha, async (client) => {
      const res = await client.query(
        `SELECT * FROM agent_memories WHERE id = $1`,
        [alphaSecretDocId]
      );
      expect(res.rows.length).toBe(1);
    });
  });

  it('FAILS CLOSED when tenant session variable is omitted', async () => {
    const rawClient = await db.pool.connect();
    try {
      // Attempt query without setting app.current_tenant_id
      const res = await rawClient.query(`SELECT * FROM agent_memories`);
      expect(res.rows.length).toBe(0);
    } finally {
      rawClient.release();
    }
  });
});
```

---

## 6. Architectural Tradeoffs & Production Considerations

| Concern | Architectural Tradeoff | Recommended Mitigation |
| :--- | :--- | :--- |
| **Query Planning Overhead** | RLS adds a policy sub-clause to every query plan, potentially impacting throughput on massive joins. | Create composite indices on `(tenant_id, id)` and `(tenant_id, created_at)`. PostgreSQL query planner can filter partitioned indices before scanning. |
| **Connection Pooling (PgBouncer)** | In transaction pooling mode, `SET` session variables bleed unless scoped to `LOCAL` or wrapped in transactions. | Always use `set_config('app.current_tenant_id', val, true)` with the 3rd parameter set to `true` (scopes variable to the current transaction block). |
| **Superuser Bypass** | By default, PostgreSQL table owners and superusers bypass RLS policies. | Run the application pool under an unprivileged role (`authenticated_role`) and explicitly execute `ALTER TABLE ... FORCE ROW LEVEL SECURITY;`. |

---

## 7. Conclusion

By enforcing tenant boundaries in the database engine via PostgreSQL Row-Level Security, enterprise AI platforms achieve **mathematical tenant isolation**. Even if an LLM is compromised by adversarial prompt injection or issues reckless queries, it cannot read or modify data outside its authenticated tenant boundary.
