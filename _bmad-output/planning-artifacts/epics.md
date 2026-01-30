---
stepsCompleted: [1, 2, 3]
inputDocuments:
  - '_bmad-output/planning-artifacts/prd.md'
  - '_bmad-output/planning-artifacts/architecture.md'
  - '_bmad-output/planning-artifacts/ux-design-specification.md'
---

# euromonitor-multi-agent-architecture - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for euromonitor-multi-agent-architecture (Passport AI-Powered Intelligence Assistant), decomposing the requirements from the PRD, UX Design Specification, and Architecture decisions into implementable stories.

## Requirements Inventory

### Functional Requirements

**Query & Intelligence Generation (9 requirements)**
- FR1: [MVP] Users can submit natural language queries about market intelligence topics
- FR2: [MVP] The system can generate Market Overview Reports for broad industry-level queries
- FR3: [GROWTH] The system can generate Category Deep Dive Reports for specific category queries
- FR4: [GROWTH] The system can generate Regulatory Impact Briefs for policy/regulation queries
- FR5: [MVP] The system can retrieve data from the knowledge graph based on query parameters
- FR6: [MVP] The system can synthesize narrative intelligence from retrieved Passport data
- FR7: [MVP] The system can generate visualizations (charts, infographics) appropriate to the report mode
- FR8: [GROWTH] The system can support multi-turn conversations with memory of previous queries
- FR9: [GROWTH] The system can provide follow-up question suggestions based on initial query results

**Mode Detection & Routing (5 requirements)**
- FR10: [GROWTH] The system can automatically detect the appropriate operational mode from query structure
- FR11: [GROWTH] The system can calculate confidence scores for mode detection decisions
- FR12: [GROWTH] The system can prompt users for clarification when mode detection confidence is below threshold (<0.85)
- FR13: [GROWTH] The system can route queries to mode-specific agent workflows without mid-conversation mode switching
- FR14: [GROWTH] Users can explicitly specify the desired mode if automatic detection is uncertain

**Quality Assurance & Validation (8 requirements)**
- FR15: [MVP] The system can score generated intelligence against multi-dimensional quality rubric
- FR16: [MVP] The system can iteratively refine outputs when quality score is below threshold (<75%)
- FR17: [MVP] The system can validate data completeness before generating intelligence
- FR18: [MVP] The system can flag coverage gaps when Passport data is incomplete for the query
- FR19: [MVP] Validators can review AI-generated intelligence with visibility into quality scores
- FR20: [MVP] Validators can approve or reject AI-generated outputs with feedback
- FR21: [GROWTH] Validators can provide structured feedback that improves future output quality
- FR22: [MVP] The system can enforce YAML business rules for each operational mode

**Citations & Transparency (6 requirements)**
- FR23: [MVP] The system can attribute every claim in generated intelligence to specific Passport source data
- FR24: [MVP] Users can view citations with report title and date for each data point
- FR25: [MVP] Users can navigate from citations directly to source Passport datasets
- FR26: [MVP] The system can validate citation accuracy before presenting reports (100% accuracy requirement)
- FR27: [MVP] The system can display methodology and data limitations in generated reports
- FR28: [MVP] The system can provide coverage cues indicating confidence levels and data gaps

**User Access & Authentication (5 requirements)**
- FR29: [MVP] Users can authenticate via Single Sign-On (SSO) using enterprise identity providers
- FR30: [MVP] The system can support SAML 2.0, OAuth 2.0, and OpenID Connect authentication protocols
- FR31: [MVP] The system can integrate with Passport's existing SSO infrastructure
- FR32: [MVP] The system can manage user sessions aligned with enterprise security policies
- FR33: [MVP] The system can support multi-factor authentication (MFA) when required

**Permissions & Data Access Control (7 requirements)**
- FR34: [MVP] The system can enforce subscription-based data access controls based on Passport tier
- FR35: [MVP] The system can restrict queries by geography based on user's subscription permissions
- FR36: [MVP] The system can restrict queries by category based on user's subscription permissions
- FR37: [MVP] The system can validate user permissions before executing data retrieval operations
- FR38: [MVP] The system can handle permission denials with clear error messages to users
- FR39: [MVP] The system can support role-based access control (End User, Validator, Admin, Operations)
- FR40: [GROWTH] Admins can override individual user permissions with audit trail documentation

**Administrative Management (8 requirements)**
- FR41: [MVP] Admins can provision and deprovision user access to the AI assistant
- FR42: [MVP] Admins can configure SSO integration settings
- FR43: [MVP] Admins can map Passport subscription tiers to AI assistant data permissions
- FR44: [MVP] Admins can manage beta testing groups with phased rollout controls
- FR45: [GROWTH] Admins can bulk import users for enterprise customer onboarding
- FR46: [GROWTH] Admins can view usage analytics and reporting dashboards
- FR47: [MVP] Admins can query audit trail logs for compliance reporting
- FR48: [MVP] Admins can configure data residency settings per customer requirements

**Operations & Monitoring (10 requirements)**
- FR49: [MVP] Operations staff can view query audit trails with complete orchestration flow details
- FR50: [GROWTH] Operations staff can filter and search audit logs by user, query, mode, or time range
- FR51: [MVP] Operations staff can access agent orchestration flow visibility for debugging failed queries
- FR52: [GROWTH] Operations staff can view quality score distribution metrics across queries
- FR53: [MVP] Operations staff can receive alerts when citation accuracy issues are detected
- FR54: [MVP] Operations staff can monitor knowledge graph health metrics (coverage, staleness)
- FR55: [MVP] Operations staff can view system performance metrics (response times, error rates, concurrent load)
- FR56: [MVP] Operations staff can investigate incidents with access to complete system state
- FR57: [MVP] Operations staff can maintain the knowledge graph with tools for identifying stale metadata
- FR58: [MVP] Operations staff can receive automated alerts for system health issues

**Export & Integration (6 requirements)**
- FR59: [MVP] Users can export generated intelligence reports to PDF format
- FR60: [GROWTH] Users can export generated intelligence reports to PowerPoint (PPTX) format
- FR61: [MVP] The system can sync with Passport data refresh cycles for knowledge graph updates
- FR62: [MVP] The system can handle Passport API rate limits gracefully without user-visible failures
- FR63: [VISION] Power users can access API endpoints to integrate with their own tools (Vision phase)
- FR64: [VISION] The system can provide webhook notifications for query completion (Future consideration)

**Knowledge Graph & Data Management (7 requirements)**
- FR65: [MVP] The system can construct knowledge graph from Passport structured and unstructured data
- FR66: [MVP] The system can maintain >95% coverage of Passport corpus in the knowledge graph
- FR67: [MVP] The system can preserve Passport taxonomy and data model in knowledge graph structure
- FR68: [MVP] The system can perform semantic search across unstructured Passport content
- FR69: [MVP] The system can enable cross-content retrieval finding connections across disparate datasets
- FR70: [MVP] The system can update knowledge graph when Passport data changes or is deprecated
- FR71: [MVP] The system can validate knowledge graph data quality during construction and updates

### Non-Functional Requirements

**Performance (7 requirements)**
- NFR1: The system must generate typical intelligence reports in less than 180 seconds (3 minutes) average response time
- NFR2: The system must maintain 95th percentile response time of less than 240 seconds (4 minutes)
- NFR3: The system must handle 100+ concurrent queries without performance degradation
- NFR4: The system must maintain error rate below 1% of all queries
- NFR5: The system must timeout gracefully after 10 minutes with clear user messaging
- NFR6: Mode detection must complete in less than 5 seconds
- NFR7: Citation validation must complete without adding more than 10 seconds to total response time

**Security (8 requirements)**
- NFR8: The system must encrypt all data at rest
- NFR9: The system must encrypt all data in transit using TLS 1.3 or higher
- NFR10: The system must prevent user data leakage between sessions or users
- NFR11: The system must securely handle Passport credentials and API tokens
- NFR12: The system must protect against injection attacks, XSS, and CSRF vulnerabilities
- NFR13: The system must implement rate limiting to prevent abuse
- NFR14: The system must undergo regular security audits and penetration testing
- NFR15: The system must have documented incident response procedures

**Reliability & Availability (5 requirements)**
- NFR16: The system must maintain 99.5% uptime SLA
- NFR17: The system must implement automated health monitoring and alerting
- NFR18: The system must gracefully degrade when components fail (e.g., visualization failure doesn't block report delivery)
- NFR19: The system must have disaster recovery and backup strategy
- NFR20: The system must support rollback capabilities for production deployments

**Scalability (7 requirements)**
- NFR21: The system must support 500+ daily queries at launch
- NFR22: The system must scale to support 2000+ daily queries within 6 months
- NFR23: The system must scale horizontally to meet growing demand
- NFR24: The system must implement auto-scaling based on demand patterns
- NFR25: The system must support 20-50 concurrent users in MVP phase
- NFR26: The system must support 100+ concurrent users in growth phase
- NFR27: The system must support 500+ concurrent users in production phase

**Data Quality & Accuracy (6 requirements)**
- NFR28: The system must achieve 100% citation accuracy (every citation links to valid Passport source)
- NFR29: The system must maintain >95% Passport corpus coverage in knowledge graph
- NFR30: The system must achieve >85% mode detection accuracy
- NFR31: The system must enforce minimum 75% quality score threshold before presenting reports
- NFR32: The system must validate data completeness and flag coverage gaps
- NFR33: The system must achieve >95% YAML business rule compliance

**Integration & Interoperability (7 requirements)**
- NFR34: The system must support SAML 2.0, OAuth 2.0, and OpenID Connect for SSO
- NFR35: The system must integrate with Passport's existing SSO infrastructure
- NFR36: The system must handle Passport API rate limits gracefully
- NFR37: The system must sync with Passport data refresh cycles automatically
- NFR38: The system must support PDF export format
- NFR39: The system must support PowerPoint (PPTX) export format
- NFR40: The system must provide API access for power users (Vision phase)

**Compliance & Auditability (6 requirements)**
- NFR41: The system must log all queries, mode detection, data retrieval, and report generation
- NFR42: The system must retain audit logs for configurable period (default: 12 months)
- NFR43: The system must provide audit trail query capabilities for admins and operations
- NFR44: The system must respect data residency requirements per customer configuration
- NFR45: The system must comply with GDPR for data subject access requests
- NFR46: The system must not store PII unnecessarily

**Maintainability & Operability (7 requirements)**
- NFR47: The system must provide operations dashboard with complete system observability
- NFR48: The system must enable debugging of failed queries via orchestration flow visibility
- NFR49: The system must alert operations staff automatically for system health issues
- NFR50: The system must alert operations staff when citation accuracy issues detected
- NFR51: The system must provide knowledge graph maintenance tools
- NFR52: The system must support containerized deployment (Kubernetes)
- NFR53: The system must support cloud deployment (AWS/Azure/GCP)

**Usability (6 requirements)**
- NFR54: The system must provide intuitive natural language query interface
- NFR55: The system must integrate seamlessly within existing Passport UI
- NFR56: The system must maintain consistent branding with Passport ecosystem
- NFR57: The system must provide clear error messages for permission denials
- NFR58: The system must provide graceful failure messaging for timeouts
- NFR59: The system must enable direct navigation from citations to Passport sources

### Additional Requirements

**Architecture & Technical Decisions**
- ARCH1: Frontend must use Vite + React 19 + TypeScript 5 + Tailwind CSS 4 + shadcn/ui component library
- ARCH2: Backend must use custom FastAPI (Python 3.10+) with LangGraph for multi-agent orchestration
- ARCH3: Knowledge Graph must use Neo4j 5.x with Vector Search Plugin
- ARCH4: LLM provider must be Claude 3.5 Sonnet (Anthropic API)
- ARCH5: Cloud infrastructure must use AWS (RDS PostgreSQL, ElastiCache Redis, ECS Fargate, SQS, SNS, CloudWatch)
- ARCH6: MVP must focus on Mode 1 (Market Overview) only, deferring Modes 2-3 to post-MVP
- ARCH7: MVP must use JWT token-based authentication (email/password), deferring SSO/SAML to Phase 5+
- ARCH8: MVP must deploy Single-AZ infrastructure (RDS, ElastiCache, ECS), deferring Multi-AZ HA to Phase 5+
- ARCH9: Knowledge Graph must implement Phase 1-2 data model only (structured Passport data), deferring Phase 3-4 (unstructured + semantic search) to post-MVP
- ARCH10: Monitoring must use AWS CloudWatch basic logs/metrics for MVP, deferring X-Ray distributed tracing to Phase 5+

**UX Design & Frontend Requirements**
- UX1: Must implement ChatGPT-style conversational interface with single search bar as primary interaction
- UX2: Must implement Perplexity-style inline citations with numbered superscripts [1], hover previews, and click to expand
- UX3: Must implement progressive intelligence disclosure (sections stream as generated, not all-at-once)
- UX4: Must display contextual progress indicators with specific messages ("Analyzing market data...", "Generating insights...")
- UX5: Must achieve <100ms query acknowledgment (optimistic UI)
- UX6: Must implement responsive design for desktop-first (1280px+) with tablet support (768px-1279px)
- UX7: Must implement WCAG AA accessibility compliance (keyboard navigation, focus indicators, screen reader support)
- UX8: Must implement command palette (Cmd/Ctrl+K) for power user quick actions
- UX9: Must use Professional Blue (#2563EB) as primary color, Accent Orange (#F97316) for citations
- UX10: Must use Inter font family for typography with clear hierarchy (H1: 36px/Bold, H2: 30px/Semibold, Body: 16px/Regular)
- UX11: Must implement 8px spacing base unit with consistent rhythm (48px between sections, 24px between components)
- UX12: Must support multi-turn conversations with context retention visible in conversation thread
- UX13: Must implement sidebar navigation for history and saved reports
- UX14: Must implement one-click export to PDF with <10 second generation time
- UX15: Must provide example queries on empty state to guide first-time users

**MVP Scope & Phase Requirements**
- MVP1: MVP timeline is 6 weeks (Phases 1-4), full production is 10 weeks (Phases 1-6+)
- MVP2: MVP monthly cost target is $800-1,100, full production cost is $2,600-6,340
- MVP3: MVP uptime is best-effort (~95%), production SLA is 99.5% with Multi-AZ
- MVP4: MVP must demonstrate Mode 1 query → intelligence report with citations in <5 minutes
- MVP5: MVP must achieve >75% quality score threshold and 100% citation accuracy
- MVP6: MVP must maintain <1% error rate with graceful error handling
- MVP7: MVP must defer admin UI, SSO, Modes 2-3, PDF/PPTX export, X-Ray tracing, disaster recovery procedures to Phase 5+ (post-MVP)

### FR Coverage Map

**Functional Requirements:**
- FR1: Epic 2 - Natural language query submission
- FR2: Epic 4 - Market Overview Report generation (Mode 1)
- FR3: DEFERRED - Category Deep Dive Reports (Growth phase)
- FR4: DEFERRED - Regulatory Impact Briefs (Growth phase)
- FR5: Epic 4 - Data retrieval from knowledge graph
- FR6: Epic 4 - Narrative synthesis from Passport data
- FR7: Epic 4 - Visualization generation
- FR8: DEFERRED - Multi-turn conversations (Growth phase)
- FR9: DEFERRED - Follow-up question suggestions (Growth phase)
- FR10-FR14: DEFERRED - Mode detection & routing (Growth phase, Mode 1 only for MVP)
- FR15: Epic 4 - Quality scoring with multi-dimensional rubric
- FR16: Epic 4 - Iterative refinement when quality <75%
- FR17: Epic 4 - Data completeness validation
- FR18: Epic 4 - Coverage gap flagging
- FR19: Epic 4 - Validator review with quality score visibility
- FR20: Epic 4 - Validator approval/rejection workflow
- FR21: DEFERRED - Structured feedback for improvement (Growth phase)
- FR22: Epic 4 - YAML business rules enforcement
- FR23: Epic 5 - Claim-level attribution to Passport sources
- FR24: Epic 6 - Citation viewing with metadata
- FR25: Epic 6 - Citation navigation to source datasets
- FR26: Epic 5 - Citation accuracy validation (100%)
- FR27: Epic 6 - Methodology and limitation display
- FR28: Epic 6 - Coverage cue indicators
- FR29: Epic 1 - JWT authentication (SSO deferred to Phase 5+)
- FR30-FR33: DEFERRED - SSO/SAML/MFA (Phase 5+)
- FR34: Epic 1 - Subscription-based data access control
- FR35: Epic 1 - Geography-based query restrictions
- FR36: Epic 1 - Category-based query restrictions
- FR37: Epic 1 - Permission validation before data retrieval
- FR38: Epic 1 - Graceful permission denial handling
- FR39: Epic 1 - RBAC implementation (User/Admin roles for MVP)
- FR40: DEFERRED - Admin permission overrides (Growth phase)
- FR41: Epic 8 - User provisioning/deprovisioning
- FR42: Epic 8 - SSO configuration placeholder
- FR43: Epic 8 - Subscription tier mapping
- FR44: Epic 8 - Beta group management
- FR45: DEFERRED - Bulk user import (Growth phase)
- FR46: DEFERRED - Usage analytics dashboards (Growth phase)
- FR47: Epic 8 - Audit trail querying
- FR48: Epic 8 - Data residency configuration
- FR49: Epic 9 - Query audit trail viewing
- FR50: DEFERRED - Advanced audit log filtering (Growth phase)
- FR51: Epic 9 - Agent orchestration flow debugging
- FR52: DEFERRED - Quality score distribution metrics (Growth phase)
- FR53: Epic 9 - Citation accuracy alerting
- FR54: Epic 9 - KG health monitoring
- FR55: Epic 9 - System performance metrics
- FR56: Epic 9 - Incident investigation access
- FR57: Epic 9 - KG maintenance tools
- FR58: Epic 9 - Automated health alerting
- FR59: Epic 7 - PDF export
- FR60: DEFERRED - PPTX export (Growth phase)
- FR61: Epic 3 - Passport data refresh sync
- FR62: Epic 3 - Passport API rate limit handling
- FR63-FR64: DEFERRED - Power user API & webhooks (Vision phase)
- FR65: Epic 3 - KG construction from Passport data
- FR66: Epic 3 - >95% corpus coverage
- FR67: Epic 3 - Passport taxonomy preservation
- FR68: Epic 3 - Semantic search (Phase 1-2 structured data for MVP)
- FR69: Epic 3 - Cross-content retrieval
- FR70: Epic 3 - KG update on data changes
- FR71: Epic 3 - KG data quality validation

**Non-Functional Requirements:**
- NFR1-NFR7: Epic 10 - Performance optimization (<3 min response, 100+ concurrent)
- NFR8-NFR15: Epic 10 - Security implementation (encryption, rate limiting, audits)
- NFR16-NFR20: Epic 10 - Reliability & availability (health monitoring, graceful degradation)
- NFR21-NFR27: Epic 10 - Scalability infrastructure (horizontal scaling, auto-scaling)
- NFR28: Epic 5 - 100% citation accuracy
- NFR29: Epic 3 - >95% KG corpus coverage
- NFR30: DEFERRED - Mode detection accuracy (Growth phase)
- NFR31: Epic 4 - 75% quality score threshold
- NFR32: Epic 4 - Data completeness validation
- NFR33: Epic 4 - >95% YAML compliance
- NFR34-NFR40: Epic 10 - Integration & interoperability (SSO placeholder, Passport API, exports)
- NFR41-NFR46: Epic 9 - Compliance & auditability (logging, retention, GDPR)
- NFR47-NFR53: Epic 9 - Maintainability & operability (dashboards, alerting, deployment)
- NFR54-NFR59: Epic 6 - Usability (query interface, error messages, navigation)

**Architecture Requirements:**
- ARCH1: Epic 6 - Frontend stack (Vite + React 19 + TypeScript + Tailwind + shadcn/ui)
- ARCH2: Epic 4 - Backend stack (FastAPI + LangGraph)
- ARCH3: Epic 3 - Neo4j with Vector Search
- ARCH4: Epic 4 - Claude 3.5 Sonnet LLM
- ARCH5: Epic 10 - AWS infrastructure (RDS, ElastiCache, ECS, SQS, SNS, CloudWatch)
- ARCH6: Epic 4 - Mode 1 only for MVP
- ARCH7: Epic 1 - JWT authentication for MVP
- ARCH8: Epic 10 - Single-AZ deployment for MVP
- ARCH9: Epic 3 - KG Phase 1-2 data model
- ARCH10: Epic 9 - CloudWatch basic monitoring

**UX Requirements:**
- UX1: Epic 2 - ChatGPT-style interface
- UX2: Epic 6 - Perplexity-style citations
- UX3: Epic 6 - Progressive intelligence disclosure
- UX4: Epic 2 - Contextual progress indicators
- UX5: Epic 2 - <100ms optimistic UI
- UX6: Epic 6 - Responsive design (desktop-first)
- UX7: Epic 6 - WCAG AA accessibility
- UX8: Epic 6 - Command palette (Cmd/Ctrl+K)
- UX9-UX11: Epic 6 - Design system (colors, typography, spacing)
- UX12: Epic 6 - Multi-turn conversation display
- UX13: Epic 6 - Sidebar navigation
- UX14: Epic 7 - One-click PDF export
- UX15: Epic 2 - Example queries on empty state

**MVP Requirements:**
- MVP1-MVP7: Cross-cutting across all epics - define scope, timeline, cost, and deferment strategy

## Epic List

### Epic 1: Secure User Authentication & Access Control
**User Outcome:** Users can securely log in with email/password and access the system based on their Passport subscription tier permissions

**Goal:** Establish complete authentication and authorization infrastructure enabling users to register, log in, and have their subscription-based data access permissions enforced. This epic delivers JWT token-based authentication with role-based access control (User/Admin roles), geography/category-based query restrictions, and graceful permission denial handling.

**FRs Covered:** FR29 (JWT authentication), FR34-39 (subscription-based permissions, RBAC, permission validation, error handling)

**Architecture Covered:** ARCH7 (JWT for MVP, SSO deferred)

**Dependencies:** None - fully standalone

**Enables:** All future epics require authenticated users with proper data access permissions

---

### Epic 2: Natural Language Query Interface
**User Outcome:** Users can type market intelligence questions in natural language and receive immediate feedback that their query is being processed

**Goal:** Implement complete query input experience with ChatGPT-style search bar, example queries for guidance, optimistic UI acknowledgment (<100ms), and contextual progress indicators. This epic delivers the frontend query submission workflow with visual feedback, ensuring users feel the system is responsive even while backend processing takes minutes.

**FRs Covered:** FR1 (natural language query submission)

**UX Covered:** UX1 (ChatGPT interface), UX4 (progress indicators), UX5 (optimistic UI), UX15 (example queries)

**Dependencies:** Epic 1 (requires authenticated users)

**Enables:** Epic 3-4 (queries are collected and routed for processing)

---

### Epic 3: Knowledge Graph Foundation
**User Outcome:** System has structured access to Passport market data enabling intelligent query responses

**Goal:** Build complete data infrastructure with Neo4j deployment, Passport API integration, Phase 1-2 data model implementation (structured market data: datasets, industries, geographies, categories), and >95% corpus coverage. This epic delivers the knowledge graph with data ingestion pipeline, quality validation, taxonomy preservation, and Passport data refresh sync.

**FRs Covered:** FR65-67, FR71 (KG construction, corpus coverage, taxonomy preservation, data validation), FR61-62 (Passport sync, API rate limit handling)

**Architecture Covered:** ARCH3 (Neo4j with Vector Search), ARCH9 (Phase 1-2 data model)

**NFRs Covered:** NFR29 (>95% corpus coverage)

**Dependencies:** None - can be built independently

**Enables:** Epic 4 (data retrieval agents query this KG)

---

### Epic 4: Multi-Agent Intelligence Generation Pipeline (Mode 1)
**User Outcome:** Users receive comprehensive Market Overview reports with executive summary, competitive landscape, regulatory changes, and 5-year forecasts

**Goal:** Implement complete 8-agent LangGraph orchestration pipeline producing Mode 1 (Market Overview) intelligence reports. Agents include Query Interpreter, Data Retrieval, Narrative Synthesizer, Visualization Generator, Quality Scorer, Data Quality Validator, Report Assembler, and Citation Specialist integration. This epic delivers end-to-end intelligence generation with quality gates (>75% threshold), iterative refinement, YAML business rule enforcement, and data completeness validation.

**FRs Covered:** FR2, FR5-7, FR15-18, FR22 (Mode 1 generation, data retrieval, narrative synthesis, visualizations, quality scoring, validation, YAML enforcement)

**Architecture Covered:** ARCH2 (FastAPI + LangGraph), ARCH4 (Claude 3.5 Sonnet), ARCH6 (Mode 1 only)

**NFRs Covered:** NFR31 (75% quality threshold), NFR32-33 (data validation, YAML compliance)

**Dependencies:** Epic 1 (authenticated users), Epic 3 (knowledge graph data)

**Enables:** Epic 5-6 (intelligence is generated and ready for display/citations)

---

### Epic 5: Citation & Transparency System
**User Outcome:** Users can verify every claim in intelligence reports through inline citations linking directly to Passport source data

**Goal:** Build complete citation infrastructure with Citation Specialist agent producing claim-level attributions, citation accuracy validation enforcing 100% requirement, source metadata tracking, and broken link monitoring. This epic delivers the transparency layer enabling users to verify every assertion in generated intelligence.

**FRs Covered:** FR23, FR26 (claim-level attribution, 100% accuracy validation)

**NFRs Covered:** NFR28 (100% citation accuracy)

**Dependencies:** Epic 4 (intelligence reports need citations)

**Enables:** Epic 6 (citations are displayed and explorable)

---

### Epic 6: Intelligence Report Display & Exploration
**User Outcome:** Users can read formatted intelligence reports, explore citations through hover previews, and interact with visualizations

**Goal:** Implement complete React frontend with Vite + TypeScript + Tailwind + shadcn/ui displaying intelligence reports. Features include Perplexity-style inline citations with hover previews, progressive intelligence disclosure (sections stream as generated), responsive design, WCAG AA accessibility, command palette, multi-turn conversation display, and sidebar navigation for history.

**FRs Covered:** FR24-25, FR27-28 (citation viewing, navigation, methodology display, coverage cues)

**Architecture Covered:** ARCH1 (Vite + React stack)

**UX Covered:** UX2-3, UX6-13 (citations, progressive loading, responsive design, accessibility, design system, navigation)

**NFRs Covered:** NFR54-59 (usability requirements)

**Dependencies:** Epic 4 (intelligence to display), Epic 5 (citations to show)

**Enables:** Epic 7 (users can export what they see)

---

### Epic 7: Report Export & Sharing
**User Outcome:** Users can export intelligence reports to PDF format for sharing with colleagues and stakeholders

**Goal:** Build PDF generation service with formatted output preserving citations, visualizations, and professional layout. One-click export completing in <10 seconds.

**FRs Covered:** FR59 (PDF export)

**UX Covered:** UX14 (one-click export)

**NFRs Covered:** NFR38 (PDF export format)

**Dependencies:** Epic 6 (reports to export)

**Enables:** Sharing and collaboration workflows

---

### Epic 8: Administrative Management Dashboard
**User Outcome:** Administrators can manage user access, configure permissions, and control system settings

**Goal:** Build admin interface for user provisioning/deprovisioning, subscription tier mapping to data permissions, beta group management, audit trail access, and data residency configuration. This epic delivers operational admin capabilities for user management and governance.

**FRs Covered:** FR41-44, FR47-48 (user provisioning, subscription mapping, beta management, audit trail, data residency)

**Dependencies:** Epic 1 (admin role requires auth system)

**Enables:** Scalable user onboarding and management

---

### Epic 9: Operations Monitoring & Observability
**User Outcome:** Operations staff can monitor system health, debug failures, maintain the knowledge graph, and respond to incidents

**Goal:** Implement operations dashboard with AWS CloudWatch integration, query audit trails, agent orchestration flow debugging, KG health monitoring, performance metrics tracking, citation accuracy alerting, KG maintenance tools, and automated health alerts. This epic delivers complete operational visibility and incident response capabilities.

**FRs Covered:** FR49, FR51, FR53-58 (audit trails, orchestration debugging, alerting, KG monitoring, performance metrics, maintenance tools)

**Architecture Covered:** ARCH10 (CloudWatch basic monitoring)

**NFRs Covered:** NFR41-53 (compliance, auditability, maintainability, operability)

**Dependencies:** Epic 3-4 (system to monitor), Epic 5 (citations to validate)

**Enables:** Production operations and reliability

---

### Epic 10: System Scalability & Performance Optimization
**User Outcome:** System reliably handles 100+ concurrent users with <3 minute average response times

**Goal:** Optimize system performance and enable horizontal scaling through caching strategies, async processing optimization, load balancing configuration, auto-scaling policies, query optimization, and security hardening (rate limiting, enhanced encryption). This epic transforms the working MVP into a production-grade system capable of handling concurrent load while maintaining <3 minute response times. NOTE: Foundational infrastructure (RDS, Redis, ECS) is deployed in Epics 1, 3-4; this epic focuses on optimization and scaling enhancements.

**NFRs Covered:** NFR1-27 (performance optimization, security hardening, reliability, horizontal scalability)

**Architecture Covered:** ARCH5 (AWS scaling infrastructure), ARCH8 (Single-AZ to Multi-AZ migration option)

**Dependencies:** Epic 1 (auth system to optimize), Epic 3 (KG to cache/optimize), Epic 4 (agents to scale), Epic 6 (UI to enhance performance)

**Enables:** Production deployment at scale with 100+ concurrent users

---

## Epic 1: Secure User Authentication & Access Control

**User Outcome:** Users can securely log in with email/password and access the system based on their Passport subscription tier permissions

**Goal:** Establish complete authentication and authorization infrastructure enabling users to register, log in, and have their subscription-based data access permissions enforced.

### Story 1.1: User Registration with Email/Password

As a new user,
I want to register an account with my email and password,
So that I can access the Passport AI Intelligence Assistant.

**Acceptance Criteria:**

**Given** I am on the registration page
**When** I submit a valid email address and password (min 8 characters)
**Then** a new user account is created in the PostgreSQL database
**And** my password is hashed using bcrypt before storage
**And** I receive a success message confirming registration
**And** I am redirected to the login page

**Given** I attempt to register with an already-used email
**When** I submit the registration form
**Then** I receive an error message "Email already registered"
**And** no duplicate account is created

**Given** I submit an invalid email format or weak password (<8 chars)
**When** I submit the registration form
**Then** I receive specific validation error messages
**And** the form highlights the invalid fields

**Technical Requirements:**

*Database Infrastructure Prerequisites (must complete before story implementation):*
- Provision AWS RDS PostgreSQL instance (Single-AZ for MVP: db.t3.micro, 20GB storage)
- Configure database security groups (accessible only from FastAPI backend)
- Store database credentials in AWS Secrets Manager (DATABASE_URL with connection string)
- Set up automated daily backups with 7-day retention
- Install asyncpg Python driver for async PostgreSQL access
- Create database connection pool in FastAPI startup (min 5, max 20 connections)

*Story Implementation:*
- Create `users` table with fields: id, email, password_hash, role, subscription_tier, created_at, updated_at
- Implement bcrypt password hashing (cost factor 12)
- Email validation using standard regex
- Password strength validation (min 8 characters)

---

### Story 1.2: User Login with JWT Token Generation

As a registered user,
I want to log in with my email and password,
So that I can access my personalized intelligence assistant session.

**Acceptance Criteria:**

**Given** I am a registered user with valid credentials
**When** I submit my email and password on the login page
**Then** the system validates my credentials against the database
**And** a JWT access token is generated with 24-hour expiry
**And** a JWT refresh token is generated with 7-day expiry
**And** both tokens are returned to the client
**And** I am redirected to the main query interface

**Given** I submit incorrect email or password
**When** I attempt to log in
**Then** I receive a generic error "Invalid email or password"
**And** no token is generated
**And** the attempt is logged for security monitoring

**Given** my JWT token is valid and not expired
**When** I make authenticated API requests
**Then** the system validates my token on each request
**And** my user context (id, role, subscription_tier) is extracted from the token
**And** the request proceeds with my permissions

**Given** my JWT token has expired
**When** I make an authenticated API request
**Then** I receive a 401 Unauthorized error
**And** the client automatically attempts token refresh using the refresh token

**Technical Requirements:**
- Implement JWT token generation with python-jose library
- Access token payload: {user_id, email, role, subscription_tier, exp: 24h}
- Refresh token payload: {user_id, exp: 7d}
- Token validation middleware for FastAPI routes
- Secure token storage on client (httpOnly cookies or localStorage)

---

### Story 1.3: User Role Assignment (User/Admin RBAC)

As an administrator,
I want to assign roles to users (User or Admin),
So that I can control who has administrative privileges.

**Acceptance Criteria:**

**Given** I am logged in as an Admin
**When** I view a user's profile in the admin dashboard
**Then** I can see their current role (User or Admin)
**And** I can change their role using a dropdown selector
**And** the role change is saved to the database immediately
**And** the user's next login reflects the updated role

**Given** a user has the "User" role
**When** they attempt to access admin-only endpoints
**Then** they receive a 403 Forbidden error
**And** the error message states "Admin privileges required"

**Given** a user has the "Admin" role
**When** they access admin-only endpoints
**Then** the request is authorized and proceeds
**And** admin actions are logged in the audit trail

**Given** a new user registers
**When** their account is created
**Then** they are assigned the "User" role by default
**And** Admin role can only be granted by existing Admins

**Technical Requirements:**
- Add `role` enum field to users table: ['user', 'admin']
- Default role = 'user' on registration
- RBAC middleware decorator: @require_role('admin')
- Admin endpoints protected with RBAC checks

---

### Story 1.4: Subscription Tier Mapping & Permission Setup

As an administrator,
I want to map user accounts to Passport subscription tiers,
So that users can only access data their subscription allows.

**Acceptance Criteria:**

**Given** I am an Admin configuring a user's account
**When** I assign them a subscription tier (e.g., "Basic", "Professional", "Enterprise")
**Then** the subscription tier is stored in the users table
**And** the tier defines their geography and category access permissions

**Given** a subscription tier is mapped to specific geographies
**When** I configure tier permissions in the admin dashboard
**Then** I can assign multiple geographies to each tier (e.g., "North America", "Europe", "Asia")
**And** these permissions are stored in a `subscription_permissions` table
**And** changes take effect immediately for all users on that tier

**Given** a subscription tier is mapped to specific categories
**When** I configure tier permissions
**Then** I can assign multiple categories to each tier (e.g., "Beverages", "Food", "Beauty")
**And** these permissions control which knowledge graph categories users can query

**Given** a user has subscription tier "Basic" with permissions for ["North America", "Beverages"]
**When** they log in
**Then** their JWT token includes their subscription_tier
**And** permission validation uses this tier to enforce data access

**Technical Requirements:**
- Create `subscription_tiers` table: id, name, description
- Create `subscription_permissions` table: tier_id, permission_type (geography/category), permission_value
- Seed default tiers: Basic, Professional, Enterprise with sample permissions
- Admin API endpoints for tier management

---

### Story 1.5: Geography-Based Query Permission Enforcement

As a system,
I want to validate user geography permissions before executing knowledge graph queries,
So that users only access data for regions their subscription allows.

**Acceptance Criteria:**

**Given** a user with subscription tier "Basic" has permission for ["North America"]
**When** they submit a query for "Soft drinks in France"
**Then** the system detects "France" is in Europe geography
**And** the permission check fails
**And** the user receives a clear error: "Your subscription does not include access to Europe data"
**And** no knowledge graph query is executed

**Given** a user with subscription tier "Professional" has permission for ["North America", "Europe"]
**When** they submit a query for "Soft drinks in France"
**Then** the system validates "France" is in their allowed geographies
**And** the permission check passes
**And** the knowledge graph query executes normally

**Given** a query does not specify a geography explicitly
**When** the system interprets the query
**Then** it extracts geography from query context (e.g., "UK soft drinks" → "United Kingdom" → Europe)
**And** validates against user's geography permissions before proceeding

**Given** an Admin user
**When** they submit any query
**Then** geography permission checks are bypassed (Admins have full access)
**And** the query proceeds without restrictions

**Technical Requirements:**
- Geography extraction from query using Query Interpreter agent
- Permission validation middleware called before Data Retrieval agent
- Geography mapping: map countries to regions (North America, Europe, Asia, etc.)
- Graceful error responses with specific permission denial messages

---

### Story 1.6: Category-Based Query Permission Enforcement

As a system,
I want to validate user category permissions before executing knowledge graph queries,
So that users only access data for categories their subscription allows.

**Acceptance Criteria:**

**Given** a user with subscription tier "Basic" has permission for ["Beverages"]
**When** they submit a query for "Bottled Water in Brazil - packaging trends"
**Then** the system detects "Bottled Water" is in Beverages category
**And** the permission check passes
**And** the knowledge graph query executes normally

**Given** a user with subscription tier "Basic" has permission for ["Beverages"]
**When** they submit a query for "Cosmetics market in France"
**Then** the system detects "Cosmetics" is in Beauty & Personal Care category
**And** the permission check fails
**And** the user receives error: "Your subscription does not include access to Beauty & Personal Care data"
**And** no knowledge graph query is executed

**Given** a user with subscription tier "Enterprise" has permission for ["All Categories"]
**When** they submit any category query
**Then** the category permission check always passes
**And** they can access all knowledge graph data (subject to geography restrictions)

**Given** a query spans multiple categories
**When** the system interprets the query
**Then** it validates the user has permissions for ALL categories mentioned
**And** if any category is unauthorized, the entire query is denied with specific category names listed

**Technical Requirements:**
- Category extraction from query using Query Interpreter agent
- Permission validation for categories before Data Retrieval agent executes
- Passport taxonomy mapping for category hierarchies
- Combined geography + category validation (both must pass)

---

### Story 1.7: Permission Validation Middleware

As a system,
I want centralized permission validation middleware,
So that all API endpoints consistently enforce subscription-based access control.

**Acceptance Criteria:**

**Given** any authenticated API request
**When** the request reaches a protected endpoint
**Then** the permission validation middleware executes automatically
**And** extracts the user's subscription_tier from JWT token
**And** loads the user's geography and category permissions from the database
**And** attaches permissions to the request context for downstream use

**Given** a request to the query submission endpoint
**When** permission validation middleware runs
**Then** it validates the user has permissions for the detected geography and category
**And** if validation passes, the request proceeds to the multi-agent pipeline
**And** if validation fails, returns 403 Forbidden with specific denial reason

**Given** a request to a non-query endpoint (e.g., export, history)
**When** permission validation runs
**Then** it applies appropriate checks for that endpoint type
**And** export requests validate user can access the original query's data
**And** history requests filter results to only show queries within user's permissions

**Given** the permission validation process encounters an error
**When** loading user permissions from the database
**Then** the system fails securely (denies access)
**And** logs the error for investigation
**And** returns 500 Internal Server Error with generic message to user

**Technical Requirements:**
- FastAPI dependency injection for permission validation
- Middleware: `validate_permissions(user: User, query_context: QueryContext)`
- Caching layer for permission lookups (Redis, 5-minute TTL)
- Permission validation exceptions with clear error messages
- Audit logging of all permission checks (pass/fail)

---

### Story 1.8: Graceful Permission Denial Handling

As a user,
I want clear, helpful error messages when my query is denied due to permissions,
So that I understand why and know what I can do about it.

**Acceptance Criteria:**

**Given** my query is denied due to geography restrictions
**When** I receive the error response
**Then** the message clearly states: "Your subscription does not include access to [Geography Name] data"
**And** suggests: "Contact your administrator to upgrade your subscription or request access to [Geography Name]"
**And** the HTTP status code is 403 Forbidden
**And** the error response includes a `permission_type: "geography"` field for client handling

**Given** my query is denied due to category restrictions
**When** I receive the error response
**Then** the message clearly states: "Your subscription does not include access to [Category Name] data"
**And** suggests: "Available categories for your subscription: [List of allowed categories]"
**And** provides a link to upgrade options

**Given** my query is denied due to both geography AND category restrictions
**When** I receive the error response
**Then** the message lists all permission failures clearly
**And** prioritizes the most restrictive failure first
**And** provides actionable guidance for each restriction

**Given** I am on the frontend and my query is denied
**When** the permission error is received
**Then** the UI displays a formatted error dialog
**And** shows my current subscription tier and permissions
**And** provides a "Contact Admin" button for quick support escalation
**And** logs the denial event for the user's audit trail

**Technical Requirements:**
- Standardized error response format: {error_type, message, details, suggestions}
- Frontend error handling component for permission denials
- User-friendly error messages (avoid technical jargon)
- Admin notification option when users hit permission limits repeatedly
- Audit trail entry for each permission denial

---

## Epic 2: Natural Language Query Interface

**User Outcome:** Users can type market intelligence questions in natural language and receive immediate feedback that their query is being processed

**Goal:** Implement complete query input experience with ChatGPT-style search bar, example queries for guidance, optimistic UI acknowledgment (<100ms), and contextual progress indicators.

### Story 2.1: Main Query Interface with Search Bar

As a user,
I want to see a prominent search bar when I arrive at the application,
So that I immediately understand how to interact with the system.

**Acceptance Criteria:**

**Given** I am an authenticated user arriving at the main page
**When** the page loads
**Then** I see a full-width search bar centered on the screen
**And** the search bar is autofocused (cursor ready)
**And** the placeholder text reads "Ask a question about market intelligence..."
**And** the design matches the ChatGPT-style interface specified in UX

**Given** I am typing a query
**When** I enter text into the search bar
**Then** the search bar expands slightly on focus (visual feedback)
**And** a "Generate Intelligence" button appears next to the bar
**And** I can submit by pressing Enter key or clicking the button

**Given** I submit a query
**When** I press Enter or click "Generate Intelligence"
**Then** the query text is sent to the backend API
**And** the search bar remains accessible for follow-up queries
**And** the submitted query appears in the conversation thread above

**Given** the search bar is empty
**When** I try to submit
**Then** the system prevents submission
**And** the placeholder text highlights briefly to indicate input is required

**Technical Requirements:**

*Project Initialization (must complete before story implementation):*
- Clone Vite + React + TypeScript + Tailwind + shadcn/ui starter template (https://github.com/doinel1a/vite-react-ts-shadcn-ui)
- Configure tailwind.config.js with design tokens (Primary: #2563EB, Accent: #F97316, Font: Inter, Spacing: 8px base)
- Install shadcn/ui base components (Button, Input, Card, Dialog, Tooltip)
- Set up project structure: src/components, src/lib, src/pages, src/services
- Dev server runs on port 5173 with hot module replacement

*Story Implementation:*
- React component: SearchBar with autofocus and controlled input
- Full-width layout (max-width 800px as per UX spec)
- Keyboard support: Enter to submit, Escape to clear
- API integration: POST /api/queries with {query_text, user_id}
- Optimistic UI: show query immediately before backend confirms

---

### Story 2.2: Example Queries Display on Empty State

As a first-time user,
I want to see example queries on the empty state,
So that I understand what kinds of questions I can ask.

**Acceptance Criteria:**

**Given** I am on the main page with no previous queries
**When** the page loads
**Then** I see 3-4 example queries displayed below the search bar
**And** examples are formatted as clickable suggestions
**And** examples match the domain: "Soft drinks industry in France", "Bottled Water in Brazil - packaging trends", "UK sugar tax impact on soft drinks"

**Given** I click on an example query
**When** the suggestion is clicked
**Then** the query text populates the search bar automatically
**And** the search bar gains focus
**And** I can edit the query before submitting or submit it as-is

**Given** I have previous queries in my history
**When** I return to the main page
**Then** the example queries are replaced by my recent query history
**And** I can still access examples via a "Show examples" link

**Given** example queries are displayed
**When** I hover over each suggestion
**Then** the suggestion highlights with a subtle background color change
**And** the cursor changes to pointer to indicate clickability

**Technical Requirements:**
- EmptyState component with example query chips
- Example queries configurable via constants file
- Click handler to populate search bar
- Conditional rendering: show examples only if no history exists
- Responsive layout for mobile (stack vertically)

---

### Story 2.3: Optimistic UI Query Acknowledgment

As a user,
I want immediate visual feedback when I submit a query,
So that I know the system received my request.

**Acceptance Criteria:**

**Given** I submit a query
**When** I press Enter or click "Generate Intelligence"
**Then** the query appears in the conversation thread within 100ms (optimistic UI)
**And** the query is styled distinctly from system responses (different background/alignment)
**And** the search bar clears immediately and is ready for the next input
**And** a progress indicator appears below the query showing "Understanding your question..."

**Given** the backend API call fails or times out
**When** the optimistic query is displayed
**Then** after the timeout period, an error indicator appears
**And** the query is marked as "Failed to submit"
**And** I see a "Retry" button next to the failed query
**And** the original query text is preserved for retry

**Given** multiple queries are submitted in sequence
**When** I submit query #2 before query #1 completes
**Then** query #2 appears in the thread below query #1
**And** both queries maintain independent progress states
**And** queries are processed in the order submitted (no race conditions)

**Technical Requirements:**
- ConversationThread component to display query/response pairs
- Optimistic rendering: add query to UI state immediately
- API error handling with retry mechanism
- Query status states: pending, processing, completed, failed
- CSS animations for smooth query appearance

---

### Story 2.4: Contextual Progress Indicators During Processing

As a user,
I want to see what the system is doing while my query is being processed,
So that I stay engaged and trust the system is working.

**Acceptance Criteria:**

**Given** my query is being processed
**When** the backend begins intelligence generation
**Then** I see a progress indicator with specific contextual messages
**And** messages update every 10-15 seconds showing current activity
**And** messages follow this sequence: "Understanding your question..." → "Analyzing market data..." → "Generating insights..." → "Validating citations..." → "Finalizing report..."

**Given** the typical query takes 3-5 minutes
**When** progress indicators are displayed
**Then** I see a time estimate: "Typically takes 3-5 minutes"
**And** the estimate appears once at the start, not repeatedly
**And** if processing exceeds 5 minutes, the message updates to "Taking longer than usual, still working..."

**Given** progress indicators are showing
**When** I see activity messages
**Then** each message has an animated icon (spinner or pulse)
**And** the animation is subtle and professional (not distracting)
**And** the current activity message is emphasized visually

**Given** processing completes successfully
**When** the intelligence report is ready
**Then** the progress indicator smoothly transitions to the report display
**And** the final progress message shows briefly: "Report ready!"
**And** the progress indicator disappears after the transition

**Given** processing fails or times out
**When** an error occurs
**Then** the progress indicator changes to an error state
**And** shows a clear error message: "Unable to generate report. Please try again."
**And** provides a "Retry" button
**And** logs the error details for debugging

**Technical Requirements:**
- ProgressIndicator component with message prop
- WebSocket or polling mechanism to receive progress updates from backend
- Progress message state machine with timing controls
- Smooth CSS transitions between progress states
- Error state handling with retry functionality
- Accessibility: screen reader announcements for progress updates

---

## Epic 3: Knowledge Graph Foundation

**User Outcome:** System has structured access to Passport market data enabling intelligent query responses

**Goal:** Build complete data infrastructure with Neo4j deployment, Passport API integration, Phase 1-2 data model implementation, and >95% corpus coverage.

### Story 3.1: Passport API Integration Layer

As a system,
I want to integrate with Passport APIs to retrieve market data,
So that I can populate the knowledge graph with authoritative data.

**Acceptance Criteria:**

**Given** I need to access Passport structured data
**When** I implement the Passport API client
**Then** I can authenticate using provided API credentials
**And** I can query market size data by geography and category
**And** I can query company market share data
**And** I can query forecast data (5-year projections)
**And** all API responses are validated against expected schemas

**Given** Passport has rate limits
**When** I make API requests
**Then** I implement exponential backoff retry logic
**And** I respect rate limits (e.g., 100 requests/minute)
**And** I queue requests if approaching rate limits
**And** I log rate limit encounters for monitoring

**Given** API requests may fail transiently
**When** failures occur
**Then** I retry failed requests up to 3 times with backoff
**And** I distinguish between retriable errors (5xx, timeout) and non-retriable (4xx auth failures)
**And** I log all API errors for debugging
**And** I gracefully degrade when data is unavailable

**Given** Passport data refreshes on a schedule
**When** implementing the integration
**Then** I track last_updated timestamps for all imported data
**And** I support incremental updates (only fetch changed data)
**And** I handle dataset deprecation events
**And** I provide API health monitoring

**Technical Requirements:**

*Infrastructure Prerequisites (must complete before story implementation):*
- Provision Neo4j AuraDB instance (small tier for MVP: 2GB memory, 8GB storage, Vector Search enabled)
- Configure database: backups (7-day retention), connection pooling (max 50), query timeout (30s)
- Install neo4j Python driver (version 5.x)
- Store credentials in AWS Secrets Manager (NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)
- Implement health check endpoint: GET /api/health/neo4j
- Create Phase 1-2 schema: Node types (Market, Industry, Geography, Category, Company, Dataset, DataPoint), Relationships (BELONGS_TO, COMPETES_IN, LOCATED_IN, HAS_DATA, CITES)
- Apply schema constraints, indexes, and document in schema/kg-schema-phase-1-2.cypher

*Story Implementation:*
- PassportClient class with async httpx library
- Authentication: API key in request headers
- Endpoints: /api/market-data, /api/company-data, /api/forecasts
- Rate limiting: token bucket algorithm
- Retry logic: exponential backoff (1s, 2s, 4s)
- Error handling: custom exceptions for different failure types
- Configuration: PASSPORT_API_BASE_URL, PASSPORT_API_KEY in environment

---

### Story 3.2: Data Ingestion Pipeline for Structured Passport Data

As a system,
I want to ingest structured Passport data into the knowledge graph,
So that the graph contains >95% corpus coverage.

**Acceptance Criteria:**

**Given** I have Passport API access
**When** I run the data ingestion pipeline
**Then** I fetch all available markets (geography × category combinations)
**And** I create Market nodes with properties: market_id, name, geography, category, market_size_usd, growth_rate, last_updated
**And** I link markets to Geography and Category nodes via relationships
**And** I track ingestion progress (X% complete)

**Given** I am ingesting company data
**When** the pipeline processes company records
**Then** I create Company nodes with properties: company_id, name, parent_company, headquarters_country, founded_year
**And** I create market share relationships: (Company)-[:COMPETES_IN {share_percentage, rank, year}]->(Market)
**And** I preserve company hierarchies: (Subsidiary)-[:SUBSIDIARY_OF]->(Parent Company)

**Given** I am ingesting forecast data
**When** the pipeline processes forecasts
**Then** I create DataPoint nodes for each year's forecast
**And** I link forecasts to markets: (Market)-[:HAS_FORECAST]->(DataPoint)
**And** each DataPoint has properties: year, value, metric_type, confidence_level, source_dataset

**Given** ingestion encounters errors
**When** processing individual records fails
**Then** I log the error with context (record_id, error message, timestamp)
**And** I continue processing other records (don't abort entire pipeline)
**And** I track error rate and fail the pipeline if error rate exceeds 5%
**And** I provide an error summary report at the end

**Given** agents need to query the ingested data
**When** implementing the query interface
**Then** I create KnowledgeGraphClient class with high-level query methods
**And** methods include: `get_market_by_geography_category()`, `get_companies_in_market()`, `get_forecast()`
**And** all methods use type hints and async/await patterns
**And** pagination is supported with limit/offset parameters (default limit: 100)
**And** query results are cached in Redis (5-minute TTL for frequently accessed data)
**And** queries timeout after 30 seconds with clear error messages

**Technical Requirements:**
- Ingestion script: scripts/ingest_passport_data.py
- Batch processing: commit every 1000 nodes (transaction management)
- Progress tracking: log every 10% completion
- Error handling: try/except per record, aggregate error report
- Validation: verify >95% of expected data is ingested
- Performance: target 1000 nodes/second ingestion rate
- Idempotency: support re-running without duplicating data
- KnowledgeGraphClient class wrapping neo4j driver with query methods
- Query result caching (Redis) and logging for debugging
- Unit tests for all query methods with mock data

---

### Story 3.3: Data Quality Validation and Coverage Monitoring

As an operator,
I want to monitor knowledge graph data quality and coverage,
So that I can ensure >95% corpus coverage requirement is met.

**Acceptance Criteria:**

**Given** the knowledge graph is populated
**When** I run data quality validation
**Then** I check total node count by type (Market, Company, Category, Geography)
**And** I verify expected node counts match Passport corpus size
**And** I calculate coverage percentage: (actual_nodes / expected_nodes) * 100
**And** I fail validation if coverage <95%

**Given** I am validating data completeness
**When** I check individual node properties
**Then** I verify required properties are not null (market_size, geography, category)
**And** I check for orphaned nodes (nodes with no relationships)
**And** I identify stale data (last_updated >30 days old)
**And** I generate a data quality report with findings

**Given** I need to monitor ongoing data quality
**When** I set up monitoring dashboards
**Then** I track coverage percentage over time (line chart)
**And** I track data staleness (nodes by last_updated age)
**And** I track ingestion error rates
**And** I set up alerts if coverage drops below 95% or error rate exceeds 5%

**Given** data quality issues are detected
**When** validation finds problems
**Then** I receive detailed error reports listing affected nodes/relationships
**And** I can trigger re-ingestion for specific data subsets
**And** I have tools to manually fix data anomalies
**And** all fixes are logged in an audit trail

**Technical Requirements:**
- Validation script: scripts/validate_kg_data.py
- Quality metrics: coverage_percentage, orphaned_nodes_count, stale_data_count, missing_properties_count
- Expected counts configuration file: config/passport_corpus_expected.yaml
- Dashboard integration: metrics exported to CloudWatch
- Alerting: SNS notifications when coverage <95%
- Data repair tools: scripts to fix common issues
- Scheduled validation: run daily via cron/Lambda

---

### Story 3.4: Knowledge Graph Update Pipeline for Data Refresh

As a system,
I want to automatically sync knowledge graph data when Passport refreshes,
So that the graph stays current with the latest market intelligence.

**Acceptance Criteria:**

**Given** Passport data is updated weekly
**When** the update pipeline runs
**Then** I detect which datasets have changed since last sync
**And** I fetch only updated records (incremental update, not full re-import)
**And** I update existing nodes with new data
**And** I mark deprecated datasets/nodes as inactive (soft delete)
**And** I track update success/failure for monitoring

**Given** a dataset is deprecated in Passport
**When** the update pipeline processes it
**Then** I mark the Dataset node with `deprecated: true, deprecated_date: timestamp`
**And** I update all citations referencing that dataset to flag as deprecated
**And** I notify operations team of deprecated datasets
**And** I do NOT delete nodes (preserve for historical queries)

**Given** new datasets are added in Passport
**When** the update pipeline discovers them
**Then** I ingest new datasets following the same ingestion logic
**And** I create new Market/Company/DataPoint nodes as needed
**And** I establish relationships to existing taxonomy nodes
**And** I log new dataset additions for tracking

**Given** the update pipeline runs on a schedule
**When** execution completes
**Then** I log execution time, records updated, errors encountered
**And** I send success/failure notifications to operations dashboard
**And** I update `last_sync_timestamp` metadata
**And** I trigger citation validation after data refresh (Epic 5 dependency)

**Technical Requirements:**
- Update pipeline script: scripts/update_kg_data.py
- Change detection: query Passport API for updated_since timestamp
- Incremental update logic: MERGE nodes (create if not exists, update if exists)
- Deprecation handling: soft delete with flags, not hard delete
- Scheduling: AWS EventBridge daily trigger
- Monitoring: CloudWatch logs, SNS notifications
- Rollback capability: backup KG snapshot before major updates

---

## Epic 4: Multi-Agent Intelligence Generation Pipeline (Mode 1)

**User Outcome:** Users receive comprehensive Market Overview reports with executive summary, competitive landscape, regulatory changes, and 5-year forecasts

**Goal:** Implement complete 8-agent LangGraph orchestration pipeline producing Mode 1 (Market Overview) intelligence reports with quality gates, iterative refinement, and YAML business rule enforcement.

### Story 4.1: Query Submission API and State Management

As a user,
I want to submit my natural language query to the backend,
So that the multi-agent pipeline can begin processing my intelligence request.

**Acceptance Criteria:**

**Given** I am an authenticated user
**When** I submit a query via POST /api/queries
**Then** the request body includes {query_text: string, user_id: string}
**And** the system validates query_text is not empty and <500 characters
**And** the system validates user_id matches authenticated JWT token
**And** the system returns a query_id immediately (UUID)
**And** the query is saved to PostgreSQL queries table with status: "pending"

**Given** my query is submitted successfully
**When** the API responds
**Then** I receive 201 Created with {query_id, status: "pending", estimated_time: "3-5 minutes"}
**And** the response includes a WebSocket URL for real-time progress updates
**And** the query processing begins asynchronously (non-blocking)

**Given** the query processing begins
**When** the orchestration pipeline starts
**Then** a LangGraph state object is created with initial state: {query_text, user_id, query_id, geography: null, category: null, status: "interpreting"}
**And** the state is persisted to Redis with 1-hour TTL
**And** the state is passed to the first agent (Query Interpreter)

**Given** I want to check query status
**When** I call GET /api/queries/{query_id}
**Then** I receive current status, progress percentage, and current agent activity
**And** if completed, the response includes the full intelligence report
**And** if failed, the response includes error details and retry options

**Technical Requirements:**

*Backend Infrastructure Prerequisites (must complete before story implementation):*
- Initialize FastAPI 0.100+ project with uvicorn[standard], Python 3.10+ with type hints
- Project structure: app/main.py, app/agents/, app/api/, app/models/, app/services/, app/core/
- Install dependencies: langgraph, langchain-anthropic, neo4j, asyncpg, redis
- Configure FastAPI on port 8000 with CORS for frontend (http://localhost:5173)
- Set up connections: Neo4j client (Epic 3), PostgreSQL, Redis
- Environment variables: ANTHROPIC_API_KEY, NEO4J_URI, DATABASE_URL, REDIS_URL from AWS Secrets Manager
- Create basic StateGraph example to verify LangGraph integration
- Docker and docker-compose for local development
- Health check endpoint: GET /api/health

*Story Implementation:*
- PostgreSQL table: queries (id, user_id, query_text, status, created_at, completed_at, error_message)
- LangGraph StateGraph with typed state class: QueryState
- Async task processing with FastAPI BackgroundTasks or Celery
- Redis state persistence for resumable workflows
- WebSocket endpoint: /ws/queries/{query_id} for real-time updates
- Status enum: pending, interpreting, retrieving, synthesizing, validating, completed, failed

---

### Story 4.2: Query Interpreter Agent Implementation

As a system,
I want the Query Interpreter agent to extract structured parameters from natural language queries,
So that downstream agents know what geography, category, and analysis type to target.

**Acceptance Criteria:**

**Given** a user query is submitted: "Soft drinks market in France - competitive landscape"
**When** the Query Interpreter agent processes it
**Then** the agent uses Claude 3.5 Sonnet to extract: {geography: "France", category: "Soft Drinks", query_type: "market_overview", sub_topics: ["competitive_landscape"]}
**And** the extracted parameters are validated against KG taxonomy
**And** the state is updated with extracted parameters
**And** processing proceeds to the next agent

**Given** a query is ambiguous: "beverage market trends"
**When** the Query Interpreter processes it
**Then** the agent identifies ambiguity (multiple geographies or categories possible)
**And** the state is marked as "needs_clarification"
**And** the user receives clarification questions: "Which geography? North America, Europe, Asia?"
**And** processing pauses until user provides clarification

**Given** a query contains invalid geography or category
**When** the Query Interpreter processes it
**Then** the agent detects the mismatch (not in KG taxonomy)
**And** suggests nearest valid alternatives: "Did you mean 'Carbonated Soft Drinks' instead of 'Sodas'?"
**And** the user can accept suggestion or rephrase query

**Given** permission validation is required
**When** the Query Interpreter extracts geography and category
**Then** the extracted values are passed to permission validation middleware
**And** if permissions fail, the query is rejected before KG queries execute
**And** if permissions pass, processing continues to Data Retrieval agent

**Technical Requirements:**
- LangGraph agent node: QueryInterpreterAgent
- Prompt template for parameter extraction with few-shot examples
- Structured output parsing: Pydantic model for extracted parameters
- Taxonomy validation against Neo4j Geography and Category nodes
- Integration with permission validation middleware (from Epic 1)
- Clarification flow: return 202 Accepted with clarification_needed flag

---

### Story 4.3: Data Retrieval Agent Implementation

As a system,
I want the Data Retrieval agent to query the knowledge graph for relevant market data,
So that the narrative synthesis has authoritative Passport data to work with.

**Acceptance Criteria:**

**Given** query parameters are extracted: {geography: "France", category: "Soft Drinks"}
**When** the Data Retrieval agent executes
**Then** it queries Neo4j for Market node matching geography + category
**And** it retrieves market size, growth rate, and 5-year forecast data
**And** it retrieves top 5 companies by market share with percentages
**And** it retrieves recent regulatory changes affecting the market
**And** all retrieved data is added to state.retrieved_data

**Given** the knowledge graph query returns results
**When** data is retrieved
**Then** each data point includes source attribution: {value, source_dataset_id, source_title, publication_date}
**And** the Data Retrieval agent tracks data completeness score (0-100%)
**And** if completeness <70%, the agent flags coverage gaps in state
**And** retrieved data is structured for easy consumption by Narrative Synthesizer

**Given** the knowledge graph query returns no results
**When** data retrieval finds no matching market
**Then** the agent returns an empty result set with clear message
**And** the state is updated with error: "No data available for France Soft Drinks"
**And** the user receives actionable feedback: "Try a different geography or category"
**And** processing terminates gracefully (no intelligence report generated)

**Given** the KG query encounters an error
**When** Neo4j connection fails or query times out
**Then** the agent retries up to 3 times with exponential backoff
**And** if all retries fail, the error is logged and state is marked "failed"
**And** the user receives error message: "Unable to retrieve data. Please try again later."

**Technical Requirements:**
- LangGraph agent node: DataRetrievalAgent
- Neo4j Cypher queries using KnowledgeGraphClient (from Epic 3)
- Data completeness calculation: (fields_populated / required_fields) * 100
- Source attribution tracking for all data points (critical for citations)
- Error handling with retries and graceful degradation
- Performance: queries complete in <30 seconds

---

### Story 4.4: Narrative Synthesizer Agent Implementation

As a system,
I want the Narrative Synthesizer agent to generate analyst-grade intelligence from retrieved data,
So that users receive insights, not just raw data.

**Acceptance Criteria:**

**Given** data has been retrieved successfully
**When** the Narrative Synthesizer agent processes it
**Then** it generates a Market Overview report with sections: Executive Summary, Market Size & Growth, Competitive Landscape, Key Trends, 5-Year Forecast, Regulatory Environment
**And** each section synthesizes insights from retrieved data (not just restating facts)
**And** the narrative is written in professional analyst tone (3rd person, objective)
**And** the report length is 800-1200 words for Mode 1

**Given** the synthesizer generates narrative text
**When** creating each section
**Then** every factual claim is grounded in retrieved data
**And** no hallucinations or unsupported assertions are included
**And** the LLM prompt includes strict instruction: "Only use provided data. Do not invent facts."
**And** claims requiring citations are marked with [CITATION_NEEDED: data_point_id]

**Given** YAML business rules are defined for Mode 1
**When** the Narrative Synthesizer generates output
**Then** the output conforms to the Mode 1 YAML specification
**And** required sections are present and in the correct order
**And** section length constraints are respected (e.g., Executive Summary: 150-200 words)
**And** YAML compliance is validated before returning output

**Given** the narrative generation encounters issues
**When** the LLM returns incomplete or malformed output
**Then** the agent retries generation up to 2 times
**And** if retries fail, the agent logs the error and marks state as "failed"
**And** partial output is discarded (no incomplete reports shown to users)

**Technical Requirements:**
- LangGraph agent node: NarrativeSynthesizerAgent
- Claude 3.5 Sonnet with extended context window (200K tokens)
- Prompt template with Mode 1 specification and examples
- YAML schema validation using Pydantic models
- Grounding verification: cross-check claims against retrieved_data
- Output length: 800-1200 words for Mode 1
- Token usage tracking for cost monitoring

---

### Story 4.5: Visualization Generator Agent Implementation

As a system,
I want the Visualization Generator agent to create charts and infographics for the intelligence report,
So that users can quickly grasp key insights visually.

**Acceptance Criteria:**

**Given** narrative synthesis is complete
**When** the Visualization Generator agent processes the report
**Then** it identifies opportunities for visualizations (market size trends, market share pie chart, forecast line chart)
**And** it generates visualization specifications in JSON format
**And** each visualization includes: type (bar/line/pie), data points, labels, colors, title, caption
**And** visualizations are added to state.visualizations array

**Given** market size and forecast data are available
**When** generating visualizations
**Then** a line chart is created showing 5-year historical + forecast trend
**And** the chart includes actual vs forecasted segments with different styling
**And** data labels show values in appropriate units ($ millions, % growth)

**Given** company market share data is available
**When** generating a market share visualization
**Then** a horizontal bar chart shows top 5 companies with share percentages
**And** companies are sorted by market share descending
**And** the chart uses brand colors if available from KG data

**Given** visualization generation fails or data is insufficient
**When** the agent cannot create a meaningful chart
**Then** it skips that visualization and continues processing
**And** the report is still valid without visualizations (degraded but functional)
**And** missing visualizations are logged for monitoring

**Technical Requirements:**
- LangGraph agent node: VisualizationGeneratorAgent
- Visualization spec format: {type, title, data, config} JSON schema
- Chart types: line, bar, pie, stacked_bar
- Frontend rendering: Chart.js or Recharts (React)
- Fallback: report works without visualizations if generation fails
- Performance: visualization generation <10 seconds

---

### Story 4.6: Quality Scorer Agent Implementation

As a system,
I want the Quality Scorer agent to evaluate generated intelligence against a multi-dimensional rubric,
So that only high-quality reports (>75% threshold) are presented to users.

**Acceptance Criteria:**

**Given** a complete intelligence report is generated
**When** the Quality Scorer agent evaluates it
**Then** it scores across dimensions: Data Completeness (0-100), Insight Quality (0-100), Citation Coverage (0-100), YAML Compliance (0-100), Readability (0-100)
**And** it calculates overall quality score: weighted average of dimension scores
**And** the quality score is added to state.quality_score

**Given** the overall quality score is >75%
**When** quality scoring completes
**Then** the report passes quality validation
**And** processing proceeds to Citation Specialist agent
**And** the quality score is stored with the report for analytics

**Given** the overall quality score is <75%
**When** quality validation fails
**Then** the report is flagged for refinement
**And** the agent identifies specific weaknesses: "Insight Quality: 65% - lacks competitive analysis depth"
**And** the report is sent back to Narrative Synthesizer for improvement (max 2 iterations)
**And** if quality still <75% after 2 iterations, human validator review is required

**Given** quality scoring includes citation coverage
**When** evaluating citation completeness
**Then** the agent checks that all [CITATION_NEEDED] markers have corresponding source attributions
**And** citation coverage score = (claims_with_citations / total_factual_claims) * 100
**And** if citation coverage <90%, the report fails quality check

**Given** YAML compliance is evaluated
**When** checking business rules
**Then** the agent validates report structure matches Mode 1 YAML spec
**And** required sections are present and correctly formatted
**And** section lengths are within specified ranges
**And** YAML compliance score reflects conformance level

**Technical Requirements:**
- LangGraph agent node: QualityScorerAgent
- Scoring rubric: weighted dimensions (Data: 25%, Insights: 30%, Citations: 25%, YAML: 10%, Readability: 10%)
- Threshold: overall score >75% to pass
- Iterative refinement loop: max 2 attempts
- Quality score storage in PostgreSQL for analytics
- Human validator escalation if quality remains <75%

---

### Story 4.7: Data Quality Validator Agent Implementation

As a system,
I want the Data Quality Validator agent to verify completeness and accuracy of retrieved data,
So that reports flag coverage gaps and don't hide data limitations.

**Acceptance Criteria:**

**Given** data has been retrieved from the knowledge graph
**When** the Data Quality Validator agent runs
**Then** it checks required data fields are present: market_size, growth_rate, top_companies, forecast_data
**And** it calculates data completeness percentage
**And** it flags missing data elements: "Warning: No regulatory data available for France Soft Drinks"
**And** completeness results are added to state.data_quality

**Given** data completeness is <70%
**When** validation identifies gaps
**Then** the validator flags coverage gaps prominently
**And** the report includes a "Data Limitations" section listing gaps
**And** users see clear disclaimer: "This analysis is based on partial data (65% coverage)"
**And** the query still completes (graceful degradation)

**Given** stale data is detected (last_updated >30 days ago)
**When** validation checks data freshness
**Then** the validator flags stale datasets
**And** the report disclaimer includes: "Some data may be outdated (last updated: 2025-12-15)"
**And** operations team is notified to trigger KG refresh

**Given** data values are suspicious or anomalous
**When** validation detects outliers
**Then** the validator flags anomalies for manual review: "Market size $500B seems unusually high for this category"
**And** the report proceeds but includes caveat
**And** anomalies are logged for knowledge graph maintenance

**Technical Requirements:**
- LangGraph agent node: DataQualityValidatorAgent
- Completeness checks: required_fields present and non-null
- Freshness threshold: flag if last_updated >30 days
- Anomaly detection: statistical outlier identification (>3 std deviations)
- Coverage gap reporting in report metadata
- Integration with KG monitoring alerts (Epic 9)

---

### Story 4.8: Citation Specialist Agent Integration (Placeholder)

As a system,
I want the Citation Specialist agent to add claim-level citations to the generated report,
So that every factual assertion links to a Passport source.

**Acceptance Criteria:**

**Given** narrative synthesis includes [CITATION_NEEDED: data_point_id] markers
**When** the Citation Specialist agent processes the report
**Then** it replaces markers with inline citation numbers [1], [2], etc.
**And** it builds a citations list mapping numbers to source metadata
**And** each citation includes: source_dataset_title, publication_date, direct_link_to_passport
**And** citations are added to state.citations array

**Given** citation accuracy must be 100%
**When** generating citations
**Then** every citation link is validated to ensure it resolves to a valid Passport dataset
**And** broken links are detected and fixed or flagged
**And** citation validation prevents any dead links from reaching users

**Technical Requirements:**
- This story is a placeholder - full implementation in Epic 5
- Integration point defined: NarrativeSynthesizerAgent outputs [CITATION_NEEDED] markers
- State structure: state.citations = [{number, claim_text, source_id, source_title, url}]
- 100% accuracy requirement enforced

---

### Story 4.9: Report Assembler Agent and LangGraph Orchestration

As a system,
I want the Report Assembler agent to combine all outputs into a final intelligence report,
So that users receive a complete, polished report with all sections, citations, and visualizations.

**Acceptance Criteria:**

**Given** all agents have completed successfully
**When** the Report Assembler agent runs
**Then** it compiles narrative sections, visualizations, citations, and metadata into final report structure
**And** the final report includes: title, executive_summary, sections[], visualizations[], citations[], methodology, data_limitations, quality_score, generated_at
**And** the report is stored in PostgreSQL reports table
**And** the query status is updated to "completed"

**Given** the LangGraph orchestration controls agent flow
**When** the query is processed
**Then** agents execute in sequence: QueryInterpreter → DataRetrieval → DataValidator → NarrativeSynthesizer → QualityScorer → (optional: iterate if quality <75%) → CitationSpecialist → VisualizationGenerator → ReportAssembler
**And** state is passed between agents and persisted after each step
**And** if any agent fails, the error is logged and processing terminates gracefully

**Given** the report generation completes
**When** the final report is ready
**Then** the user is notified via WebSocket: {event: "report_ready", query_id, report_id}
**And** the frontend fetches the full report: GET /api/reports/{report_id}
**And** the report is displayed in the UI (Epic 6)

**Given** processing fails at any stage
**When** an error occurs
**Then** the query status is updated to "failed" with error details
**And** the user receives clear error message with retry option
**And** partial state is preserved for debugging
**And** operations team is alerted if error rate exceeds threshold

**Technical Requirements:**
- LangGraph agent node: ReportAssemblerAgent
- Final report schema: Pydantic model IntelligenceReport
- PostgreSQL table: reports (id, query_id, content_json, quality_score, created_at)
- LangGraph StateGraph with conditional edges for quality iteration
- WebSocket notifications for real-time updates
- Error handling and rollback on failures
- Orchestration diagram documentation

---

### Story 4.10: YAML Business Rules Engine for Mode 1

As a system,
I want to enforce YAML business rules for Mode 1 intelligence generation,
So that LLM outputs are predictable and conform to specifications.

**Acceptance Criteria:**

**Given** Mode 1 has a defined YAML specification
**When** I define the YAML rules
**Then** I specify required sections: executive_summary, market_size_and_growth, competitive_landscape, key_trends, forecast, regulatory_environment
**And** I specify section length constraints (min/max word counts)
**And** I specify required data elements for each section
**And** I specify output format rules (markdown, heading levels, citation format)

**Given** the Narrative Synthesizer generates output
**When** YAML validation runs
**Then** the output is parsed and validated against the Mode 1 YAML schema
**And** missing required sections trigger validation failure
**And** section length violations trigger warnings
**And** malformed markdown or citation syntax triggers errors

**Given** YAML compliance score is calculated
**When** validation completes
**Then** the score reflects conformance level: (rules_passed / total_rules) * 100
**And** a score >95% is required to pass YAML validation
**And** if score <95%, specific violations are listed for correction
**And** the Narrative Synthesizer retries with explicit correction instructions

**Technical Requirements:**
- YAML specification file: config/mode-1-specification.yaml
- Pydantic schema for Mode 1 report structure
- Validation function: validate_mode1_compliance(report_content)
- >95% compliance threshold
- Detailed violation reporting for debugging
- Integration with Quality Scorer agent (YAML dimension)

---

## Epic 5: Citation & Transparency System

**User Outcome:** Users can verify every claim in intelligence reports through inline citations linking directly to Passport source data

**Goal:** Build complete citation infrastructure with Citation Specialist agent producing claim-level attributions, citation accuracy validation enforcing 100% requirement, source metadata tracking, and broken link monitoring.

### Story 5.1: Citation Specialist Agent Full Implementation

As a system,
I want the Citation Specialist agent to generate claim-level citations with 100% accuracy,
So that every factual assertion in reports links to a valid Passport source.

**Acceptance Criteria:**

**Given** the Narrative Synthesizer outputs [CITATION_NEEDED: data_point_id] markers
**When** the Citation Specialist agent processes the report
**Then** it maps each marker to the corresponding data point from retrieved_data
**And** it generates inline citation numbers [1], [2], [3] sequentially
**And** it replaces markers with citation numbers in the narrative text
**And** it builds a citations array with full source metadata

**Given** a citation is created
**When** generating citation metadata
**Then** each citation includes: citation_number, claim_text, source_dataset_id, source_title, publication_date, direct_url_to_passport, data_point_specifics
**And** the direct URL is constructed using Passport's dataset URL pattern
**And** all metadata is pulled from the knowledge graph Dataset nodes

**Given** multiple claims cite the same source
**When** processing citations
**Then** the agent reuses the same citation number for the same source
**And** the citations list contains unique sources only
**And** citation numbers are sorted in order of first appearance in text

**Given** a claim has no corresponding source attribution
**When** the agent finds an unmapped [CITATION_NEEDED] marker
**Then** it logs a critical error: "Missing source attribution for claim: {claim_text}"
**And** it marks the report as failed citation validation
**And** the report is not presented to the user until citations are complete

**Technical Requirements:**
- LangGraph agent node: CitationSpecialistAgent
- Citation mapping: match data_point_id from markers to retrieved_data sources
- URL construction: follow Passport URL patterns for dataset deep links
- Citation deduplication: track used sources, reuse numbers
- 100% coverage requirement: all markers must resolve to valid citations
- Integration point after Quality Scorer, before Report Assembler

---

### Story 5.2: Citation Accuracy Validation (100% Requirement)

As a system,
I want to validate citation accuracy with 100% success rate before presenting reports,
So that users never encounter broken or invalid citation links.

**Acceptance Criteria:**

**Given** citations have been generated
**When** the validation process runs
**Then** every citation URL is tested via HTTP HEAD request
**And** URLs returning 200 OK pass validation
**And** URLs returning 404 Not Found or 500 errors fail validation
**And** validation results are logged for each citation

**Given** all citations pass validation (100% success)
**When** validation completes
**Then** the report proceeds to final assembly
**And** the citation_accuracy_score is set to 100%
**And** the report is marked ready for user presentation

**Given** any citation fails validation (<100% success)
**When** broken links are detected
**Then** the report is flagged as "citation_validation_failed"
**And** operations team is alerted immediately
**And** the failed citations are logged with details: citation_number, url, http_status
**And** the report is NOT presented to the user
**And** automated remediation attempts to find alternative sources

**Given** citation validation runs at scale
**When** validating reports concurrently
**Then** validation requests are rate-limited to avoid overwhelming Passport servers
**And** validation caching is used (5-minute TTL per URL)
**And** validation completes within 10 seconds per report

**Technical Requirements:**
- Citation validator: async HTTP HEAD requests with httpx
- 100% accuracy hard requirement: any failure blocks report
- Automated alerting: SNS notification to operations team
- Caching layer: Redis cache for recently validated URLs
- Rate limiting: max 10 concurrent validation requests
- Retry logic: 3 retries with backoff for transient failures

---

### Story 5.3: Source Metadata Tracking and Knowledge Graph Integration

As a system,
I want comprehensive source metadata tracked in the knowledge graph,
So that citations have complete provenance information.

**Acceptance Criteria:**

**Given** Passport data is ingested into the knowledge graph
**When** Dataset nodes are created
**Then** each node includes: dataset_id, title, publication_date, url, data_type, category, geography, last_validated_at
**And** relationships link datasets to Markets, Companies, and DataPoints
**And** metadata is sufficient for citation generation

**Given** a DataPoint is used in a report
**When** citations are generated
**Then** the citation traces back through relationships: DataPoint → CITES → Dataset
**And** the Dataset node provides all required citation metadata
**And** the citation URL is constructed from dataset_id using Passport's URL schema

**Given** dataset URLs may change over time
**When** Passport updates dataset locations
**Then** the KG update pipeline (Epic 3) detects URL changes
**And** Dataset nodes are updated with new URLs
**And** citation validation flags discrepancies for manual review
**And** historical citations are updated retroactively

**Given** datasets may be deprecated
**When** a Dataset node is marked deprecated=true
**Then** existing reports with citations to that dataset show warning: "Source deprecated"
**And** new reports attempt to use alternative sources when available
**And** deprecated datasets are flagged in citation metadata

**Technical Requirements:**
- Enhanced Dataset schema: add url, publication_date, last_validated_at fields
- Relationship: (DataPoint)-[:CITES]->(Dataset) for provenance tracking
- URL schema mapping: configurable pattern for Passport dataset URLs
- Deprecation handling: soft delete with warning flags
- Citation update pipeline: retroactively update citations when URLs change

---

### Story 5.4: Broken Link Monitoring and Automated Remediation

As a system,
I want continuous monitoring of citation link health,
So that broken links are detected and fixed proactively.

**Acceptance Criteria:**

**Given** reports with citations exist in the system
**When** the broken link monitor runs (daily scheduled job)
**Then** it samples 10% of all citations from recent reports
**And** it validates URLs via HTTP HEAD requests
**And** it tracks broken link rate over time
**And** it alerts if broken link rate exceeds 1%

**Given** a citation link is found to be broken
**When** validation fails repeatedly (3+ attempts over 24 hours)
**Then** the monitor logs the broken citation with report_id and citation details
**And** it attempts automated remediation: search KG for alternative sources for the same data
**And** if alternative found, it updates the citation URL
**And** if no alternative, it escalates to operations team for manual review

**Given** broken links are detected at scale
**When** multiple citations fail
**Then** the system identifies common patterns (e.g., all citations to specific dataset failing)
**And** it correlates failures with KG Dataset deprecation status
**And** it triggers KG update pipeline to refresh dataset metadata
**And** it provides consolidated alert rather than spamming operations

**Given** citation health metrics are tracked
**When** monitoring over time
**Then** metrics include: total_citations_validated, broken_link_count, broken_link_percentage, mean_time_to_remediation
**And** metrics are exported to CloudWatch for dashboarding
**And** historical trends are visible to identify systemic issues

**Technical Requirements:**
- Scheduled job: AWS Lambda triggered daily via EventBridge
- Sampling strategy: random 10% of citations from reports created in last 7 days
- Remediation logic: query KG for alternative Dataset nodes with same data
- Alerting threshold: >1% broken link rate triggers SNS notification
- Metrics export: CloudWatch custom metrics
- Integration with KG update pipeline for dataset refresh

---

## Epic 6: Intelligence Report Display & Exploration

**User Outcome:** Users can read formatted intelligence reports, explore citations through hover previews, and interact with visualizations

**Goal:** Implement complete React frontend with Vite + TypeScript + Tailwind + shadcn/ui displaying intelligence reports with Perplexity-style citations, progressive disclosure, accessibility, and responsive design.

### Story 6.1: Report Display Container and Layout

As a user,
I want to see my intelligence report in a clean, professional layout,
So that I can easily read and navigate the content.

**Acceptance Criteria:**

**Given** my query has completed successfully
**When** the report is loaded
**Then** I see the report title prominently at the top (H1, 36px, Bold)
**And** I see metadata: query text, generated date/time, quality score badge
**And** the report content is displayed in a centered column (max-width 800px)
**And** the layout matches the UX design specification

**Given** the report has multiple sections
**When** viewing the content
**Then** sections are separated by 48px vertical spacing
**And** section headings are styled as H2 (30px, Semibold)
**And** body text is 16px Regular in Inter font
**And** line height is 1.6 for readability
**And** all design tokens match the UX spec

**Given** I am viewing on desktop (>1280px)
**When** the page renders
**Then** the report takes up the main content area
**And** a sidebar shows table of contents and history
**And** the layout is responsive and adapts smoothly

**Given** I am viewing on tablet (768px-1279px)
**When** the page renders
**Then** the sidebar collapses into a hamburger menu
**And** the report content reflows to full width
**And** all content remains accessible

**Technical Requirements:**
- React component: ReportDisplay with props: {report: IntelligenceReport}
- Layout: flex container with main content + sidebar
- Typography: Inter font, size/weight hierarchy per UX spec
- Spacing: 8px base unit, consistent rhythm
- Responsive breakpoints: 768px (tablet), 1280px (desktop)
- Accessibility: semantic HTML (article, section, nav)

---

### Story 6.2: Progressive Intelligence Disclosure (Streaming Sections)

As a user,
I want to see report sections appear progressively as they're generated,
So that I stay engaged during the 3-5 minute generation process.

**Acceptance Criteria:**

**Given** my query is being processed
**When** each agent completes
**Then** its output section streams to the frontend immediately
**And** I see sections appear in sequence: Executive Summary → Market Size & Growth → Competitive Landscape → etc.
**And** newly appeared sections animate smoothly (fade-in, 300ms)

**Given** a section is still being generated
**When** waiting for next section
**Then** I see a skeleton loader indicating content is coming
**And** the loader shows estimated remaining sections
**And** the loader does not distract from reading completed sections

**Given** all sections have been generated
**When** the report is complete
**Then** the streaming stops and final polish is applied
**And** table of contents updates to show all sections
**And** scroll-to-section navigation becomes active

**Given** I refresh the page mid-generation
**When** reconnecting
**Then** the frontend fetches current state and displays completed sections
**And** it resumes streaming from where it left off
**And** I don't lose progress

**Technical Requirements:**
- WebSocket connection: /ws/queries/{query_id} for real-time updates
- State management: Zustand or React Context for report sections
- Streaming protocol: backend sends {event: "section_complete", section_name, content}
- Animation: Framer Motion or CSS transitions
- Skeleton loaders: shadcn/ui Skeleton component
- Reconnection logic: resume streaming on page reload

---

### Story 6.3: Perplexity-Style Inline Citations with Hover Previews

As a user,
I want to see inline citation numbers and preview source details on hover,
So that I can quickly verify claims without leaving the report.

**Acceptance Criteria:**

**Given** the report narrative contains citations
**When** viewing the text
**Then** I see numbered superscript citations [1], [2], [3] inline with claims
**And** citation numbers are styled in Accent Orange (#F97316)
**And** they are clickable and hoverable

**Given** I hover over a citation number
**When** the hover state activates
**Then** a tooltip appears showing citation preview: source title, publication date, snippet
**And** the tooltip positions intelligently (above/below based on screen space)
**And** the tooltip appears after 200ms delay (not instant)
**And** the tooltip disappears when mouse leaves

**Given** I click on a citation number
**When** the click event fires
**Then** I am scrolled to the full citation in the references list at bottom
**And** the clicked citation is highlighted briefly (2-second highlight fade)
**And** the citation shows complete metadata and "View Source" link

**Given** I click "View Source" on a citation
**When** the link is activated
**Then** a new tab opens to the Passport dataset page
**And** the link uses target="_blank" rel="noopener noreferrer" for security
**And** the click is logged for analytics

**Technical Requirements:**
- Citation component: InlineCitation with number prop
- Tooltip library: shadcn/ui Tooltip or Radix UI
- Styling: superscript, Accent Orange, hover state
- Click handler: smooth scroll to citation in references section
- External link security: noopener noreferrer attributes
- Accessibility: aria-describedby linking citation to source

---

### Story 6.4: Visualization Rendering and Interaction

As a user,
I want to see interactive charts and visualizations in the report,
So that I can grasp key insights quickly and explore data visually.

**Acceptance Criteria:**

**Given** the report includes visualization specifications
**When** rendering visualizations
**Then** each visualization is rendered as an interactive chart
**And** charts use Chart.js or Recharts library (React-friendly)
**And** charts follow the design system color palette
**And** charts have titles, labels, and legends

**Given** a line chart visualization is rendered
**When** viewing the chart
**Then** I see historical data + forecast with distinct styling (solid line vs dashed)
**And** data labels appear on hover
**And** the chart animates on initial render (smooth draw-in)
**And** the chart is responsive and resizes with window

**Given** a bar chart visualization is rendered
**When** viewing company market shares
**Then** companies are sorted by share descending
**And** each bar shows percentage label
**And** hovering a bar shows additional details (company name, exact share, rank)

**Given** visualizations fail to load
**When** data is missing or malformed
**Then** a fallback message appears: "Visualization unavailable"
**And** the report remains functional without the chart
**And** the error is logged for debugging

**Given** I am on mobile
**When** viewing charts
**Then** charts scale down appropriately
**And** labels remain legible
**And** touch interactions work for tooltips

**Technical Requirements:**
- Chart library: Recharts (preferred) or Chart.js
- Visualization types: LineChart, BarChart, PieChart
- Props: {type, data, title, config} from backend spec
- Responsive: container queries for chart sizing
- Accessibility: chart data available as table (hidden but screen reader accessible)
- Fallback: graceful error handling if chart fails

---

### Story 6.5: Command Palette (Cmd/Ctrl+K) for Power Users

As a power user,
I want to use a command palette for quick actions,
So that I can navigate and perform actions efficiently with keyboard shortcuts.

**Acceptance Criteria:**

**Given** I press Cmd+K (Mac) or Ctrl+K (Windows/Linux)
**When** the command palette opens
**Then** I see a search input with placeholder "Type a command..."
**And** I see a list of available commands organized by category
**And** the palette overlays the page with backdrop blur effect
**And** focus is immediately in the search input

**Given** I type in the command palette
**When** searching for commands
**Then** results filter in real-time as I type
**And** fuzzy matching works (e.g., "exp" matches "Export to PDF")
**And** the top result is highlighted by default
**And** I can navigate results with arrow keys

**Given** command categories are shown
**When** no search query is entered
**Then** I see categories: Navigation, Reports, Export, Settings
**And** each category shows top 3-4 commands
**And** commands have keyboard shortcuts displayed (e.g., "Export PDF - Ctrl+E")

**Given** I select a command
**When** pressing Enter or clicking
**Then** the command executes immediately
**And** the palette closes
**And** feedback is shown if the command requires time (e.g., "Exporting...")

**Given** I press Escape
**When** the palette is open
**Then** it closes immediately
**And** focus returns to previous element

**Technical Requirements:**
- Command palette library: cmdk (by Patr Team) or custom with shadcn/ui Dialog
- Keyboard shortcut: Cmd+K / Ctrl+K global listener
- Commands: export PDF, new query, view history, jump to section, copy report link
- Search: fuzzy matching with fuse.js
- Accessibility: proper focus trap, Escape to close, aria labels

---

### Story 6.6: Sidebar Navigation and Report History

As a user,
I want a sidebar to navigate between sections and access my report history,
So that I can efficiently explore reports and find previous queries.

**Acceptance Criteria:**

**Given** I am viewing a report
**When** the sidebar is visible
**Then** I see a table of contents with all report sections listed
**And** clicking a section name scrolls smoothly to that section
**And** the active section is highlighted as I scroll (sticky navigation)

**Given** the table of contents tracks scroll position
**When** I scroll through the report
**Then** the TOC highlights the current section automatically
**And** the highlighting updates smoothly without jank
**And** I always know which section I'm reading

**Given** I want to view my report history
**When** I click the "History" tab in sidebar
**Then** I see a list of my recent queries (last 10)
**And** each entry shows: query text snippet, date/time, status badge
**And** clicking an entry loads that report
**And** the list is sorted by most recent first

**Given** I am on mobile
**When** accessing the sidebar
**Then** it appears as a slide-out drawer from the left
**And** it overlays the report content
**And** a backdrop dismisses the drawer on click
**And** the hamburger menu icon toggles the drawer

**Technical Requirements:**
- Sidebar component: fixed position on desktop, drawer on mobile
- TOC generation: extract H2 headings from report content, generate anchor links
- Scroll tracking: IntersectionObserver API to detect active section
- History fetching: GET /api/queries?user_id={user_id}&limit=10&status=completed
- Responsive: breakpoint at 768px for mobile drawer behavior
- Animation: smooth scrolling, drawer slide transitions

---

### Story 6.7: Accessibility and Responsive Design Compliance

As a user with accessibility needs,
I want the report interface to be fully accessible and WCAG AA compliant,
So that I can use screen readers, keyboard navigation, and assistive technologies.

**Acceptance Criteria:**

**Given** I navigate the report with keyboard only
**When** using Tab, Shift+Tab, Enter, and arrow keys
**Then** all interactive elements are reachable and operable
**And** focus indicators are visible and clear (2px outline)
**And** focus order is logical (top to bottom, left to right)
**And** no keyboard traps exist

**Given** I use a screen reader
**When** the report loads
**Then** semantic HTML elements are used (article, section, nav, main)
**And** headings have proper hierarchy (H1 → H2 → H3)
**And** images have alt text
**And** citations have aria-labels describing the source
**And** the screen reader announces section changes during progressive loading

**Given** I have visual impairments
**When** viewing the report
**Then** color contrast ratios meet WCAG AA (4.5:1 for text)
**And** text can be resized up to 200% without breaking layout
**And** focus indicators have 3:1 contrast against background
**And** colors are not the only way to convey information

**Given** I have motor impairments
**When** interacting with the report
**Then** clickable targets are at least 44x44px (touch-friendly)
**And** hover states are not required for functionality
**And** time limits can be extended or disabled

**Given** the interface is responsive
**When** viewing on different screen sizes
**Then** the layout adapts from 320px (small mobile) to 1920px (large desktop)
**And** no horizontal scrolling occurs
**And** text remains readable at all sizes
**And** touch targets are appropriately sized on mobile

**Technical Requirements:**
- WCAG AA compliance validation with axe-core or Lighthouse
- Semantic HTML: article, section, nav, header, footer, main
- Keyboard navigation: tab order, focus management, Escape to close modals
- Screen reader testing: NVDA, JAWS, VoiceOver compatibility
- Color contrast: minimum 4.5:1 for normal text, 3:1 for large text and UI components
- Responsive: breakpoints at 320px, 768px, 1280px, 1920px

---

## Epic 7: Report Export & Sharing

**User Outcome:** Users can export intelligence reports to PDF format for sharing with colleagues and stakeholders

**Goal:** Build PDF generation service with formatted output preserving citations, visualizations, and professional layout.

### Story 7.1: PDF Export Generation Service

As a user,
I want to export my intelligence report to PDF format,
So that I can share it with colleagues via email or presentations.

**Acceptance Criteria:**

**Given** I am viewing a completed report
**When** I click the "Export to PDF" button
**Then** the system generates a PDF within 10 seconds
**And** I receive a download link or automatic browser download
**And** the PDF includes the complete report with all sections, citations, and visualizations

**Given** the PDF is being generated
**When** processing
**Then** I see a progress indicator: "Generating PDF..."
**And** the button is disabled to prevent duplicate requests
**And** I can continue reading the report while PDF generates (non-blocking)

**Given** the PDF generation completes
**When** the file is ready
**Then** the browser automatically downloads the file: "Market_Overview_France_SoftDrinks_2026-01-21.pdf"
**And** the filename includes query summary and date for easy identification
**And** the button re-enables for future exports

**Given** the PDF includes formatted content
**When** viewing the PDF
**Then** the layout matches professional analyst report standards
**And** sections are properly paginated (no awkward page breaks mid-paragraph)
**And** fonts are embedded (Inter font family)
**And** images and charts render clearly (high resolution)
**And** citations are hyperlinks to Passport sources

**Given** PDF generation fails
**When** an error occurs
**Then** I receive error message: "Unable to generate PDF. Please try again."
**And** the error is logged for debugging
**And** I have a "Retry" option

**Technical Requirements:**
- PDF generation library: WeasyPrint (Python) or Puppeteer (Node.js)
- Backend endpoint: POST /api/reports/{report_id}/export/pdf
- Template: HTML template with CSS for PDF layout
- Font embedding: Inter font included in PDF for consistency
- Image handling: embed charts as SVG or high-res PNG
- File naming: {report_type}_{geography}_{category}_{date}.pdf
- Storage: temporary S3 storage with 1-hour expiry, presigned URL for download
- Performance: <10 seconds generation time

---

### Story 7.2: Export Button Integration and Download UX

As a user,
I want one-click export with clear feedback,
So that I understand the export process and can easily download my PDF.

**Acceptance Criteria:**

**Given** I am viewing a report
**When** I locate the export button
**Then** it is prominently placed in the report header
**And** it is labeled "Export to PDF" with a download icon
**And** it is styled as a primary action button (Professional Blue)

**Given** I click the export button
**When** the request is sent
**Then** the button immediately shows loading state: "Generating..."
**And** a spinner icon replaces the download icon
**And** the button is disabled to prevent duplicate exports
**And** the UI remains responsive (no blocking)

**Given** the PDF is ready
**When** generation completes successfully
**Then** the browser automatically downloads the file
**And** a toast notification appears: "PDF downloaded successfully"
**And** the button returns to normal state
**And** I can export again if needed

**Given** I have slow network or large report
**When** PDF generation takes longer than expected
**Then** I see a progress percentage if available
**And** a message appears: "Large report, this may take a moment..."
**And** I can cancel the export if desired

**Given** I want to share the report
**When** export is complete
**Then** I have the PDF file in my Downloads folder
**And** I can email, upload to Teams/Slack, or attach to presentations
**And** the PDF is fully self-contained (no dependencies on external links except citations)

**Technical Requirements:**
- Export button: shadcn/ui Button with loading state
- API call: axios POST with progress tracking
- Toast notifications: shadcn/ui Toast or react-hot-toast
- Loading state management: React useState for button state
- Download trigger: browser download via Content-Disposition header or presigned S3 URL
- Cancel option: abort controller for request cancellation
- Analytics: track export events (report_id, user_id, timestamp)

---

## Epic 8: Administrative Management Dashboard

**User Outcome:** Administrators can manage user access, configure permissions, and control system settings

**Goal:** Build admin interface for user provisioning, subscription tier mapping, beta group management, audit trail access, and data residency configuration.

### Story 8.1: Admin Dashboard Main Interface

As an administrator,
I want a dedicated admin dashboard,
So that I can manage users, permissions, and system configuration.

**Acceptance Criteria:**

**Given** I am logged in as an Admin
**When** I navigate to /admin
**Then** I see the admin dashboard with navigation: Users, Permissions, Beta Groups, Audit Trail, Settings
**And** I am denied access if my role is not Admin (403 Forbidden)
**And** the dashboard layout is clean and professional

**Given** I am on the admin dashboard
**When** viewing navigation
**Then** I see tabs or sidebar menu for each admin section
**And** the active section is highlighted
**And** I can switch between sections without page reload (SPA navigation)

**Given** I view admin metrics
**When** the dashboard loads
**Then** I see key metrics: total users, active users (last 7 days), queries today, reports generated this month, error rate
**And** metrics are displayed as cards with icons
**And** metrics update in real-time or refresh every 30 seconds

**Technical Requirements:**
- Admin dashboard route: /admin (protected by @require_role('admin'))
- React components: AdminDashboard, AdminNav, MetricsCards
- Metrics API: GET /api/admin/metrics
- Authorization: JWT role check, redirect non-admin users
- Layout: sidebar navigation + main content area
- Responsive: adapt for tablet (collapse sidebar)

---

### Story 8.2: User Management (Provisioning and Deprovisioning)

As an administrator,
I want to create, view, edit, and delete user accounts,
So that I can onboard new users and offboard departing users.

**Acceptance Criteria:**

**Given** I am on the Users section
**When** viewing the user list
**Then** I see a table with columns: Email, Role, Subscription Tier, Created Date, Status, Actions
**And** the table supports pagination (50 users per page)
**And** I can search users by email or name
**And** I can filter by role or subscription tier

**Given** I want to create a new user
**When** I click "Add User" button
**Then** a modal opens with form fields: Email, Password, Role, Subscription Tier
**And** I can set role to User or Admin
**And** I can assign subscription tier (Basic, Professional, Enterprise)
**And** form validation ensures email is unique and password meets requirements
**And** submitting the form creates the user and shows success message

**Given** I want to edit a user
**When** I click "Edit" on a user row
**Then** a modal opens pre-filled with current user data
**And** I can change role, subscription tier, or reset password
**And** I cannot change the user's email (immutable)
**And** submitting saves changes and logs the action to audit trail

**Given** I want to delete a user
**When** I click "Delete" on a user row
**Then** a confirmation dialog appears: "Are you sure? This action cannot be undone."
**And** confirming the deletion soft-deletes the user (sets status=inactive)
**And** the user can no longer log in
**And** the deletion is logged to audit trail

**Technical Requirements:**
- Backend endpoints: GET/POST/PUT/DELETE /api/admin/users
- User table component: shadcn/ui DataTable with sorting, filtering, pagination
- Modal forms: shadcn/ui Dialog with form validation
- Soft delete: users.status = 'inactive' (retain data for audit)
- Audit logging: all user management actions logged to audit_trail table

---

### Story 8.3: Subscription Tier Mapping and Permission Configuration

As an administrator,
I want to configure subscription tiers and map geography/category permissions,
So that user data access aligns with their Passport subscriptions.

**Acceptance Criteria:**

**Given** I am on the Permissions section
**When** viewing subscription tiers
**Then** I see existing tiers: Basic, Professional, Enterprise
**And** I can view permissions for each tier (geographies and categories)
**And** I can edit tier permissions by clicking "Edit" on a tier

**Given** I am editing a subscription tier
**When** configuring permissions
**Then** I see two multi-select dropdowns: Geographies and Categories
**And** geographies include: North America, Europe, Asia, Latin America, Middle East & Africa, All Geographies
**And** categories include: Beverages, Food, Beauty & Personal Care, etc., All Categories
**And** I can select multiple options for each
**And** changes save immediately and apply to all users on that tier

**Given** I assign a user to a subscription tier
**When** editing a user
**Then** the tier dropdown shows available tiers
**And** selecting a tier automatically applies that tier's permissions to the user
**And** the user's next query enforces the new permissions

**Given** I want to create a custom tier
**When** I click "Add Tier"
**Then** a form appears: Tier Name, Description, Geographies, Categories
**And** the new tier is saved and available for user assignment
**And** custom tiers work identically to default tiers

**Technical Requirements:**
- Backend endpoints: GET/PUT /api/admin/subscription-tiers
- Multi-select component: shadcn/ui Multi-Select or custom
- Permissions storage: subscription_permissions table (tier_id, permission_type, permission_value)
- Permission enforcement: middleware checks tier permissions on each query
- Real-time updates: permissions apply on next user request (no session restart needed)

---

### Story 8.4: Beta Group Management and Feature Flags

As an administrator,
I want to manage beta testing groups,
So that I can roll out new features to select users before general availability.

**Acceptance Criteria:**

**Given** I am on the Beta Groups section
**When** viewing beta groups
**Then** I see existing groups: Beta Testers, Early Access, Internal QA
**And** I see user count for each group
**And** I can view group members by clicking on the group

**Given** I want to create a beta group
**When** I click "Create Group"
**Then** a form appears: Group Name, Description, Feature Flags
**And** feature flags are checkboxes: Mode 2 (Category Deep Dive), Mode 3 (Regulatory Brief), Advanced Export, etc.
**And** I can select which features are enabled for this group
**And** submitting creates the group

**Given** I want to add users to a beta group
**When** viewing a group's member list
**Then** I can click "Add Members"
**And** I see a searchable user list with checkboxes
**And** I can select multiple users and add them in bulk
**And** added users immediately gain access to enabled features

**Given** I want to remove users from a beta group
**When** viewing group members
**Then** I can click "Remove" next to a user
**And** the user loses access to beta features on their next request
**And** the action is logged to audit trail

**Given** beta features are feature-flagged
**When** a beta user submits a query
**Then** the system checks their beta group membership
**And** if they're in a group with "Mode 2" enabled, Mode 2 options appear in UI
**And** if not, Mode 2 remains hidden
**And** feature flag checks are fast (<10ms overhead)

**Technical Requirements:**
- Backend tables: beta_groups, beta_group_members, feature_flags
- Endpoints: GET/POST/PUT /api/admin/beta-groups
- Feature flag checking: middleware or decorator @feature_flag('mode_2')
- Frontend: conditional rendering based on user's enabled features
- Caching: Redis cache for beta group membership (5-minute TTL)

---

### Story 8.5: Audit Trail Access and Compliance Reporting

As an administrator,
I want to query audit trail logs for compliance and debugging,
So that I can investigate incidents and generate compliance reports.

**Acceptance Criteria:**

**Given** I am on the Audit Trail section
**When** viewing logs
**Then** I see a filterable table with columns: Timestamp, User, Action, Resource, Details, IP Address
**And** I can filter by date range, user, action type
**And** I can search by keywords in details field
**And** the table paginates for performance (100 logs per page)

**Given** I select a date range
**When** filtering audit logs
**Then** I can use a date picker to select start and end dates
**And** the logs update to show only events within that range
**And** default view is last 7 days

**Given** I want to investigate a specific user
**When** I filter by user email
**Then** I see all actions taken by that user: logins, queries, exports, permission denials
**And** I can trace the user's activity timeline chronologically
**And** sensitive actions (e.g., permission denial, failed login) are flagged

**Given** I want to export audit logs for compliance
**When** I click "Export Logs"
**Then** the system generates a CSV file with filtered logs
**And** the CSV includes all columns with full timestamps
**And** the file is downloaded: "audit_logs_2026-01-21.csv"

**Given** I view audit log details
**When** I click on a log entry
**Then** a modal shows full details including: user_id, session_id, request payload, response status, error messages
**And** sensitive data (passwords) is redacted
**And** I can copy log details for tickets or reports

**Technical Requirements:**
- Backend endpoint: GET /api/admin/audit-trail with filtering params
- Audit trail table: timestamped logs with user_id, action, resource, details, ip_address
- Filtering: query params for date_range, user_id, action_type
- Export: CSV generation with filtered results
- Retention: configurable (default 12 months), automated archival to S3 for compliance
- Performance: indexed queries, pagination for large result sets

---

## Epic 9: Operations Monitoring & Observability

**User Outcome:** Operations staff can monitor system health, debug failures, maintain the knowledge graph, and respond to incidents

**Goal:** Implement operations dashboard with AWS CloudWatch integration, query audit trails, agent orchestration flow debugging, KG health monitoring, performance metrics tracking, citation accuracy alerting, KG maintenance tools, and automated health alerts.

### Story 9.1: Operations Dashboard and CloudWatch Integration

As an operations engineer,
I want a real-time operations dashboard with CloudWatch metrics,
So that I can monitor system health and identify issues quickly.

**Acceptance Criteria:**

**Given** I am logged in as an Operations user
**When** I navigate to /operations
**Then** I see the operations dashboard with sections: System Health, Performance, Knowledge Graph, Citations, Errors
**And** access is restricted to Admin and Operations roles

**Given** I view system health metrics
**When** the dashboard loads
**Then** I see CloudWatch metrics: API response time (p50, p95, p99), error rate (%), concurrent queries, active users
**And** metrics are displayed as time-series charts (last 24 hours by default)
**And** I can change time range: 1 hour, 24 hours, 7 days, 30 days
**And** metrics refresh every 60 seconds automatically

**Given** I view performance metrics
**When** checking query performance
**Then** I see average query processing time, agent execution breakdown (time per agent), LLM token usage, KG query latency
**And** I can identify slow agents or bottlenecks
**And** metrics are color-coded: green (<3 min), yellow (3-5 min), red (>5 min)

**Given** I view error metrics
**When** checking system errors
**Then** I see error rate over time, top 10 error types, recent error logs (last 50)
**And** I can click an error to view full details and stack trace
**And** errors are categorized: LLM failures, KG timeouts, permission denials, citation validation failures

**Technical Requirements:**
- Operations dashboard route: /operations (protected by @require_role(['admin', 'operations']))
- CloudWatch metrics: custom metrics exported via boto3
- Metrics: query_latency, error_rate, concurrent_queries, agent_execution_time
- Frontend: Recharts for time-series visualizations
- Refresh interval: 60 seconds, configurable
- Alerting integration: link to SNS alert configuration

---

### Story 9.2: Query Audit Trail and Orchestration Flow Debugging

As an operations engineer,
I want to view complete query orchestration flows for debugging,
So that I can diagnose failures and optimize agent performance.

**Acceptance Criteria:**

**Given** I want to debug a failed query
**When** I search for the query in audit trail
**Then** I can find it by query_id, user_id, or query text
**And** I see query status: pending, completed, failed
**And** I can click "View Details" to see full orchestration flow

**Given** I view a query's orchestration flow
**When** details load
**Then** I see a visual flow diagram: QueryInterpreter → DataRetrieval → NarrativeSynthesizer → QualityScorer → ...
**And** each agent node shows: execution time, status (success/failed), input/output preview
**And** failed agents are highlighted in red with error details

**Given** I inspect an individual agent execution
**When** I click on an agent node
**Then** I see full details: input state, output state, LLM prompts, LLM responses, execution time, error messages
**And** I can copy prompts/responses for testing or refinement
**And** I can see LLM token usage for cost analysis

**Given** I want to analyze agent performance across queries
**When** I view aggregate statistics
**Then** I see average execution time per agent type
**And** I can identify consistently slow agents
**And** I can filter by date range or user cohort

**Given** I want to retry a failed query
**When** viewing a failed query
**Then** I see a "Retry Query" button
**And** clicking it re-submits the query through the pipeline
**And** I can monitor the retry in real-time
**And** I can compare original vs retry execution

**Technical Requirements:**
- Query audit: queries table with full state snapshots at each agent
- Orchestration flow: store agent execution log in JSON format
- Flow visualization: React Flow or custom SVG diagram
- Query search: indexed search by query_id, user_id, text
- Retry mechanism: re-submit query to pipeline with original parameters
- Performance analytics: aggregate agent execution times, identify outliers

---

### Story 9.3: Knowledge Graph Health Monitoring and Maintenance Tools

As an operations engineer,
I want to monitor knowledge graph health and perform maintenance,
So that I ensure >95% corpus coverage and detect stale data.

**Acceptance Criteria:**

**Given** I view KG health metrics
**When** the dashboard loads
**Then** I see coverage percentage (actual nodes / expected nodes)
**And** I see node counts by type: Market, Company, Category, Geography, Dataset
**And** I see data staleness: nodes by last_updated age (<7 days, 7-30 days, >30 days)
**And** I see KG query latency percentiles (p50, p95, p99)

**Given** coverage drops below 95%
**When** the threshold is breached
**Then** an alert is triggered via SNS notification
**And** the dashboard shows a red warning banner
**And** the alert includes details: missing node count, affected categories/geographies
**And** I can trigger KG re-ingestion from the dashboard

**Given** I detect stale data
**When** viewing data staleness metrics
**Then** I see which datasets haven't been updated in >30 days
**And** I can filter by category or geography to identify patterns
**And** I can trigger selective KG updates for specific datasets

**Given** I want to manually maintain the KG
**When** using maintenance tools
**Then** I can trigger full KG re-ingestion (warning: takes hours)
**And** I can trigger incremental update (only changed datasets)
**And** I can mark specific datasets as deprecated
**And** I can validate KG schema integrity
**And** all maintenance actions are logged to audit trail

**Given** KG queries are slow
**When** latency exceeds thresholds
**Then** I receive alert: "KG query latency high (p95: 8 seconds)"
**And** I can view slow query logs to identify problematic Cypher queries
**And** I can reindex Neo4j if needed
**And** I can scale up Neo4j resources via dashboard link

**Technical Requirements:**
- KG health metrics: coverage_percentage, node_counts, staleness_distribution, query_latency
- Maintenance tools: endpoints for re-ingestion, incremental update, deprecation
- Alerts: SNS notifications when coverage <95% or latency >10s
- Slow query log: Neo4j query logging enabled, integrated into dashboard
- Automation: scheduled KG health checks (daily via Lambda)

---

### Story 9.4: Citation Accuracy Monitoring and Broken Link Alerting

As an operations engineer,
I want to monitor citation accuracy and receive alerts for broken links,
So that I maintain the 100% citation accuracy requirement.

**Acceptance Criteria:**

**Given** I view citation metrics
**When** the dashboard loads
**Then** I see citation accuracy rate: (valid_citations / total_citations) * 100
**And** I see broken link count and percentage
**And** I see mean time to remediation for broken links
**And** I see citation validation failures over time (trend chart)

**Given** citation accuracy drops below 100%
**When** broken links are detected
**Then** an alert is triggered: "CRITICAL: Broken citation links detected (5 failures)"
**And** I receive SNS notification with details: report_ids, citation_numbers, URLs
**And** the dashboard highlights affected reports

**Given** I investigate broken citations
**When** viewing broken link details
**Then** I see list of broken citations: report_id, citation_number, url, last_validated_at, http_status
**And** I can click "Test Link" to manually validate
**And** I can click "Find Alternative" to search KG for replacement sources
**And** I can mark citation as "Acknowledged" to suppress repeated alerts

**Given** automated remediation runs
**When** broken links are detected
**Then** the system attempts to find alternative Dataset nodes with same data
**And** if found, citations are auto-updated and reports are regenerated
**And** if not found, operations team is alerted for manual intervention
**And** remediation attempts are logged

**Given** I want historical citation health data
**When** viewing trends
**Then** I can see citation accuracy over time (last 30 days)
**And** I can correlate broken links with KG update events
**And** I can identify patterns (e.g., specific datasets frequently breaking)

**Technical Requirements:**
- Citation metrics: accuracy_rate, broken_link_count, remediation_time
- Broken link detection: scheduled job (daily) validates sample of citations
- Alerting: SNS critical alert if accuracy <100%
- Remediation: automated alternative source search + manual workflow
- Dashboard: broken link list with test/remediate actions
- Historical tracking: time-series data in CloudWatch custom metrics

---

### Story 9.5: Automated Health Alerts and Incident Response

As an operations engineer,
I want automated alerts for system health issues,
So that I can respond to incidents quickly before they impact users.

**Acceptance Criteria:**

**Given** the system monitors health metrics
**When** thresholds are breached
**Then** alerts are sent via SNS to operations team
**And** alerts are categorized by severity: INFO, WARNING, CRITICAL
**And** each alert includes: metric name, current value, threshold, timestamp, affected resources

**Given** error rate exceeds 1%
**When** errors spike
**Then** CRITICAL alert is sent: "Error rate: 3.5% (threshold: 1%)"
**And** the alert includes top error types and recent error logs
**And** I can click link to operations dashboard for investigation

**Given** query latency exceeds 5 minutes (p95)
**When** performance degrades
**Then** WARNING alert is sent: "Query latency high: p95 = 6.2 minutes"
**And** the alert suggests checking LLM API status and KG query performance
**And** I can scale resources if needed

**Given** KG coverage drops below 95%
**When** coverage threshold is breached
**Then** CRITICAL alert is sent: "KG coverage: 92% (threshold: 95%)"
**And** the alert identifies missing node types and affected categories
**And** I can trigger KG re-ingestion from alert link

**Given** citation accuracy drops below 100%
**When** broken links are detected
**Then** CRITICAL alert is sent: "Citation accuracy: 97% (3 broken links)"
**And** the alert lists affected reports and URLs
**And** I can initiate remediation workflow

**Given** I receive multiple alerts
**When** investigating incidents
**Then** alerts are consolidated (not spamming)
**And** related alerts are grouped: e.g., "KG issues: coverage + query latency"
**And** I can acknowledge alerts to suppress repeat notifications
**And** I can configure alert thresholds via dashboard

**Technical Requirements:**
- Alerting: AWS SNS topics for different severity levels
- Alert subscribers: operations team emails, Slack/Teams webhooks
- Thresholds: configurable via operations dashboard or environment variables
- Alert rules: error_rate >1%, query_latency_p95 >5min, kg_coverage <95%, citation_accuracy <100%
- Consolidation: debounce repeated alerts (15-minute window)
- Acknowledgment: mark alerts as acknowledged to suppress repeats

---

## Epic 10: System Scalability & Performance Optimization

**User Outcome:** System reliably handles 100+ concurrent users with <3 minute average response times

**Goal:** Implement complete AWS infrastructure with ECS Fargate, RDS PostgreSQL, ElastiCache Redis, SQS/SNS, horizontal scaling, caching strategies, async processing, health checks, graceful degradation, and security hardening.

### Story 10.1: AWS Infrastructure Foundation (VPC, RDS, ElastiCache)

As a DevOps engineer,
I want to provision core AWS infrastructure,
So that the application has secure, scalable backend services.

**Acceptance Criteria:**

**Given** I need to provision AWS infrastructure
**When** deploying the foundation
**Then** I create a VPC with public and private subnets across 1 availability zone (Single-AZ for MVP)
**And** I create RDS PostgreSQL instance (db.t3.medium) in private subnet
**And** I create ElastiCache Redis cluster (cache.t3.micro, single node) in private subnet
**And** I configure security groups: RDS/Redis only accessible from ECS tasks

**Given** RDS PostgreSQL is provisioned
**When** configuring the database
**Then** I enable automated backups (7-day retention)
**And** I enable encryption at rest (AWS KMS)
**And** I enable encryption in transit (SSL connections required)
**And** I set performance_insights enabled for monitoring
**And** I configure connection pooling limits (max 100 connections)

**Given** ElastiCache Redis is provisioned
**When** configuring caching
**Then** I enable encryption at rest and in transit
**And** I configure eviction policy: allkeys-lru
**And** I set maxmemory appropriate for cache.t3.micro (500MB)
**And** I enable CloudWatch metrics

**Given** networking is configured
**When** setting up connectivity
**Then** ECS tasks can access RDS and Redis via private IPs
**And** NAT Gateway provides outbound internet access for ECS tasks (API calls to Anthropic, Passport)
**And** No inbound internet access to RDS/Redis (security)

**Technical Requirements:**
- Infrastructure as Code: Terraform or AWS CDK
- VPC: 1 public subnet, 2 private subnets, NAT Gateway
- RDS: PostgreSQL 15, db.t3.medium, 50GB storage, automated backups
- ElastiCache: Redis 7.x, cache.t3.micro, single node (MVP)
- Security groups: strict ingress rules (only ECS tasks can access RDS/Redis)
- Secrets: database credentials in AWS Secrets Manager

---

### Story 10.2: ECS Fargate Deployment and Container Orchestration

As a DevOps engineer,
I want to deploy the FastAPI backend on ECS Fargate,
So that the application scales horizontally and is highly available.

**Acceptance Criteria:**

**Given** I have a Docker container for FastAPI backend
**When** deploying to ECS
**Then** I create an ECS cluster with Fargate launch type
**And** I define task definition: 2 vCPU, 4GB memory, FastAPI container
**And** I create ECS service with 1 task for MVP (scale later)
**And** I configure health checks: /api/health endpoint

**Given** the ECS service is running
**When** tasks launch
**Then** environment variables are loaded from AWS Secrets Manager
**And** tasks connect to RDS, Redis, and Neo4j successfully
**And** health checks pass within 60 seconds of task start
**And** logs stream to CloudWatch Logs

**Given** I need load balancing
**When** configuring ALB
**Then** I create Application Load Balancer in public subnets
**And** ALB forwards HTTPS traffic to ECS tasks
**And** SSL certificate is provisioned via ACM
**And** HTTP requests redirect to HTTPS

**Given** I want auto-scaling (future)
**When** configuring scaling policies
**Then** I define target tracking: scale up when CPU >70%, scale down when CPU <30%
**And** min tasks = 1, max tasks = 10 (for MVP growth)
**And** scaling adjustments take 2-3 minutes

**Given** deployments need zero downtime
**When** updating the service
**Then** I use rolling updates: 1 new task starts, health check passes, old task drains, old task stops
**And** health check grace period is 60 seconds
**And** deployment completes in ~5 minutes

**Technical Requirements:**
- ECS cluster: Fargate launch type
- Task definition: FastAPI container, 2 vCPU, 4GB memory
- Service: desired count = 1 (MVP), rolling update, health checks
- ALB: HTTPS listener (port 443), target group routing to ECS tasks
- Auto-scaling: target tracking on CPU utilization (optional for MVP)
- Logging: CloudWatch Logs with 7-day retention

---

### Story 10.3: Asynchronous Task Processing with SQS and SNS

As a system,
I want to process queries asynchronously using SQS,
So that the API responds immediately and long-running tasks don't block.

**Acceptance Criteria:**

**Given** a user submits a query
**When** POST /api/queries is called
**Then** the API immediately returns 201 Created with query_id
**And** the query is published to SQS queue: intelligence-generation-queue
**And** the API response time is <100ms (non-blocking)

**Given** a query message is in SQS
**When** a worker picks up the message
**Then** the worker initiates LangGraph orchestration pipeline
**And** the message visibility timeout is 10 minutes (max processing time)
**And** if processing completes, message is deleted from queue
**And** if processing fails, message is moved to dead-letter queue after 3 retries

**Given** the query completes successfully
**When** the report is generated
**Then** SNS notification is published to report-complete topic
**And** subscribers receive notification: {query_id, report_id, user_id, status: "completed"}
**And** WebSocket clients are notified in real-time

**Given** the query fails
**When** an error occurs
**Then** SNS notification is published to query-failed topic
**And** operations team is alerted
**And** the user receives error notification via WebSocket

**Given** I want to scale workers
**When** query volume increases
**Then** ECS service auto-scaling launches additional worker tasks
**And** workers poll SQS and process queries in parallel
**And** each worker processes 1 query at a time (concurrency = 1 per worker)

**Technical Requirements:**
- SQS queues: intelligence-generation-queue, dead-letter-queue
- Queue configuration: visibility timeout = 600s (10 min), message retention = 4 days
- SNS topics: report-complete, query-failed
- Worker implementation: separate ECS task definition polling SQS
- Message format: {query_id, user_id, query_text, timestamp}
- Error handling: retry 3 times with exponential backoff, then DLQ

---

### Story 10.4: Caching Strategy with Redis for Performance

As a system,
I want intelligent caching with Redis,
So that repeated queries and common data are served instantly.

**Acceptance Criteria:**

**Given** a query is submitted
**When** checking for cached results
**Then** the system generates cache key: hash(query_text + user_subscription_tier + query_type)
**And** if cache hit, return cached report immediately (<100ms response)
**And** if cache miss, proceed with normal orchestration pipeline

**Given** a report is generated
**When** caching the result
**Then** the full report is stored in Redis with key: report:{cache_key}
**And** TTL is set to 24 hours (reports are valid for 1 day)
**And** cache size is monitored (evict least recently used if full)

**Given** KG query results are frequently accessed
**When** caching KG data
**Then** common queries are cached: get_market(geography, category), get_companies(market_id)
**And** TTL is 5 minutes (data is relatively fresh)
**And** cache key includes geography + category for uniqueness

**Given** user permissions are checked frequently
**When** validating permissions
**Then** subscription tier permissions are cached: permissions:{user_id}
**And** TTL is 5 minutes (permissions change infrequently)
**And** cache is invalidated when admin updates user subscription tier

**Given** cache is full
**When** Redis reaches maxmemory
**Then** allkeys-lru eviction policy removes least recently used keys
**And** critical data (e.g., user sessions) is preserved with longer TTL
**And** cache hit rate is monitored via CloudWatch

**Given** I want to invalidate cache
**When** data changes
**Then** KG updates trigger cache invalidation for affected geographies/categories
**And** admin permission changes invalidate affected user permission cache
**And** manual cache flush is available via operations dashboard

**Technical Requirements:**
- Redis client: aioredis for async operations
- Cache keys: namespaced (report:, kg:, permissions:)
- TTL: reports = 24h, KG = 5min, permissions = 5min
- Eviction: allkeys-lru policy
- Monitoring: cache hit rate, eviction rate via CloudWatch
- Invalidation: event-driven cache clearing on data updates

---

### Story 10.5: Rate Limiting and Abuse Prevention

As a system,
I want rate limiting to prevent abuse and ensure fair usage,
So that no single user can overwhelm the system.

**Acceptance Criteria:**

**Given** a user makes API requests
**When** rate limiting is enforced
**Then** users are limited to 100 queries per day
**And** users are limited to 5 concurrent queries at a time
**And** rate limits are tracked per user_id

**Given** a user exceeds their rate limit
**When** making additional requests
**Then** the API returns 429 Too Many Requests
**And** the response includes Retry-After header (seconds until reset)
**And** the error message explains: "Daily query limit reached (100 queries). Limit resets at midnight UTC."

**Given** rate limits are checked
**When** each request arrives
**Then** Redis tracks request counts: rate_limit:{user_id}:daily and rate_limit:{user_id}:concurrent
**And** rate limit check adds <10ms latency
**And** rate limit counters reset at appropriate intervals (daily at midnight, concurrent on query completion)

**Given** an admin user makes requests
**When** rate limiting is applied
**Then** admins have higher limits: 1000 queries/day, 20 concurrent
**And** operations users have unlimited queries for debugging

**Given** malicious behavior is detected
**When** a user attempts rapid-fire requests
**Then** the system implements exponential backoff after repeated 429s
**And** suspicious IPs are temporarily blocked (1-hour ban)
**And** operations team is alerted to investigate

**Technical Requirements:**
- Rate limiting: Redis with sliding window algorithm
- Limits: 100 queries/day per user, 5 concurrent per user
- Rate limit keys: rate_limit:{user_id}:daily (TTL 24h), rate_limit:{user_id}:concurrent (reset on completion)
- Response: 429 status, Retry-After header, clear error message
- Admin exemption: check role before applying limits
- Monitoring: track rate limit violations, alert on abuse patterns

---

### Story 10.6: Security Hardening (Encryption, SQL Injection, XSS Prevention)

As a system,
I want comprehensive security hardening,
So that the application is protected against common attacks.

**Acceptance Criteria:**

**Given** data is transmitted
**When** communicating between services
**Then** all connections use TLS 1.3 or higher
**And** ALB forces HTTPS redirection (HTTP → HTTPS)
**And** database connections use SSL (RDS requires SSL)
**And** Redis connections use TLS

**Given** data is stored
**When** persisting to databases
**Then** RDS encryption at rest is enabled (AWS KMS)
**And** ElastiCache encryption at rest is enabled
**And** S3 buckets use default encryption (AES-256)
**And** secrets are stored in AWS Secrets Manager (never in code or logs)

**Given** user input is received
**When** processing requests
**Then** all inputs are validated using Pydantic models
**And** SQL injection is prevented via parameterized queries (SQLAlchemy ORM)
**And** XSS is prevented: HTML output is escaped on frontend
**And** CSRF protection uses JWT tokens (stateless, no session cookies)

**Given** API endpoints are exposed
**When** handling requests
**Then** CORS is configured with specific allowed origins (no wildcard *)
**And** security headers are set: X-Content-Type-Options: nosniff, X-Frame-Options: DENY, Strict-Transport-Security
**And** rate limiting prevents brute force attacks

**Given** logging is implemented
**When** capturing logs
**Then** sensitive data is redacted: passwords, API keys, JWT tokens
**And** logs include correlation IDs for request tracing
**And** logs are structured JSON for easy parsing

**Given** dependencies are used
**When** maintaining the codebase
**Then** dependency scanning runs in CI/CD (Dependabot or Snyk)
**And** known vulnerabilities trigger alerts
**And** dependencies are updated regularly

**Technical Requirements:**
- TLS: enforce TLS 1.3 on ALB, RDS, ElastiCache
- Encryption: at rest (KMS) and in transit (TLS) for all data
- Input validation: Pydantic models for all API requests
- SQL injection prevention: SQLAlchemy ORM with parameterized queries
- XSS prevention: React auto-escapes, CSP headers on backend
- Security headers: Helmet.js equivalent for FastAPI
- Secrets management: AWS Secrets Manager, never hardcode
- Dependency scanning: Dependabot enabled, automated PRs

---

### Story 10.7: Health Checks and Graceful Degradation

As a system,
I want comprehensive health checks and graceful degradation,
So that failures in one component don't cascade to others.

**Acceptance Criteria:**

**Given** the system is running
**When** health checks execute
**Then** /api/health endpoint returns 200 OK if all dependencies are healthy
**And** health check validates: FastAPI process, RDS connection, Redis connection, Neo4j connection, Claude API access
**And** response includes status for each dependency: {database: "healthy", cache: "healthy", kg: "healthy", llm: "healthy"}

**Given** a dependency fails
**When** health check detects failure
**Then** /api/health returns 503 Service Unavailable
**And** response indicates which dependency failed: {database: "unhealthy", error: "Connection timeout"}
**And** ALB health checks detect failure and stop routing traffic to unhealthy tasks
**And** ECS launches replacement task automatically

**Given** Neo4j is temporarily unavailable
**When** a query requires KG data
**Then** the system retries Neo4j connection 3 times with backoff
**And** if all retries fail, returns user-friendly error: "Knowledge graph temporarily unavailable. Please try again in a few minutes."
**And** the query fails gracefully (no crash, no cascade)

**Given** Claude API is rate-limited
**When** making LLM requests
**Then** the system detects 429 rate limit responses
**And** implements exponential backoff (1s, 2s, 4s, 8s)
**And** if backoff exhausted, queues query for retry in 1 minute
**And** user is notified: "High demand detected. Your query is queued and will complete shortly."

**Given** visualization generation fails
**When** the Visualization Generator agent encounters error
**Then** the error is logged but not bubbled
**And** the report proceeds without visualizations
**And** the user sees message: "Visualizations unavailable for this report"
**And** the report is still functional and useful

**Given** quality score is <75% after 2 iterations
**When** iterative refinement fails
**Then** the report is flagged for human validator review
**And** the user sees message: "Your report is being reviewed by our team for quality assurance"
**And** the query does not fail (queued for manual review)

**Technical Requirements:**
- Health check endpoint: GET /api/health with dependency status
- Health check frequency: ECS checks every 30 seconds
- Retry logic: 3 attempts with exponential backoff for transient failures
- Circuit breaker pattern: open circuit after 5 consecutive failures, half-open after 1 minute
- Graceful degradation: visualizations optional, citations required, quality threshold enforced
- Error handling: try/except all external calls, return user-friendly messages

---

### Story 10.8: Performance Optimization and Monitoring

As a system,
I want optimized performance to meet <3 minute average response time,
So that users receive intelligence reports quickly.

**Acceptance Criteria:**

**Given** performance metrics are tracked
**When** monitoring the system
**Then** CloudWatch tracks: query_latency_avg, query_latency_p95, agent_execution_time, kg_query_time, llm_response_time
**And** metrics are visualized on operations dashboard
**And** historical trends are visible (30-day view)

**Given** query latency exceeds targets
**When** average response time >3 minutes
**Then** operations team is alerted via SNS
**And** the alert includes breakdown: which agent is slow, LLM vs KG bottleneck
**And** I can investigate specific slow queries via audit trail

**Given** KG queries are slow
**When** Cypher query latency >10 seconds
**Then** slow queries are logged with execution plan
**And** I can identify missing indexes or inefficient patterns
**And** I can add indexes to Neo4j to optimize

**Given** LLM API latency is high
**When** Claude API response time >30 seconds
**Then** the system logs slow LLM calls
**And** I can review prompts for optimization (reduce token count)
**And** I can consider caching common LLM responses

**Given** I want to optimize performance
**When** analyzing bottlenecks
**Then** I can use distributed tracing (future: X-Ray) to see request flow
**And** I can identify which service calls take longest
**And** I can optimize critical paths: parallelize agent calls, optimize KG queries, reduce LLM token usage

**Given** performance meets targets
**When** system is optimized
**Then** average query latency is <180 seconds (3 minutes)
**And** p95 latency is <240 seconds (4 minutes)
**And** 100+ concurrent queries process without degradation
**And** error rate remains <1%

**Technical Requirements:**
- CloudWatch custom metrics: query_latency, agent_execution_time, kg_query_time, llm_response_time
- Performance targets: avg <3 min, p95 <4 min, >100 concurrent, <1% errors
- Alerting: SNS alert if avg latency >3 min sustained for 10 minutes
- Slow query logging: log queries >5 min with full details
- Optimization: indexes on frequently queried KG properties, LLM prompt optimization, parallel agent execution where possible
- Monitoring: Prometheus + Grafana or CloudWatch dashboards

