---
stepsCompleted: [1, 2, 3, 4, 5, 6]
inputDocuments:
  - '_bmad-output/planning-artifacts/prd.md'
  - '_bmad-output/analysis/architect-technical-brief.md'
  - '_bmad-output/planning-artifacts/ux-design-specification.md'
  - 'docs/brainstorming-session-2026-01-10.md'
workflowType: 'architecture'
project_name: 'euromonitor-multi-agent-architecture'
user_name: 'Karthikmg'
date: '2026-01-21'
status: 'complete'
---

# Architecture Decision Document

_This document builds collaboratively through step-by-step discovery. Sections are appended as we work through each architectural decision together._

---

## 🎯 MVP SCOPE SUMMARY

### Purpose & Scope

This architecture document describes the **complete production-ready system** for the Euromonitor Passport AI-Powered Intelligence Assistant. However, for **MVP demo purposes**, we will implement a **focused subset** (~40% of full architecture) that demonstrates core intelligence generation capabilities while deferring advanced enterprise features to Phase 5+ (post-MVP production hardening).

**MVP Goal:** Demonstrate natural language query → verified intelligence report with citations in <5 minutes, using Mode 1 (Market Overview) only.

**Timeline:** 6-week MVP implementation (Phases 1-4) vs. 10-week full production deployment (Phases 1-6+)

**Cost Target:** $800-1,100/month (MVP) vs. $2,600-6,340/month (full production)

---

### ✅ IN SCOPE FOR MVP DEMO

#### Core Intelligence Generation (Mode 1 Only)
- ✓ **Natural Language Query Interface**: Single-turn queries for Market Overview reports
- ✓ **Mode 1: Market Overview** ONLY (defer Modes 2-3 to post-MVP)
- ✓ **8 Core LangGraph Agents**: Query Interpreter, Data Retrieval, Narrative Synthesizer, Citation Specialist, Quality Scorer, Report Assembler, Visualization Generator, Data Quality Validator
- ✓ **Quality Assurance Loop**: Multi-dimensional scoring with >75% threshold
- ✓ **Claim-Level Citations**: 100% citation accuracy validation with Passport source attribution
- ✓ **Report Display**: In-app visualization (no PDF/PPTX export for MVP)

#### Technology Stack (Simplified)
- ✓ **Frontend**: React 19 + TypeScript + Vite + Tailwind CSS + shadcn/ui + TanStack Query + Zustand
- ✓ **Backend**: Custom FastAPI (Python 3.10+) + LangGraph for multi-agent orchestration
- ✓ **LLM**: Claude 3.5 Sonnet (Anthropic API)
- ✓ **Knowledge Graph**: Neo4j AuraDB with **Phase 1-2 data only** (structured Passport data, defer Phase 4 citation metadata and semantic search)
- ✓ **Relational DB**: PostgreSQL (AWS RDS) - **Single-AZ deployment** for MVP
- ✓ **Caching**: Redis (AWS ElastiCache) - **Single-node** for MVP
- ✓ **Message Queue**: AWS SQS + SNS for agent task routing
- ✓ **Monitoring**: AWS CloudWatch **basic logs and metrics only** (no X-Ray tracing)
- ✓ **Deployment**: AWS ECS Fargate - **Single task** (no HA for MVP)

#### Authentication & Access Control (Simplified)
- ✓ **JWT Token-Based Auth**: Email/password login only
- ✓ **Basic RBAC**: Simple user/admin roles (defer Validator/Operations roles)
- ✓ **Session Management**: 24-hour JWT expiry with refresh tokens
- ✗ **Defer**: SSO/SAML integration, MFA, enterprise IdP integration (Phase 5+)

#### Data Access & Permissions (Simplified)
- ✓ **Subscription-Based Access**: Geography/category filtering based on user subscription tier
- ✓ **Query-Level Validation**: Check permissions before KG queries execute
- ✗ **Defer**: Advanced permission overrides, audit trail queries, data residency configuration

#### Monitoring & Operations (Basic)
- ✓ **CloudWatch Logs**: Application logs with structured JSON format
- ✓ **Basic Metrics**: Query latency, error rates, LLM token usage
- ✓ **Query Audit Trail**: Store in PostgreSQL (user_id, query, timestamp, mode, quality_score)
- ✗ **Defer**: X-Ray distributed tracing, advanced dashboards, incident investigation tools, quality score distribution analytics

#### Infrastructure (Simplified)
- ✓ **Single-AZ Deployment**: RDS, ElastiCache, ECS all in one availability zone
- ✓ **Automated Backups**: 7-day retention for RDS, daily Neo4j snapshots
- ✓ **Environment Variables**: AWS Secrets Manager for API keys and credentials
- ✗ **Defer**: Multi-AZ deployments, cross-region DR, disaster recovery procedures, failover testing

---

### ❌ DEFERRED TO PHASE 5+ (POST-MVP)

#### Authentication & Enterprise Features
- ❌ **SSO/SAML Integration** (Lines 921-933): SAML 2.0, OAuth 2.0, OpenID Connect with Okta/Azure AD/OneLogin
- ❌ **MFA Support**: Two-factor authentication via authenticator apps
- ❌ **Enterprise Session Management**: Centralized session control and forced logout
- ❌ **Advanced RBAC**: Validator and Operations roles with granular permissions

#### Administrative Capabilities (FR41-FR48)
- ❌ **Admin UI for User Management**: Provisioning/deprovisioning workflows, SSO configuration
- ❌ **Beta Group Management**: Feature flag controls for user cohorts
- ❌ **Bulk User Import**: CSV upload for enterprise customer onboarding
- ❌ **Usage Analytics Dashboards**: Query patterns, adoption metrics, cost tracking
- ❌ **Audit Trail UI**: Searchable audit log interface for compliance
- ❌ **Data Residency Configuration**: Per-customer data location controls
- **MVP Alternative**: Manual admin via CLI/database for MVP demo

#### Advanced Monitoring & Observability
- ❌ **AWS X-Ray Distributed Tracing** (Line 1459): Service maps, agent debugging visibility, latency analysis
- ❌ **Advanced Dashboards**: Quality score distribution, citation accuracy trends, KG health metrics
- ❌ **Incident Investigation Tools**: Log aggregation, trace correlation, root cause analysis
- ❌ **Automated Alerting**: PagerDuty/Opsgenie integration for on-call rotation
- **Cost Savings**: ~$15/month X-Ray cost deferred

#### Export & Integration Features
- ❌ **PDF/PPTX Generation** (FR59-FR60): One-click export with formatting (<10 seconds)
- ❌ **Power User API** (FR63): RESTful API access for programmatic queries (Vision phase)
- ❌ **Webhook Notifications** (FR64): Event-driven integrations for report completion
- ❌ **Passport Data Refresh Sync** (FR60): Automated sync pipeline for corpus updates
- **MVP Alternative**: Display reports in-app only, manual JSON export for testing

#### Operational Modes (Focus Mode 1 Only)
- ❌ **Mode 2: Category Deep Dive** (Line 33): Competitive analysis and market share insights
- ❌ **Mode 3: Regulatory Impact Brief** (Line 33): Regulatory intelligence and compliance analysis
- ❌ **Multi-Turn Conversations** (FR4): Context retention across queries
- **MVP Scope**: Mode 1 (Market Overview) single-turn queries ONLY

#### Knowledge Graph Advanced Features
- ❌ **Phase 3: Unstructured Data** (Lines 3344-3421): Vector embeddings for PDFs, reports, articles
- ❌ **Phase 4: Citation Metadata** (Line 3391): Structured data + semantic search for claim-source linking
- ❌ **Cross-Content Retrieval**: Multi-source data synthesis across structured/unstructured
- ❌ **KG Update Pipeline**: Automated corpus refresh with change detection
- **MVP Scope**: Phase 1-2 ONLY (core structured Passport data: datasets, industries, geographies, categories)

#### Infrastructure High Availability & DR
- ❌ **Multi-AZ Deployment** (Lines 3458-3507): RDS Multi-AZ (99.5% SLA), ElastiCache cluster mode (3 nodes), ECS multi-AZ task placement
- ❌ **Disaster Recovery Procedures** (Lines 3511-3589): Cross-region backup replication, RTO/RPO targets (6-8 hour RTO), security breach recovery, data corruption PITR
- ❌ **Automated Failover**: RDS automatic failover (1-2 minutes), health checks with auto-recovery
- ❌ **Backup Retention**: 30-day retention for PostgreSQL (7-day for MVP), quarterly failover drills
- **Cost Savings**: ~$100-200/month by avoiding Multi-AZ initially

#### Cost Optimization & Advanced Features
- ❌ **Fargate Spot Instances** (Line 3726): 70% savings on workers (~$175/month saved)
- ❌ **Claude Prompt Caching** (Line 3738): 50-90% LLM cost reduction (~$500-1,000/month saved)
- ❌ **Self-Hosted Neo4j** (Line 3741): Migrate from AuraDB to ECS-hosted (~$300-400/month saved)
- ❌ **Reserved Instances**: 1-year commitment for RDS/ElastiCache (30-40% savings)
- ❌ **Prompt Optimization**: Token reduction strategies (20% savings on LLM costs)
- **MVP Approach**: Use standard on-demand pricing; optimize in Phase 5+ after usage patterns emerge

#### Compliance & Governance
- ❌ **GDPR Compliance Workflows**: Data subject access requests, right-to-deletion automation
- ❌ **YAML Governance Process** (Lines 3839-4067): 7-phase change management, versioning, rollback procedures
- ❌ **Comprehensive Audit Logging**: Orchestration flow details, admin action tracking
- ❌ **Security Hardening**: Penetration testing, vulnerability scanning, incident response playbooks
- **MVP Scope**: Basic audit logs to database, manual YAML change management

---

### 📊 MVP vs. PRODUCTION COMPARISON

| **Dimension** | **MVP Demo** | **Full Production (Phase 5+)** |
|---------------|--------------|--------------------------------|
| **Timeline** | 6 weeks (Phases 1-4) | 10 weeks (Phases 1-6+) |
| **Monthly Cost** | $800-1,100 | $2,600-6,340 |
| **Uptime SLA** | Best-effort (~95%) | 99.5% with Multi-AZ |
| **Authentication** | JWT (email/password) | SSO/SAML + MFA |
| **Operational Modes** | Mode 1 only (Market Overview) | Modes 1-3 (all types) |
| **KG Data Scope** | Phase 1-2 (structured Passport) | Phase 1-4 (structured + unstructured + semantic search) |
| **Monitoring** | CloudWatch basic | CloudWatch + X-Ray + Advanced Dashboards |
| **Deployment** | Single-AZ, 1 ECS task | Multi-AZ, HA with auto-scaling |
| **Export** | In-app display only | PDF/PPTX generation |
| **Disaster Recovery** | Daily backups (7-day retention) | Multi-region DR (RTO: 6-8 hours) |
| **Admin Features** | Manual CLI/database | Full admin UI with SSO config |
| **RBAC** | User/Admin only | 4 roles (User, Validator, Admin, Operations) |

---

### 🛠️ MVP CRITICAL PATH (6-Week Timeline)

**Weeks 1-2 (Phase 1): Foundation**
- AWS infrastructure setup (VPC, RDS Single-AZ, ElastiCache single-node, S3, SQS, SNS)
- Neo4j AuraDB provisioning and schema design (Phase 1-2 data model)
- PostgreSQL schema for users, queries, reports, audit logs
- JWT authentication service with email/password login

**Weeks 3-4 (Phase 2-3): Core Services + Frontend**
- FastAPI backend with health checks, authentication endpoints
- LangGraph multi-agent orchestration (8 core agents, Mode 1 workflow)
- React frontend with query interface and report display
- Basic CloudWatch logging and metrics

**Weeks 5-6 (Phase 4): Integration + Testing**
- End-to-end testing of Mode 1 queries
- Citation accuracy validation (100% requirement)
- Quality score threshold tuning (>75% target)
- Performance testing (<180s avg response time)
- Security review (encryption, auth, SQL injection prevention)

**Post-Week 6: Phase 5+ Production Hardening**
- Multi-AZ deployment, X-Ray tracing, SSO integration, admin UI, Modes 2-3, disaster recovery

---

### 🎯 SUCCESS CRITERIA FOR MVP DEMO

1. ✅ **Functional**: Mode 1 query → intelligence report with citations in <5 minutes
2. ✅ **Quality**: >75% quality score threshold, 100% citation accuracy
3. ✅ **Authentication**: Email/password login with JWT tokens
4. ✅ **Data Access**: Subscription-based geography/category filtering
5. ✅ **Monitoring**: CloudWatch logs with query latency and error metrics
6. ✅ **Stability**: <1% error rate, graceful error handling with user-friendly messages
7. ✅ **Cost**: Stay within $800-1,100/month budget during demo period

---

### 📍 DOCUMENT NAVIGATION

Throughout this architecture document:
- **Phase 5+ features** are explicitly marked with "Phase 5+", "Production Phase", or "Post-MVP"
- **Cost estimates** distinguish between MVP ($800-1,100/month) and production ($2,600-6,340/month) configurations
- **Deployment phases** indicate which weeks correspond to MVP (Phases 1-4) vs. production hardening (Phases 5+)

**Key Sections with Phase 5+ Details:**
- **Authentication & SSO**: Lines 921-933 (SSO deferred to Phase 5+)
- **Monitoring & X-Ray**: Line 1459 (X-Ray in Phase 5)
- **Knowledge Graph Phases**: Lines 3344-3421 (Phases 3-4 deferred)
- **Disaster Recovery**: Lines 3511-3589 (DR procedures deferred)
- **Cost Management**: Lines 3702-3754 (optimization strategies for Phase 5+)
- **YAML Governance**: Lines 3839-4067 (formal governance deferred)

---

## Project Context Analysis

### Executive Summary

The Passport AI-Powered Intelligence Assistant is an enterprise-grade, multi-agentic AI system designed to transform market intelligence workflows for Euromonitor Passport customers. This is a greenfield SaaS B2B platform targeting Fortune 500 analysts, category managers, and strategy teams who need analyst-grade intelligence reports generated from natural language queries in minutes instead of weeks.

**Core Value Proposition:** Natural language query → Verified intelligence report with claim-level citations, delivered in <5 minutes with >75% quality score threshold.

### Requirements Overview

**Functional Requirements Summary:**

The system encompasses **71 functional requirements** organized into 10 capability domains:

1. **Query & Intelligence Generation (FR1-FR9):** Natural language query interface, three operational modes (Market Overview, Category Deep Dive, Regulatory Impact Brief), narrative synthesis from Passport data, visualization generation, multi-turn conversations with context retention.

2. **Mode Detection & Routing (FR10-FR14):** Automatic operational mode detection from query structure, confidence scoring (>85% accuracy target), clarification flows when uncertain, mode-specific agent workflow routing.

3. **Quality Assurance & Validation (FR15-FR22):** Multi-dimensional quality rubric scoring, iterative refinement loops when quality <75%, data completeness validation, coverage gap flagging, human-in-the-loop validation workflow, YAML business rule enforcement.

4. **Citations & Transparency (FR23-FR28):** Claim-level attribution to Passport sources, citation accuracy validation (100% requirement), navigation to source datasets, methodology/limitation disclosure, coverage confidence indicators.

5. **User Access & Authentication (FR29-FR33):** SSO integration (SAML 2.0, OAuth 2.0, OpenID Connect), Passport SSO infrastructure integration, enterprise session management, MFA support.

6. **Permissions & Data Access Control (FR34-FR40):** Subscription-based data access by geography/category, query-level permission enforcement, RBAC implementation (End User, Validator, Admin, Operations roles), graceful permission denial handling, admin permission overrides with audit trail.

7. **Administrative Management (FR41-FR48):** User provisioning/deprovisioning, SSO configuration, subscription tier mapping, beta group management, bulk user import, usage analytics dashboards, audit trail querying, data residency configuration.

8. **Operations & Monitoring (FR49-FR58):** Query audit trails with orchestration flow details, agent debugging visibility, quality score distribution metrics, citation accuracy monitoring, KG health dashboards, system performance metrics, incident investigation tools, automated alerting.

9. **Export & Integration (FR59-FR64):** PDF/PPTX export, Passport data refresh sync, API rate limit handling, power user API access (Vision phase), webhook notifications (future).

10. **Knowledge Graph & Data Management (FR65-FR71):** KG construction from structured + unstructured Passport data, >95% corpus coverage requirement, taxonomy preservation, semantic search, cross-content retrieval, KG update pipeline, data quality validation.

**Non-Functional Requirements Summary:**

The system has **59 non-functional requirements** across 8 critical domains:

1. **Performance (NFR1-NFR7):**
   - <180 seconds (3 min) average response time
   - 95th percentile <240 seconds (4 min)
   - 100+ concurrent queries without degradation
   - <1% error rate
   - Mode detection <5 seconds
   - Citation validation <10 seconds overhead

2. **Security (NFR8-NFR15):**
   - Encryption at rest and in transit (TLS 1.3+)
   - Zero data leakage between users/sessions
   - Protection against injection, XSS, CSRF
   - Rate limiting for abuse prevention
   - Regular penetration testing
   - Incident response procedures

3. **Reliability & Availability (NFR16-NFR20):**
   - 99.5% uptime SLA
   - Automated health monitoring and alerting
   - Graceful degradation on component failures
   - Disaster recovery and backup strategy
   - Production rollback capabilities

4. **Scalability (NFR21-NFR27):**
   - Launch: 500+ daily queries, 20-50 concurrent users
   - 6 months: 2000+ daily queries, 100+ concurrent users
   - Production: 500+ concurrent users
   - Horizontal scaling architecture
   - Auto-scaling based on demand

5. **Data Quality & Accuracy (NFR28-NFR33):**
   - **100% citation accuracy (hard requirement)**
   - >95% Passport corpus coverage in KG
   - >85% mode detection accuracy
   - >75% quality score threshold (minimum)
   - Data completeness validation with gap flagging
   - >95% YAML business rule compliance

6. **Integration & Interoperability (NFR34-NFR40):**
   - Multi-protocol SSO support
   - Passport API graceful rate limit handling
   - Automatic Passport data refresh sync
   - PDF and PPTX export formats
   - Power user API access (future)

7. **Compliance & Auditability (NFR41-NFR46):**
   - Comprehensive audit logging (queries, mode detection, data retrieval, report generation)
   - 12-month default retention (configurable)
   - Admin/operations audit trail access
   - Data residency compliance per customer
   - GDPR compliance (data subject access, minimal PII)

8. **Maintainability & Operability (NFR47-NFR53):**
   - Operations dashboard with full observability
   - Failed query debugging via orchestration flow visibility
   - Automated alerting for health/citation issues
   - KG maintenance tools
   - Containerized deployment (Kubernetes)
   - Cloud deployment support (AWS/Azure/GCP)

**UX Design Requirements:**

From the comprehensive UX specification, key architectural implications:

- **Design System:** Tailwind CSS + shadcn/ui (React/TypeScript frontend)
- **Interaction Model:** ChatGPT-style conversational interface with progressive intelligence disclosure (sections stream as generated)
- **Citation Pattern:** Perplexity-style inline citations with hover previews, click to expand
- **Platform:** Desktop-first standalone web app (1280px+), modern browser support (Chrome/Firefox/Safari/Edge)
- **Performance Expectations:** Optimistic UI (<100ms acknowledgment), progressive loading, no blank spinners (contextual progress messages)
- **Accessibility:** WCAG AA compliance minimum
- **Export:** One-click PDF/PPTX generation (<10 seconds)
- **Authentication:** Simple email/password for MVP (SSO in production)

### Scale & Complexity Assessment

**Complexity Level:** **HIGH / ENTERPRISE-GRADE**

**Rationale:**
- Multi-agent orchestration (8+ agents) with state management and error handling
- Knowledge graph construction and maintenance at TB scale (Passport corpus)
- Hybrid KG + vector search architecture for cross-content retrieval
- Novel YAML-constraint pattern for LLM output predictability
- Strict quality gates (100% citation accuracy, 75% quality threshold, <1% error rate)
- Enterprise SaaS requirements (SSO, multi-tenancy permissions, audit trails, 99.5% SLA)
- Real-time concurrent processing (100+ queries)
- Multiple operational modes with automatic detection (>85% accuracy)

**Primary Technical Domain:** Full-Stack SaaS Platform

- **Frontend:** React SPA with Tailwind + shadcn/ui
- **Backend:** Multi-agent orchestration engine
- **Data Layer:** Knowledge graph + vector database + relational store
- **Integration Layer:** LLM APIs, Passport APIs, SSO providers
- **Infrastructure:** Cloud-based, containerized (Kubernetes), horizontally scalable

**Estimated Architectural Components:** 18-22 major components

**Core Processing Pipeline:**
1. Query Ingestion & Mode Detection
2. Multi-Agent Orchestration Engine
3. Knowledge Graph Query Engine
4. Data Retrieval & Validation Layer
5. LLM Gateway & Prompt Management
6. YAML Business Rules Engine
7. Narrative Synthesis Service
8. Citation Specialist & Validator
9. Visualization Generator
10. Quality Scoring Framework
11. Report Assembly & Formatting
12. Export Engine (PDF/PPTX)

**Supporting Infrastructure:**
13. Authentication & Authorization Service (SSO integration)
14. Permission Management (subscription-based access control)
15. Audit Trail & Logging Service
16. Monitoring & Observability Platform
17. Admin Dashboard Backend
18. Operations Dashboard Backend
19. KG Maintenance & Update Pipeline
20. Passport Integration Layer
21. Caching Layer (query results, KG fragments, LLM responses)
22. Message Queue / Event Bus (agent coordination)

### Technical Constraints & Dependencies

**External Dependencies:**

1. **Euromonitor Passport Platform:**
   - Read-only API access to structured data (market size, forecasts, company shares)
   - Access to unstructured content (reports, documents, analysis)
   - Passport's existing data access controls must be respected
   - Passport API rate limits require graceful handling
   - Data refresh cycles dictate KG update frequency

2. **LLM Provider(s):**
   - Primary LLM service (Claude 3.5 Sonnet / GPT-4 decision needed)
   - API rate limits and cost management considerations
   - Prompt token limits (context window constraints)
   - Fine-tuning requirements for Passport domain
   - Fallback strategy if primary provider unavailable

3. **SSO/Identity Providers:**
   - SAML 2.0, OAuth 2.0, OpenID Connect protocol support
   - Integration with enterprise identity systems (Okta, Azure AD, etc.)
   - Session management aligned with enterprise security policies

**Known Constraints:**

1. **Performance Constraints:**
   - <5 minute response time target (3-4 min average)
   - 100+ concurrent query processing requirement
   - Mode detection must complete in <5 seconds
   - Citation validation <10 seconds overhead
   - These are hard constraints driven by user experience expectations

2. **Quality Constraints:**
   - 100% citation accuracy (zero tolerance for broken links)
   - >75% quality score before presentation (iterative refinement if below)
   - >85% mode detection accuracy
   - >95% YAML compliance (LLM outputs must conform to specifications)

3. **Data Constraints:**
   - Must achieve >95% Passport corpus coverage in KG
   - Knowledge graph must preserve Passport taxonomy exactly
   - Data residency requirements per customer configuration
   - GDPR compliance for minimal PII handling

4. **Scalability Constraints:**
   - MVP: 20-50 concurrent users
   - Growth: 100+ concurrent users
   - Production: 500+ concurrent users
   - Daily query volume: 500 → 2000+ over 6 months
   - Architecture must scale horizontally

5. **Reliability Constraints:**
   - 99.5% uptime SLA
   - <1% query error rate
   - Graceful degradation on component failures
   - No cascading agent failures

**Technology Decision Points (To Be Resolved):**

The Technical Brief identifies critical technology selection needs:

1. **Knowledge Graph Technology:** Neo4j vs Amazon Neptune vs TigerGraph
2. **Vector Database:** Pinecone vs Weaviate vs Qdrant
3. **Agent Framework:** LangGraph vs AutoGen vs Custom
4. **LLM Provider:** Claude 3.5 Sonnet vs GPT-4 vs Multi-provider
5. **Backend Language:** Python (FastAPI) vs Node.js
6. **Cloud Provider:** AWS vs Azure vs GCP
7. **Orchestration:** Kubernetes vs AWS ECS
8. **Monitoring:** Datadog vs New Relic vs Prometheus

These decisions will be addressed systematically in subsequent architectural decision steps.

### Cross-Cutting Concerns Identified

**1. Security & Compliance:**
- Affects: All components (authentication, authorization, data access, audit logging)
- Requirements: SSO integration, subscription-based permissions, RBAC, audit trails, GDPR compliance, data residency
- Architectural Impact: Dedicated security layer, permission middleware, comprehensive logging infrastructure

**2. Performance & Scalability:**
- Affects: Query ingestion, agent orchestration, KG queries, LLM calls, concurrent processing
- Requirements: <5 min response, 100+ concurrent queries, horizontal scaling, auto-scaling
- Architectural Impact: Async processing, caching strategies, load balancing, stateless agents, distributed architecture

**3. Quality Assurance & Validation:**
- Affects: Multi-agent pipeline (Data Validator, Quality Scorer), citation validation, YAML enforcement
- Requirements: 100% citation accuracy, >75% quality threshold, iterative refinement loops
- Architectural Impact: Multi-stage validation gates, feedback loops, citation verification service, YAML schema validators

**4. Observability & Debugging:**
- Affects: All agent workflows, KG queries, quality metrics, system health
- Requirements: Agent flow visibility, quality score tracking, citation accuracy monitoring, incident investigation
- Architectural Impact: Comprehensive logging, distributed tracing, metrics collection, operations dashboards, alerting infrastructure

**5. Data Consistency & Freshness:**
- Affects: Knowledge graph, Passport integration, citation links, data coverage
- Requirements: KG sync with Passport refreshes, stale metadata detection, coverage gap flagging
- Architectural Impact: KG update pipeline, data validation checks, freshness tracking, automated staleness alerts

**6. Multi-Agent Coordination:**
- Affects: Core orchestration pipeline (8 agents + mode-specific agents)
- Requirements: State persistence, error handling, retry logic, circuit breakers, no cascade failures
- Architectural Impact: Message queue/event bus, state management service, orchestration engine with fault tolerance

**7. YAML-Driven Business Rules:**
- Affects: Mode detection, data retrieval, narrative synthesis, quality scoring, report assembly
- Requirements: Strict schema enforcement, LLM output validation, mode-specific YAML specs
- Architectural Impact: YAML parser/validator, schema registry, LLM constraint enforcement mechanisms

**8. Citation Transparency & Traceability:**
- Affects: Narrative synthesis, citation specialist, report assembly, source linking
- Requirements: Claim-level attribution, 100% accuracy, direct Passport source navigation
- Architectural Impact: Citation service, source metadata tracking, link validation, broken link monitoring

### Architectural Priorities

Based on the requirements analysis, the following architectural priorities emerge:

**P0 (Critical - System Viability):**
1. Multi-agent orchestration reliability (no cascade failures, <1% error rate)
2. Citation accuracy infrastructure (100% requirement)
3. Knowledge graph construction and query performance (<5 min total response)
4. Quality validation gates (>75% threshold enforcement)
5. Performance at scale (100+ concurrent queries without degradation)

**P1 (High - User Trust & Experience):**
1. Mode detection accuracy (>85% target)
2. YAML business rules enforcement (predictable outputs)
3. SSO integration and permission management
4. Observability and debugging infrastructure
5. Graceful error handling and user feedback

**P2 (Medium - Operational Excellence):**
1. KG maintenance and update pipeline
2. Comprehensive audit trail system
3. Admin and operations dashboards
4. Export functionality (PDF/PPTX)
5. Monitoring and alerting infrastructure

**P3 (Low - Future Enhancement):**
1. Power user API access
2. Advanced collaboration features
3. Model fine-tuning for Passport domain
4. Webhook notifications

### Risk Factors for Architecture

**High-Risk Areas Requiring Careful Design:**

1. **Multi-Agent Orchestration Complexity:**
   - Risk: 8-agent pipeline with state management could have cascading failures
   - Impact: System reliability, <1% error rate requirement
   - Mitigation Approach: Robust error handling, circuit breakers, state persistence, extensive load testing

2. **Knowledge Graph Quality & Scale:**
   - Risk: KG gaps/errors compromise all outputs; TB-scale construction performance
   - Impact: Data coverage >95% requirement, citation accuracy, query performance
   - Mitigation Approach: Comprehensive validation pipeline, quality metrics dashboard, incremental validation

3. **LLM Hallucination Prevention:**
   - Risk: LLM generates plausible but incorrect analysis ("sophisticated nonsense")
   - Impact: Quality threshold, citation accuracy, user trust
   - Mitigation Approach: Strict grounding in Passport data (RAG), YAML constraints, citation requirement, quality scoring

4. **Performance at Scale:**
   - Risk: System too slow with 100+ concurrent users or complex queries
   - Impact: <5 min response time, user experience, scalability targets
   - Mitigation Approach: Caching strategies, async processing, load testing, horizontal scaling architecture

5. **Citation Accuracy Maintenance:**
   - Risk: Passport dataset deprecation, stale KG metadata, broken links
   - Impact: 100% citation accuracy requirement (zero tolerance)
   - Mitigation Approach: Automated validation, broken link monitoring, KG update pipeline, incident response process

## Starter Template Evaluation

### Primary Technology Domain

**Full-Stack SaaS Platform with AI/ML Backend**

The project requires two distinct technology stacks working in concert:

- **Frontend:** React SPA (Single Page Application) for standalone web interface
- **Backend:** Python FastAPI with Multi-Agent Orchestration (LangGraph) for intelligence generation pipeline

This separation allows independent scaling, development velocity, and leverages the strengths of each ecosystem (React for modern UX, Python for AI/ML tooling).

### Technical Preferences Established

**From UX Design Specification:**

The UX specification already established foundational frontend technical decisions:

- **Frontend Framework:** React with TypeScript
- **Styling Solution:** Tailwind CSS + shadcn/ui component library
- **Platform Target:** Desktop-first standalone web application (1280px+)
- **Browser Support:** Chrome, Firefox, Safari, Edge (latest 2 versions)
- **Design System:** Tailwind CSS utility-first approach with shadcn/ui components
- **Performance Expectations:** Optimistic UI (<100ms acknowledgment), progressive loading, contextual progress indicators

**From Technical Brief:**

Backend technology decisions identified for evaluation:

- **Backend Language:** Python (FastAPI) - chosen for AI/ML ecosystem dominance
- **Agent Framework:** LangGraph - production-ready state graph orchestration
- **Knowledge Graph:** Neo4j vs Amazon Neptune vs TigerGraph (to be decided)
- **Vector Database:** Pinecone vs Weaviate vs Qdrant (to be decided)
- **LLM Provider:** Claude 3.5 Sonnet vs GPT-4 vs Multi-provider (to be decided)

### Starter Options Considered

**Frontend Evaluation:**

**Option 1: Vite + React 19 + TypeScript + Tailwind 4 + shadcn/ui**
- Template: doinel1a/vite-react-ts-shadcn-ui
- Evaluation: Perfect alignment with UX specification, optimized for SPA use case
- Build Tool: Vite 7 with SWC compiler (faster than Webpack/Next.js for SPAs)
- Components: React 19, TypeScript 5, TailwindCSS 4, shadcn/ui pre-configured
- Developer Experience: ESLint 9, Prettier, Husky pre-commit hooks
- Production Readiness: All code quality automation in place

**Option 2: Next.js 15 + shadcn/ui**
- Template: siddharthamaity/nextjs-15-starter-shadcn
- Evaluation: More features than needed (SSR, API routes, image optimization)
- Trade-off: Heavier framework overhead for standalone SPA use case
- Decision: Not selected - Next.js shines for content-heavy SSR sites, not authenticated SPAs

**Backend Evaluation:**

**Decision: Custom FastAPI Backend from Scratch**
- Evaluation: Full architectural control for multi-agent orchestration requirements
- Rationale: Build exactly what's needed without template assumptions or unnecessary abstractions
- Approach: Start with minimal FastAPI setup, add LangGraph and infrastructure incrementally
- Benefits:
  - Complete control over agent orchestration patterns
  - No template cruft to remove or work around
  - Learn and optimize each architectural decision
  - Tailored specifically to Passport intelligence generation pipeline
- Trade-offs: More upfront architectural work, but better long-term maintainability

### Selected Starters

**Frontend: Vite + React 19 + TypeScript + Tailwind 4 + shadcn/ui**

**Rationale for Selection:**

1. **Perfect UX Spec Alignment:** Matches Tailwind + shadcn/ui requirements exactly
2. **SPA Optimization:** Vite is purpose-built for standalone SPAs with fastest dev server and build times
3. **Modern Stack:** React 19, TypeScript 5, Tailwind 4 (latest stable versions)
4. **Developer Experience:** SWC compiler, hot module replacement, ESLint 9, Prettier, Husky
5. **Production Ready:** All code quality automation and pre-commit hooks configured
6. **No Overhead:** Unlike Next.js, no SSR complexity for a use case that doesn't need it

**Initialization Commands:**

Option A - Clone the starter (fastest bootstrap):
```bash
git clone https://github.com/doinel1a/vite-react-ts-shadcn-ui.git passport-intelligence-frontend
cd passport-intelligence-frontend
npm install
npm run dev
```

Option B - Official Vite + manual shadcn/ui setup (more control):
```bash
npm create vite@latest passport-intelligence-frontend -- --template react-ts
cd passport-intelligence-frontend
npm install
npx shadcn@latest init
npm run dev
```

**Architectural Decisions Provided by Frontend Starter:**

**Language & Runtime:**
- TypeScript 5 with strict mode enabled
- React 19 with latest JSX transform
- ES2022 target for modern JavaScript features
- Node.js 18+ runtime requirement

**Styling Solution:**
- Tailwind CSS 4 with JIT (Just-In-Time) compiler
- shadcn/ui component library (Radix UI primitives)
- CSS Modules support for component-scoped styles
- PostCSS for CSS processing pipeline

**Build Tooling:**
- Vite 7 as build tool and dev server
- SWC (Speedy Web Compiler) instead of Babel for 20x faster compilation
- Rollup for production bundling with tree-shaking
- Automatic code splitting and lazy loading
- Asset optimization (images, fonts, icons)

**Testing Framework:**
- Testing setup ready for Vitest (Vite-native test runner)
- React Testing Library patterns
- Component testing infrastructure

**Code Organization:**
- `src/` directory for all source code
- `src/components/` for React components
- `src/lib/` for utility functions and shared code
- `src/assets/` for static assets (images, fonts)
- `src/styles/` for global styles and Tailwind configuration
- Component co-location pattern (component + test + styles in same directory)

**Development Experience:**
- ESLint 9 with TypeScript and React plugins
- Prettier for consistent code formatting
- Husky for Git hooks (pre-commit linting and formatting)
- VS Code configuration included (.vscode/ settings)
- Hot module replacement (HMR) for instant feedback
- Fast Refresh for React component updates without losing state

---

**Backend: Custom FastAPI + LangGraph Multi-Agent Architecture**

**Rationale for Custom Build:**

1. **Architectural Control:** Full control over multi-agent orchestration patterns without template constraints
2. **Tailored Infrastructure:** Build exactly what's needed for Passport intelligence generation (no unused features)
3. **Clean Foundation:** Start minimal, add complexity incrementally as requirements emerge
4. **Learning & Optimization:** Understand every architectural decision deeply for long-term maintainability
5. **No Technical Debt:** Avoid inheriting template assumptions or abstractions that don't fit use case

**Why FastAPI + LangGraph:**

**FastAPI Selection:**
- **Async-First Design:** Perfect for concurrent LLM calls, KG queries, Passport API integrations (I/O-bound operations)
- **Type Safety:** Pydantic models ideal for YAML business rule validation and request/response schemas
- **Performance:** High throughput for concurrent query processing (100+ concurrent users requirement)
- **Auto Documentation:** OpenAPI/Swagger docs auto-generated (useful for frontend integration and power user APIs)
- **Python AI Ecosystem:** Native compatibility with LangChain, LangGraph, major LLM SDKs

**LangGraph for Multi-Agent Orchestration:**

Based on 2026 production best practices research:
- **Production Stable:** 86% of enterprise copilot spending uses agent frameworks; LangGraph has reached production maturity
- **State Graph Model:** Nodes (agents) and edges (control flow) with conditional routing - perfect for mode detection, quality scoring loops, iterative refinement
- **Observability:** Graph execution traces provide agent flow visibility (critical debugging requirement)
- **Modularity:** Independent agent development and testing, agents can be composed into subgraphs (mode-specific variations)
- **Control Flow Patterns:** Supervisor/Orchestrator, Router + Experts (mode detection), Shared State (unified query/KG/quality data access)

**Initialization Commands:**

```bash
# Create project directory
mkdir passport-intelligence-backend
cd passport-intelligence-backend

# Initialize Python environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install core dependencies
pip install fastapi uvicorn[standard] pydantic pydantic-settings
pip install langgraph langchain langchain-core
pip install httpx python-multipart python-jose[cryptography] passlib[bcrypt]

# Create initial project structure
mkdir -p app/{agents,api,models,services,core}
touch app/__init__.py app/main.py
touch app/agents/__init__.py app/api/__init__.py
touch app/models/__init__.py app/services/__init__.py app/core/__init__.py

# Start development server
uvicorn app.main:app --reload
```

**Architectural Decisions for Custom Backend:**

**Language & Runtime:**
- Python 3.10+ with type hints throughout
- FastAPI 0.100+ framework (async-first ASGI)
- Pydantic v2 for data validation and settings
- asyncio for concurrent operations
- Poetry or pip for dependency management

**Agent Orchestration:**
- LangGraph for state graph-based agent coordination
- State management with typed state objects
- Agent node definitions with input/output schemas
- Conditional edge routing for dynamic workflows
- Checkpoint/resume capabilities for long-running operations
- Agent composition patterns (hierarchical, parallel, sequential)

**Memory & State:**
- pgvector support for long-term memory (conversation history, user context)
- In-memory state for request lifecycle
- Redis integration option for distributed state (scalability)
- State persistence patterns for resumable workflows

**Authentication & Security:**
- JWT token-based authentication ready
- Session management patterns
- Rate limiting middleware (per-user, per-endpoint)
- CORS configuration
- Request validation with Pydantic models
- Security headers middleware

**API Design:**
- RESTful endpoint conventions
- API versioning support (v1, v2 routes)
- Request/response models with Pydantic
- Automatic OpenAPI/Swagger documentation
- Health check endpoints
- Graceful error handling with structured responses

**Observability:**
- Prometheus metrics integration (request count, duration, errors)
- Structured logging with correlation IDs
- Request tracing patterns
- Health and readiness endpoints
- Metrics export for monitoring stack integration

**Testing Infrastructure:**
- pytest framework setup
- Async test support with pytest-asyncio
- Test fixtures for common scenarios
- API endpoint testing patterns
- Agent workflow testing examples

**Code Organization:**
- `app/` root directory for application code
- `app/agents/` for LangGraph agent definitions
- `app/api/` for FastAPI route handlers
- `app/models/` for Pydantic models and schemas
- `app/services/` for business logic layer
- `app/core/` for configuration and core utilities
- `app/db/` for database connections and models
- `tests/` for test suite
- Agent isolation pattern (each agent as independent module)

**Development Experience:**
- Hot reload with uvicorn --reload
- Automatic API documentation (Swagger UI at /docs)
- Type checking with mypy
- Code formatting with black and isort
- Linting with flake8 or ruff
- Docker and docker-compose for local development
- Environment-based configuration (.env files)

**Deployment:**
- Docker containerization with multi-stage builds
- docker-compose for local orchestration
- Health checks for container orchestration
- Environment variable configuration
- Gunicorn + Uvicorn workers for production
- Horizontal scaling patterns (stateless request handling)

### Technology Stack Summary

**Frontend Stack:**
- **Framework:** React 19
- **Language:** TypeScript 5
- **Build Tool:** Vite 7 (SWC compiler)
- **Styling:** Tailwind CSS 4
- **Components:** shadcn/ui (Radix UI primitives)
- **State Management:** (To be decided - React Context, Zustand, or Redux Toolkit)
- **HTTP Client:** (To be decided - fetch API, axios, or react-query)
- **Code Quality:** ESLint 9, Prettier, Husky
- **Testing:** Vitest, React Testing Library

**Backend Stack:**
- **Framework:** FastAPI (async ASGI)
- **Language:** Python 3.10+
- **Agent Framework:** LangGraph (state graph orchestration)
- **Validation:** Pydantic v2
- **Authentication:** JWT patterns (to be enhanced with SSO)
- **Observability:** Prometheus metrics, structured logging
- **Testing:** pytest, pytest-asyncio
- **Containerization:** Docker, docker-compose

**Infrastructure (To Be Decided in Next Steps):**
- **Knowledge Graph:** Neo4j vs Amazon Neptune vs TigerGraph
- **Vector Database:** Pinecone vs Weaviate vs Qdrant
- **LLM Provider:** Claude 3.5 Sonnet vs GPT-4 vs Multi-provider
- **Cloud Provider:** AWS vs Azure vs GCP
- **Orchestration:** Kubernetes vs AWS ECS
- **Monitoring:** Datadog vs New Relic vs Prometheus + Grafana
- **Message Queue:** RabbitMQ vs AWS SQS vs Redis Streams (for agent coordination)
- **Cache Layer:** Redis vs Memcached

### First Implementation Story

**Project Initialization:**

The first development story should initialize both frontend and backend projects using these starters:

**Story: Initialize Frontend and Backend Projects**

**Frontend Setup:**
1. Clone or create Vite + React + TypeScript project with shadcn/ui
2. Verify all dependencies install correctly
3. Configure Tailwind CSS with project-specific design tokens (colors, typography from UX spec)
4. Set up initial component structure (AppShell, Header, Sidebar, SearchBar stubs)
5. Verify hot reload and development server
6. Commit initial project structure

**Backend Setup:**
1. Create FastAPI project from scratch with initial directory structure
2. Create Python virtual environment and install core dependencies (FastAPI, LangGraph, Pydantic)
3. Configure environment variables (.env template)
4. Create minimal FastAPI app with health check endpoint
5. Verify FastAPI server starts and /docs endpoint accessible
6. Create initial agent structure stubs (app/agents/ with QueryInterpreter, DataRetrieval placeholders)
7. Set up Neo4j connection configuration stub
8. Create requirements.txt with pinned versions
9. Commit initial project structure

**Integration Verification:**
1. Configure frontend to call backend health endpoint
2. Set up CORS in backend for frontend origin
3. Verify end-to-end connectivity (frontend → backend → response)
4. Document API endpoint patterns for team

**Acceptance Criteria:**
- Frontend dev server runs on port 5173 (Vite default)
- Backend API server runs on port 8000 (FastAPI default)
- Frontend can successfully call backend health endpoint
- Both projects have README with setup instructions
- All linting and formatting passes
- Docker containers build successfully (if using Docker for development)

### Note on Starter Template Philosophy

**What Starters Provide:**
- Foundational architecture and project structure
- Best practice configurations (linting, formatting, testing)
- Development workflow automation (hot reload, pre-commit hooks)
- Production-ready patterns (error handling, logging, security)

**What Starters Don't Provide:**
- Domain-specific business logic (your 8-agent pipeline, mode detection, YAML rules)
- External service integrations (Passport APIs, LLM providers, KG technology)
- Deployment-specific configurations (cloud provider, orchestration platform)
- Data models and schemas (intelligence reports, citations, user permissions)

**Expected Customization:**
- Remove unused template features (long-term memory if not needed immediately)
- Add project-specific middleware (permission checks, Passport API auth)
- Implement domain models (Query, IntelligenceReport, Citation, QualityScore)
- Configure production deployment (Kubernetes manifests, CI/CD pipelines)
- Add monitoring and alerting specific to agent workflows

This starter template foundation provides the architectural scaffolding while preserving full flexibility for the unique multi-agent intelligence generation requirements.

## Core Architectural Decisions

### Decision Priority Analysis

**Critical Decisions (Block Implementation):**

These decisions were made collaboratively to establish the foundational architecture before implementation can begin:

1. **Knowledge Graph Technology:** Neo4j with Vector Search Plugin
2. **LLM Provider:** Claude 3.5 Sonnet (Anthropic API)
3. **Cloud Provider:** AWS
4. **Container Orchestration:** Amazon ECS (with Fargate)
5. **Relational Database:** Amazon RDS (PostgreSQL)
6. **Caching Layer:** Amazon ElastiCache (Redis)

**Important Decisions (Shape Architecture):**

7. **Message Queue:** AWS SQS + SNS (agent coordination)
8. **Monitoring & Observability:** AWS CloudWatch + X-Ray
9. **Frontend State Management:** TanStack Query (React Query) + Zustand
10. **Authentication Strategy:** JWT tokens (MVP), SSO path for production
11. **API Documentation:** FastAPI auto-generated (Swagger/OpenAPI)

**Deferred Decisions (Post-MVP):**

- **SSO Integration:** Defer SAML 2.0/OAuth 2.0 implementation to production phase (use simple JWT auth for MVP)
- **Advanced Observability:** Start with CloudWatch; evaluate Datadog/Prometheus if agent debugging becomes complex
- **Multi-LLM Strategy:** Start with Claude 3.5 Sonnet; add GPT-4 fallback only if needed for resilience
- **CI/CD Pipeline:** Defer detailed pipeline design until core application architecture is implemented
- **Advanced Caching Strategies:** Start simple; optimize based on performance profiling

### Data Architecture

**Decision 1: Knowledge Graph Technology**

**Choice:** Neo4j with Vector Search Plugin

**Version:** Neo4j 5.x (latest stable) with Vector Search enabled

**Rationale:**
- **Unified Data Layer:** Single database handles both graph relationships (structured Passport taxonomy) and vector similarity (semantic search across unstructured content)
- **Architectural Simplicity:** No separate vector database to manage, reducing operational complexity
- **Query Efficiency:** Single query can combine graph traversal (e.g., "find all competitors in beverage category") + vector similarity (e.g., "semantically similar regulatory changes")
- **Mature Ecosystem:** Rich graph algorithms, Cypher query language expressiveness, excellent visualization tools (Neo4j Bloom, Neo4j Browser)
- **Cross-Content Retrieval:** Enables "connections current tools can't find" by combining structured relationships with semantic similarity

**Deployment:**
- **AWS Marketplace:** Neo4j AuraDB (fully managed) for MVP/development
- **Production Option:** Self-hosted on ECS for cost optimization and full control
- **Scaling:** Read replicas for query load distribution, sharding if corpus exceeds single-node capacity

**Integration Points:**
- Python client: `neo4j` driver for Cypher queries
- Vector embeddings: Claude/OpenAI embeddings (1536-3072 dimensions)
- Data ingestion: Batch import from Passport APIs, incremental updates via change detection

**Affects:**
- Data Retrieval Agent (KG queries)
- Citation Specialist (source metadata tracking)
- KG Maintenance Pipeline (data sync, validation)

**Trade-offs Accepted:**
- Neo4j Vector Search is newer than dedicated vector DBs (Pinecone, Weaviate), but sufficient for requirements
- Potential future migration to dedicated vector DB if semantic search needs become more complex

---

**Decision 2: Relational Database**

**Choice:** Amazon RDS (PostgreSQL)

**Version:** PostgreSQL 15.x (latest stable on RDS)

**Rationale:**
- **Managed Service:** Automatic backups, patching, multi-AZ for 99.5% SLA requirement
- **Enterprise Features:** JSON/JSONB support for flexible audit log schemas, full-text search, row-level security
- **Python Ecosystem:** Excellent libraries (SQLAlchemy ORM, asyncpg for async operations, Alembic for migrations)
- **Audit Trail Requirements:** Handles 12-month retention (NFR42) with efficient indexing and partitioning

**Use Cases:**
- **User Management:** Accounts, profiles, preferences
- **RBAC:** Role assignments, permission mappings
- **Subscription Permissions:** Geography/category access control by subscription tier
- **Audit Logs:** Comprehensive logging (queries, mode detection, data retrieval, report generation, user actions)
- **Admin/Operations Data:** Configuration, beta group management, system settings

**Schema Design Approach:**
- **Users Table:** id, email, hashed_password, created_at, updated_at
- **Roles Table:** id, name, permissions (JSONB)
- **User_Roles Table:** user_id, role_id (many-to-many)
- **Subscriptions Table:** user_id, geography_permissions (array), category_permissions (array), tier
- **Audit_Logs Table:** id, user_id, action_type, payload (JSONB), timestamp, correlation_id

**Deployment:**
- Multi-AZ deployment for high availability
- db.t3.medium instance type for MVP (scalable to larger instances)
- Automated daily backups with 12-month retention
- Read replicas for analytics/reporting workloads (if needed)

**Integration Points:**
- SQLAlchemy ORM for data models
- Alembic for schema migrations
- asyncpg for high-performance async database operations

**Affects:**
- Authentication & Authorization Service
- Admin Dashboard Backend
- Operations Dashboard Backend
- Audit Trail & Logging Service

---

**Decision 3: Caching Layer**

**Choice:** Amazon ElastiCache (Redis)

**Version:** Redis 7.x (latest stable on ElastiCache)

**Rationale:**
- **Managed Service:** Automatic failover, scaling, backups, patching
- **Performance Optimization:** Reduces LLM API calls (cost), KG query load (latency), improves <3 min response time target
- **Flexible Data Structures:** Strings (simple cache), Hashes (structured data), Lists (query history), Sets (user permissions)
- **TTL Support:** Automatic expiration for time-sensitive caches

**Caching Strategy:**

**LLM Response Caching:**
- Key: `llm:hash(prompt+model+params)` → Value: LLM response
- TTL: 24 hours (balance freshness vs cost savings)
- Invalidation: Manual flush on YAML rule changes

**KG Query Results Caching:**
- Key: `kg:query:hash(cypher_query)` → Value: Query results
- TTL: 1 hour (Passport data refreshes infrequently)
- Invalidation: Clear on KG data updates

**Common Queries Caching:**
- Key: `report:mode:hash(user_query)` → Value: Full intelligence report
- TTL: 6 hours (balance between freshness and performance)
- Invalidation: User can force refresh via UI

**Session Storage (Future):**
- Key: `session:user_id` → Value: Session data
- TTL: Based on JWT token expiration

**Deployment:**
- cache.t3.medium node type for MVP
- Single-node for MVP, cluster mode for production (high availability)
- Automatic backups enabled

**Integration Points:**
- `redis-py` (async Redis client) or `aioredis`
- Cache middleware in FastAPI
- Cache invalidation hooks in agent pipeline

**Affects:**
- LLM Gateway & Prompt Management
- Knowledge Graph Query Engine
- Query Ingestion service (check cache before agent orchestration)

---

### Authentication & Security

**Decision 4: Authentication Strategy**

**Choice:** JWT Tokens (MVP), SSO Integration Path (Production)

**Version:**
- JWT: `python-jose` library (latest stable)
- Hashing: `passlib[bcrypt]` for password hashing

**MVP Implementation (Phase 1-2):**

**JWT Token-Based Authentication:**
- **Access Token:** Short-lived (15 minutes), contains user_id, roles, permissions
- **Refresh Token:** Long-lived (7 days), stored in httpOnly cookie, used to obtain new access tokens
- **Token Structure:** `{ "sub": user_id, "roles": [...], "permissions": {...}, "exp": timestamp }`
- **Storage:** Access token in memory (React state), refresh token in httpOnly cookie

**Endpoints:**
- POST `/api/v1/auth/register` - User registration
- POST `/api/v1/auth/login` - Login (returns access + refresh tokens)
- POST `/api/v1/auth/refresh` - Refresh access token
- POST `/api/v1/auth/logout` - Invalidate refresh token

**Security Measures:**
- Password hashing with bcrypt (cost factor: 12)
- Rate limiting on auth endpoints (10 requests/minute per IP)
- CORS configuration (restrict to frontend origin)
- HTTPS only (enforce in production)

**Production Path (Phase 5+):**

**SSO Integration:**
- SAML 2.0 for enterprise identity providers (Okta, Azure AD, OneLogin)
- OAuth 2.0 / OpenID Connect for modern identity providers
- Maintain JWT token format internally (SSO provides identity, backend issues JWT)
- Map SSO user attributes to internal roles/permissions

**Implementation Strategy:**
- Add SSO middleware to FastAPI (e.g., `python-saml`, `authlib`)
- SSO endpoints: `/api/v1/auth/sso/login`, `/api/v1/auth/sso/callback`
- Keep existing JWT infrastructure (SSO just changes token issuance source)

**Rationale:**
- **Stateless Scaling:** JWT tokens scale horizontally with ECS (no session storage dependency)
- **SPA Compatibility:** Standard pattern for React + FastAPI architecture
- **Production Flexibility:** JWT format preserved when adding SSO (minimal frontend changes)
- **Security:** Refresh token rotation, short-lived access tokens, httpOnly cookies

**Integration Points:**
- FastAPI dependencies for auth middleware (protect routes)
- React Query auth hooks
- Zustand store for auth state (user, roles, permissions)

**Affects:**
- Authentication & Authorization Service
- Permission Management middleware
- All protected API endpoints
- Frontend auth flows

---

### API & Communication Patterns

**Decision 5: Message Queue / Event Bus**

**Choice:** AWS SQS (Simple Queue Service) + SNS (Simple Notification Service)

**Version:** AWS managed service (always latest)

**Rationale:**
- **Fully Managed:** Zero operational overhead (no servers to manage)
- **ECS Integration:** Seamless with Fargate containers, IAM role-based access
- **Reliability:** 99.9% availability SLA, at-least-once delivery guarantee
- **Scalability:** Automatic scaling, no capacity planning needed
- **Cost Efficiency:** Pay-per-use model (no idle costs)

**Architecture Patterns:**

**SQS for Agent Task Queuing:**
- **Query Processing Queue:** Main queue for intelligence generation requests
- **Mode-Specific Queues:** Separate queues for each mode (optional for load balancing)
- **Dead Letter Queue (DLQ):** Failed tasks after retries for manual investigation
- **Message Format:** JSON payload with `query_id`, `user_query`, `mode`, `user_context`, `correlation_id`

**SNS for Event Notifications:**
- **Report Completion Topic:** Notify frontend when intelligence report ready
- **Citation Accuracy Alerts Topic:** Notify ops team when broken citations detected
- **KG Update Topic:** Trigger cache invalidation when knowledge graph updated
- **System Health Topic:** Alert on service degradation

**Multi-Agent Coordination Pattern:**

```
User Query → API Gateway
    ↓
Queue: intelligence-generation-queue
    ↓
Agent Orchestrator (polls queue)
    ↓
LangGraph State Machine
    ↓ (agent transitions)
Query Interpreter → Data Retrieval → Narrative Synthesizer → ...
    ↓ (checkpoints saved)
SNS: report-completion-topic
    ↓
Frontend (WebSocket or polling)
```

**Configuration:**
- **Visibility Timeout:** 300 seconds (5 minutes - matches max agent processing time)
- **Message Retention:** 4 days (sufficient for delayed processing + debugging)
- **Max Retries:** 3 attempts before DLQ
- **Batching:** Batch reads (10 messages) for efficiency

**Integration Points:**
- `boto3` (AWS SDK for Python)
- FastAPI background tasks or dedicated worker processes (polling SQS)
- LangGraph checkpointing (state persistence between agent transitions)

**Affects:**
- Multi-Agent Orchestration Engine
- Query Ingestion service
- Report Assembly service
- All agents in the 8-agent pipeline

---

**Decision 6: API Documentation**

**Choice:** FastAPI Auto-Generated OpenAPI/Swagger Documentation

**Version:** Built-in to FastAPI (OpenAPI 3.0.x)

**Rationale:**
- **Zero Maintenance:** Automatically generated from code (Pydantic models, route decorators)
- **Always In Sync:** Documentation reflects actual API implementation
- **Interactive Testing:** Swagger UI allows testing endpoints directly from browser
- **Standards Compliant:** OpenAPI 3.0 specification (industry standard)

**Documentation Endpoints:**
- `/docs` - Swagger UI (interactive documentation)
- `/redoc` - ReDoc (alternative cleaner view)
- `/openapi.json` - Raw OpenAPI schema (for code generation tools)

**Enhanced Documentation Strategy:**

**Route Documentation:**
```python
@router.post(
    "/query",
    response_model=IntelligenceReportResponse,
    summary="Generate Intelligence Report",
    description="Submit a natural language query to generate an intelligence report. "
                "Mode is automatically detected from query structure.",
    responses={
        200: {"description": "Intelligence report generated successfully"},
        400: {"description": "Invalid query or unsupported mode"},
        429: {"description": "Rate limit exceeded"},
        500: {"description": "Internal server error during report generation"}
    }
)
```

**Model Documentation:**
```python
class QueryRequest(BaseModel):
    query: str = Field(..., description="Natural language query", example="Soft drinks industry in France")
    user_id: str = Field(..., description="Authenticated user ID")
    correlation_id: Optional[str] = Field(None, description="Request tracking ID")

    class Config:
        schema_extra = {
            "example": {
                "query": "Bottled Water in Brazil - packaging trends",
                "user_id": "user_123"
            }
        }
```

**Integration Points:**
- Frontend developers reference `/docs` for API contracts
- Pydantic models serve as single source of truth for request/response schemas
- OpenAPI schema can generate TypeScript types for frontend (via `openapi-typescript`)

**Affects:**
- All API endpoints
- Frontend integration (TypeScript type generation)
- API testing and validation

---

### Frontend Architecture

**Decision 7: Frontend State Management**

**Choice:** TanStack Query (React Query) for Server State + Zustand for Client State

**Versions:**
- TanStack Query v5.x (latest stable)
- Zustand v4.x (latest stable)

**Rationale:**

**TanStack Query for Server State:**
- **Automatic Caching:** Reduces API calls, improves perceived performance
- **Background Refetching:** Keeps data fresh without user interaction
- **Optimistic Updates:** UI responds immediately while API processes
- **Stale-While-Revalidate:** Shows cached data while fetching fresh data
- **Perfect for Intelligence Reports:** Handles streaming updates, pagination, infinite scroll for history

**Zustand for Client State:**
- **Minimal Boilerplate:** Simple API, less verbose than Redux
- **Small Bundle Size:** ~1KB (vs 3KB for Redux Toolkit)
- **TypeScript Native:** Excellent type inference
- **Perfect for UI State:** Theme, sidebar state, modals, transient UI preferences

**State Division of Responsibility:**

**React Query Manages (Server State):**
- Intelligence reports (query, cache, invalidation)
- Query history (paginated fetching)
- Citation data (lazy loading on hover)
- User profile (fetch, cache)
- Admin dashboard data
- Operations metrics

**Zustand Manages (Client State):**
- Authentication state (user, token, roles, permissions)
- UI preferences (theme, sidebar open/closed, layout density)
- Temporary UI state (modal visibility, toast notifications)
- Form state (multi-step forms, draft queries)

**Implementation Patterns:**

**React Query Setup:**
```typescript
// queries/intelligence.ts
export const useIntelligenceReport = (queryId: string) => {
  return useQuery({
    queryKey: ['intelligence-report', queryId],
    queryFn: () => fetchIntelligenceReport(queryId),
    staleTime: 5 * 60 * 1000, // 5 minutes
    retry: 3,
  });
};

export const useGenerateReport = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (query: string) => generateReport(query),
    onSuccess: (data) => {
      queryClient.invalidateQueries(['query-history']);
      queryClient.setQueryData(['intelligence-report', data.id], data);
    },
  });
};
```

**Zustand Setup:**
```typescript
// stores/authStore.ts
export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  token: null,
  isAuthenticated: false,
  login: (user, token) => set({ user, token, isAuthenticated: true }),
  logout: () => set({ user: null, token: null, isAuthenticated: false }),
}));

// stores/uiStore.ts
export const useUIStore = create<UIState>((set) => ({
  sidebarOpen: true,
  theme: 'light',
  toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),
  setTheme: (theme) => set({ theme }),
}));
```

**Integration Points:**
- React Query DevTools for debugging API state
- Zustand DevTools for debugging client state
- React Query + Zustand work independently (no conflicts)

**Affects:**
- All React components
- API integration layer
- Authentication flows
- UI state management

---

### Infrastructure & Deployment

**Decision 8: Cloud Provider**

**Choice:** Amazon Web Services (AWS)

**Rationale:**
- **Comprehensive Service Catalog:** ECS, RDS, ElastiCache, SQS/SNS, CloudWatch - all services needed available natively
- **Enterprise Maturity:** Proven at scale, established SLAs (99.5%+ for critical services)
- **Neo4j Support:** AWS Marketplace offers Neo4j AuraDB (managed) and easy self-hosting on EC2/ECS
- **Regional Presence:** Global regions support data residency requirements (GDPR, customer-specific)
- **Security & Compliance:** SOC 2, ISO 27001, HIPAA compliance (if needed), IAM for fine-grained access control

**AWS Services Mapping:**

| Requirement | AWS Service | Configuration |
|-------------|-------------|---------------|
| Container Orchestration | ECS with Fargate | Serverless containers |
| Knowledge Graph | EC2 or ECS (Neo4j) | t3.large+ instances |
| Relational DB | RDS (PostgreSQL) | Multi-AZ, db.t3.medium |
| Caching | ElastiCache (Redis) | cache.t3.medium |
| Message Queue | SQS + SNS | Standard queues |
| Monitoring | CloudWatch + X-Ray | Logs, metrics, traces |
| Load Balancing | Application Load Balancer | HTTPS termination |
| Storage | S3 | Exported reports, backups |
| Secrets | Secrets Manager | API keys, DB credentials |
| DNS | Route 53 | Domain management |

**Deployment Architecture:**

```
Internet → Route 53 → ALB → ECS Fargate
                              ↓
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
    Frontend           Backend API          Agent Workers
    Container          Containers           (SQS polling)
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              ↓
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   RDS PostgreSQL       ElastiCache           Neo4j
   (Multi-AZ)              (Redis)          (ECS/EC2)
```

**Cost Optimization Strategies:**
- **Fargate Spot:** Use Spot instances for non-critical agent workers (70% savings)
- **RDS Reserved Instances:** 1-year commitment for predictable database workload
- **S3 Intelligent-Tiering:** Automatic cost optimization for exported reports
- **CloudWatch Log Retention:** 30 days hot, archive to S3 for 12-month audit retention

**Affects:**
- All infrastructure components
- Deployment pipelines
- Monitoring and alerting
- Cost management

---

**Decision 9: Container Orchestration**

**Choice:** Amazon ECS (Elastic Container Service) with AWS Fargate

**Rationale:**
- **Simpler than Kubernetes:** Lower operational overhead, no cluster management, faster initial setup
- **AWS Native:** Tight integration with ALB, CloudWatch, IAM, Secrets Manager, ECS Service Connect
- **Fargate Serverless:** No EC2 instance management, automatic scaling, pay-per-container
- **Sufficient for Requirements:** Multi-service architecture (frontend, backend, workers), horizontal scaling, health checks, rolling deployments

**Service Architecture:**

**ECS Services:**

1. **Frontend Service:**
   - Task Definition: Nginx serving React SPA
   - Count: 2 tasks (high availability)
   - ALB Target: Port 80/443
   - Auto-scaling: CPU > 70% or request count

2. **Backend API Service:**
   - Task Definition: FastAPI + Uvicorn
   - Count: 3+ tasks (scales with load)
   - ALB Target: Port 8000
   - Auto-scaling: CPU > 60% or active connections
   - Health Check: `/health` endpoint

3. **Agent Worker Service:**
   - Task Definition: SQS polling + LangGraph agents
   - Count: 5+ tasks (scales with queue depth)
   - No ALB (internal only)
   - Auto-scaling: SQS queue depth > 10 messages
   - Health Check: CloudWatch heartbeat

**Task Definitions:**

**Backend API Task:**
```json
{
  "family": "passport-intelligence-api",
  "cpu": "1024",
  "memory": "2048",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "containerDefinitions": [{
    "name": "api",
    "image": "<account>.dkr.ecr.<region>.amazonaws.com/passport-api:latest",
    "portMappings": [{"containerPort": 8000}],
    "environment": [
      {"name": "DATABASE_URL", "valueFrom": "arn:aws:secretsmanager:..."},
      {"name": "NEO4J_URI", "valueFrom": "arn:aws:secretsmanager:..."},
      {"name": "REDIS_URL", "valueFrom": "arn:aws:secretsmanager:..."},
      {"name": "ANTHROPIC_API_KEY", "valueFrom": "arn:aws:secretsmanager:..."}
    ],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "/ecs/passport-api",
        "awslogs-region": "us-east-1",
        "awslogs-stream-prefix": "api"
      }
    }
  }]
}
```

**Auto-Scaling Configuration:**
- **Target Tracking:** CPU utilization 60%, Memory utilization 70%
- **Step Scaling:** Queue depth (SQS) for agent workers
- **Scale-out Cooldown:** 60 seconds
- **Scale-in Cooldown:** 300 seconds (avoid thrashing)

**Deployment Strategy:**
- **Rolling Update:** Replace tasks gradually (min 50% healthy)
- **Circuit Breaker:** Auto-rollback if health checks fail
- **Blue/Green:** Use ECS deployment controller for zero-downtime production deployments

**Affects:**
- All containerized services
- Scaling strategy
- Deployment pipelines
- Infrastructure as Code (Terraform or CDK)

---

**Decision 10: Monitoring & Observability**

**Choice:** AWS CloudWatch (metrics, logs, alarms) + AWS X-Ray (distributed tracing)

**Rationale:**
- **Native Integration:** Zero configuration for ECS metrics, automatic log collection
- **Unified AWS Platform:** Single vendor, single billing, IAM-based access control
- **Sufficient for Requirements:** Covers NFR47 (operations dashboard), NFR48 (agent flow visibility), NFR49/50 (alerting)
- **Cost Efficiency:** Pay-per-use, no per-host licensing like Datadog

**CloudWatch Implementation:**

**Metrics Collection:**
- **ECS Metrics:** CPU, memory, network (automatic)
- **API Metrics:** Request count, latency, error rate (custom metrics via FastAPI middleware)
- **Agent Metrics:** Queue depth, processing time, quality scores (custom metrics from agent pipeline)
- **Database Metrics:** RDS connections, query performance (automatic)
- **Cache Metrics:** ElastiCache hit rate, memory usage (automatic)

**CloudWatch Logs:**
- **Log Groups:**
  - `/ecs/passport-api` - Backend API logs
  - `/ecs/passport-workers` - Agent worker logs
  - `/aws/rds/passport-db` - Database logs
  - `/aws/elasticache/passport-cache` - Cache logs

- **Log Insights Queries:**
  - Failed agent executions: `fields @timestamp, @message | filter @message like /ERROR/ | sort @timestamp desc`
  - Slow queries: `fields @timestamp, latency | filter latency > 5000 | stats avg(latency) by bin(5m)`
  - Citation accuracy issues: `fields @timestamp, query_id | filter @message like /citation.*failed/`

**CloudWatch Alarms:**

**Critical Alarms (PagerDuty/SNS):**
- API error rate > 1% (sustained 5 minutes) → NFR3 requirement
- Agent worker queue depth > 100 (sustained 10 minutes) → Backlog building
- RDS CPU > 80% (sustained 5 minutes) → Database overload
- Citation validation failures > 0 → NFR28 (100% accuracy requirement)

**Warning Alarms (Email/Slack):**
- API latency p95 > 4 minutes → Approaching NFR2 threshold
- Cache hit rate < 50% → Cache effectiveness degradation
- ECS task launch failures → Deployment or capacity issues

**X-Ray Distributed Tracing:**

**Instrumentation:**
- FastAPI middleware: Auto-instrument all API requests
- LangGraph agents: Custom segments for each agent execution
- Database calls: Trace PostgreSQL and Neo4j queries
- LLM calls: Trace Anthropic API requests with latency

**Trace Visualization:**
```
User Request → API Gateway
    ↓ (50ms)
Mode Detection Agent
    ↓ (200ms)
Data Retrieval Agent → Neo4j KG Query (800ms)
    ↓
Narrative Synthesizer → Claude API (2000ms)
    ↓
Citation Specialist → Validation (300ms)
    ↓
Quality Scorer (150ms)
    ↓
Report Assembly (100ms)
    ↓
Total: 3.6 seconds
```

**X-Ray Service Map:**
- Visual representation of microservices interactions
- Identify bottlenecks (slow agents, database queries)
- Error path analysis (where do failures occur?)

**Operations Dashboard:**
- **CloudWatch Dashboard:** Custom dashboard with key metrics
  - API request volume (line chart)
  - Agent processing times (bar chart)
  - Error rates by service (pie chart)
  - Queue depths (area chart)
  - Quality score distribution (histogram)

**Integration Points:**
- `boto3` CloudWatch API for custom metrics
- `aws-xray-sdk` for Python instrumentation
- CloudWatch Logs Insights for log analysis
- SNS topics for alert routing

**Affects:**
- All ECS services (automatic instrumentation)
- Operations Dashboard Backend (reads CloudWatch metrics)
- Alerting and incident response
- Agent orchestration debugging (NFR48 requirement)

---

### Decision Impact Analysis

**Implementation Sequence (Dependency Order):**

**Phase 1: Foundation (Week 1-2)**
1. Set up AWS account, IAM roles, VPC, subnets
2. Deploy RDS PostgreSQL (user database)
3. Deploy ElastiCache Redis (caching layer)
4. Set up CloudWatch log groups and basic alarms
5. Create ECR repositories for Docker images

**Phase 2: Core Services (Week 3-4)**
6. Deploy Neo4j (ECS or EC2) + configure Vector Search
7. Build FastAPI backend skeleton (auth, health checks)
8. Deploy ECS cluster + API service (no agents yet)
9. Set up SQS queues + SNS topics
10. Implement JWT authentication

**Phase 3: Frontend (Week 5)**
11. Initialize Vite + React frontend
12. Configure React Query + Zustand
13. Deploy frontend to ECS via ALB
14. Verify frontend ↔ backend connectivity

**Phase 4: Agent Pipeline (Week 6-8)**
15. Implement LangGraph state machine
16. Build core agents (Query Interpreter, Data Retrieval, Narrative Synthesizer)
17. Integrate Claude 3.5 Sonnet API
18. Deploy agent worker service (SQS polling)
19. Implement YAML business rules engine

**Phase 5: Integration & Testing (Week 9-10)**
20. End-to-end testing of Mode 1 (Market Overview Report)
21. X-Ray distributed tracing setup
22. Performance testing (concurrent load)
23. Security hardening (rate limiting, input validation)

**Cross-Component Dependencies:**

**Neo4j → All Agents:**
- Data Retrieval Agent queries KG
- Citation Specialist validates sources in KG
- Mode Detection may use KG metadata

**PostgreSQL → Authentication + Audit:**
- All API requests validate auth against PostgreSQL
- Audit logs written to PostgreSQL asynchronously (via SQS)

**ElastiCache → Performance:**
- LLM Gateway checks cache before Claude API call
- KG Query Engine caches Cypher query results
- API middleware caches common queries

**SQS/SNS → Agent Orchestration:**
- Query submitted → SQS queue
- Agent worker polls SQS → executes LangGraph
- Completion → SNS notification → Frontend

**CloudWatch + X-Ray → All Services:**
- Every service sends logs, metrics, traces
- Operations dashboard reads CloudWatch metrics
- Agent debugging requires X-Ray traces

**Critical Path for MVP (Mode 1 Only):**
```
AWS Infrastructure → RDS + Redis + Neo4j
    ↓
FastAPI Backend + Auth
    ↓
LangGraph + Core Agents (Mode 1)
    ↓
Frontend (Query → Report Display)
    ↓
CloudWatch Monitoring
```

### Technology Stack - Final Summary

**Data Layer:**
- **Knowledge Graph:** Neo4j 5.x with Vector Search Plugin
- **Relational Database:** Amazon RDS (PostgreSQL 15.x)
- **Caching:** Amazon ElastiCache (Redis 7.x)
- **Message Queue:** AWS SQS + SNS

**Application Layer:**
- **Backend Framework:** FastAPI (async ASGI, Python 3.10+)
- **Agent Framework:** LangGraph (state graph orchestration)
- **LLM Provider:** Claude 3.5 Sonnet (Anthropic API)
- **Frontend Framework:** React 19 + TypeScript 5
- **Build Tool:** Vite 7 (SWC compiler)
- **Styling:** Tailwind CSS 4 + shadcn/ui
- **State Management:** TanStack Query v5 + Zustand v4
- **Authentication:** JWT tokens (python-jose, passlib[bcrypt])

**Infrastructure (AWS):**
- **Compute:** Amazon ECS (Fargate serverless containers)
- **Load Balancing:** Application Load Balancer (ALB)
- **Monitoring:** AWS CloudWatch + X-Ray
- **Secrets:** AWS Secrets Manager
- **Storage:** Amazon S3 (exported reports, backups)
- **DNS:** Route 53

**Development Tools:**
- **API Documentation:** FastAPI auto-generated (OpenAPI/Swagger)
- **Testing:** pytest (backend), Vitest + React Testing Library (frontend)
- **Code Quality:** ESLint 9, Prettier, Black, isort, mypy
- **Version Control:** Git + GitHub
- **CI/CD:** GitHub Actions (TBD in implementation phase)

**External Services:**
- **LLM API:** Anthropic Claude API
- **Passport Integration:** Euromonitor Passport APIs (read-only)

---

This comprehensive architectural foundation provides clear technical direction for implementation while maintaining flexibility for optimization based on real-world performance data and user feedback.

## Implementation Patterns & Consistency Rules

### Overview

This section defines mandatory patterns that ALL AI agents must follow when implementing code for this project. These patterns prevent integration conflicts, ensure code compatibility, and maintain architectural consistency across the multi-agent intelligence platform.

**Critical Conflict Points Addressed:** 15 areas where AI agents could make different implementation choices

**Pattern Philosophy:** Use ecosystem conventions, follow framework defaults, prioritize developer experience.

---

### Naming Patterns

#### Database Naming Conventions (PostgreSQL)

**Tables:**
- **Format:** Plural, snake_case
- **Examples:** `users`, `queries`, `intelligence_reports`, `audit_logs`
- **Rationale:** PostgreSQL best practice, matches Python conventions, SQLAlchemy default

**Columns:**
- **Format:** snake_case
- **Examples:** `user_id`, `created_at`, `query_text`, `quality_score`
- **Rationale:** Matches Python snake_case, consistent with table naming

**Primary Keys:**
- **Format:** `id` (integer or UUID)
- **Example:** `users.id`, `queries.id`
- **Rationale:** Simple, universal, SQLAlchemy default

**Foreign Keys:**
- **Format:** `{referenced_table_singular}_id`
- **Examples:** `user_id`, `query_id`, `report_id`
- **Rationale:** Clear relationship indication, consistent pattern

**Indexes:**
- **Format:** `idx_{table}_{column(s)}`
- **Examples:** `idx_users_email`, `idx_queries_user_id_created_at`
- **Rationale:** Descriptive, easy to understand index purpose

**Constraints:**
- **Format:** `{type}_{table}_{column(s)}`
- **Examples:** `uq_users_email`, `chk_quality_score_range`, `fk_queries_user_id`
- **Rationale:** Explicit constraint type identification

**Enums:**
- **Format:** snake_case enum type, UPPER_SNAKE_CASE values
- **Example:** `mode_type` enum with values `MARKET_OVERVIEW`, `CATEGORY_DEEP_DIVE`, `REGULATORY_IMPACT`
- **Rationale:** SQL convention for enum values

---

#### API Naming Conventions (FastAPI)

**Endpoints:**
- **Format:** Plural nouns, kebab-case for multi-word resources, versioned
- **Examples:**
  - `/api/v1/users`
  - `/api/v1/queries`
  - `/api/v1/intelligence-reports`
  - `/api/v1/admin/audit-logs`
- **Rationale:** RESTful standard, collection semantics, URL-friendly

**Path Parameters:**
- **Format:** `{param_name}` in snake_case
- **Examples:** `/api/v1/users/{user_id}`, `/api/v1/queries/{query_id}/report`
- **Rationale:** FastAPI convention, consistent with Python

**Query Parameters:**
- **Format:** snake_case
- **Examples:** `?user_id=123&start_date=2026-01-01&page_size=20`
- **Rationale:** Matches backend Python conventions

**HTTP Methods:**
- **GET:** Retrieve resources (list or single)
- **POST:** Create new resources
- **PUT:** Full update of resource
- **PATCH:** Partial update of resource
- **DELETE:** Remove resource
- **Rationale:** Standard REST semantics

**Status Codes:**
- **200 OK:** Successful GET, PUT, PATCH
- **201 Created:** Successful POST
- **204 No Content:** Successful DELETE
- **400 Bad Request:** Validation error
- **401 Unauthorized:** Missing/invalid auth token
- **403 Forbidden:** Valid auth but insufficient permissions
- **404 Not Found:** Resource doesn't exist
- **429 Too Many Requests:** Rate limit exceeded
- **500 Internal Server Error:** Unexpected server error
- **503 Service Unavailable:** Temporary outage (maintenance, overload)
- **Rationale:** Standard HTTP status code semantics

---

#### Code Naming Conventions

**Backend (Python/FastAPI):**

**Files:**
- **Format:** snake_case
- **Examples:** `query_interpreter.py`, `data_retrieval_agent.py`, `auth_middleware.py`
- **Rationale:** PEP 8 Python style guide

**Classes:**
- **Format:** PascalCase
- **Examples:** `QueryInterpreter`, `DataRetrievalAgent`, `IntelligenceReport`
- **Rationale:** PEP 8 standard

**Functions/Methods:**
- **Format:** snake_case, verb_noun pattern
- **Examples:** `get_user()`, `create_query()`, `validate_citation()`, `calculate_quality_score()`
- **Rationale:** PEP 8, clear action indication

**Variables:**
- **Format:** snake_case
- **Examples:** `user_id`, `query_text`, `quality_score`, `neo4j_connection`
- **Rationale:** PEP 8 standard

**Constants:**
- **Format:** UPPER_SNAKE_CASE
- **Examples:** `MAX_QUERY_LENGTH`, `DEFAULT_QUALITY_THRESHOLD`, `ANTHROPIC_API_KEY`
- **Rationale:** PEP 8 constant convention

**Private Methods/Variables:**
- **Format:** Leading underscore `_private_method`, `_internal_var`
- **Examples:** `_validate_internal()`, `_cache_key`
- **Rationale:** Python convention for internal use

**Frontend (React/TypeScript):**

**Files:**
- **Components:** PascalCase `.tsx`
- **Utilities:** camelCase `.ts`
- **Examples:** `UserCard.tsx`, `QueryInput.tsx`, `apiClient.ts`, `formatUtils.ts`
- **Rationale:** React ecosystem convention

**Components:**
- **Format:** PascalCase, noun or noun phrase
- **Examples:** `QueryInterface`, `IntelligenceReportView`, `CitationTooltip`, `LoadingSpinner`
- **Rationale:** React/JSX convention

**Functions:**
- **Format:** camelCase, verb_noun pattern
- **Examples:** `fetchUserData()`, `handleSubmit()`, `formatDate()`, `validateQuery()`
- **Rationale:** JavaScript standard

**Variables:**
- **Format:** camelCase
- **Examples:** `userId`, `queryText`, `isLoading`, `reportData`
- **Rationale:** JavaScript convention

**Constants:**
- **Format:** UPPER_SNAKE_CASE
- **Examples:** `API_BASE_URL`, `MAX_RETRIES`, `DEFAULT_TIMEOUT`
- **Rationale:** JavaScript constant convention

**Hooks:**
- **Format:** `use` prefix + PascalCase
- **Examples:** `useAuth()`, `useIntelligenceReport()`, `useDebounce()`
- **Rationale:** React Hooks convention

**Types/Interfaces:**
- **Format:** PascalCase, descriptive noun
- **Examples:** `User`, `Query`, `IntelligenceReport`, `ApiResponse<T>`
- **Rationale:** TypeScript convention

---

#### JSON Field Naming (API Contracts)

**Backend → Frontend (Pydantic Auto-Conversion):**

**Python Models Use snake_case:**
```python
class IntelligenceReport(BaseModel):
    report_id: str
    user_id: str
    query_text: str
    created_at: datetime
    quality_score: float

    class Config:
        # Pydantic will auto-convert to camelCase in JSON
        alias_generator = lambda s: ''.join(
            word.capitalize() if i > 0 else word
            for i, word in enumerate(s.split('_'))
        )
        populate_by_name = True
```

**JSON Response Uses camelCase:**
```json
{
  "reportId": "rep_123",
  "userId": "usr_456",
  "queryText": "Bottled water in France",
  "createdAt": "2026-01-21T10:30:00Z",
  "qualityScore": 0.87
}
```

**Rationale:**
- Backend uses Python conventions (snake_case)
- Frontend receives JavaScript conventions (camelCase)
- Pydantic handles conversion automatically
- No manual mapping needed

**Special Cases:**
- **Nested Objects:** Apply same conversion recursively
- **Arrays:** Item fields also converted to camelCase
- **Enums:** Use UPPER_SNAKE_CASE in backend, keep uppercase in JSON

---

#### Event Naming Conventions (SQS/SNS)

**Format:** `{domain}.{entity}.{action}` (lowercase, dot-separated)

**Examples:**
- `intelligence.query.submitted`
- `intelligence.report.completed`
- `intelligence.citation.validated`
- `system.kg.updated`
- `system.cache.invalidated`
- `user.subscription.changed`

**Rationale:** Hierarchical, clear intent, easy to filter/route

**Payload Structure:**
```json
{
  "eventId": "evt_123",
  "eventType": "intelligence.report.completed",
  "timestamp": "2026-01-21T10:30:00Z",
  "correlationId": "corr_456",
  "data": {
    "reportId": "rep_789",
    "userId": "usr_101",
    "mode": "MARKET_OVERVIEW",
    "qualityScore": 0.85
  },
  "metadata": {
    "source": "agent-orchestrator",
    "version": "1.0"
  }
}
```

**Rationale:** Consistent structure, traceability, versioning support

---

### Structure Patterns

#### Project Organization

**Backend (FastAPI + LangGraph):**

```
passport-intelligence-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI app entry point
│   ├── agents/                    # LangGraph agents
│   │   ├── __init__.py
│   │   ├── query_interpreter.py
│   │   ├── data_retrieval.py
│   │   ├── narrative_synthesizer.py
│   │   ├── citation_specialist.py
│   │   ├── quality_scorer.py
│   │   └── orchestrator.py        # LangGraph state machine
│   ├── api/                       # API route handlers
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── queries.py
│   │   │   ├── reports.py
│   │   │   └── users.py
│   │   └── dependencies.py        # Shared dependencies
│   ├── core/                      # Core utilities
│   │   ├── __init__.py
│   │   ├── config.py              # Settings (Pydantic)
│   │   ├── security.py            # JWT, auth utils
│   │   ├── logging.py             # Logging setup
│   │   └── exceptions.py          # Custom exceptions
│   ├── db/                        # Database layer
│   │   ├── __init__.py
│   │   ├── postgresql.py          # PostgreSQL connection
│   │   ├── neo4j.py               # Neo4j connection
│   │   ├── redis.py               # Redis connection
│   │   └── models.py              # SQLAlchemy models
│   ├── models/                    # Pydantic models (schemas)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── query.py
│   │   ├── report.py
│   │   └── common.py              # Shared models
│   ├── services/                  # Business logic
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── query_service.py
│   │   ├── kg_service.py
│   │   ├── llm_service.py         # Claude API wrapper
│   │   └── cache_service.py
│   └── utils/                     # Helper utilities
│       ├── __init__.py
│       ├── validators.py
│       ├── formatters.py
│       └── yaml_parser.py         # YAML business rules
├── tests/                         # Test suite
│   ├── __init__.py
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── alembic/                       # Database migrations
│   ├── versions/
│   └── env.py
├── .env.example
├── requirements.txt
├── Dockerfile
└── README.md
```

**Frontend (React + Vite):**

```
passport-intelligence-frontend/
├── src/
│   ├── main.tsx                   # App entry point
│   ├── App.tsx                    # Root component
│   ├── components/                # Reusable components
│   │   ├── ui/                    # shadcn/ui components
│   │   │   ├── button.tsx
│   │   │   ├── input.tsx
│   │   │   └── ...
│   │   ├── layout/
│   │   │   ├── AppShell.tsx
│   │   │   ├── Header.tsx
│   │   │   └── Sidebar.tsx
│   │   ├── query/
│   │   │   ├── QueryInput.tsx
│   │   │   └── QueryHistory.tsx
│   │   └── report/
│   │       ├── ReportView.tsx
│   │       ├── CitationTooltip.tsx
│   │       └── SectionRenderer.tsx
│   ├── features/                  # Feature modules
│   │   ├── auth/
│   │   │   ├── components/
│   │   │   ├── hooks/
│   │   │   └── api/
│   │   ├── intelligence/
│   │   │   ├── components/
│   │   │   ├── hooks/
│   │   │   └── api/
│   │   └── admin/
│   │       ├── components/
│   │       ├── hooks/
│   │       └── api/
│   ├── lib/                       # Shared utilities
│   │   ├── apiClient.ts           # Axios/fetch wrapper
│   │   ├── formatters.ts
│   │   ├── validators.ts
│   │   └── constants.ts
│   ├── hooks/                     # Shared custom hooks
│   │   ├── useDebounce.ts
│   │   └── useLocalStorage.ts
│   ├── stores/                    # Zustand stores
│   │   ├── authStore.ts
│   │   └── uiStore.ts
│   ├── queries/                   # React Query hooks
│   │   ├── useAuth.ts
│   │   ├── useIntelligence.ts
│   │   └── useUsers.ts
│   ├── types/                     # TypeScript types
│   │   ├── api.ts
│   │   ├── models.ts
│   │   └── index.ts
│   ├── styles/                    # Global styles
│   │   └── globals.css
│   └── assets/                    # Static assets
│       ├── images/
│       └── fonts/
├── public/
├── tests/
│   ├── unit/
│   └── integration/
├── .env.example
├── vite.config.ts
├── tsconfig.json
├── tailwind.config.js
├── package.json
└── README.md
```

**Rationale:**
- **Backend:** Feature-based organization (agents, api, services) with clear separation of concerns
- **Frontend:** Component-first with feature modules for complex domains
- **Both:** Tests in separate directory, clear entry points, configuration at root

---

#### Test Organization

**Backend Tests:**

**Location:** Separate `/tests` directory mirroring `/app` structure

**Structure:**
```
tests/
├── unit/
│   ├── agents/
│   │   └── test_query_interpreter.py
│   ├── services/
│   │   └── test_llm_service.py
│   └── utils/
│       └── test_validators.py
├── integration/
│   ├── test_api_endpoints.py
│   ├── test_agent_pipeline.py
│   └── test_database.py
└── e2e/
    └── test_full_report_generation.py
```

**Naming:** `test_{module_name}.py` for test files, `test_{function_name}` for test functions

**Frontend Tests:**

**Location:** Co-located with components (`.test.tsx`) OR separate `/tests` directory

**Examples:**
- `QueryInput.test.tsx` (co-located)
- `tests/unit/components/QueryInput.test.tsx` (separate)

**Rationale:** Backend uses separate tests/ (Python convention), Frontend can use co-location (React convention)

---

### Format Patterns

#### API Response Formats

**Success Response (Standard Wrapper):**

```json
{
  "data": {
    "reportId": "rep_123",
    "queryText": "Bottled water in France",
    "sections": [...]
  },
  "meta": {
    "timestamp": "2026-01-21T10:30:00Z",
    "requestId": "req_456",
    "processingTimeMs": 3200
  }
}
```

**List Response (Paginated):**

```json
{
  "data": [
    {"id": "1", "name": "..."},
    {"id": "2", "name": "..."}
  ],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "totalItems": 150,
    "totalPages": 8,
    "hasNext": true,
    "hasPrev": false
  },
  "meta": {
    "timestamp": "2026-01-21T10:30:00Z",
    "requestId": "req_789"
  }
}
```

**Error Response (Standardized):**

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid query format",
    "details": [
      {
        "field": "queryText",
        "issue": "Query text cannot be empty"
      }
    ]
  },
  "meta": {
    "timestamp": "2026-01-21T10:30:00Z",
    "requestId": "req_101",
    "path": "/api/v1/queries"
  }
}
```

**Error Codes (Standardized):**
- `VALIDATION_ERROR` - Input validation failed
- `AUTHENTICATION_ERROR` - Missing or invalid auth token
- `AUTHORIZATION_ERROR` - Insufficient permissions
- `NOT_FOUND` - Resource doesn't exist
- `RATE_LIMIT_EXCEEDED` - Too many requests
- `INTERNAL_ERROR` - Unexpected server error
- `SERVICE_UNAVAILABLE` - Temporary outage
- `MODE_DETECTION_FAILED` - Could not determine query mode
- `QUALITY_THRESHOLD_NOT_MET` - Report quality below threshold
- `CITATION_VALIDATION_FAILED` - Citation accuracy issue

**Rationale:** Consistent structure, machine-parseable error codes, request tracing

---

#### Data Format Standards

**Dates/Times:**
- **Format:** ISO 8601 strings in UTC
- **Example:** `"2026-01-21T10:30:00Z"`
- **Rationale:** Universal standard, timezone-aware, JavaScript Date() compatible

**Booleans:**
- **Format:** `true` / `false` (JSON native)
- **Never:** `1/0`, `"true"/"false"`, `"yes"/"no"`
- **Rationale:** Type safety, JSON standard

**Null Handling:**
- **Use `null` for missing optional fields**
- **Omit field entirely if optional and not set** (preferred for API responses)
- **Never use empty strings `""` to represent null**
- **Rationale:** Clear null semantics, reduces payload size

**Numeric Precision:**
- **Integers:** No quotes: `123`
- **Floats:** Include decimal: `0.85` (never `85` for percentage)
- **Currency:** Use integers (cents): `1250` for $12.50
- **Rationale:** Avoid floating-point precision issues

**IDs:**
- **Format:** String with prefix
- **Examples:** `"usr_123"`, `"rep_456"`, `"qry_789"`
- **Rationale:** Type-safe, human-readable, sortable, database-agnostic

---

### Communication Patterns

#### LangGraph State Management

**State Object Structure:**

```python
from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    # Input
    query_id: str
    user_id: str
    query_text: str
    correlation_id: str

    # Mode Detection
    detected_mode: Optional[str]
    mode_confidence: Optional[float]

    # Data Retrieval
    kg_results: Optional[dict]
    retrieved_data: Optional[List[dict]]

    # Narrative Synthesis
    narrative_sections: Optional[List[dict]]

    # Citations
    citations: Optional[List[dict]]
    citation_validation_status: Optional[str]

    # Quality
    quality_score: Optional[float]
    quality_feedback: Optional[str]

    # Final Output
    intelligence_report: Optional[dict]

    # Meta
    errors: List[str]
    warnings: List[str]
    agent_execution_log: List[dict]
```

**State Update Pattern:**
- **Immutable Updates:** Each agent returns new state (doesn't mutate)
- **Partial Updates:** Agent only updates fields it owns
- **Validation:** Pydantic models validate state at each step

**Rationale:** Type-safe, traceable, debuggable agent pipeline

---

#### Event Payload Standards

**SQS Message Format:**

```json
{
  "messageId": "msg_123",
  "messageType": "intelligence.query.submitted",
  "timestamp": "2026-01-21T10:30:00Z",
  "correlationId": "corr_456",
  "payload": {
    "queryId": "qry_789",
    "userId": "usr_101",
    "queryText": "Bottled water trends in France",
    "permissions": {
      "geographies": ["FR", "EU"],
      "categories": ["beverages"]
    }
  },
  "metadata": {
    "source": "api-gateway",
    "version": "1.0",
    "retryCount": 0
  }
}
```

**Rationale:** Consistent structure, correlation IDs for tracing, versioning for evolution

---

### Process Patterns

#### Error Handling

**Backend Error Handling:**

**Custom Exceptions:**
```python
# app/core/exceptions.py
class PassportIntelligenceException(Exception):
    """Base exception for all custom errors"""
    def __init__(self, message: str, code: str, details: dict = None):
        self.message = message
        self.code = code
        self.details = details or {}
        super().__init__(self.message)

class ValidationError(PassportIntelligenceException):
    """Input validation failed"""
    pass

class ModeDetectionError(PassportIntelligenceException):
    """Could not determine query mode"""
    pass

class QualityThresholdError(PassportIntelligenceException):
    """Report quality below acceptable threshold"""
    pass
```

**Global Exception Handler:**
```python
# app/main.py
@app.exception_handler(PassportIntelligenceException)
async def custom_exception_handler(request: Request, exc: PassportIntelligenceException):
    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
                "details": exc.details
            },
            "meta": {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "requestId": request.state.request_id,
                "path": request.url.path
            }
        }
    )
```

**Frontend Error Handling:**

**React Error Boundary:**
```tsx
// src/components/ErrorBoundary.tsx
class ErrorBoundary extends React.Component<Props, State> {
  // Standard React error boundary pattern
  // Catches render errors, logs to monitoring, shows fallback UI
}
```

**React Query Error Handling:**
```tsx
// src/queries/useIntelligence.ts
export const useGenerateReport = () => {
  return useMutation({
    mutationFn: generateReport,
    onError: (error: ApiError) => {
      // Log to monitoring
      console.error('Report generation failed:', error);

      // Show user-friendly toast notification
      toast.error(
        error.code === 'MODE_DETECTION_FAILED'
          ? 'Could not understand your query. Please rephrase.'
          : 'Failed to generate report. Please try again.'
      );
    },
  });
};
```

**Rationale:** Consistent error structure, centralized handling, user-friendly messages

---

#### Loading State Patterns

**Backend (Async Processing):**

```python
# Immediate response with job ID
@router.post("/queries", status_code=202)
async def create_query(query: QueryCreate):
    query_id = str(uuid.uuid4())

    # Send to SQS for async processing
    await sqs_client.send_message(
        queue_url=QUERY_QUEUE_URL,
        message_body=json.dumps({
            "queryId": query_id,
            "queryText": query.query_text,
            "userId": query.user_id
        })
    )

    return {
        "data": {
            "queryId": query_id,
            "status": "PROCESSING",
            "estimatedTimeSeconds": 180
        }
    }

# Polling endpoint for status
@router.get("/queries/{query_id}/status")
async def get_query_status(query_id: str):
    # Check status in database or cache
    status = await get_status(query_id)

    return {
        "data": {
            "queryId": query_id,
            "status": status.value,  # PROCESSING, COMPLETED, FAILED
            "progress": status.progress_percentage,
            "reportId": status.report_id if status.completed else None
        }
    }
```

**Frontend (React Query + Polling):**

```tsx
// src/queries/useIntelligence.ts
export const useReportStatus = (queryId: string) => {
  return useQuery({
    queryKey: ['report-status', queryId],
    queryFn: () => fetchReportStatus(queryId),
    refetchInterval: (data) => {
      // Poll every 2 seconds while processing
      return data?.status === 'PROCESSING' ? 2000 : false;
    },
    enabled: !!queryId,
  });
};

// Component usage
function ReportGenerator() {
  const generateMutation = useGenerateReport();
  const { data: status } = useReportStatus(generateMutation.data?.queryId);

  return (
    <div>
      {status?.status === 'PROCESSING' && (
        <ProgressBar value={status.progress} />
      )}
      {status?.status === 'COMPLETED' && (
        <ReportView reportId={status.reportId} />
      )}
    </div>
  );
}
```

**Rationale:** Non-blocking UI, clear progress indication, efficient polling

---

### Enforcement Guidelines

#### Mandatory Patterns - ALL AI Agents MUST:

1. **Follow naming conventions exactly** - No exceptions for database, API, code, JSON field names
2. **Use standardized API response/error formats** - All endpoints return consistent structure
3. **Implement error handling with custom exceptions** - No generic `Exception` catches
4. **Use type hints/types everywhere** - Python type hints, TypeScript strict mode
5. **Follow project organization structure** - Files go in designated directories
6. **Write tests for new code** - Minimum 80% coverage for critical paths
7. **Use Pydantic models for API schemas** - Auto-validation, auto-documentation
8. **Include correlation IDs in logs/events** - End-to-end request tracing
9. **Never commit secrets** - Use environment variables, AWS Secrets Manager
10. **Follow async patterns** - Use `async/await` in Python, avoid blocking I/O

#### Pattern Verification:

**Automated Checks (CI/CD):**
- **Linting:** `black`, `isort`, `mypy` (Python), `eslint`, `prettier` (TypeScript)
- **Type Checking:** `mypy --strict` (Python), `tsc --noEmit` (TypeScript)
- **Tests:** `pytest` with coverage threshold (Python), `vitest` (TypeScript)
- **API Schema Validation:** OpenAPI schema validation in integration tests

**Manual Checks (Code Review):**
- Verify naming conventions followed
- Check error handling patterns used
- Confirm test coverage adequate
- Validate API response formats match standard

**Pattern Violations:**
- Document in GitHub Issue with `architecture-violation` label
- Fix immediately if critical (breaks integration)
- Discuss in team meeting if pattern needs revision

**Pattern Updates:**
- Propose changes via Architecture Decision Record (ADR)
- Requires architect approval
- Update this document
- Notify all agents/developers

---

### Pattern Examples

#### Good Examples

**✅ Good: Proper API Endpoint with Error Handling**

```python
@router.post(
    "/queries",
    response_model=QueryResponse,
    status_code=202,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
    }
)
async def create_query(
    query: QueryCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Submit intelligence query for processing."""
    try:
        # Validate permissions
        if not has_permission(current_user, query.geography, query.category):
            raise AuthorizationError(
                message="Insufficient permissions for requested data",
                code="AUTHORIZATION_ERROR",
                details={"geography": query.geography, "category": query.category}
            )

        # Create query record
        query_id = str(uuid.uuid4())
        query_record = await db.execute(
            insert(queries).values(
                id=query_id,
                user_id=current_user.id,
                query_text=query.query_text,
                status="SUBMITTED"
            )
        )
        await db.commit()

        # Send to SQS for async processing
        await sqs_client.send_message(...)

        return QueryResponse(
            data=QueryData(
                query_id=query_id,
                status="PROCESSING"
            ),
            meta=MetaData(
                timestamp=datetime.utcnow(),
                request_id=request.state.request_id
            )
        )

    except AuthorizationError as e:
        raise
    except Exception as e:
        logger.error(f"Query creation failed: {e}", exc_info=True)
        raise InternalError(
            message="Failed to create query",
            code="INTERNAL_ERROR"
        )
```

**✅ Good: React Component with Proper State Management**

```tsx
// src/features/intelligence/components/QueryInput.tsx
export function QueryInput() {
  const [queryText, setQueryText] = useState('');
  const { user } = useAuthStore();
  const generateMutation = useGenerateReport();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!queryText.trim()) {
      toast.error('Please enter a query');
      return;
    }

    try {
      await generateMutation.mutateAsync({
        queryText: queryText.trim(),
        userId: user.id,
      });

      toast.success('Query submitted successfully');
      setQueryText(''); // Clear input
    } catch (error) {
      // Error handled by React Query onError
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <Input
        value={queryText}
        onChange={(e) => setQueryText(e.target.value)}
        placeholder="Ask about market trends..."
        disabled={generateMutation.isPending}
      />
      <Button type="submit" disabled={generateMutation.isPending}>
        {generateMutation.isPending ? 'Generating...' : 'Generate Report'}
      </Button>
    </form>
  );
}
```

---

#### Anti-Patterns (What to Avoid)

**❌ Bad: Inconsistent Naming**

```python
# DON'T: Mixed naming conventions
@router.get("/Users/{userId}")  # Wrong: should be /users/{user_id}
def GetUser(UserID: str):       # Wrong: function should be snake_case
    user_Data = query_db(UserID)  # Wrong: variable should be user_data
    return user_Data
```

**❌ Bad: No Error Handling**

```python
# DON'T: Bare except blocks, generic errors
@router.post("/queries")
async def create_query(query: QueryCreate):
    try:
        result = await process_query(query)
        return result
    except:  # Wrong: catches everything, no context
        return {"error": "Something went wrong"}  # Wrong: no error code, structure
```

**❌ Bad: No Type Annotations**

```python
# DON'T: Missing type hints
def calculate_quality_score(report):  # Wrong: no types
    sections = report['sections']     # Wrong: dict access without validation
    score = 0
    for section in sections:
        score += section['score']     # Wrong: might KeyError
    return score / len(sections)      # Wrong: might ZeroDivisionError
```

**❌ Bad: Inconsistent API Response**

```json
// DON'T: Custom response format
{
  "success": true,
  "result": {...},
  "time": 1234567890
}

// DO: Use standard format
{
  "data": {...},
  "meta": {
    "timestamp": "2026-01-21T10:30:00Z",
    "requestId": "req_123"
  }
}
```

**❌ Bad: Hardcoded Values**

```python
# DON'T: Hardcoded config
ANTHROPIC_API_KEY = "sk-ant-1234..."  # Wrong: never commit secrets
neo4j_uri = "bolt://localhost:7687"   # Wrong: should be env var

# DO: Use config management
from app.core.config import settings

llm_client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
neo4j_driver = GraphDatabase.driver(settings.NEO4J_URI)
```

---

### Pattern Summary

**Total Patterns Defined:** 50+ specific rules across 5 categories

**Coverage:**
- ✅ Naming: Database, API, Code, JSON, Events
- ✅ Structure: Backend, Frontend, Tests
- ✅ Format: API responses, Errors, Dates, IDs
- ✅ Communication: LangGraph state, SQS messages
- ✅ Process: Error handling, Loading states

**Enforcement:**
- Automated linting and type checking (CI/CD)
- Manual code review checklist
- Architecture violation tracking
- Pattern update process via ADRs

**Goal:** Zero integration conflicts between AI agents, consistent codebase, maintainable architecture

## Architectural Boundaries & Component Mapping

### Architectural Boundaries

#### API Boundaries

**External API (Public-facing):**

**Authentication Boundary:**
- **Entry Point:** `/api/v1/auth/*`
- **Authentication:** Public endpoints (no auth required for login/register)
- **Responsibility:** User authentication, token issuance
- **Consumes:** PostgreSQL (user data)
- **Produces:** JWT tokens
- **Endpoints:**
  - `POST /api/v1/auth/register`
  - `POST /api/v1/auth/login`
  - `POST /api/v1/auth/refresh`
  - `POST /api/v1/auth/logout`

**Intelligence Query Boundary:**
- **Entry Point:** `/api/v1/queries/*`
- **Authentication:** JWT required
- **Responsibility:** Query submission, status checking, report retrieval
- **Consumes:** PostgreSQL (query metadata), SQS (async processing), Redis (caching)
- **Produces:** Intelligence reports, query status
- **Endpoints:**
  - `POST /api/v1/queries` → Submit query for processing (202 Accepted)
  - `GET /api/v1/queries/{query_id}/status` → Poll processing status
  - `GET /api/v1/queries/{query_id}/report` → Retrieve completed report
  - `GET /api/v1/queries` → List user's queries (paginated)

**User Management Boundary:**
- **Entry Point:** `/api/v1/users/*`
- **Authentication:** JWT required (self or admin)
- **Responsibility:** User profile, preferences, subscription info
- **Consumes:** PostgreSQL (user data, subscriptions)
- **Produces:** User profile data
- **Endpoints:**
  - `GET /api/v1/users/{user_id}`
  - `PATCH /api/v1/users/{user_id}`
  - `GET /api/v1/users/{user_id}/subscription`

**Admin Boundary:**
- **Entry Point:** `/api/v1/admin/*`
- **Authentication:** JWT required (admin role)
- **Responsibility:** User provisioning, audit logs, system config
- **Consumes:** PostgreSQL (all tables), CloudWatch (metrics)
- **Produces:** Admin data, analytics
- **Endpoints:**
  - `GET /api/v1/admin/users` → List all users
  - `POST /api/v1/admin/users` → Create user
  - `GET /api/v1/admin/audit-logs` → Query audit trail
  - `GET /api/v1/admin/metrics` → System health metrics

**Operations Boundary:**
- **Entry Point:** `/api/v1/ops/*`
- **Authentication:** JWT required (operations role)
- **Responsibility:** Agent debugging, KG health, citation monitoring
- **Consumes:** CloudWatch (logs, metrics), Neo4j (KG health)
- **Produces:** Operational insights
- **Endpoints:**
  - `GET /api/v1/ops/agent-logs/{query_id}` → Agent execution logs
  - `GET /api/v1/ops/kg-health` → Knowledge graph health
  - `GET /api/v1/ops/citation-accuracy` → Citation validation stats

**Internal API (Service-to-Service):**

**Agent Orchestration Boundary:**
- **Entry Point:** Internal (not exposed via HTTP)
- **Authentication:** IAM roles (service-to-service)
- **Responsibility:** Coordinate 8-agent pipeline
- **Consumes:** SQS (query messages), Neo4j (KG), Claude API (LLM), PostgreSQL (metadata)
- **Produces:** Intelligence reports, status updates
- **Communication:** SQS message polling, SNS publishing

**LLM Service Boundary:**
- **Entry Point:** Internal service class
- **Authentication:** Anthropic API key (env var)
- **Responsibility:** Claude API calls, prompt management, caching
- **Consumes:** Redis (response cache), Claude API
- **Produces:** LLM responses (narratives, summaries, insights)
- **Rate Limiting:** Exponential backoff, retry logic

**Knowledge Graph Service Boundary:**
- **Entry Point:** Internal service class
- **Authentication:** Neo4j credentials (env var)
- **Responsibility:** Cypher queries, vector search, KG updates
- **Consumes:** Neo4j (graph database)
- **Produces:** Structured data, semantic search results
- **Caching:** Redis for frequently accessed subgraphs

---

#### Component Boundaries (Frontend)

**Authentication Context Boundary:**
- **Location:** `src/stores/authStore.ts` (Zustand)
- **Responsibility:** Auth state (user, token, roles, permissions)
- **Consumes:** `/api/v1/auth/*` endpoints
- **Produces:** Auth state for all components
- **Access Pattern:** `const { user, isAuthenticated, login, logout } = useAuthStore()`

**Query Submission Boundary:**
- **Location:** `src/features/intelligence/`
- **Responsibility:** Query input, validation, submission
- **Consumes:** `/api/v1/queries` (POST), React Query cache
- **Produces:** Query ID, processing status
- **Components:** `QueryInput`, `ModeSelector`, `QueryValidation`

**Report Display Boundary:**
- **Location:** `src/features/intelligence/components/report/`
- **Responsibility:** Render intelligence reports, citations, visualizations
- **Consumes:** `/api/v1/queries/{query_id}/report`, React Query cache
- **Produces:** Formatted report UI, export actions
- **Components:** `ReportView`, `SectionRenderer`, `CitationTooltip`, `VisualizationRenderer`

**Query History Boundary:**
- **Location:** `src/features/intelligence/components/history/`
- **Responsibility:** Display past queries, re-run, export
- **Consumes:** `/api/v1/queries` (GET), React Query cache (paginated)
- **Produces:** Query list, navigation to past reports
- **Components:** `QueryHistory`, `QueryCard`, `Pagination`

**Admin Dashboard Boundary:**
- **Location:** `src/features/admin/`
- **Responsibility:** User management, audit logs, system config
- **Consumes:** `/api/v1/admin/*`, React Query
- **Produces:** Admin UI, user provisioning forms
- **Access Control:** Only renders if user has admin role

**Operations Dashboard Boundary:**
- **Location:** `src/features/ops/`
- **Responsibility:** Agent debugging, KG health, citation monitoring
- **Consumes:** `/api/v1/ops/*`, CloudWatch metrics via API
- **Produces:** Operational insights, debugging tools
- **Access Control:** Only renders if user has operations role

---

#### Service Boundaries (Backend)

**Agent Orchestration Service:**
- **Location:** `app/agents/orchestrator.py`
- **Responsibility:** LangGraph state machine, agent coordination
- **Input:** SQS message (query payload)
- **Output:** SNS notification (report completion), PostgreSQL (status updates)
- **Dependencies:** All 8 agents, Neo4j, Claude API, PostgreSQL
- **State Persistence:** LangGraph checkpoints (Redis or PostgreSQL)
- **Error Handling:** Catch agent exceptions, retry logic, DLQ for failures

**Authentication Service:**
- **Location:** `app/services/auth_service.py`
- **Responsibility:** JWT issuance, validation, refresh, logout
- **Input:** User credentials (email/password), refresh token
- **Output:** Access token, refresh token
- **Dependencies:** PostgreSQL (users table), bcrypt (password hashing)
- **Security:** Token expiration, rotation, blacklist (Redis)

**Query Service:**
- **Location:** `app/services/query_service.py`
- **Responsibility:** Query submission, status tracking, report retrieval
- **Input:** User query, user context
- **Output:** Query ID, status, intelligence report
- **Dependencies:** PostgreSQL (queries table), SQS (message publishing), Redis (caching)
- **Caching:** Full report cache (6 hours), status cache (30 seconds)

**LLM Service:**
- **Location:** `app/services/llm_service.py`
- **Responsibility:** Claude API wrapper, prompt management, response caching
- **Input:** Prompt, system message, temperature, max_tokens
- **Output:** LLM response text
- **Dependencies:** Anthropic API (Claude 3.5 Sonnet), Redis (response cache)
- **Caching:** Hash(prompt+params) → response (24 hours TTL)
- **Rate Limiting:** Exponential backoff, 429 handling

**Knowledge Graph Service:**
- **Location:** `app/services/kg_service.py`
- **Responsibility:** Neo4j queries, vector search, KG updates
- **Input:** Cypher query or semantic search query
- **Output:** Graph data, vector search results
- **Dependencies:** Neo4j (graph + vector), Redis (query result cache)
- **Caching:** Cypher query hash → results (1 hour TTL)

**Citation Service:**
- **Location:** `app/services/citation_service.py`
- **Responsibility:** Citation validation, link verification, source metadata
- **Input:** Citation references, Passport source IDs
- **Output:** Validated citations, broken link flags
- **Dependencies:** Neo4j (source metadata), Passport API (validation)
- **Quality Gate:** 100% citation accuracy enforcement

**Quality Scoring Service:**
- **Location:** `app/services/quality_service.py`
- **Responsibility:** Multi-dimensional quality rubric, threshold enforcement
- **Input:** Intelligence report sections
- **Output:** Quality score (0-1), feedback for refinement
- **Dependencies:** YAML business rules (quality criteria), LLM (quality assessment)
- **Threshold:** >0.75 required for report completion

---

#### Data Boundaries

**PostgreSQL Boundary (Relational Data):**

**Schema Ownership:**
- **`users` table:** Owned by Authentication Service
- **`queries` table:** Owned by Query Service
- **`intelligence_reports` table:** Owned by Query Service + Agent Orchestrator
- **`audit_logs` table:** Owned by Audit Service (all services write)
- **`roles` / `user_roles` tables:** Owned by Authorization Service

**Access Patterns:**
- **Read:** Services use SQLAlchemy ORM with async sessions
- **Write:** Transactional writes via `async with db.begin()`
- **Migrations:** Alembic manages schema versions
- **Connection Pooling:** SQLAlchemy pool (min=5, max=20 connections)

**Neo4j Boundary (Graph Data):**

**Schema Ownership:**
- **Passport Taxonomy Nodes:** Owned by KG Maintenance Service
- **Market Intelligence Relationships:** Owned by KG Maintenance Service
- **Citation Source Metadata:** Owned by Citation Service
- **Vector Embeddings:** Owned by KG Maintenance Service (bulk import)

**Access Patterns:**
- **Read:** Cypher queries via `neo4j` Python driver
- **Write:** Batch imports via `LOAD CSV` or `UNWIND`
- **Vector Search:** `db.index.vector.queryNodes()` for semantic search
- **Transactions:** Use Neo4j transactions for multi-step writes

**Redis Boundary (Cache):**

**Key Namespaces:**
- **`llm:{hash}`:** LLM response cache (24h TTL)
- **`kg:query:{hash}`:** KG query result cache (1h TTL)
- **`report:{query_id}`:** Full intelligence report (6h TTL)
- **`status:{query_id}`:** Query processing status (30s TTL)
- **`session:{user_id}`:** User session data (JWT exp TTL)

**Access Patterns:**
- **Read:** `redis.get(key)` with JSON deserialization
- **Write:** `redis.setex(key, ttl, value)` with JSON serialization
- **Invalidation:** Pattern matching `redis.delete(pattern)`
- **Pub/Sub:** SNS → Lambda → Redis invalidation (KG updates)

**SQS Boundary (Message Queue):**

**Queue Ownership:**
- **`intelligence-generation-queue`:** Owned by Query Service (producer), Agent Orchestrator (consumer)
- **`citation-validation-queue`:** Owned by Citation Specialist Agent
- **`kg-update-queue`:** Owned by KG Maintenance Service
- **DLQ (Dead Letter Queue):** Owned by Operations Service (manual review)

**Message Format:**
- **Standard:** JSON payload with `messageId`, `correlationId`, `payload`, `metadata`
- **Visibility Timeout:** 300 seconds (5 minutes)
- **Retention:** 4 days
- **Batching:** Poll 10 messages at a time

**SNS Boundary (Event Bus):**

**Topic Ownership:**
- **`intelligence.report.completed`:** Published by Agent Orchestrator
- **`intelligence.citation.validated`:** Published by Citation Specialist
- **`system.kg.updated`:** Published by KG Maintenance Service
- **`system.cache.invalidated`:** Published by various services

**Subscribers:**
- Frontend (WebSocket server relay)
- Operations Dashboard (metrics aggregation)
- Audit Service (comprehensive logging)
- Cache Invalidation Lambda (Redis)

---

### Requirements to Structure Mapping

**Functional Requirements → Project Structure:**

**FR Category 1: Query & Intelligence Generation (FR1-FR9)**
- **Backend:**
  - `app/api/v1/queries.py` - Query submission endpoints
  - `app/agents/query_interpreter.py` - Query analysis agent
  - `app/agents/narrative_synthesizer.py` - Report generation agent
  - `app/services/query_service.py` - Query business logic
- **Frontend:**
  - `src/features/intelligence/components/QueryInput.tsx`
  - `src/features/intelligence/components/report/ReportView.tsx`
  - `src/queries/useIntelligence.ts` - React Query hooks

**FR Category 2: Mode Detection & Routing (FR10-FR14)**
- **Backend:**
  - `app/agents/query_interpreter.py` - Mode detection logic
  - `app/utils/yaml_parser.py` - YAML mode specification parsing
  - `app/models/mode.py` - Mode enums and schemas
- **Frontend:**
  - `src/features/intelligence/components/ModeIndicator.tsx`
  - `src/features/intelligence/components/ClarificationDialog.tsx`

**FR Category 3: Quality Assurance & Validation (FR15-FR22)**
- **Backend:**
  - `app/agents/quality_scorer.py` - Quality rubric agent
  - `app/agents/data_retrieval.py` - Data completeness validation
  - `app/services/quality_service.py` - Quality scoring logic
  - `app/utils/yaml_parser.py` - YAML quality rule parsing
- **Frontend:**
  - `src/features/intelligence/components/report/QualityBadge.tsx`
  - `src/features/admin/components/ValidationWorkflow.tsx`

**FR Category 4: Citations & Transparency (FR23-FR28)**
- **Backend:**
  - `app/agents/citation_specialist.py` - Citation validation agent
  - `app/services/citation_service.py` - Citation verification
  - `app/db/neo4j.py` - Source metadata queries
- **Frontend:**
  - `src/features/intelligence/components/report/CitationTooltip.tsx`
  - `src/features/intelligence/components/report/SourceLinkButton.tsx`
  - `src/features/intelligence/components/report/MethodologyDisclosure.tsx`

**FR Category 5: User Access & Authentication (FR29-FR33)**
- **Backend:**
  - `app/api/v1/auth.py` - Auth endpoints
  - `app/core/security.py` - JWT, password hashing
  - `app/services/auth_service.py` - Auth business logic
  - `app/db/models.py` - User model (SQLAlchemy)
- **Frontend:**
  - `src/features/auth/components/LoginForm.tsx`
  - `src/features/auth/components/RegisterForm.tsx`
  - `src/stores/authStore.ts` - Auth state management

**FR Category 6: Permissions & Data Access Control (FR34-FR40)**
- **Backend:**
  - `app/api/dependencies.py` - Permission middleware
  - `app/core/security.py` - RBAC enforcement
  - `app/db/models.py` - Subscriptions, roles tables
  - `app/services/permission_service.py` - Permission checks
- **Frontend:**
  - `src/components/layout/ProtectedRoute.tsx`
  - `src/features/auth/hooks/usePermissions.ts`

**FR Category 7: Administrative Management (FR41-FR48)**
- **Backend:**
  - `app/api/v1/admin/users.py` - User management endpoints
  - `app/api/v1/admin/config.py` - SSO configuration
  - `app/api/v1/admin/analytics.py` - Usage analytics
  - `app/services/admin_service.py` - Admin business logic
- **Frontend:**
  - `src/features/admin/components/UserManagement.tsx`
  - `src/features/admin/components/SSOConfig.tsx`
  - `src/features/admin/components/AnalyticsDashboard.tsx`

**FR Category 8: Operations & Monitoring (FR49-FR58)**
- **Backend:**
  - `app/api/v1/ops/logs.py` - Agent log endpoints
  - `app/api/v1/ops/metrics.py` - System metrics endpoints
  - `app/core/logging.py` - Structured logging setup
  - CloudWatch integration (automatic via ECS)
- **Frontend:**
  - `src/features/ops/components/AgentDebugger.tsx`
  - `src/features/ops/components/MetricsDashboard.tsx`
  - `src/features/ops/components/CitationMonitor.tsx`

**FR Category 9: Export & Integration (FR59-FR64)**
- **Backend:**
  - `app/services/export_service.py` - PDF/PPTX generation
  - `app/services/passport_service.py` - Passport API client
  - `app/api/v1/reports.py` - Export endpoints
- **Frontend:**
  - `src/features/intelligence/components/report/ExportButton.tsx`
  - `src/lib/exportUtils.ts` - Export formatting

**FR Category 10: Knowledge Graph & Data Management (FR65-FR71)**
- **Backend:**
  - `app/services/kg_service.py` - KG queries, vector search
  - `app/services/kg_maintenance.py` - KG update pipeline
  - `app/db/neo4j.py` - Neo4j connection, drivers
  - Separate KG ETL service (batch jobs)
- **Admin/Ops:**
  - KG health monitoring dashboard
  - Data quality validation tools

---

### Integration Points

#### Internal Communication Patterns

**Synchronous Communication (Request/Response):**

1. **Frontend → Backend API:**
   - **Protocol:** HTTPS REST
   - **Format:** JSON (camelCase)
   - **Authentication:** JWT Bearer token in `Authorization` header
   - **Error Handling:** Standard error response format
   - **Example:** `POST /api/v1/queries` → `202 Accepted` with `queryId`

2. **Backend API → PostgreSQL:**
   - **Protocol:** TCP (PostgreSQL wire protocol)
   - **Library:** SQLAlchemy (async ORM)
   - **Connection Pooling:** Min 5, Max 20 connections
   - **Transactions:** `async with db.begin()` for atomic operations

3. **Backend Services → Neo4j:**
   - **Protocol:** Bolt (binary)
   - **Library:** `neo4j` Python driver
   - **Query Language:** Cypher
   - **Connection Pooling:** Maintained by driver
   - **Example:** `MATCH (c:Category {name: $name}) RETURN c`

4. **Backend Services → Redis:**
   - **Protocol:** RESP (Redis Serialization Protocol)
   - **Library:** `redis-py` or `aioredis`
   - **Operations:** GET, SET, SETEX, DELETE, PUBLISH/SUBSCRIBE
   - **Connection Pooling:** Connection pool per service

5. **Backend Services → Claude API:**
   - **Protocol:** HTTPS REST
   - **Library:** `anthropic` Python SDK
   - **Authentication:** API key in header
   - **Rate Limiting:** Exponential backoff, retry with jitter
   - **Example:** `client.messages.create(model="claude-3-5-sonnet-20241022")`

**Asynchronous Communication (Message Queuing):**

1. **Query Service → SQS → Agent Orchestrator:**
   - **Flow:** Query submission publishes to SQS → Worker polls queue → Agent pipeline executes
   - **Message Format:** JSON with `queryId`, `userId`, `queryText`, `permissions`
   - **Retry:** 3 attempts with exponential backoff
   - **DLQ:** Failed messages routed to Dead Letter Queue

2. **Agent Orchestrator → SNS → Frontend (via WebSocket):**
   - **Flow:** Report completion publishes to SNS → Lambda relays to WebSocket connections
   - **Message Format:** Event type + payload
   - **Delivery:** At-least-once delivery guarantee
   - **Frontend:** Poll status endpoint as fallback if WebSocket disconnected

3. **Services → SNS → Cache Invalidation:**
   - **Flow:** KG update publishes to SNS → Lambda invalidates Redis cache
   - **Pattern Matching:** Delete keys matching `kg:*` pattern
   - **Consistency:** Eventually consistent (cache may serve stale briefly)

#### External Integration Points

**1. Anthropic Claude API:**
- **Purpose:** LLM inference for narrative generation, mode detection, quality scoring
- **Authentication:** API key from AWS Secrets Manager
- **Rate Limits:** Per-minute token limits (handled by SDK)
- **Error Handling:** Retry 429 with exponential backoff, fallback for 503
- **Cost Management:** Cache responses in Redis, deduplicate prompts
- **Monitoring:** Log all API calls with latency and token usage

**2. Euromonitor Passport API:**
- **Purpose:** Source data retrieval for KG construction, citation validation
- **Authentication:** OAuth 2.0 or API key (depends on Passport setup)
- **Rate Limits:** Graceful handling with backoff
- **Data Sync:** Scheduled batch jobs (nightly or weekly)
- **Validation:** Verify citation links resolve to valid Passport resources
- **Monitoring:** Track API availability, latency, error rates

**3. AWS Services (Native):**
- **CloudWatch:** Automatic log/metric collection from ECS
- **X-Ray:** Distributed tracing (instrumented via middleware)
- **Secrets Manager:** API keys, database credentials
- **S3:** Exported reports (PDF/PPTX), backup storage
- **Route 53:** DNS management

**4. SSO Providers (Future - Production Phase):**
- **SAML 2.0:** Okta, Azure AD, OneLogin
- **OAuth 2.0 / OpenID Connect:** Google Workspace, Microsoft 365
- **Integration:** FastAPI middleware, callback URLs
- **User Mapping:** Map SSO user attributes to internal roles/permissions

#### Data Flow Diagrams

**Intelligence Report Generation Flow:**

```
User (Frontend)
    ↓ [1. POST /api/v1/queries]
Backend API (Query Service)
    ↓ [2. Save query metadata to PostgreSQL]
    ↓ [3. Publish message to SQS]
Amazon SQS (intelligence-generation-queue)
    ↓ [4. Worker polls queue]
Agent Orchestrator (LangGraph)
    ↓ [5. Query Interpreter Agent]
    ↓ [6. Mode Detection]
    ↓ [7. Data Retrieval Agent → Neo4j KG Query]
    ↓ [8. Narrative Synthesizer → Claude API]
    ↓ [9. Citation Specialist → Validate sources]
    ↓ [10. Quality Scorer → Check threshold]
    ↓ [11. Report Assembly]
    ↓ [12. Save report to PostgreSQL]
    ↓ [13. Cache report in Redis]
    ↓ [14. Publish completion event to SNS]
Amazon SNS (intelligence.report.completed)
    ↓ [15. Lambda relays to WebSocket]
Frontend (WebSocket or Polling)
    ↓ [16. GET /api/v1/queries/{query_id}/report]
    ↓ [17. Display intelligence report]
```

**Authentication Flow:**

```
User (Frontend)
    ↓ [1. POST /api/v1/auth/login]
Backend API (Auth Service)
    ↓ [2. Query PostgreSQL for user]
    ↓ [3. Verify bcrypt password hash]
    ↓ [4. Generate JWT access token (15 min)]
    ↓ [5. Generate refresh token (7 days)]
    ↓ [6. Return tokens to frontend]
Frontend
    ↓ [7. Store access token in memory]
    ↓ [8. Store refresh token in httpOnly cookie]
    ↓ [9. Include access token in Authorization header for API calls]
Backend API (Protected Routes)
    ↓ [10. Validate JWT signature + expiration]
    ↓ [11. Extract user_id, roles, permissions]
    ↓ [12. Authorize request]
```

**Knowledge Graph Update Flow:**

```
KG Maintenance Service (Scheduled Batch Job)
    ↓ [1. Fetch new Passport data via API]
    ↓ [2. Transform to graph format]
    ↓ [3. Generate embeddings (Claude/OpenAI)]
    ↓ [4. Batch import to Neo4j via Cypher]
    ↓ [5. Update vector index]
    ↓ [6. Validate data quality]
    ↓ [7. Publish KG update event to SNS]
Amazon SNS (system.kg.updated)
    ↓ [8. Trigger cache invalidation Lambda]
Redis Cache
    ↓ [9. Delete all kg:* keys]
    ↓ [10. Fresh queries will repopulate cache]
```

---

### Development Workflow Integration

#### Development Server Structure

**Backend Development:**
```bash
# Terminal 1: PostgreSQL (Docker)
docker run -p 5432:5432 -e POSTGRES_PASSWORD=dev postgres:15

# Terminal 2: Redis (Docker)
docker run -p 6379:6379 redis:7

# Terminal 3: Neo4j (Docker)
docker run -p 7687:7687 -p 7474:7474 neo4j:5

# Terminal 4: FastAPI Development Server
cd passport-intelligence-backend
source venv/bin/activate
uvicorn app.main:app --reload --port 8000

# Auto-reload on file changes
# Access API docs at http://localhost:8000/docs
```

**Frontend Development:**
```bash
# Terminal 1: Vite Development Server
cd passport-intelligence-frontend
npm run dev

# Hot Module Replacement (HMR) enabled
# Access frontend at http://localhost:5173
# Proxies API requests to http://localhost:8000
```

**LocalStack (AWS Services Emulation - Optional):**
```bash
# Terminal: LocalStack for SQS/SNS/S3 local development
docker run -p 4566:4566 localstack/localstack

# Configure AWS SDK to use LocalStack endpoint
export AWS_ENDPOINT_URL=http://localhost:4566
```

#### Build Process Structure

**Backend Build:**
```bash
# Install dependencies
pip install -r requirements.txt

# Run linters
black app/ --check
isort app/ --check
mypy app/ --strict

# Run tests
pytest tests/ --cov=app --cov-report=html

# Build Docker image
docker build -t passport-api:latest -f Dockerfile .
```

**Frontend Build:**
```bash
# Install dependencies
npm install

# Run linters
npm run lint
npm run type-check

# Run tests
npm run test

# Build for production
npm run build
# Output: dist/ directory with optimized assets

# Build Docker image
docker build -t passport-frontend:latest -f Dockerfile .
```

#### Deployment Structure

**AWS ECS Deployment (via Docker + ECR):**

**Backend Deployment:**
```bash
# 1. Build and tag Docker image
docker build -t passport-api:v1.0.0 .

# 2. Push to AWS ECR
aws ecr get-login-password | docker login --username AWS --password-stdin <account>.dkr.ecr.us-east-1.amazonaws.com
docker tag passport-api:v1.0.0 <account>.dkr.ecr.us-east-1.amazonaws.com/passport-api:v1.0.0
docker push <account>.dkr.ecr.us-east-1.amazonaws.com/passport-api:v1.0.0

# 3. Update ECS task definition
aws ecs register-task-definition --cli-input-json file://task-definition.json

# 4. Update ECS service
aws ecs update-service --cluster passport-cluster --service passport-api --task-definition passport-api:latest --force-new-deployment
```

**Frontend Deployment:**
```bash
# 1. Build optimized production bundle
npm run build

# 2. Push to AWS ECR (containerized with Nginx)
docker build -t passport-frontend:v1.0.0 -f Dockerfile.prod .
docker tag passport-frontend:v1.0.0 <account>.dkr.ecr.us-east-1.amazonaws.com/passport-frontend:v1.0.0
docker push <account>.dkr.ecr.us-east-1.amazonaws.com/passport-frontend:v1.0.0

# 3. Update ECS service
aws ecs update-service --cluster passport-cluster --service passport-frontend --task-definition passport-frontend:latest --force-new-deployment
```

**Infrastructure as Code (Terraform or AWS CDK):**
```bash
# Define all AWS resources in code
# - ECS cluster, services, task definitions
# - RDS, ElastiCache, SQS, SNS
# - ALB, Route 53, CloudWatch, X-Ray
# - IAM roles, Security Groups, VPC

# Deploy infrastructure
terraform init
terraform plan
terraform apply

# Or with AWS CDK (Python/TypeScript)
cdk deploy PassportIntelligencePlatformStack
```

---

This comprehensive boundary and mapping documentation ensures AI agents understand exactly where each piece of functionality lives and how components communicate across architectural boundaries.

## Missing Components & Risk Mitigation

### Critical Gaps Identified in Architectural Reflection

During architectural review, five critical components were identified as missing from the initial design. These components are essential for production readiness and must be addressed before implementation.

---

### 1. Knowledge Graph Construction Project Plan

**Problem Statement:**

The architecture assumes Neo4j Knowledge Graph "exists" with >95% Passport corpus coverage, but provides no plan for how this graph gets built. This is a **critical blocker** - without the KG, agents cannot retrieve data, citations cannot be validated, and the entire system is non-functional.

**Scope & Complexity:**

- **Data Volume:** Passport corpus potentially contains millions of data points (market sizes, forecasts, company data, reports, analysis documents) across 100+ categories and 200+ countries
- **Data Types:** Structured (market data, forecasts) + Unstructured (reports, documents, analysis)
- **Relationships:** Category taxonomies, geographic hierarchies, competitive landscapes, M&A connections, regulatory impacts
- **Vector Embeddings:** Semantic search requires embedding generation for unstructured content (Claude/OpenAI embeddings API)
- **Quality Requirements:** >95% coverage, taxonomy preservation, citation source metadata accuracy

**Estimated Effort:** 6-8 weeks for initial construction, then ongoing maintenance

---

#### KG Construction Architecture

**Components Required:**

1. **Passport Data Extraction Service**
   - **Location:** Separate service or batch job (not part of main FastAPI app)
   - **Responsibility:** Fetch data from Passport APIs, handle pagination, rate limiting, authentication
   - **Technology:** Python (requests or httpx), scheduled via AWS Lambda or ECS Scheduled Task
   - **Output:** Raw Passport data stored in S3 (staging area)

2. **Data Transformation Pipeline**
   - **Location:** ETL service (AWS Glue, Apache Airflow, or custom Python scripts)
   - **Responsibility:** Transform Passport data into graph-friendly format (nodes, relationships, properties)
   - **Technology:** Python + pandas for data wrangling, Pydantic for validation
   - **Output:** CSV files or JSON ready for Neo4j import

3. **Neo4j Bulk Import Process**
   - **Location:** Neo4j Admin Tools or custom Cypher scripts
   - **Responsibility:** Load transformed data into Neo4j via `LOAD CSV` or `neo4j-admin import`
   - **Technology:** Cypher queries, Neo4j Admin Tools, bulk import for initial load
   - **Output:** Populated Neo4j graph database

4. **Vector Embedding Generation**
   - **Location:** Separate batch job (CPU/GPU intensive)
   - **Responsibility:** Generate embeddings for unstructured content (reports, documents)
   - **Technology:** Claude API or OpenAI Embeddings API, batch processing
   - **Output:** Embedding vectors stored in Neo4j vector index

5. **Data Quality Validation**
   - **Location:** Validation scripts post-import
   - **Responsibility:** Verify >95% coverage, check relationship integrity, validate taxonomy
   - **Technology:** Python + Neo4j driver, Cypher queries for coverage metrics
   - **Output:** Validation report, metrics dashboard

6. **Citation Source Metadata Indexing**
   - **Location:** Part of KG construction
   - **Responsibility:** Index all Passport source identifiers, URLs, metadata for citation validation
   - **Technology:** Neo4j nodes with source metadata properties
   - **Output:** Queryable citation source index

---

#### KG Construction Phases

**Phase 1: Pilot (Week 1-2) - Single Category**
- **Goal:** Prove KG construction process with one category (e.g., "Soft Drinks")
- **Scope:** One category, 5-10 countries, structured data only
- **Deliverables:**
  - Data extraction script for Soft Drinks category
  - Transformation logic for market size, forecasts, company data
  - Neo4j schema design (node labels, relationship types, properties)
  - Bulk import script
  - Validation metrics (coverage %, relationship counts)
- **Success Criteria:** >90% coverage for pilot category, query performance <1 second

**Phase 2: Structured Data (Week 3-5) - Full Coverage**
- **Goal:** Load all structured Passport data (market sizes, forecasts, company shares)
- **Scope:** All categories, all countries, structured data only
- **Deliverables:**
  - Scalable data extraction (pagination, rate limiting, error handling)
  - Complete taxonomy preservation (category hierarchy, geographic hierarchy)
  - Relationship modeling (competitive landscape, category connections)
  - Performance optimization (indexes, connection pooling)
  - Automated validation dashboard
- **Success Criteria:** >95% structured data coverage, query performance validated

**Phase 3: Unstructured Data + Vectors (Week 6-8) - Semantic Search**
- **Goal:** Add unstructured content and vector embeddings for semantic search
- **Scope:** Reports, documents, analysis (text content)
- **Deliverables:**
  - Text extraction from Passport documents
  - Embedding generation (batch processing, cost-optimized)
  - Neo4j vector index creation
  - Semantic search query patterns
  - Cross-content retrieval validation
- **Success Criteria:** Vector search returns relevant results, <2 second query time

**Phase 4: Citation Metadata (Week 8) - 100% Accuracy Foundation**
- **Goal:** Index all citation sources for validation
- **Scope:** Source metadata, URLs, identifiers, timestamps
- **Deliverables:**
  - Citation source node structure
  - Validation query patterns (check if citation exists in KG)
  - Broken link detection logic
  - Source metadata freshness tracking
- **Success Criteria:** All Passport sources indexed, 100% citation validation accuracy

---

#### KG Maintenance Strategy

**Incremental Updates (Daily/Weekly):**
- **Trigger:** Passport data refresh events (API webhook or scheduled check)
- **Process:**
  1. Detect changed datasets (compare timestamps, version numbers)
  2. Extract only changed data (incremental fetch)
  3. Transform and merge into Neo4j (MERGE queries, not full reload)
  4. Invalidate related cache keys in Redis
  5. Publish `system.kg.updated` event to SNS
- **Technology:** AWS Lambda triggered by CloudWatch Events or Passport webhooks

**Full Refresh (Monthly/Quarterly):**
- **Trigger:** Major Passport taxonomy changes or data quality issues
- **Process:**
  1. Create new Neo4j database instance
  2. Full data extraction and transformation
  3. Bulk import into new instance
  4. Validation and testing
  5. Blue/green deployment (switch traffic to new instance)
  6. Archive old instance (backup)
- **Downtime:** Zero (blue/green deployment pattern)

**Data Quality Monitoring:**
- **Metrics:**
  - Coverage percentage (total nodes vs expected Passport entities)
  - Relationship integrity (orphaned nodes, missing relationships)
  - Citation source availability (broken links, deprecated sources)
  - Embedding freshness (vectors generated in last 90 days)
- **Alerting:**
  - Coverage drops below 95% → Critical alert
  - Citation validation failure rate >0.1% → Warning alert
  - Embedding generation lag >7 days → Warning alert
- **Dashboard:** CloudWatch + custom metrics, visualized in Operations Dashboard

---

#### KG Construction Ownership

**Recommendation:** This should be a **separate team or contracted effort**, not part of main application development.

**Skills Required:**
- Data engineering (ETL pipelines, data quality)
- Neo4j expertise (graph modeling, Cypher optimization, bulk import)
- Passport domain knowledge (taxonomy, data structure)
- Python data wrangling (pandas, data validation)

**Alternative:** Partner with Euromonitor to provide pre-built KG or data export in graph-friendly format.

---

### 2. Disaster Recovery & Business Continuity

**Problem Statement:**

99.5% uptime SLA requires robust disaster recovery procedures, but none are documented. Data loss or extended outages could be catastrophic for enterprise users.

---

#### Backup Strategy

**PostgreSQL (RDS) Backups:**
- **Automated Daily Snapshots:**
  - RDS automated backups enabled (default 7-day retention)
  - Extended retention: 30 days for compliance
  - Cross-region backup replication to different AWS region (DR region)
- **Point-in-Time Recovery (PITR):**
  - Enabled via RDS transaction log backups
  - Can restore to any point within retention period (30 days)
  - RPO: <5 minutes (transaction log flush interval)
- **Backup Testing:**
  - Monthly restore drill (restore to test environment, verify data integrity)
  - Document restore procedure, time to restore (RTO)
- **Encryption:** Backups encrypted at rest (AWS KMS)

**Neo4j Knowledge Graph Backups:**
- **Full Database Snapshots:**
  - Daily full backup to S3 (compressed, encrypted)
  - Backup script: `neo4j-admin dump --database=neo4j --to=/backup/neo4j-$(date +%Y%m%d).dump`
  - S3 lifecycle policy: Move to Glacier after 30 days, delete after 1 year
- **Incremental Transaction Logs:**
  - Neo4j transaction logs archived to S3 hourly (if high write volume)
  - Enables point-in-time recovery
- **Backup Testing:**
  - Quarterly restore drill (restore to test Neo4j instance, verify queries work)
  - Test vector index reconstruction
- **RPO:** 24 hours (daily backup) or 1 hour (if transaction logs enabled)
- **RTO:** 4-6 hours (depends on graph size, restore time, index rebuild)

**ElastiCache Redis Backups:**
- **Automated Snapshots:**
  - Daily automatic backups (Redis AOF or RDB snapshots)
  - 7-day retention
- **Backup Strategy:**
  - Cache is ephemeral (can be rebuilt from source data)
  - Focus on configuration backup, not data backup
  - Document cache warming procedure (how to repopulate after restore)
- **RPO:** Acceptable data loss (cache can be rebuilt)
- **RTO:** 30 minutes (provision new ElastiCache, warm cache)

**Application Code & Configuration:**
- **Git Repository:** All code in GitHub (source of truth)
- **Infrastructure as Code:** Terraform or AWS CDK for all AWS resources (version controlled)
- **Secrets:** AWS Secrets Manager (automatically backed up by AWS)
- **Deployment Artifacts:** Docker images in ECR (retained for 90 days)

---

#### Disaster Scenarios & Recovery Procedures

**Scenario 1: Single AZ Failure (Most Common)**
- **Impact:** One availability zone goes down
- **AWS Auto-Recovery:**
  - RDS Multi-AZ: Automatic failover to standby (1-2 minutes)
  - ECS: Tasks restart in healthy AZ (2-5 minutes)
  - ElastiCache: Automatic failover if cluster mode enabled
- **Manual Actions:** None required (AWS handles automatically)
- **RTO:** 5 minutes
- **RPO:** Zero (Multi-AZ replication is synchronous)

**Scenario 2: Region-Wide Outage (Rare)**
- **Impact:** Entire AWS region unavailable
- **Recovery Procedure:**
  1. Activate DR region (pre-provisioned standby environment)
  2. Restore RDS from cross-region backup (2-4 hours)
  3. Restore Neo4j from S3 backup to DR region (4-6 hours)
  4. Update Route 53 DNS to point to DR region (5 minutes to propagate)
  5. Verify application functionality, data integrity
  6. Notify users of temporary degraded performance
- **Manual Actions:**
  - Terraform apply in DR region
  - Data restoration scripts
  - DNS cutover
- **RTO:** 6-8 hours (depends on data size)
- **RPO:** 24 hours (last daily backup)

**Scenario 3: Data Corruption or Accidental Deletion**
- **Impact:** Application bug or admin error corrupts data
- **Recovery Procedure:**
  1. Identify corruption timeline (when did it start?)
  2. Restore PostgreSQL to point before corruption (PITR)
  3. Restore Neo4j from most recent clean snapshot
  4. Identify affected queries/reports, notify users
  5. Validate data integrity post-restore
- **Manual Actions:**
  - RDS point-in-time restore command
  - Neo4j restore from backup
  - Data validation queries
- **RTO:** 4-6 hours
- **RPO:** Variable (PITR for PostgreSQL, 24h for Neo4j)

**Scenario 4: Security Breach / Ransomware**
- **Impact:** Unauthorized access, data encryption by attacker
- **Recovery Procedure:**
  1. **Immediate:** Isolate affected systems, revoke credentials, block attacker access
  2. **Forensics:** Preserve logs for investigation, identify breach timeline
  3. **Recovery:** Restore from known-clean backup (before breach occurred)
  4. **Hardening:** Patch vulnerabilities, rotate all credentials, enhance monitoring
  5. **Notification:** Inform users per GDPR/compliance requirements
- **Manual Actions:**
  - Security incident response team activation
  - Full environment rebuild from clean backups
  - Credential rotation across all services
- **RTO:** 12-24 hours (forensics + rebuild)
- **RPO:** Variable (restore from last known-clean backup)

---

#### Business Continuity Procedures

**Communication Plan:**
- **Status Page:** Public status page (StatusPage.io or similar) for transparency
- **User Notifications:** Email, in-app banners for planned maintenance or outages
- **Escalation Chain:** On-call rotation, PagerDuty for critical alerts
- **Stakeholder Updates:** Hourly updates during major incidents

**Incident Response Runbook:**
- **P0 (Critical):** Complete outage, data loss, security breach → Immediate response, CEO notified
- **P1 (High):** Partial outage, degraded performance → 30-minute response time
- **P2 (Medium):** Non-critical service impact → 2-hour response time
- **P3 (Low):** Minor issue, no user impact → Next business day

**Regular DR Testing:**
- **Quarterly Failover Drills:** Test RDS failover, ECS task recovery, DNS cutover
- **Annual Full DR Test:** Activate DR region, restore all services, validate end-to-end
- **Documentation Review:** Update runbooks quarterly based on lessons learned

---

### 3. Cost Management & Optimization Strategy

**Problem Statement:**

No cost estimation exists for running this platform. AWS + Claude API costs could be substantial at scale (2000+ daily queries, 100+ concurrent users). Budget overruns could halt development or force architectural compromises mid-implementation.

---

#### Cost Estimation Model

**AWS Infrastructure (Monthly Estimates):**

**Compute (ECS Fargate):**
- **Frontend:** 2 tasks × 0.5 vCPU × 1 GB RAM × 24/7 = ~$40/month
- **Backend API:** 5 tasks × 1 vCPU × 2 GB RAM × 24/7 = ~$250/month
- **Agent Workers:** 10 tasks × 1 vCPU × 2 GB RAM × 16 hrs/day (peak hours) = ~$250/month
- **Total Compute:** ~$540/month

**Database (RDS PostgreSQL):**
- **Instance Type:** db.t3.medium (2 vCPU, 4 GB RAM)
- **Multi-AZ Deployment:** Yes (for 99.5% SLA)
- **Storage:** 100 GB SSD (gp3) + backups (30 days retention)
- **Cost:** ~$150/month (instance) + ~$20/month (storage) = **~$170/month**

**Cache (ElastiCache Redis):**
- **Instance Type:** cache.t3.medium (2 vCPU, 3.09 GB RAM)
- **Cluster Mode:** Single node for MVP, 3 nodes for production
- **Cost:** ~$80/month (single node) or ~$240/month (3-node cluster)

**Neo4j Knowledge Graph:**
- **Option 1:** Neo4j AuraDB (managed) - Enterprise tier
  - Estimated: 8 GB RAM, 4 vCPUs
  - Cost: ~$400-600/month (depends on data size)
- **Option 2:** Self-hosted on ECS
  - 1 task × 4 vCPU × 8 GB RAM × 24/7
  - Cost: ~$200/month + storage (~$50/month for 500 GB)
- **Recommendation:** Start with AuraDB for simplicity, migrate to self-hosted if cost becomes issue

**Message Queue (SQS + SNS):**
- **SQS:** 2000 daily queries × 30 days = 60,000 messages/month
- **SNS:** Similar volume for notifications
- **Cost:** ~$1/month (SQS) + ~$1/month (SNS) = **~$2/month** (negligible)

**Monitoring (CloudWatch + X-Ray):**
- **Logs:** ~50 GB ingestion/month
- **Metrics:** ~100 custom metrics
- **X-Ray Traces:** ~60,000 traces/month (2000 queries/day × 30 days)
- **Cost:** ~$30/month (logs) + ~$10/month (metrics) + ~$15/month (X-Ray) = **~$55/month**

**Load Balancer (ALB):**
- **Cost:** ~$25/month (fixed) + ~$10/month (LCU charges) = **~$35/month**

**Other (S3, Secrets Manager, Route 53):**
- **S3:** Exported reports, backups (~100 GB) = ~$3/month
- **Secrets Manager:** ~10 secrets × $0.40/month = ~$4/month
- **Route 53:** 1 hosted zone + queries = ~$1/month
- **Total:** **~$8/month**

**AWS Infrastructure Total (MVP):** ~$1,100/month (AuraDB) or ~$800/month (self-hosted Neo4j)

**AWS Infrastructure Total (Production at Scale):** ~$2,500-3,000/month

---

**Claude API Costs (Anthropic):**

**Usage Assumptions:**
- 2000 queries/day at steady state
- Average tokens per query:
  - Mode detection: 1,000 input + 200 output = 1,200 tokens
  - Narrative generation: 5,000 input + 2,000 output = 7,000 tokens
  - Quality scoring: 3,000 input + 500 output = 3,500 tokens
- **Total per query:** ~11,700 tokens (~8,000 input + ~3,700 output)

**Claude 3.5 Sonnet Pricing (as of 2026-01):**
- Input: $3 per million tokens
- Output: $15 per million tokens

**Monthly Cost Calculation:**
- Input: 2000 queries/day × 8,000 tokens × 30 days × $3/1M = $1,440/month
- Output: 2000 queries/day × 3,700 tokens × 30 days × $15/1M = $3,330/month
- **Total Claude API (no caching):** ~$4,770/month

**With Caching (Estimate):**
- Cache hit rate assumption: 30% (repeated queries, similar prompts)
- Effective cost: $4,770 × 0.70 = **~$3,340/month**

**Claude API Total:** ~$3,340/month (with 30% cache hit rate)

---

**Total Monthly Cost Estimate:**

| Component | MVP (20-50 users) | Production (500 users) |
|-----------|-------------------|------------------------|
| AWS Infrastructure | $1,100 | $3,000 |
| Claude API | $1,500 (500 queries/day) | $3,340 (2000 queries/day) |
| **Total** | **~$2,600/month** | **~$6,340/month** |
| **Annual** | **~$31,200/year** | **~$76,000/year** |

**Cost Drivers:**
1. Claude API (50-60% of total cost) - scales with query volume
2. Neo4j (15-20% of total cost) - depends on data size
3. ECS Fargate (10-15% of total cost) - scales with concurrency
4. RDS PostgreSQL (5-10% of total cost) - scales with data growth

---

#### Cost Optimization Strategies

**Short-Term (MVP Phase):**

1. **Use Fargate Spot for Agent Workers:**
   - 70% cost savings on non-critical workloads
   - Risk: Task interruption (acceptable for retriable query processing)
   - Savings: ~$175/month on agent workers

2. **Aggressive Caching:**
   - Target 50% cache hit rate for LLM responses
   - Savings: ~$850/month on Claude API
   - Implementation: Redis with 24-hour TTL, hash(prompt+params) keys

3. **Right-Size Resources:**
   - Start with smaller RDS instance (db.t3.small)
   - Scale up only when needed based on metrics
   - Savings: ~$85/month initially

4. **Reserved Instances for Predictable Workloads:**
   - RDS Reserved Instance (1-year): 40% savings
   - ElastiCache Reserved Instance (1-year): 40% savings
   - Savings: ~$100/month

**Long-Term (Production Phase):**

5. **Prompt Optimization:**
   - Reduce prompt length (fewer examples, tighter instructions)
   - Target: 20% token reduction
   - Savings: ~$670/month on Claude API

6. **Batch Processing:**
   - Batch similar queries together (if possible)
   - Shared context across queries reduces token usage
   - Savings: Variable, depends on query patterns

7. **Claude Prompt Caching (Anthropic Feature):**
   - Cache common prompt prefixes (system message, YAML rules)
   - Reduces input token costs by 50-90% for cached portions
   - Savings: ~$500-1,000/month (if applicable)

8. **Self-Hosted Neo4j:**
   - Migrate from AuraDB to self-hosted on ECS
   - Savings: ~$300-400/month
   - Trade-off: More operational overhead

9. **S3 Intelligent-Tiering:**
   - Automatically move infrequently accessed exports to cheaper storage
   - Savings: Minimal (~$5-10/month) but good practice

10. **Monitor and Alert:**
    - CloudWatch billing alerts at $5,000/month (75% of budget)
    - Detailed cost allocation tags (service, environment, team)
    - Monthly cost review meetings

---

#### Budget Approval Process

**Before Implementation Starts:**

1. **Executive Approval:** Present cost model to stakeholders, get budget approved
2. **Pilot Budget:** $10,000 for first 3 months (MVP development + testing)
3. **Production Budget:** $90,000/year ($7,500/month) with quarterly reviews
4. **Contingency:** 20% buffer for unexpected costs ($18,000/year)

**Cost Monitoring:**
- **Weekly:** Review AWS Cost Explorer, identify anomalies
- **Monthly:** Detailed cost breakdown by service, compare to budget
- **Quarterly:** Cost optimization review, adjust strategy

---

### 4. Agent Testing Patterns & Quality Assurance

**Problem Statement:**

LLM-powered agents produce non-deterministic outputs. Traditional unit tests (assert output == expected) don't work. Without proper testing patterns, quality issues will slip through, and regressions will be hard to catch.

---

#### Testing Philosophy for LLM Agents

**Core Challenge:** Same input → Different outputs (due to LLM non-determinism)

**Solution:** Test for **quality characteristics** and **constraints**, not exact output matching.

---

#### Agent Testing Layers

**Layer 1: Unit Tests (Agent Logic, Not LLM Output)**

Test deterministic components:
- **Input Validation:** Agent receives correct schema
- **State Updates:** Agent correctly updates LangGraph state
- **Error Handling:** Agent handles exceptions gracefully
- **Configuration:** Agent loads YAML rules correctly

**Example:**
```python
# tests/unit/agents/test_query_interpreter.py
def test_query_interpreter_updates_state():
    """Test that QueryInterpreter agent updates state with mode detection."""
    agent = QueryInterpreter()
    initial_state = {
        "query_text": "Soft drinks in France",
        "detected_mode": None
    }

    # Mock LLM response
    with patch_llm_response(mode="MARKET_OVERVIEW", confidence=0.95):
        new_state = agent.execute(initial_state)

    assert new_state["detected_mode"] == "MARKET_OVERVIEW"
    assert new_state["mode_confidence"] == 0.95
    assert "query_text" in new_state  # Preserves input
```

**Layer 2: Integration Tests (Agent + LLM, Quality Checks)**

Test agent behavior with real or mocked LLM:
- **Output Schema Validation:** Agent output matches Pydantic schema
- **YAML Compliance:** Output adheres to YAML business rules
- **Quality Thresholds:** Output meets minimum quality criteria

**Example:**
```python
# tests/integration/agents/test_narrative_synthesizer.py
@pytest.mark.integration
def test_narrative_synthesizer_output_quality():
    """Test that NarrativeSynthesizer produces valid report sections."""
    agent = NarrativeSynthesizer(llm_client=real_claude_client)

    state = {
        "query_text": "Soft drinks in France",
        "detected_mode": "MARKET_OVERVIEW",
        "retrieved_data": {...}  # Real KG data
    }

    new_state = agent.execute(state)

    # Validate schema
    assert "narrative_sections" in new_state
    assert len(new_state["narrative_sections"]) >= 3  # Min 3 sections

    # Validate content quality
    for section in new_state["narrative_sections"]:
        assert len(section["content"]) > 100  # Not empty
        assert section["section_type"] in ["overview", "trends", "insights"]
        assert "citations" in section  # Must include citations

    # Validate YAML compliance
    assert validate_yaml_compliance(new_state["narrative_sections"], mode="MARKET_OVERVIEW")
```

**Layer 3: Golden Dataset Tests (Regression Detection)**

Maintain a curated set of "golden" queries with known-good outputs:
- **Purpose:** Catch regressions when prompt or agent logic changes
- **Approach:** Compare new output to golden output using similarity metrics (not exact match)

**Example:**
```python
# tests/golden/test_golden_queries.py
@pytest.mark.golden
@pytest.mark.parametrize("golden_query", load_golden_queries())
def test_golden_query_similarity(golden_query):
    """Test that golden queries produce similar quality to baseline."""
    # Run query through full agent pipeline
    result = run_full_pipeline(golden_query["query_text"])

    # Compare to golden baseline
    similarity_score = calculate_similarity(
        result["intelligence_report"],
        golden_query["expected_baseline"]
    )

    # Assert similarity above threshold (e.g., 80%)
    assert similarity_score > 0.80, f"Output diverged from golden baseline: {similarity_score}"

    # Also check quality score
    assert result["quality_score"] >= 0.75  # Min threshold
```

**Layer 4: Property-Based Tests (Invariant Checks)**

Test invariant properties that should **always** hold:
- **Citation Count:** Every claim has at least one citation
- **Mode Detection:** Confidence threshold is always 0-1
- **Quality Score:** Always between 0-1, calculated correctly
- **Data Completeness:** Required sections are never missing

**Example:**
```python
# tests/property/test_citation_invariants.py
@given(st.text(min_size=10))  # Hypothesis library for property testing
def test_all_claims_have_citations(query_text):
    """Property: Every claim in narrative must have at least one citation."""
    result = run_narrative_synthesizer(query_text)

    for section in result["narrative_sections"]:
        # Parse claims from section
        claims = extract_claims(section["content"])

        for claim in claims:
            # Each claim must have citation reference
            assert has_citation_reference(claim, section["citations"]), \
                f"Claim without citation: {claim}"
```

**Layer 5: Human Evaluation (Quality Rubric)**

Automated tests can't fully assess quality - need human eval:
- **Sample 10% of queries** for manual review
- **Quality Rubric:** Rate on multiple dimensions (accuracy, relevance, clarity, citation quality)
- **A/B Testing:** Compare prompt variations, agent changes

**Process:**
1. Agent Validator role reviews 10% sample weekly
2. Rates each report on 5-point scale (1=poor, 5=excellent)
3. Flags issues for agent improvement
4. Tracks quality trend over time

---

#### Testing Infrastructure

**Test Data Management:**
- **Mock Passport Data:** Fixture data for unit/integration tests (avoid real API calls)
- **Golden Query Dataset:** 50-100 curated queries covering all modes, edge cases
- **Synthetic Queries:** Generate varied test queries (different categories, geographies, complexity)

**CI/CD Integration:**
- **Unit Tests:** Run on every commit (<2 minutes)
- **Integration Tests:** Run on every PR (<10 minutes, uses mocked LLM)
- **Golden Dataset Tests:** Run nightly (uses real Claude API, ~30 minutes)
- **Human Eval:** Weekly manual review (not automated)

**Quality Metrics Dashboard:**
- Track over time:
  - Average quality score (target: >0.80)
  - Citation accuracy rate (target: 100%)
  - Mode detection accuracy (target: >85%)
  - Test pass rate (target: >95%)
- Alert on regressions (quality drop >5%, test failures)

---

#### Prompt Versioning & Management

**Problem:** Prompts change frequently, need version control and testing

**Solution: Prompt Registry**

```python
# app/prompts/registry.py
PROMPTS = {
    "narrative_synthesizer_v3": {
        "version": "3.0.0",
        "created_at": "2026-01-15",
        "system_message": """You are an expert market intelligence analyst...""",
        "user_template": """Generate a {mode} report for: {query_text}...""",
        "tested": True,  # Passed golden dataset tests
        "quality_baseline": 0.83,  # Average quality score
        "changelog": "Improved citation formatting, added data completeness checks"
    }
}
```

**Workflow:**
1. Developer changes prompt → Creates new version (v3.1.0)
2. Runs golden dataset tests → Compares quality to baseline
3. If quality improves → Promote to production
4. If quality degrades → Investigate, revert, or iterate

---

### 5. YAML Business Rules Governance

**Problem Statement:**

YAML business rules are **critical to system behavior** (mode detection, data retrieval, quality scoring), but we have no governance process. Ad-hoc changes could break agents, introduce inconsistencies, or violate quality requirements.

---

#### YAML Governance Framework

**Principle:** Treat YAML business rules like production code (version controlled, reviewed, tested, documented).

---

#### YAML File Organization

**Location:** `app/yaml_rules/` (version controlled in git)

**Structure:**
```
app/yaml_rules/
├── modes/
│   ├── market_overview.yaml
│   ├── category_deep_dive.yaml
│   └── regulatory_impact.yaml
├── quality_rubrics/
│   ├── market_overview_rubric.yaml
│   ├── category_deep_dive_rubric.yaml
│   └── regulatory_impact_rubric.yaml
├── data_retrieval/
│   ├── market_overview_data.yaml
│   └── category_deep_dive_data.yaml
├── schemas/
│   ├── mode_schema.json (JSON Schema for mode YAML)
│   ├── quality_rubric_schema.json
│   └── data_retrieval_schema.json
└── README.md (YAML documentation, change process)
```

---

#### YAML Schema Validation

**Every YAML file has a JSON Schema for validation:**

**Example: Mode Schema**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["mode_name", "description", "data_requirements", "narrative_structure"],
  "properties": {
    "mode_name": {"type": "string", "enum": ["MARKET_OVERVIEW", "CATEGORY_DEEP_DIVE", "REGULATORY_IMPACT"]},
    "description": {"type": "string"},
    "detection_keywords": {"type": "array", "items": {"type": "string"}},
    "data_requirements": {
      "type": "object",
      "properties": {
        "required_metrics": {"type": "array"},
        "required_entities": {"type": "array"},
        "time_period": {"type": "string"}
      }
    },
    "narrative_structure": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["section_name", "content_requirements"],
        "properties": {
          "section_name": {"type": "string"},
          "content_requirements": {"type": "array"}
        }
      }
    }
  }
}
```

**Validation in Code:**
```python
# app/utils/yaml_parser.py
from jsonschema import validate, ValidationError

def load_mode_yaml(mode: str) -> dict:
    """Load and validate mode YAML against schema."""
    yaml_path = f"app/yaml_rules/modes/{mode.lower()}.yaml"
    schema_path = "app/yaml_rules/schemas/mode_schema.json"

    with open(yaml_path) as f:
        yaml_data = yaml.safe_load(f)

    with open(schema_path) as f:
        schema = json.load(f)

    try:
        validate(instance=yaml_data, schema=schema)
    except ValidationError as e:
        raise ValueError(f"Invalid YAML for mode {mode}: {e.message}")

    return yaml_data
```

---

#### YAML Change Management Process

**1. Proposal Phase:**
- **Who:** Product Manager, Analyst, or Developer
- **What:** Identify need for YAML change (new mode, quality criteria update, data requirement change)
- **How:** Create GitHub Issue with template:
  - Title: `[YAML Change] Update Market Overview quality rubric`
  - Description: Why this change is needed, expected impact
  - Proposed YAML diff

**2. Review Phase:**
- **Who:** Architect + Domain Expert (Euromonitor analyst)
- **What:** Review proposal for correctness, consistency, feasibility
- **Questions to Answer:**
  - Does this align with Passport taxonomy?
  - Will this break existing queries?
  - Is this testable/measurable?
  - Does it conflict with other modes?

**3. Implementation Phase:**
- **Who:** Developer
- **What:**
  1. Create feature branch: `yaml-changes/market-overview-quality-update`
  2. Update YAML file
  3. Validate against JSON Schema (automated test)
  4. Update related code if needed (agent prompts, parsing logic)
  5. Run regression tests (golden dataset)
  6. Update documentation (README, inline comments)

**4. Testing Phase:**
- **Automated Tests:**
  - JSON Schema validation (must pass)
  - Unit tests for YAML parsing (must pass)
  - Integration tests with new YAML (must pass)
  - Golden dataset tests (quality must not degrade >5%)
- **Manual Testing:**
  - Test with 5-10 real queries
  - Verify outputs match expectations
  - Check no unintended side effects

**5. Approval Phase:**
- **Who:** Architect (required) + Product Manager (if user-facing change)
- **What:** Review PR with YAML changes, test results
- **Approval Criteria:**
  - All tests pass
  - Quality metrics maintained or improved
  - Documentation updated
  - No breaking changes (or migration plan documented)

**6. Deployment Phase:**
- **Who:** DevOps / Developer
- **What:**
  1. Merge PR to main branch
  2. Deploy to staging environment
  3. Smoke test in staging (10-20 queries)
  4. Monitor quality metrics for 24 hours
  5. Deploy to production (canary deployment: 10% traffic first)
  6. Monitor production metrics for 48 hours
  7. Rollback procedure if issues detected

**7. Monitoring Phase:**
- **Track for 2 weeks:**
  - Quality score distribution (before/after change)
  - Mode detection accuracy (if mode YAML changed)
  - User feedback / complaints
  - Agent error rates
- **If metrics degrade:** Investigate, fix, or roll back

---

#### YAML Versioning Strategy

**Semantic Versioning for YAML:**
- **Major:** Breaking change (incompatible with existing agents)
  - Example: Change required field names, remove sections
  - Requires: Agent code updates, migration path
- **Minor:** Backward-compatible addition
  - Example: Add new optional field, new quality criterion
  - Requires: Test that old queries still work
- **Patch:** Non-functional change
  - Example: Fix typo, clarify documentation, reorder fields
  - Requires: Minimal testing

**Version Tracking:**
```yaml
# app/yaml_rules/modes/market_overview.yaml
version: "2.1.0"
last_updated: "2026-01-15"
changelog:
  - version: "2.1.0"
    date: "2026-01-15"
    changes: "Added 'sustainability trends' as optional section"
    author: "karthikmg"
  - version: "2.0.0"
    date: "2026-01-01"
    changes: "Major restructure: changed section format, added citation requirements"
    author: "architect"

mode_name: "MARKET_OVERVIEW"
description: "High-level market analysis with key trends and outlook"
...
```

---

#### YAML Documentation Standards

**Every YAML file must have:**
1. **Header Comment:** Purpose, version, last updated
2. **Inline Comments:** Explain non-obvious rules, constraints
3. **Examples:** Sample queries that trigger this mode, expected outputs
4. **Validation Rules:** What makes this YAML valid/invalid

**Example:**
```yaml
# Market Overview Mode Configuration
# Version: 2.1.0
# Last Updated: 2026-01-15
# Purpose: Define structure and requirements for Market Overview intelligence reports
# Used by: QueryInterpreter (mode detection), DataRetrieval (data fetching), NarrativeSynthesizer (report structure)

version: "2.1.0"
mode_name: "MARKET_OVERVIEW"

# Mode Detection: Keywords that suggest user wants a Market Overview
detection_keywords:
  - "market overview"
  - "industry trends"
  - "market size"
  - "category outlook"
  # Note: These are hints, not strict rules. LLM uses semantic understanding.

# Data Requirements: What data must be retrieved from KG
data_requirements:
  required_metrics:
    - "market_value_usd"  # Total market size in USD
    - "market_volume_units"  # Total volume in standard units
    - "cagr_forecast_5y"  # 5-year forecast CAGR
  required_entities:
    - "category"  # Primary category (e.g., "Soft Drinks")
    - "geography"  # Primary geography (e.g., "France")
  time_period: "last_5_years_plus_5_year_forecast"  # Historical + Forecast

# Narrative Structure: Required sections for this mode
narrative_structure:
  - section_name: "Market Overview"
    order: 1
    content_requirements:
      - "Current market size (value and volume)"
      - "Key market trends (2-3 bullets)"
      - "Outlook summary (1-2 sentences)"
    min_length_words: 150
    max_length_words: 300
    requires_citations: true  # Every factual claim must have citation

  - section_name: "Competitive Landscape"
    order: 2
    content_requirements:
      - "Top 3-5 companies by market share"
      - "Recent M&A or strategic moves"
    min_length_words: 100
    max_length_words: 200
    requires_citations: true

  # ... more sections ...

# Quality Rubric: How to score this mode
quality_rubric_ref: "quality_rubrics/market_overview_rubric.yaml"

# Example Queries:
examples:
  - "Soft drinks market in France"
  - "What is the size of the bottled water category in Brazil?"
  - "Give me an overview of the automotive industry in Germany"
```

---

#### YAML Regression Testing

**Golden YAML Test Suite:**
- **Purpose:** Ensure YAML changes don't break existing functionality
- **Approach:** Store snapshot of YAML files + expected agent behaviors
- **When Run:** On every PR that touches YAML files

**Example Test:**
```python
# tests/yaml/test_mode_yaml_regression.py
def test_market_overview_yaml_stability():
    """Ensure Market Overview YAML structure hasn't changed unexpectedly."""
    current_yaml = load_mode_yaml("MARKET_OVERVIEW")

    # Check required fields still exist
    assert "mode_name" in current_yaml
    assert "data_requirements" in current_yaml
    assert "narrative_structure" in current_yaml

    # Check narrative structure hasn't removed required sections
    section_names = [s["section_name"] for s in current_yaml["narrative_structure"]]
    assert "Market Overview" in section_names
    assert "Competitive Landscape" in section_names

    # Check data requirements are valid
    assert "required_metrics" in current_yaml["data_requirements"]
    assert len(current_yaml["data_requirements"]["required_metrics"]) > 0
```

---

#### YAML Change Impact Analysis

**Before merging YAML changes, analyze impact:**

**Impact Categories:**
1. **Agent Prompts:** Which prompts reference this YAML? Need updates?
2. **Test Cases:** Which tests rely on this YAML structure? Need updates?
3. **User Queries:** How many historical queries used this mode? Risk of behavior change?
4. **Documentation:** What user-facing docs need updates?

**Tool: YAML Dependency Analyzer (Custom Script)**
```bash
# Find all references to a YAML file in codebase
python scripts/analyze_yaml_impact.py app/yaml_rules/modes/market_overview.yaml

# Output:
# - 12 agent files reference this YAML
# - 23 test files use this YAML
# - 847 historical queries matched this mode (last 30 days)
# - 3 documentation pages mention this mode
```

---

## Summary: Missing Components Now Addressed

**✅ KG Construction Project Plan**
- 8-week phased approach (pilot → structured → unstructured → citations)
- Ownership recommendation (separate team/contractor)
- Maintenance strategy (incremental updates, full refresh, monitoring)

**✅ Disaster Recovery Procedures**
- Backup strategy for all data stores (RDS, Neo4j, Redis)
- Recovery procedures for 4 disaster scenarios
- RTO/RPO targets defined
- Quarterly DR testing plan

**✅ Cost Management Strategy**
- Detailed cost estimation ($2,600/month MVP → $6,340/month production)
- Cost breakdown by service
- 10 optimization strategies
- Budget approval process and monitoring

**✅ Agent Testing Patterns**
- 5-layer testing approach (unit, integration, golden dataset, property-based, human eval)
- Quality metrics dashboard
- Prompt versioning and management
- CI/CD integration

**✅ YAML Governance Process**
- 7-phase change management (proposal → deployment → monitoring)
- Schema validation for all YAML files
- Semantic versioning strategy
- Documentation standards
- Regression testing
- Change impact analysis

These components are now documented and ready for implementation planning.
