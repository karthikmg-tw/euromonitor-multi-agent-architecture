---
stepsCompleted: [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
inputDocuments:
  - '_bmad-output/analysis/architect-technical-brief.md'
  - 'docs/brainstorming-session-2026-01-10.md'
  - '_bmad-output/analysis/brainstorming-session-2026-01-12.md'
briefCount: 1
researchCount: 0
brainstormingCount: 2
projectDocsCount: 0
workflowType: 'prd'
lastStep: 11
completed: true
completedDate: '2026-01-21'
lastUpdated: '2026-01-21'
phaseSegregation: true
phaseSegregationDate: '2026-01-21'
mvpRequirements: 48
growthRequirements: 21
visionRequirements: 2
---

# Product Requirements Document - euromonitor-multi-agent-architecture

**Author:** Karthikmg
**Date:** 2026-01-21

## Executive Summary

**Product Name:** Passport AI-Powered Intelligence Assistant

**Vision:** Transform how Euromonitor Passport customers access and synthesize market intelligence by providing a multi-agentic AI system that delivers analyst-grade narratives through natural language interaction, reducing analysis time from days to minutes while maintaining claim-level transparency and trust.

**The Problem:** Passport customers, especially non-experts or infrequent users, struggle to find the right data, dashboards, or reports within Passport's extensive database. Manual navigation is time-consuming, requires specialist knowledge, and current tools cannot make cross-content connections or synthesize insights into narrative intelligence.

**The Solution:** Multi-agentic AI system with knowledge graph that enables natural language queries and delivers three distinct types of intelligence reports: Market Overview Reports, Category Deep Dive Reports, and Regulatory Impact Briefs. Each mode operates with YAML-driven business rules ensuring predictable, high-quality outputs with full citation transparency.

**Target Users:** Euromonitor Passport customers including market intelligence analysts, category managers, strategy teams, and executives who need fast, narrative-driven insights from complex market data without becoming Passport navigation experts.

**Core Value Proposition:**
- **Speed:** Analysis-grade narratives in minutes instead of days
- **Accessibility:** Non-experts can access insights previously requiring specialist Passport knowledge
- **Trust:** Claim-level citations to Passport sources enable complete verification
- **Quality:** Internal scoring framework with >75% threshold ensures analyst-grade output
- **Intelligence:** Cross-content retrieval finds connections current tools can't discover

### What Makes This Special

**1. Multi-Agent Architecture with Knowledge Graph**
Eight core agents orchestrate the intelligence generation process, working from a knowledge graph built from structured and unstructured Passport data. This enables cross-content retrieval and connections that current Passport tools cannot find, preserving Passport taxonomy while enabling semantic search across the entire corpus.

**2. YAML-Driven Business Rules Engine**
Each operational mode is governed by strict YAML specifications that define data selection rules, required metrics, narrative structure, compliance requirements, and formatting standards. The LLM has constrained dynamism - creative within guardrails - making outputs predictable, testable, and maintainable.

**3. Three Distinct Operational Modes**
- **Mode 1: Market Overview Report** - Broad industry intelligence with 5-year forecast, top 5 competitors, regulatory changes
- **Mode 2: Category Deep Dive Report** - Focused category strategy with 5-year historical data, adaptive category-specific sections, top 3 focus
- **Mode 3: Regulatory Impact Brief** - Before/after policy analysis with 2+2 year windows, causal analysis, regulatory infographics

Automatic mode detection from query structure with no mid-conversation mode switching ensures focused, complete intelligence delivery.

**4. Claim-Level Citations with Transparency**
Every statement in generated intelligence is traceable to specific Passport source data with report title and date. Users can drill into source material immediately, building trust through complete verifiability. Citation accuracy requirement: 100%.

**5. Quality Scoring Framework**
Multi-dimensional internal rubric validates completeness, citation quality, insight depth, coherence, and forecast quality before presenting to users. Minimum quality threshold of 75% required; below threshold triggers iterative refinement. Human validation remains the final gate.

**6. Narrative-First Intelligence Synthesis**
Unlike traditional tools that provide raw data dumps, this system transforms Passport data into analyst-grade intelligence narratives with clear structure, visual elements, and actionable insights - matching the quality of elite human analyst teams.

## Project Classification

**Technical Type:** SaaS B2B Platform
**Domain:** Scientific/Research Intelligence
**Complexity:** Medium
**Project Context:** Greenfield - new project

**Classification Rationale:**

This is a SaaS B2B platform designed for enterprise Passport customers with multi-tenant considerations, SSO integration, subscription-based data access controls, and embedded UI deployment within the existing Passport ecosystem.

The domain classification as "Scientific/Research Intelligence" reflects the system's focus on research data synthesis, computational analysis methodology (knowledge graph, vector search), validation requirements (quality scoring, citation accuracy), and reproducibility concerns (transparent citations, explainable reasoning). While focused on business intelligence rather than academic research, the methodological rigor and validation frameworks align with scientific computing practices.

Medium complexity accounts for the need for robust validation methodology, accuracy metrics, performance requirements (<5 min response time, >95% data coverage), and quality assurance frameworks, while being less regulated than healthcare or fintech domains.

## Success Criteria

### User Success

**Primary Success Outcomes:**
- **100x Speed Improvement:** Analysts complete intelligence gathering in hours instead of weeks (traditional 6-8 weeks → AI-assisted 3-5 days or minutes for initial drafts)
- **Accessibility for Non-Experts:** Non-expert Passport users can access insights previously requiring specialist knowledge and extensive database navigation experience
- **Trust and Confidence:** Users trust AI-generated intelligence enough to act on it, validated through human-in-the-loop workflow where analysts review and refine outputs
- **Discovery of Hidden Connections:** Users experience "aha!" moments through cross-content retrieval that finds connections current Passport tools cannot discover

**User Experience Indicators:**
- Task completion rate: Users successfully get answers to their intelligence queries
- Time saved per query vs traditional Passport navigation measured and reported
- Follow-up question rate indicates clarity of initial responses
- Return user rate (% who use it multiple times) demonstrates sustained value
- Users report feeling "this was worth it" through satisfaction surveys

### Business Success

**Launch Metrics (3 Months):**
- **User Adoption:** >40% of Passport users actively using AI assistant
- **Query Volume:** 500+ daily queries across all modes
- **Concurrent Capacity:** System handles 100+ concurrent users without degradation

**Growth Metrics (6 Months):**
- **Query Volume Growth:** 2000+ daily queries (4x launch volume)
- **Productivity Gains:** Measurable reports-per-analyst productivity multiplier
- **Customer Retention:** Positive impact on Passport renewal rates

**Steady State (12 Months):**
- AI assistant is standard feature in Passport ecosystem
- Customer satisfaction score >4.0/5.0
- Support ticket reduction through successful self-service
- Premium pricing justification validated through customer feedback

**Key Business Indicators:**
- User adoption rate (% of Passport users actively engaging)
- Query volume trends (daily/weekly/monthly growth)
- Customer retention impact (Passport subscription renewals)
- Support efficiency (ticket reduction, self-service success)
- NPS score >40 indicating strong user satisfaction

### Technical Success

**Performance Requirements:**
- **Response Time:** <5 minutes average for typical query (end-to-end report generation)
- **Error Rate:** <1% of queries fail or produce low-quality output
- **Uptime:** 99.5% SLA met consistently
- **Concurrent Scale:** 100+ concurrent queries supported without performance degradation

**Quality Requirements:**
- **Quality Score:** >75% on internal rubric before presentation to users
- **Citation Accuracy:** 100% of citations correctly link to valid Passport sources
- **Mode Detection:** >85% accuracy in automatically classifying queries into correct mode
- **Data Coverage:** >95% of Passport corpus accessible via knowledge graph
- **Expert Validation:** High pass rate when outputs reviewed by senior analysts

**System Reliability:**
- Knowledge graph construction complete with >95% Passport data coverage
- Multi-agent orchestration working reliably end-to-end across all modes
- YAML business rules enforced strictly (no LLM hallucination outside guardrails)
- All 3 operational modes tested and validated
- Passport integration working seamlessly (SSO, APIs, UI embedding)

### Measurable Outcomes

**At 3 Months Post-Launch:**
- 40%+ Passport users have tried the AI assistant
- 500+ daily queries with <1% error rate
- Average response time <5 minutes
- User satisfaction score >4.0/5.0

**At 6 Months Post-Launch:**
- 2000+ daily queries (4x growth)
- Proven productivity multiplier (analysts generating 5-10x more intelligence reports)
- Measurable impact on Passport customer retention
- Quality metrics consistently above thresholds

**At 12 Months Post-Launch:**
- AI assistant is standard Passport capability
- Continued query volume growth
- Established track record of quality and reliability
- Validated business case for continued investment and expansion

## Product Scope

### MVP - Minimum Viable Product (Phase 1-2: Months 1-4)

**What Must Work:**
- **Knowledge Graph Foundation:** Constructed from Passport structured + unstructured data with >95% corpus coverage
- **Mode 1 Operational:** Market Overview Report fully functional end-to-end
- **Core Agent System:** All 8 core agents orchestrating successfully for Mode 1
- **Basic UI:** Search bar interface, narrative display with formatting, citation links to Passport sources
- **Quality Framework:** Internal scoring rubric operational with minimum 75% threshold enforcement
- **YAML Rules Engine:** Mode 1 business rules defined and enforced
- **Passport Integration:** Basic API access, authentication working

**MVP Success Criteria:**
- Mode 1 generates analyst-grade market overviews
- Quality score consistently >0.75
- Response time <5 minutes
- Citations 100% accurate
- 5+ diverse test cases validated by EM analysts

### Growth Features (Phase 3-4: Months 5-9)

**What Makes It Competitive:**
- **Modes 2 & 3 Complete:** Category Deep Dive and Regulatory Impact Brief operational
- **Mode Detection System:** Automatic query classification with >85% accuracy
- **Enhanced UI:** Multi-turn conversation with memory, follow-up questions, coverage cues
- **Visualization Suite:** Mode-specific charts, infographics, before/after comparisons
- **Export Capabilities:** PDF and PPTX export options
- **Beta Testing:** 10-20 Passport users providing real-world validation
- **Iterative Refinement:** User feedback incorporated into quality improvements

**Growth Phase Success Criteria:**
- All 3 modes passing 10+ diverse test cases each
- Mode detection accuracy >85%
- Beta users reporting 80%+ positive experience
- User adoption rate >60% among beta group

### Vision (Phase 5-6: Months 10-12+)

**Dream Version Capabilities:**
- **Full Rollout:** Available to entire Passport customer base
- **Advanced Features:** Additional report modes based on user feedback
- **Enhanced Visualizations:** Interactive charts, customizable templates
- **Collaborative Features:** Sharing, commenting, team workspaces
- **API Access:** Power users can integrate with their own tools
- **Model Fine-Tuning:** LLM optimized specifically for Passport domain
- **Continuous Improvement:** Regular KG updates, quality metric improvements, faster response times
- **Analytics Dashboard:** User behavior analysis, popular query patterns, quality metrics tracking

**Vision Phase Success Criteria:**
- Continuous month-over-month user growth
- Quality metrics improving quarter-over-quarter
- New feature adoption >30%
- Reduced support ticket volume (self-service success)
- Established as competitive differentiator for Euromonitor Passport

## User Journeys

### Journey 1: Sarah Chen - The Overwhelmed Market Analyst Racing Against Deadlines

Sarah is a market intelligence analyst at a Fortune 500 beverage company. Her VP of Strategy just asked for a comprehensive soft drinks market analysis for France - covering market size, competitive landscape, regulatory changes, and 5-year forecasts. She has 2 days. Using traditional Passport navigation, this would take her at least a week: finding the right datasets, cross-referencing reports, building tables manually, checking citations, creating charts, and writing the narrative synthesis.

At 9 AM Monday, instead of spending hours navigating Passport's database structure, Sarah types into the AI assistant: "Soft drinks industry in France." Within 4 minutes, she receives a complete Market Overview Report with executive summary, key drivers and inhibitors, competitive landscape with top 5 players including recent M&A activity, regulatory changes impacting the market, and full 5-year forecast - all with claim-level citations linking back to specific Passport datasets.

Sarah spends the next few hours validating the AI output (her training as an analyst makes her skeptical), clicking through citations to verify sources, and adding her own judgment calls on market dynamics. The breakthrough comes when she discovers a connection between two regulatory changes that the AI surfaced from different Passport reports - something she would have missed in manual navigation. By Tuesday morning, she delivers a boardroom-ready intelligence report that impresses her VP. Three months later, Sarah is generating 10x more analysis than before, spending 80% of her time on strategic synthesis instead of data hunting.

### Journey 2: Miguel Rodriguez - The Category Manager Without Passport Expertise

Miguel recently joined a consumer goods company as Category Manager for Bottled Water in Brazil. He's an operations expert, not a market research specialist. His CEO wants to understand packaging trends and sustainability impacts before making a $50M investment decision. Miguel has a Passport subscription but feels lost - he doesn't know which reports to read, which metrics matter, or how to synthesize data into strategic recommendations. The last time he tried navigating Passport, he spent 3 frustrating hours and still couldn't find what he needed.

On Monday afternoon, feeling desperate, Miguel asks the AI assistant: "Bottled Water in Brazil - packaging and sustainability trends." The system detects this as Mode 2 (Category Deep Dive) and within 5 minutes generates a focused report with 5 years of historical data, packaging segmentation (PET vs glass vs bulk), an adaptive section specifically on "Packaging and Sustainability Trends" (generated because the AI detected the category), top 3 brands analysis, and call-out boxes highlighting key insights about the shift toward recycled PET materials.

Miguel can't believe it. He clicks through the citations to verify - everything links back to legitimate Passport datasets he would never have known existed. He adds his operational perspective on supply chain implications and presents to the CEO the next day. The CEO is impressed by Miguel's "deep Passport expertise." Miguel smiles, knowing the AI made him look like a market research pro. He becomes a power user, running 20+ category analyses over the next quarter that inform strategic decisions across the portfolio.

### Journey 3: Dr. Priya Kapoor - The Senior Analyst Validating AI Outputs

Dr. Kapoor is a 15-year veteran analyst who's seen every market research fad come and go. She's skeptical of AI "magic" but intrigued by the potential productivity gains. Her firm has designated her as the quality validator - all AI-generated intelligence must pass through her review before being used in client recommendations. She's looking for hallucinations, weak citations, logical gaps, and "sophisticated nonsense."

Tuesday morning, she receives an AI-generated Regulatory Impact Brief analyzing the sugar tax impact on UK soft drinks. She immediately dives into adversarial validation mode: clicking every single citation to verify sources, checking if the before/after data windows are actually 2+2 years as specified, examining whether the causal analysis disclaimers are appropriate (correlation ≠ causation), and scrutinizing the product attribute data (sugar content per liter).

The citations are rock solid - every claim links to specific Passport datasets with report titles and dates. The data quality validator agent flagged coverage gaps where Passport data was incomplete. The quality score was 82% (above the 75% threshold). But Dr. Kapoor finds an issue: the AI narrative overstated causality between the tax and consumption decline without acknowledging confounding factors like the pandemic timing. She rejects the output with specific feedback.

The system learns. The next version includes more conservative language around causality and adds pandemic context from adjacent Passport data. Dr. Kapoor approves it with minor edits. Over the next six months, she notices the AI quality improving as the system learns from her validations. She transitions from full adversarial review to spot-checking, trusting the system's quality framework. Her team is now generating 5x more intelligence while maintaining the high standards she's known for.

### Journey 4: James Kim - The System Administrator Managing Access

James is the IT administrator at Euromonitor responsible for managing the Passport AI Assistant rollout. He needs to configure SSO integration, set up subscription-based data access controls (users can only access Passport data their subscription allows), manage the beta testing group, and ensure audit trails capture all queries and results for compliance.

On Monday, James logs into the admin dashboard to configure the first batch of 20 beta users. He maps each user's Passport subscription tier to their AI assistant permissions, ensuring analysts can only generate reports for geographies and categories they're authorized to access. He enables SSO using the company's existing authentication system and sets up audit logging to capture every query, mode detection, data retrieval, and report generation for compliance tracking.

During beta testing, a user reports that they can't access data for a specific region. James checks the audit trail, sees the permission denial was correct based on their subscription tier, and explains the situation. Another user asks about data residency - James confirms all queries and generated reports stay within the designated geographic region per EM's data residency requirements. When security wants a report on usage patterns, James exports the audit logs showing 500+ queries in the first week with <1% error rate.

### Journey 5: Lisa Yamamoto - The Support Engineer Troubleshooting Quality Issues

Lisa works on EM's operations team supporting the Passport AI Assistant. At 2 PM, she receives an escalation: an analyst reported that a Mode 1 Market Overview Report had a citation that linked to a broken Passport dataset. This is a critical quality issue - 100% citation accuracy is non-negotiable.

Lisa logs into the operations dashboard and pulls up the specific query from the audit trail. She can see the complete agent orchestration flow: query interpretation, mode detection (Mode 1, confidence 0.92), data retrieval agent queries, citation specialist attributions, and quality scorer results (78%). She identifies the issue - the knowledge graph had stale metadata pointing to a Passport dataset that was recently deprecated and moved.

She flags the KG issue for the data team to fix, manually updates the citation in the affected report, and notifies the user. She also runs a sweep to find other reports potentially affected by the same stale metadata issue (finds 3 more). Within 2 hours, all affected citations are corrected. She documents the incident and adds a check to the data validation pipeline to catch deprecated dataset references before they make it into the knowledge graph.

### Journey Requirements Summary

**Core User Experience Capabilities:**
- Natural language query interface (ChatGPT-style search bar)
- <5 minute response time for typical queries
- Three operational modes with automatic mode detection (>85% accuracy)
- Claim-level citations with direct links to Passport sources (100% accuracy)
- Quality scoring framework with >75% threshold enforcement
- Cross-content retrieval finding hidden connections
- Export capabilities (PDF, PPTX) for presentations

**Mode-Specific Capabilities:**
- **Mode 1 (Market Overview):** 5-year forecast, top 5 competitors, regulatory changes, M&A activity
- **Mode 2 (Category Deep Dive):** 5-year historical data, adaptive category-specific sections, call-out boxes, packaging/segmentation analysis, top 3 focus
- **Mode 3 (Regulatory Impact):** 2+2 year before/after windows, causal analysis disclaimers, product attribute tracking, regulatory infographics

**Validation & Quality Capabilities:**
- Human-in-the-loop validation workflow
- Quality score visibility for validators
- Iterative refinement based on human feedback
- Coverage gap flagging when Passport data incomplete
- Ability to reject outputs with feedback
- Track record building over time

**Administrative & Operational Capabilities:**
- Admin dashboard for user management
- SSO integration with enterprise authentication
- Subscription-based data access controls (fine-grained permissions by geography/category)
- Audit trail logging (all queries, results, user actions, mode detection)
- User provisioning and beta group management
- Data residency compliance configuration
- Usage reporting and analytics

**Support & Maintenance Capabilities:**
- Operations dashboard with query audit trail visibility
- Agent orchestration flow visibility for debugging
- Quality score and validation results access
- Knowledge graph maintenance tools
- Citation accuracy monitoring and alerting
- Incident investigation capabilities
- Data validation pipeline integration
- User notification system for issue resolution

## Innovation & Novel Patterns

### Detected Innovation Areas

**1. YAML-Driven LLM Constraint Architecture**

The use of YAML business rules to constrain LLM creativity represents a novel approach to making AI outputs predictable, testable, and maintainable in enterprise settings. Rather than relying on prompt engineering alone, each operational mode has strict YAML specifications defining data selection rules, required metrics, narrative structure, and compliance requirements. This creates "constrained dynamism" - the LLM is creative within strict guardrails, solving the enterprise trust problem of unpredictable AI behavior.

**Innovation Insight:** Most AI intelligence tools struggle with consistency and predictability. By treating YAML as source of truth and validating LLM output against schema, this approach makes AI behavior deterministic enough for enterprise decision-making while maintaining the natural language benefits.

**2. Multi-Agent Orchestration for Business Intelligence Synthesis**

The application of multi-agent architecture (8 core agents + mode-specific agents) to market intelligence generation is uncommon in the business intelligence space. The orchestration includes Query Interpreter, Data Retrieval, Data Quality Validator, Narrative Synthesizer, Citation Specialist, Visualization Generator, Quality Scorer, and Report Assembler working in coordination. Each agent has specialized responsibility, with state management and error handling across the pipeline.

**Innovation Insight:** Traditional BI tools provide data access; this system provides intelligence synthesis. The multi-agent approach enables sophisticated reasoning workflows (quality validation → iterative refinement → human validation) that single-LLM architectures cannot achieve reliably.

**3. Mode-Based Intelligence Routing with Automatic Detection**

Three independent operational modes (Market Overview, Category Deep Dive, Regulatory Impact) with automatic mode detection from query structure represents a unique UX pattern. Unlike conversational AI that tries to handle all queries flexibly, this system routes queries to specialized workflows with no mid-conversation mode switching. Each mode has its own YAML rules, agent configurations, and quality thresholds.

**Innovation Insight:** By designing independent modes rather than flexible conversation, the system achieves higher quality and predictability. The mode detection confidence threshold (>0.85) with clarification flows when uncertain balances automation with user control.

**4. Knowledge Graph + Vector Search Hybrid for Cross-Content Intelligence**

The combination of knowledge graph (preserving Passport taxonomy and structured relationships) with vector search (semantic retrieval across unstructured content) enables "cross-content retrieval that finds connections current tools can't." The KG maintains data lineage and citation accuracy while vector embeddings enable semantic similarity discovery across the entire Passport corpus.

**Innovation Insight:** Most BI tools are either structured (SQL queries) or unstructured (semantic search). This hybrid approach maintains the rigor of structured data while unlocking the discovery potential of semantic search, enabling analysts to find non-obvious connections.

**5. Claim-Level Citation System for AI Transparency**

Requiring 100% citation accuracy where every statement in generated intelligence is traceable to specific Passport source data with report title and date raises the bar for AI transparency. The Citation Specialist agent operates as part of the orchestration pipeline, ensuring no narrative content is presented without verifiable sourcing.

**Innovation Insight:** Most AI tools provide general citations or disclaimers. This claim-level attribution enables true verification - analysts can drill into every assertion to validate the underlying data, building trust through complete transparency rather than asking users to "trust the AI."

### Market Context & Competitive Landscape

**Current Market State:**

The business intelligence AI tool market is rapidly evolving with multiple players attempting to make data more accessible through natural language interfaces. However, most solutions fall into two categories:

1. **Conversational BI Tools** (e.g., ThoughtSpot, Mode Analytics with AI features) - Focus on flexible natural language queries but struggle with consistency and enterprise trust due to unpredictable outputs

2. **AI-Augmented Research Platforms** (e.g., Gartner's AI features, CB Insights) - Provide AI-generated summaries but lack the deep integration with proprietary data sources and quality validation frameworks

**Competitive Differentiation:**

The Passport AI Intelligence Assistant differentiates through:

- **Predictability through YAML-driven constraints** - Enterprise-grade consistency competitors lack
- **Multi-agent quality assurance** - Quality scoring with iterative refinement before presentation
- **Mode-based specialization** - Optimized workflows rather than "one size fits all" flexibility
- **Knowledge graph foundation** - Deep integration with Passport's proprietary taxonomy and data model
- **Claim-level transparency** - Every assertion verifiable, not just general citations

**Market Timing:**

The market is ready for sophisticated AI intelligence tools, but enterprise adoption has been held back by trust and consistency concerns. The YAML-constraint innovation directly addresses the primary barrier to enterprise adoption.

### Validation Approach

**Technical Validation:**

1. **YAML Schema Enforcement Testing**
   - Validate that LLM outputs strictly conform to YAML specifications
   - Test edge cases where LLM might deviate from rules
   - Measure compliance rate across diverse queries (target: >95% YAML compliance)

2. **Multi-Agent Pipeline Reliability**
   - Test agent orchestration under concurrent load (100+ queries)
   - Validate error handling and retry logic across agent failures
   - Measure end-to-end success rate (target: <1% pipeline failures)

3. **Knowledge Graph + Vector Search Performance**
   - Validate cross-content retrieval finds relevant connections (precision/recall metrics)
   - Test against manually curated "ground truth" connection examples
   - Measure query response time at scale (target: <5 minutes)

4. **Mode Detection Accuracy**
   - Test with diverse query corpus (500+ queries across all modes)
   - Measure mode detection accuracy (target: >85%)
   - Validate clarification flow triggers appropriately for ambiguous queries

5. **Citation Accuracy Validation**
   - Audit random sample of generated intelligence for citation correctness
   - Verify 100% of citations link to valid Passport sources
   - Test against dataset deprecation scenarios

**Business Validation:**

1. **Beta Testing with Real Analysts (Phase 4)**
   - 10-20 Passport users across different expertise levels
   - Measure adoption rate, task completion, time saved vs traditional navigation
   - Collect qualitative feedback on trust, quality, and usability

2. **Human Validation Study**
   - Senior analysts compare AI-generated intelligence to human-generated reports
   - Blind quality assessment - can experts distinguish AI vs human outputs?
   - Measure validation pass rate (target: >75% quality score)

3. **Productivity Multiplier Evidence**
   - Track reports-per-analyst before and after AI assistant adoption
   - Document specific use cases where analysts achieved 5-10x productivity gains
   - Measure time allocation shift (data hunting → strategic synthesis)

**Market Validation:**

1. **User Adoption Metrics (Phase 5)**
   - Track adoption rate among Passport user base (target: >40% in 3 months)
   - Monitor query volume growth (500+ → 2000+ daily queries in 6 months)
   - Measure return user rate and NPS scores

2. **Customer Retention Impact**
   - Correlate AI assistant usage with Passport renewal rates
   - Track customer satisfaction improvements
   - Document premium pricing justification validation

### Risk Mitigation

**Innovation Risk 1: YAML-Driven Constraints May Be Too Rigid**

**Risk:** YAML rules might over-constrain LLM, producing formulaic outputs that lack insight quality or fail to adapt to diverse user needs.

**Mitigation:**
- Iterative YAML refinement during beta testing based on user feedback
- LLM has flexibility within guardrails for narrative synthesis and insight generation
- Mode-specific YAML allows customization per intelligence type
- Fallback: If rigidity proves problematic, expand "allowed flexibility" zones in YAML while maintaining core structural requirements

**Innovation Risk 2: Multi-Agent Orchestration Complexity Creates Reliability Issues**

**Risk:** 8-agent pipeline with state management could have cascading failures, making system unreliable at scale.

**Mitigation:**
- Comprehensive error handling and retry logic at each agent
- Circuit breaker patterns to prevent cascade failures
- State persistence for resumable workflows after failures
- Extensive load testing before production launch (100+ concurrent users)
- Monitoring and alerting on agent-level health metrics
- Fallback: Implement simpler pipeline with fewer agents if orchestration proves too complex

**Innovation Risk 3: Mode Detection Accuracy Insufficient for Good UX**

**Risk:** If mode detection confidence is frequently <0.85, users will be annoyed by constant clarification questions.

**Mitigation:**
- Train mode detection with diverse query corpus (500+ examples)
- Implement confidence threshold tuning based on real usage patterns
- Clarification questions are quick and conversational, not punitive
- User can explicitly specify mode if they prefer
- Fallback: Provide mode selection UI as alternative to automatic detection

**Innovation Risk 4: Knowledge Graph Quality Degrades Over Time**

**Risk:** As Passport data changes (datasets deprecated, new data added), KG could have stale metadata leading to broken citations.

**Mitigation:**
- Automated KG update pipeline synced with Passport data refresh cycles
- Data validation checks during KG construction and updates
- Citation accuracy monitoring with automated alerts on broken links
- Incident response process to quickly fix stale metadata issues (demonstrated in Lisa's journey)
- Fallback: Manual KG maintenance with dedicated data team support

**Innovation Risk 5: Enterprise Users Don't Trust "Black Box" AI Despite Transparency**

**Risk:** Even with claim-level citations, skeptical enterprise users might not adopt due to general AI distrust.

**Mitigation:**
- Human-in-the-loop validation workflow positions AI as assistant, not replacement
- Quality score visibility lets validators see AI's self-assessment
- Track record building over time demonstrates reliability
- Senior analyst validators serve as trust bridges to broader organization
- Extensive beta testing with early adopters who provide testimonials
- Fallback: Position as "analyst productivity tool" rather than "AI intelligence generator"

**Innovation Risk 6: Competitive Response from Established Players**

**Risk:** Competitors (ThoughtSpot, Gartner) could quickly copy YAML-constraint approach or multi-agent architecture.

**Mitigation:**
- First-mover advantage with deep Passport integration
- Continuous improvement and feature velocity
- Build switching costs through user habit formation and workflow integration
- Focus on execution excellence and quality rather than feature announcements
- Euromonitor's brand and customer relationships provide competitive moat
- Fallback: Compete on quality, reliability, and customer success rather than novelty alone

## SaaS B2B Platform Specific Requirements

### Project-Type Overview

The Passport AI Intelligence Assistant is a SaaS B2B platform deployed within the Euromonitor Passport ecosystem. It serves enterprise customers (Fortune 500 companies, mid-market firms, consulting agencies) who subscribe to Passport for market intelligence. The platform architecture must support multi-tenant data isolation, enterprise-grade security, subscription-based access controls, and seamless integration with existing Passport infrastructure.

### Technical Architecture Considerations

**Multi-Tenancy Model:**

The system implements subscription-based data access control where users can only access Passport data their subscription tier allows. This is not traditional multi-tenancy with separate customer databases, but rather fine-grained permission-based access within the shared Passport ecosystem.

**Architecture Characteristics:**
- Shared infrastructure and knowledge graph across all Passport customers
- Data access governed by user's Passport subscription tier (geography permissions, category permissions)
- Query-level permission enforcement before data retrieval agent executes
- Audit trail captures all access attempts for compliance and security monitoring

**Permission & Access Control Model:**

**Subscription-Based Permissions:**
- Users inherit data access permissions from their Passport subscription tier
- Geography-based restrictions (e.g., user can only query France, UK, Germany markets)
- Category-based restrictions (e.g., user can only access beverage, food categories)
- Combined geography + category permissions for fine-grained control

**Role-Based Access Control (RBAC):**
- **End User Role:** Generate intelligence reports, export outputs, view citations
- **Validator Role:** Review AI outputs, provide feedback, reject/approve reports, access quality scores
- **Admin Role:** User provisioning, SSO configuration, subscription tier mapping, audit trail access
- **Operations Role:** System health monitoring, knowledge graph maintenance, incident investigation, citation accuracy monitoring

**Permission Enforcement:**
- Pre-query validation checks user permissions before data retrieval
- Mode-specific permission checks (e.g., regulatory data access for Mode 3)
- Permission denial handled gracefully with clear error messages to users and admins

### Enterprise Integration Requirements

**Single Sign-On (SSO) Integration:**
- Support for enterprise authentication systems (SAML 2.0, OAuth 2.0, OpenID Connect)
- Integration with Passport's existing SSO infrastructure
- Session management aligned with enterprise security policies
- Multi-factor authentication (MFA) support when required by customer

**Passport API Integration:**
- Read-only access to Passport structured data (market size, company shares, forecasts)
- Access to Passport unstructured content (reports, documents, analysis)
- Respect Passport's existing data access controls and subscription permissions
- Handle Passport API rate limits gracefully
- Sync with Passport data refresh cycles for knowledge graph updates

**User Interface Integration:**
- Embedded within existing Passport UI (ChatGPT-style search bar interface)
- Consistent branding and design language with Passport ecosystem
- Seamless user experience - users don't leave Passport to access AI assistant
- Citation links navigate directly to source Passport datasets

**Export and Third-Party Integration:**
- PDF export for intelligence reports (MVP and Growth phases)
- PowerPoint (PPTX) export for presentations (Growth phase)
- API access for power users to integrate with their own tools (Vision phase)
- Webhook support for query completion notifications (Future consideration)

### Security & Compliance Requirements

**Data Security:**
- Encryption at rest for stored queries and generated reports
- Encryption in transit (TLS 1.3) for all API communications
- No user data leakage between sessions or users
- Secure handling of Passport credentials and API tokens

**Audit & Compliance:**
- **Comprehensive Audit Trail:** Log all queries, mode detection decisions, data retrieval operations, report generation, user actions, permission denials
- **Audit Trail Retention:** Configurable retention period per customer requirements (default: 12 months)
- **Audit Trail Access:** Admin and operations roles can query audit logs for compliance reporting
- **Data Residency:** Respect Euromonitor's data residency requirements - queries and generated reports stay within designated geographic regions
- **GDPR Compliance:** No personally identifiable information (PII) stored unnecessarily; data subject access requests supported

**System Security:**
- Regular security audits and penetration testing before production launch
- Vulnerability scanning and patch management process
- Incident response procedures for security events
- Rate limiting to prevent abuse and ensure fair resource allocation
- Protection against injection attacks, XSS, CSRF standard web vulnerabilities

### Subscription & Tier Management

**Subscription Model:**
- AI assistant access inherited from Passport subscription (no separate subscription required in MVP)
- Future consideration: Premium AI features for higher-tier Passport subscribers
- Beta testing group management during Phase 4 rollout

**User Provisioning:**
- Admin dashboard for adding/removing users from AI assistant access
- Bulk user import for enterprise customer onboarding
- Automatic sync with Passport user directory when possible
- Beta group management with phased rollout controls (10% → 50% → 100%)

**Subscription Tier Mapping:**
- Map Passport subscription tiers to AI assistant data permissions
- Geography and category access automatically inherited from Passport
- Admin can override permissions for specific users if needed (with audit trail)
- Permission changes propagate immediately (no caching delay)

### Scalability & Performance Requirements

**Concurrent User Support:**
- MVP (Phase 1-2): Support 20-50 concurrent beta users
- Growth (Phase 3-4): Support 100+ concurrent users
- Production (Phase 5): Support 500+ concurrent users without performance degradation

**Query Volume Capacity:**
- Launch target: 500+ daily queries across all modes
- 6-month target: 2000+ daily queries (4x growth)
- System architecture must scale horizontally to meet growing demand

**Response Time:**
- Target: <5 minutes average for typical query (end-to-end report generation)
- 95th percentile: <8 minutes
- Timeout threshold: 10 minutes (with graceful failure messaging)

**System Reliability:**
- 99.5% uptime SLA
- Automated health monitoring and alerting
- Graceful degradation if components fail (e.g., visualization generator failure doesn't block report delivery)
- Disaster recovery and backup strategy defined

### Monitoring & Operational Requirements

**Admin Dashboard Capabilities:**
- User management (add, remove, modify permissions)
- SSO configuration and testing
- Subscription tier mapping interface
- Beta group management (phased rollout controls)
- Usage analytics and reporting
- Audit trail query interface

**Operations Dashboard Capabilities:**
- Query audit trail with filtering and search
- Agent orchestration flow visibility for debugging failed queries
- Quality score distribution metrics
- Citation accuracy monitoring with broken link alerts
- Knowledge graph health metrics (data coverage, staleness indicators)
- System performance metrics (response times, error rates, concurrent load)
- Incident investigation tools

**Alerting & Notification:**
- Automated alerts for system health issues (error rate spikes, response time degradation)
- Citation accuracy alerts when broken links detected
- Knowledge graph staleness alerts when Passport data updates available
- Security alerts for suspicious access patterns
- User notification system for incident resolution and system maintenance

### Implementation Considerations

**Deployment Architecture:**
- Cloud-based deployment (AWS/Azure/GCP) with regional presence for data residency
- Containerized services (Kubernetes orchestration) for scalability
- Load balancing for concurrent query handling
- Auto-scaling based on demand patterns

**Phased Rollout Strategy:**
- Phase 1-2 (MVP): Beta environment with 20 users for initial validation
- Phase 3-4 (Growth): Expanded beta with 100+ users across diverse customer segments
- Phase 5 (Production): Phased rollout to full Passport user base (10% → 50% → 100%)
- Rollback capabilities if production issues detected

**Integration Testing:**
- SSO integration testing with multiple enterprise identity providers
- Passport API integration testing with various subscription tier scenarios
- Permission enforcement testing with edge cases
- Load testing at target concurrency levels (100+ concurrent users)
- Data residency compliance validation

**Cost Management:**
- LLM API call optimization (prompt caching, response streaming where applicable)
- Knowledge graph query optimization to minimize compute costs
- Resource allocation aligned with subscription tier value
- Cost per query monitoring for profitability analysis

## Functional Requirements

**Phase Distribution Summary:**
- **MVP (Phase 1-2):** 48 requirements (68%)
- **Growth (Phase 3-4):** 21 requirements (30%)
- **Vision (Phase 5-6):** 2 requirements (3%)

**Legend:**
- **[MVP]** = Must be delivered in Phase 1-2 (Months 1-4)
- **[GROWTH]** = Phase 3-4 features (Months 5-9)
- **[VISION]** = Phase 5-6 long-term features (Months 10-12+)

---

### Query & Intelligence Generation

- FR1: **[MVP]** Users can submit natural language queries about market intelligence topics
- FR2: **[MVP]** The system can generate Market Overview Reports for broad industry-level queries
- FR3: **[GROWTH]** The system can generate Category Deep Dive Reports for specific category queries
- FR4: **[GROWTH]** The system can generate Regulatory Impact Briefs for policy/regulation queries
- FR5: **[MVP]** The system can retrieve data from the knowledge graph based on query parameters
- FR6: **[MVP]** The system can synthesize narrative intelligence from retrieved Passport data
- FR7: **[MVP]** The system can generate visualizations (charts, infographics) appropriate to the report mode
- FR8: **[GROWTH]** The system can support multi-turn conversations with memory of previous queries
- FR9: **[GROWTH]** The system can provide follow-up question suggestions based on initial query results

### Mode Detection & Routing

- FR10: **[GROWTH]** The system can automatically detect the appropriate operational mode from query structure
- FR11: **[GROWTH]** The system can calculate confidence scores for mode detection decisions
- FR12: **[GROWTH]** The system can prompt users for clarification when mode detection confidence is below threshold (<0.85)
- FR13: **[GROWTH]** The system can route queries to mode-specific agent workflows without mid-conversation mode switching
- FR14: **[GROWTH]** Users can explicitly specify the desired mode if automatic detection is uncertain

### Quality Assurance & Validation

- FR15: **[MVP]** The system can score generated intelligence against multi-dimensional quality rubric
- FR16: **[MVP]** The system can iteratively refine outputs when quality score is below threshold (<75%)
- FR17: **[MVP]** The system can validate data completeness before generating intelligence
- FR18: **[MVP]** The system can flag coverage gaps when Passport data is incomplete for the query
- FR19: **[MVP]** Validators can review AI-generated intelligence with visibility into quality scores
- FR20: **[MVP]** Validators can approve or reject AI-generated outputs with feedback
- FR21: **[GROWTH]** Validators can provide structured feedback that improves future output quality
- FR22: **[MVP]** The system can enforce YAML business rules for each operational mode

### Citations & Transparency

- FR23: **[MVP]** The system can attribute every claim in generated intelligence to specific Passport source data
- FR24: **[MVP]** Users can view citations with report title and date for each data point
- FR25: **[MVP]** Users can navigate from citations directly to source Passport datasets
- FR26: **[MVP]** The system can validate citation accuracy before presenting reports (100% accuracy requirement)
- FR27: **[MVP]** The system can display methodology and data limitations in generated reports
- FR28: **[MVP]** The system can provide coverage cues indicating confidence levels and data gaps

### User Access & Authentication

- FR29: **[MVP]** Users can authenticate via Single Sign-On (SSO) using enterprise identity providers
- FR30: **[MVP]** The system can support SAML 2.0, OAuth 2.0, and OpenID Connect authentication protocols
- FR31: **[MVP]** The system can integrate with Passport's existing SSO infrastructure
- FR32: **[MVP]** The system can manage user sessions aligned with enterprise security policies
- FR33: **[MVP]** The system can support multi-factor authentication (MFA) when required

### Permissions & Data Access Control

- FR34: **[MVP]** The system can enforce subscription-based data access controls based on Passport tier
- FR35: **[MVP]** The system can restrict queries by geography based on user's subscription permissions
- FR36: **[MVP]** The system can restrict queries by category based on user's subscription permissions
- FR37: **[MVP]** The system can validate user permissions before executing data retrieval operations
- FR38: **[MVP]** The system can handle permission denials with clear error messages to users
- FR39: **[MVP]** The system can support role-based access control (End User, Validator, Admin, Operations)
- FR40: **[GROWTH]** Admins can override individual user permissions with audit trail documentation

### Administrative Management

- FR41: **[MVP]** Admins can provision and deprovision user access to the AI assistant
- FR42: **[MVP]** Admins can configure SSO integration settings
- FR43: **[MVP]** Admins can map Passport subscription tiers to AI assistant data permissions
- FR44: **[MVP]** Admins can manage beta testing groups with phased rollout controls
- FR45: **[GROWTH]** Admins can bulk import users for enterprise customer onboarding
- FR46: **[GROWTH]** Admins can view usage analytics and reporting dashboards
- FR47: **[MVP]** Admins can query audit trail logs for compliance reporting
- FR48: **[MVP]** Admins can configure data residency settings per customer requirements

### Operations & Monitoring

- FR49: **[MVP]** Operations staff can view query audit trails with complete orchestration flow details
- FR50: **[GROWTH]** Operations staff can filter and search audit logs by user, query, mode, or time range
- FR51: **[MVP]** Operations staff can access agent orchestration flow visibility for debugging failed queries
- FR52: **[GROWTH]** Operations staff can view quality score distribution metrics across queries
- FR53: **[MVP]** Operations staff can receive alerts when citation accuracy issues are detected
- FR54: **[MVP]** Operations staff can monitor knowledge graph health metrics (coverage, staleness)
- FR55: **[MVP]** Operations staff can view system performance metrics (response times, error rates, concurrent load)
- FR56: **[MVP]** Operations staff can investigate incidents with access to complete system state
- FR57: **[MVP]** Operations staff can maintain the knowledge graph with tools for identifying stale metadata
- FR58: **[MVP]** Operations staff can receive automated alerts for system health issues

### Export & Integration

- FR59: **[MVP]** Users can export generated intelligence reports to PDF format
- FR60: **[GROWTH]** Users can export generated intelligence reports to PowerPoint (PPTX) format
- FR61: **[MVP]** The system can sync with Passport data refresh cycles for knowledge graph updates
- FR62: **[MVP]** The system can handle Passport API rate limits gracefully without user-visible failures
- FR63: **[VISION]** Power users can access API endpoints to integrate with their own tools (Vision phase)
- FR64: **[VISION]** The system can provide webhook notifications for query completion (Future consideration)

### Knowledge Graph & Data Management

- FR65: **[MVP]** The system can construct knowledge graph from Passport structured and unstructured data
- FR66: **[MVP]** The system can maintain >95% coverage of Passport corpus in the knowledge graph
- FR67: **[MVP]** The system can preserve Passport taxonomy and data model in knowledge graph structure
- FR68: **[MVP]** The system can perform semantic search across unstructured Passport content
- FR69: **[MVP]** The system can enable cross-content retrieval finding connections across disparate datasets
- FR70: **[MVP]** The system can update knowledge graph when Passport data changes or is deprecated
- FR71: **[MVP]** The system can validate knowledge graph data quality during construction and updates

## Non-Functional Requirements

### Performance

- NFR1: The system must generate typical intelligence reports in less than 180 seconds (3 minutes) average response time
- NFR2: The system must maintain 95th percentile response time of less than 240 seconds (4 minutes)
- NFR3: The system must handle 100+ concurrent queries without performance degradation
- NFR4: The system must maintain error rate below 1% of all queries
- NFR5: The system must timeout gracefully after 10 minutes with clear user messaging
- NFR6: Mode detection must complete in less than 5 seconds
- NFR7: Citation validation must complete without adding more than 10 seconds to total response time

### Security

- NFR8: The system must encrypt all data at rest
- NFR9: The system must encrypt all data in transit using TLS 1.3 or higher
- NFR10: The system must prevent user data leakage between sessions or users
- NFR11: The system must securely handle Passport credentials and API tokens
- NFR12: The system must protect against injection attacks, XSS, and CSRF vulnerabilities
- NFR13: The system must implement rate limiting to prevent abuse
- NFR14: The system must undergo regular security audits and penetration testing
- NFR15: The system must have documented incident response procedures

### Reliability & Availability

- NFR16: The system must maintain 99.5% uptime SLA
- NFR17: The system must implement automated health monitoring and alerting
- NFR18: The system must gracefully degrade when components fail (e.g., visualization failure doesn't block report delivery)
- NFR19: The system must have disaster recovery and backup strategy
- NFR20: The system must support rollback capabilities for production deployments

### Scalability

- NFR21: The system must support 500+ daily queries at launch
- NFR22: The system must scale to support 2000+ daily queries within 6 months
- NFR23: The system must scale horizontally to meet growing demand
- NFR24: The system must implement auto-scaling based on demand patterns
- NFR25: The system must support 20-50 concurrent users in MVP phase
- NFR26: The system must support 100+ concurrent users in growth phase
- NFR27: The system must support 500+ concurrent users in production phase

### Data Quality & Accuracy

- NFR28: The system must achieve 100% citation accuracy (every citation links to valid Passport source)
- NFR29: The system must maintain >95% Passport corpus coverage in knowledge graph
- NFR30: The system must achieve >85% mode detection accuracy
- NFR31: The system must enforce minimum 75% quality score threshold before presenting reports
- NFR32: The system must validate data completeness and flag coverage gaps
- NFR33: The system must achieve >95% YAML business rule compliance

### Integration & Interoperability

- NFR34: The system must support SAML 2.0, OAuth 2.0, and OpenID Connect for SSO
- NFR35: The system must integrate with Passport's existing SSO infrastructure
- NFR36: The system must handle Passport API rate limits gracefully
- NFR37: The system must sync with Passport data refresh cycles automatically
- NFR38: The system must support PDF export format
- NFR39: The system must support PowerPoint (PPTX) export format
- NFR40: The system must provide API access for power users (Vision phase)

### Compliance & Auditability

- NFR41: The system must log all queries, mode detection, data retrieval, and report generation
- NFR42: The system must retain audit logs for configurable period (default: 12 months)
- NFR43: The system must provide audit trail query capabilities for admins and operations
- NFR44: The system must respect data residency requirements per customer configuration
- NFR45: The system must comply with GDPR for data subject access requests
- NFR46: The system must not store PII unnecessarily

### Maintainability & Operability

- NFR47: The system must provide operations dashboard with complete system observability
- NFR48: The system must enable debugging of failed queries via orchestration flow visibility
- NFR49: The system must alert operations staff automatically for system health issues
- NFR50: The system must alert operations staff when citation accuracy issues detected
- NFR51: The system must provide knowledge graph maintenance tools
- NFR52: The system must support containerized deployment (Kubernetes)
- NFR53: The system must support cloud deployment (AWS/Azure/GCP)

### Usability

- NFR54: The system must provide intuitive natural language query interface
- NFR55: The system must integrate seamlessly within existing Passport UI
- NFR56: The system must maintain consistent branding with Passport ecosystem
- NFR57: The system must provide clear error messages for permission denials
- NFR58: The system must provide graceful failure messaging for timeouts
- NFR59: The system must enable direct navigation from citations to Passport sources
