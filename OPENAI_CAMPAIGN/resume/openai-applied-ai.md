# Scott Hardie

**Enterprise Applied AI Architect** · AI Agents, Enterprise Integrations & Technical GTM · Production AI Systems  
Greater Toronto Area, Canada · 416.618.1058 · scottrmhardie@gmail.com  
[LinkedIn: linkedin.com/in/scottrmhardie](https://linkedin.com/in/scottrmhardie) · [GitHub: github.com/hardonian](https://github.com/hardonian)  

---

## Executive Summary

Enterprise Solutions Architect and Hands-on AI Systems Engineer with a 15-year record operating across complex institutional environments, SaaS platforms, and distributed agent infrastructure. Expert at taking ambiguous enterprise AI initiatives from initial discovery through architecture, security review, production deployment, evaluation, and organizational adoption. Combines deep systems-engineering capability (Go, TypeScript, Next.js, PostgreSQL RLS, Model Context Protocol) with proven commercial and consultative acumen across multi-stakeholder enterprise ecosystems.

---

## Core Competencies & Architecture Specializations

- **Enterprise AI Agent Architecture**: Agent gateways, Model Context Protocol (MCP) routing, least-privilege tool execution, dynamic provider abstraction, and resilient model fallback.
- **Enterprise Data Isolation & Governance**: Strict multi-tenant PostgreSQL Row-Level Security (RLS), capability authorization, immutable audit logging, and automated cross-tenant penetration testing.
- **Human-in-the-Loop (HITL) Controls**: Cryptographic token-bound approvals for high-risk and destructive side effects outside the foundation model.
- **Inference FinOps & Spend Governance**: Real-time token consumption tracking, tenant daily spend limits, request cost estimation, and graceful degradation.
- **Continuous Evaluation & Quality Gates**: Executable test suites measuring tool selection accuracy, argument validation, prompt injection resilience, and JSON schema adherence.
- **Complex Enterprise Integrations**: Enterprise identity (SAML 2.0, OIDC, Keycloak), LMS/SIS standards (LTI 1.3), asynchronous event messaging (Kafka), and REST/GraphQL architectures.
- **Technical GTM & Executive Alignment**: Translating C-level business imperatives into technical account roadmaps, leading pre-sales discovery, and establishing feedback loops with core engineering teams.

---

## Technical Stack

- **Languages & Frameworks**: TypeScript, Go, Python, Rust, SQL, Next.js (App Router), React 19, Node.js, Tailwind CSS
- **AI Infrastructure**: OpenAI APIs (gpt-4o, gpt-4o-mini, o3-mini), Model Context Protocol (MCP), Agent-to-Agent (A2A), OpenTelemetry, Ollama
- **Data & Security**: PostgreSQL 15, Supabase RLS, TimescaleDB, Redis, Prisma, Keycloak OIDC, Cryptographic SHA-256 Nonces
- **Delivery & Observability**: Docker, Kubernetes Operators, Vercel, Pino Structured Logging, Vitest, Playwright, GitHub Actions CI/CD

---

## Flagship Applied AI & Systems Platforms

### [AgentMesh](https://github.com/Hardonian/AgentMesh) — Open Control Plane for A2A & MCP Agents
*Go 1.25 · Kubernetes Operator · Model Context Protocol · OpenTelemetry · 100% Test-Passing Across 48 Packages*
- Architected a distributed agent control plane providing identity, deterministic policy enforcement, dynamic tool routing, and provider abstraction (OpenAI, Gemini, Local).
- Built a standards-compliant **MCP Tool Gateway** that enforces least-privilege tool access, intercepts privileged mutations until verified human approval tokens are provided, and sanitizes upstream secrets.
- Implemented **ModelRouter** with automated, policy-governed fallback from `gpt-4o` to `gpt-4o-mini` during upstream rate limits or service disruptions.
- Shipped an automated evaluation battery (`internal/evaluation`) achieving a 100% score across tool selection accuracy, argument schemas, cross-tenant isolation, and structured outputs.

### [Settler](https://github.com/Hardonian/Settler) — Multi-Tenant Financial Reconciliation & Audit Operating System
*TypeScript · Next.js · PostgreSQL · Supabase RLS · TimescaleDB · Stripe · Vitest*
- Designed and built a high-volume enterprise reconciliation engine enforcing mathematical tenant isolation via PostgreSQL Row-Level Security (RLS).
- Authored automated negative test suites (`test:cross-tenant`, `validate:tenant-isolation`) verifying that tenant boundaries remain impenetrable under arbitrary or malicious queries.
- Structured an auditable proofpack pipeline generating cryptographic Merkle chains of custody for compliance and institutional financial audits.

### [ReadyLayer](https://github.com/Hardonian/ReadyLayer) — Enterprise AI Governance & Delivery SaaS
*Next.js 16 App Router · React 19 · Supabase RLS · Pino Structured Logging · Stripe · Vitest*
- Developed a production Next.js SaaS platform governing AI-assisted software delivery and autonomous coding agents.
- Implemented policy engines evaluating generated code against ethical AI gates, feature drift detection, and SOC2/ISO compliance checkpoints.
- Engineered multi-tenant usage accounting, token consumption monitoring, and Stripe billing integrations with background worker queues.

### [enterprise-integration-fabric](https://github.com/Hardonian/enterprise-integration-fabric) — Reference Integration Architecture
*Spring Boot 3 · Apache Camel 4 · Keycloak OIDC · Redpanda (Kafka) · OpenAPI / AsyncAPI*
- Production-grade enterprise reference architecture connecting legacy SIS, LMS, CRM, billing, and identity platforms through a governed, event-driven integration layer.

---

## Professional Experience

### Solutions Architect — McGraw Hill
*Dec 2022 – Present · Greater Toronto Area, Canada*
- Lead enterprise solution discovery, systems architecture, and implementation design for digital learning platforms, institutional integrations (LTI 1.3, SAML 2.0), and AI-assisted content workflows.
- Serve as the primary technical counterpart to university CIOs, CTOs, and institutional security review boards, navigating stringent data privacy (FERPA, SOC2), accessibility (WCAG 2.1 AA), and tenancy requirements.
- Collaborate cross-functionally with enterprise sales, software engineering, product management, and customer success teams to architect custom integration roadmaps that accelerate customer adoption.
- Pilot and evaluate applied AI capabilities for automated content generation and assessment workflows, establishing benchmarking criteria for model hallucination, latency, and instructional grounding.

### Senior Digital Solutions Consultant — McGraw Hill / Pearson
*2019 – 2022 · Greater Toronto Area, Canada*
- Acted as senior customer-facing technical advisor for complex institutional digital transformations, scoping custom data exchange architectures and automated synchronization pipelines.
- Reduced manual administrative onboarding overhead by 30% through disciplined solution design, standardized technical runbooks, and automated integration tooling.
- Partnered with enterprise account executives to define technical account plans, conduct high-stakes technical demonstrations, and remove architectural blockers during complex procurement cycles.

### Portfolio & Product Management — Pearson / McGraw Hill
*2015 – 2019 · Greater Toronto Area, Canada*
- Held commercial and technical ownership of an $8.5M enterprise higher-education portfolio across 15+ software platforms and digital courseware solutions.
- Drove user research, technical feasibility evaluations, and interactive prototyping, translating complex customer requirements directly into engineering backlogs and roadmap milestones.
- Guided cross-functional delivery teams across software engineering, UX design, marketing, and commercial operations through successful platform launches.

### Account Executive & Consultative Advisory — Pearson / McGraw Hill
*Pre-2015 · Greater Toronto Area, Canada*
- Managed a $2.5M+ enterprise territory across Canadian institutions, winning the President's Award for Sales Excellence.
- Guided institutional executive leadership through print-to-digital platform adoptions, overcoming cultural and technical resistance through consultative advisory and clear ROI modeling.

---

## Education & Credentials

- **Master of Arts (MA), Political Science** — Public Opinion & Research Methods · Wilfrid Laurier University
- **Bachelor of Arts (BA), Political Science & Communication Studies** · Wilfrid Laurier University
- **MindStudio AI Agent Certification**
- **Microsoft Office Specialist Certification**
