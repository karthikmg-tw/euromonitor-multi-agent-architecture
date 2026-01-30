# Technical Architecture Brief for AI Intelligence Assistant
**Project:** Passport AI-Powered Intelligence Assistant for Euromonitor
**Prepared For:** Technical Architect
**Date:** 2026-01-12
**Source:** Brainstorming Session Analysis

---

## Executive Summary for Architect

**What We're Building:**
Multi-agentic AI system with knowledge graph that helps Passport users find and synthesize market intelligence through natural language queries. Three operational modes (Market Overview, Category Deep Dive, Regulatory Impact) with YAML-driven business rules.

**Your Key Decisions Needed:**
1. Knowledge graph technology stack confirmation
2. Multi-agent orchestration framework selection
3. Passport integration approach (APIs, auth, deployment)
4. Scalability and performance architecture
5. Quality validation framework implementation

---

## Technical Architecture Overview

### System Components

**1. Knowledge Graph Layer**
- **Purpose:** Store structured + unstructured Passport data for intelligent retrieval
- **Requirements:**
  - Preserve Passport taxonomy and data model
  - Enable cross-content retrieval ("connections current tools can't find")
  - Update strategy as Passport data refreshes (annual? quarterly?)
  - >95% coverage of Passport corpus
- **Questions for Architect:**
  - Graph DB choice? (Neo4j? Amazon Neptune? TigerGraph?)
  - Schema design approach?
  - Incremental update strategy vs full rebuild?
  - Performance targets (query latency)?

**2. Multi-Agent Orchestration**
- **Core Agents (All 3 Modes):**
  1. Query Interpreter - Mode detection, parameter extraction
  2. Data Retrieval - KG queries, Passport API calls
  3. Data Quality Validator - Completeness checks
  4. Narrative Synthesizer - LLM-based narrative generation
  5. Citation Specialist - Claim-level source attribution
  6. Visualization Generator - Charts, infographics
  7. Quality Scorer - Internal scoring framework
  8. Report Assembler - Final formatting

- **Mode-Specific Agents:**
  - Mode 2: Category Theme Detector (adaptive sections)
  - Mode 3: Regulatory Parser, Causal Analysis, Infographic Generator

- **Questions for Architect:**
  - Agent framework? (LangGraph? AutoGen? Custom?)
  - Agent communication protocol?
  - State management across agents?
  - Error handling and retry logic?
  - Observability and debugging strategy?

**3. YAML Business Rules Engine**
- **Purpose:** Strict enforcement of mode-specific requirements
- **Structure:** One YAML per mode + mode detection YAML
- **Content:** Data selection rules, required metrics, narrative structure, compliance rules, formatting rules
- **Questions for Architect:**
  - YAML parsing and validation library?
  - How to ensure LLM strictly follows YAML?
  - YAML version control and rollback?
  - How to test YAML changes don't break system?

**4. LLM Integration**
- **Use Cases:**
  - Narrative synthesis (main intelligence generation)
  - Insight generation (pattern highlighting)
  - Mode detection (query interpretation)
  - Adaptive section generation (Mode 2 category-specific content)

- **Questions for Architect:**
  - LLM provider? (Claude? GPT-4? Both?)
  - Fine-tuning strategy for Passport domain?
  - Cost management at scale (caching? prompt optimization?)
  - Fallback strategy if LLM unavailable?
  - How to prevent hallucination/ensure grounding in data?

**5. Passport Integration Layer**
- **Requirements:**
  - Read access to Passport data (structured + unstructured)
  - SSO integration (user authentication)
  - UI embedding (seamless user experience)
  - Citation links back to Passport sources

- **Questions for Architect:**
  - Passport API capabilities and limitations?
  - Authentication mechanism (OAuth? SAML? Other?)
  - Deployment model (SaaS? On-prem? Hybrid?)
  - Data residency and security requirements?
  - Rate limits and access patterns?

---

## Three Operational Modes (Business Logic)

### Mode 1: Market Overview Report
**Trigger:** Broad industry queries ("Soft drinks industry in France")
**Data:** Latest annual + 5-year forecast
**Output:** 5-section report, Top 5 companies/brands
**Special:** M&A activity, regulatory changes

### Mode 2: Category Deep Dive Report
**Trigger:** Specific category queries ("Bottled Water in Brazil")
**Data:** 5 years historical, packaging segmentation
**Output:** 5-section report with adaptive category-specific section
**Special:** Call-out boxes for key insights, top 3 focus (not 5)

### Mode 3: Regulatory Impact Brief
**Trigger:** Policy/regulation queries ("Sugar tax impact on UK soft drinks")
**Data:** 2 years before + 2 years after regulation
**Output:** 4-section report with before/after analysis
**Special:** Product attributes (sugar content), infographics, causal analysis disclaimers

**Key Architectural Note:**
- Modes are **independent workflows** (no interaction between modes)
- **Automatic mode detection** (no user selection)
- **No mid-conversation mode switching** (mode runs to completion)

---

## Data Flow Architecture

```
User Query
    ↓
Mode Detection (YAML rules + LLM)
    ↓
Query Interpreter Agent (extract params: geography, category, etc.)
    ↓
Data Retrieval Agent → Knowledge Graph + Passport APIs
    ↓
Data Quality Validator (check completeness per mode YAML)
    ↓
[Mode-Specific Processing]
    ↓
    ├─ Narrative Synthesizer (LLM + YAML template)
    ├─ Citation Specialist (source attribution)
    └─ Visualization Generator (charts per mode)
    ↓
Quality Scorer (validate against scoring rubric)
    ↓
    If score < threshold → Iterate (feedback to Synthesizer)
    If score >= threshold → Continue
    ↓
Report Assembler (format, branding, compliance)
    ↓
Present to User (UI with citations, charts, narrative)
```

---

## Technical Requirements

### Performance Targets
- **Response Time:** <5 minutes for typical query (end-to-end)
- **Concurrent Users:** Support 100+ concurrent queries
- **Uptime:** 99.5% SLA
- **Error Rate:** <1% of queries fail or produce low-quality output

### Scalability Requirements
- **Daily Query Volume:** 500+ queries (at launch), 2000+ (6 months post-launch)
- **Knowledge Graph Size:** Full Passport corpus (~TBs of data?)
- **Agent Processing:** Parallel where possible, sequential where dependencies exist

### Quality Requirements
- **Citation Accuracy:** 100% of citations must link to valid Passport sources
- **Quality Score:** >75% on internal rubric before presentation
- **Mode Detection Accuracy:** >85% correct mode classification
- **Data Coverage:** >95% of Passport data accessible via KG

### Security & Compliance
- **Data Access:** User can only access Passport data their subscription allows
- **Audit Trail:** Log all queries, results, and user actions
- **Data Residency:** Respect EM's data residency requirements
- **PII Handling:** No user data leakage between sessions

---

## Technology Stack Considerations

**Proposed (Needs Architect Validation):**

| Component | Technology Options | Decision Needed |
|-----------|-------------------|-----------------|
| **Knowledge Graph** | Neo4j / Amazon Neptune / TigerGraph | ? |
| **Vector DB** | Pinecone / Weaviate / Qdrant | ? |
| **LLM** | Claude 3.5 Sonnet / GPT-4 / Both | ? |
| **Agent Framework** | LangGraph / AutoGen / Custom | ? |
| **Backend** | Python (FastAPI) / Node.js | ? |
| **Frontend** | React / Vue / Embed in Passport UI | ? |
| **Orchestration** | Kubernetes / AWS ECS / Other | ? |
| **Monitoring** | Datadog / New Relic / Prometheus | ? |
| **CI/CD** | GitHub Actions / GitLab CI / Jenkins | ? |

---

## Critical Technical Risks

### Risk 1: Knowledge Graph Quality
**Issue:** If KG has gaps or errors, entire system outputs are compromised
**Mitigation:**
- Comprehensive data validation pipeline during KG construction
- Ongoing quality metrics dashboard
- Incremental validation with EM domain experts

### Risk 2: Multi-Agent Coordination Failures
**Issue:** Agent failures cascade, context lost, system produces incomplete output
**Mitigation:**
- Robust error handling at each agent
- State persistence (resume from failure point)
- Comprehensive logging and observability
- Circuit breaker patterns

### Risk 3: LLM Hallucination (Sophisticated Nonsense)
**Issue:** LLM generates plausible but incorrect analysis
**Mitigation:**
- Strict grounding in Passport data (RAG approach)
- YAML constraints limit LLM creativity to safe zones
- Citation requirement forces data linkage
- Quality scoring with iterative refinement
- Human validation as final gate

### Risk 4: Performance at Scale
**Issue:** System too slow with many concurrent users or complex queries
**Mitigation:**
- Caching strategies (common queries, KG results)
- Async processing where possible
- Load testing early and often
- Horizontal scaling architecture

### Risk 5: Integration Complexity
**Issue:** Passport APIs limited, auth complex, deployment constraints
**Mitigation:**
- Early technical discovery with EM IT team
- Phased integration (read-only → full integration)
- Fallback strategies if APIs insufficient
- Close collaboration with Passport engineering

---

## Implementation Phases (Technical Focus)

### Phase 1: Foundation (Months 1-2)
**Architect Leads:**
- KG schema design and technology selection
- Multi-agent framework selection and setup
- YAML engine design
- Integration architecture with Passport

**Deliverables:**
- Architecture decision records (ADRs)
- System design document
- PoC: Basic KG query + single agent
- Technical risk assessment

### Phase 2: Mode 1 PoC (Months 3-4)
**Architect Oversees:**
- Full agent orchestration for Mode 1
- KG construction from Passport data
- LLM integration and prompt engineering
- Quality scoring implementation

**Deliverables:**
- Working Mode 1 end-to-end
- Performance benchmarks
- Quality metrics baseline

### Phase 3-6: Scale, Complete, Launch
**Architect Focuses:**
- Modes 2 & 3 reuse of Mode 1 architecture
- Performance optimization
- Security hardening
- Production infrastructure
- Monitoring and alerting

---

## Questions for Architect Discussion

**Immediate (This Week):**
1. Do you agree with KG approach, or prefer alternative (vector DB only, hybrid)?
2. What agent framework do you recommend?
3. What are Passport API capabilities - have you reviewed docs?
4. What's our development environment setup?

**Short-term (Next 2 Weeks):**
5. How do we enforce YAML rules strictly on LLM output?
6. What's the data sync strategy (Passport → KG)?
7. What observability tools for debugging multi-agent flows?
8. How do we test quality at scale (thousands of query variations)?

**Medium-term (Month 1):**
9. What's the deployment architecture (cloud provider, regions)?
10. How do we handle model updates (Claude 3.5 → 4.0)?
11. What's the disaster recovery and backup strategy?
12. How do we measure and optimize cost (LLM calls, infra)?

---

## Next Steps

**For Architect:**
1. Review this brief (30-60 min)
2. Review full brainstorming document if desired (sections 5 & 7 most relevant)
3. Schedule technical design session (2-3 hours)
4. Begin drafting technical design document
5. Create ADRs for key technology choices

**For Team:**
1. Architect presents proposed architecture to team
2. Team provides feedback and identifies gaps
3. Begin Phase 1 technical discovery
4. Set up development environment

---

## Reference Documents

- **Full Brainstorming Session:** `_bmad-output/analysis/brainstorming-session-2026-01-12.md`
- **YAML Specifications (Detailed):** See Section 5 of brainstorming doc
- **Implementation Roadmap:** See Section 7 of brainstorming doc

---

**This brief contains the technical essence for architectural decision-making. The full brainstorming document has additional context on user needs, business value, and risks if needed.**
