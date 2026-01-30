---
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8]
inputDocuments:
  - '_bmad-output/planning-artifacts/prd.md'
  - '_bmad-output/analysis/architect-technical-brief.md'
  - 'docs/brainstorming-session-2026-01-10.md'
  - '_bmad-output/analysis/brainstorming-session-2026-01-12.md'
completed: true
completedDate: '2026-01-21'
---

# UX Design Specification euromonitor-multi-agent-architecture

**Author:** Karthikmg
**Date:** 2026-01-21

---

## Executive Summary

### Project Vision

The Passport AI-Powered Intelligence Assistant transforms how Euromonitor Passport customers access and synthesize market intelligence. Rather than navigating complex database structures manually, users engage in natural language conversations to receive analyst-grade intelligence narratives - complete with claim-level citations, visualizations, and strategic insights. The system operates through three distinct modes (Market Overview, Category Deep Dive, Regulatory Impact Brief), each optimized for different strategic questions, delivering intelligence in minutes rather than weeks while maintaining complete transparency and traceability to Passport source data.

**Core UX Promise:** "Ask your business question in plain language. Receive strategic intelligence you can trust and act on immediately."

### Target Users

**Primary User Archetypes:**

1. **Time-Pressured Analysts (Sarah Chen)**
   - Market intelligence professionals at Fortune 500 companies
   - Expert Passport users facing tight deadlines
   - **Need:** Speed without sacrificing quality or verification
   - **Success Metric:** Delivers boardroom-ready intelligence in hours instead of weeks
   - **Tech Comfort:** High - comfortable with data tools, research platforms

2. **Non-Expert Navigators (Miguel Rodriguez)**
   - Category managers, strategy teams, operational leaders
   - Occasional Passport users lacking specialist knowledge
   - **Need:** Guided discovery and accessible insights without database expertise
   - **Success Metric:** Confidently presents intelligence without feeling lost
   - **Tech Comfort:** Medium - familiar with business software, prefers intuitive interfaces

3. **Quality Validators (Dr. Priya Kapoor)**
   - Senior analysts serving as quality gatekeepers
   - Adversarial reviewers ensuring AI outputs meet standards
   - **Need:** Complete transparency, citation accuracy, quality metrics visibility
   - **Success Metric:** Trusts AI enough to approve outputs for decision-making
   - **Tech Comfort:** High - demands rigor and verifiability

**User Context:**
- **Decision Stakes:** High - intelligence informs $50M+ capital allocation decisions
- **Usage Patterns:** Both single-query spot checks and multi-turn exploratory sessions
- **Environment:** Desktop-first (Passport ecosystem), professional work context
- **Collaboration:** Individual intelligence gathering with team sharing (PDF/PPTX exports)

### Key Design Challenges

1. **Trust Paradox: Speed vs Verification**
   - Challenge: Users need fast intelligence but also need to verify every claim
   - UX Consideration: How do we make citation verification effortless without slowing the primary flow?
   - Risk: If verification feels tedious, users skip it; if intelligence feels "black box," users don't trust it

2. **Multi-Mode Complexity Without Cognitive Overhead**
   - Challenge: Three distinct operational modes with different outputs, but users shouldn't need to understand the system architecture
   - UX Consideration: Automatic mode detection must feel invisible; clarification flows must feel natural, not like system errors
   - Risk: If users feel confused about "why am I getting this format," the system loses credibility

3. **Progressive Disclosure for Novices, Power for Experts**
   - Challenge: Non-experts (Miguel) need simplicity; experts (Dr. Kapoor) need depth and control
   - UX Consideration: How do we serve both personas without cluttering the interface or hiding critical information?
   - Risk: Designing for experts alienates novices; designing for novices frustrates experts

4. **Human-in-the-Loop Validation Without Workflow Friction**
   - Challenge: Outputs require human review, but review shouldn't feel like extra work
   - UX Consideration: How do we make validation feel natural, collaborative, and value-adding rather than bureaucratic?
   - Risk: Validation becomes a bottleneck that users try to bypass

### Design Opportunities

1. **ChatGPT Familiarity as Trojan Horse for Complexity**
   - Opportunity: Leverage users' ChatGPT muscle memory to make sophisticated multi-agent system feel simple
   - UX Innovation: Familiar search bar interface hides YAML-driven business rules, knowledge graph queries, and 8-agent orchestration
   - Competitive Advantage: Users feel competent immediately (no training required) while accessing enterprise-grade intelligence

2. **Citations as Trust-Building Storytelling, Not Just References**
   - Opportunity: Transform claim-level citations from "compliance requirement" into "confidence builder"
   - UX Innovation: Make citations discoverable-on-hover, explorable-on-click, with visual cues showing data freshness and coverage
   - Competitive Advantage: Users develop trust through transparency; citations become part of the narrative, not footnotes

3. **Mode-Specific Narrative Structures as Template for Thinking**
   - Opportunity: Three distinct modes teach users how to think about different strategic questions
   - UX Innovation: Consistent section structures (Mode 1's 5 sections, Mode 2's adaptive insights, Mode 3's before/after) become mental models users internalize
   - Competitive Advantage: Users learn strategic analysis frameworks through using the tool; the UX is educational

4. **Quality Scoring as Co-Pilot Signal, Not Gatekeeper**
   - Opportunity: Internal quality score (>75% threshold) can inform UX signals without being punitive
   - UX Innovation: Surface quality indicators as "confidence levels" that help users interpret intelligence, not as pass/fail judgments
   - Competitive Advantage: Users understand limitations proactively; sets expectations appropriately; builds realistic trust

## Core User Experience

### Defining Experience

**Core User Action:** Ask business/market intelligence questions in natural language and receive structured, cited intelligence reports.

**The Essential Loop:**
1. User enters a question (natural language, no special syntax required)
2. System generates intelligence report (Mode 1, 2, or 3 automatically detected)
3. User reads narrative, explores citations, validates insights
4. User asks follow-up questions or exports report
5. User returns for next intelligence need

**MVP Scope - Standalone Application:**
This is a standalone web application (not embedded in Passport) focused on demonstrating the multi-agentic intelligence generation concept. The experience prioritizes simplicity and core value delivery over feature completeness.

**Core Value Delivered:** Transform "I have a complex business question" into "I have a trusted, verifiable intelligence report" in minutes.

### Platform Strategy

**Primary Platform:** Standalone web application
- **Device Focus:** Desktop-first (laptop/desktop screens 1280px+)
- **Browser Support:** Modern browsers (Chrome, Firefox, Safari, Edge - latest 2 versions)
- **Responsive Considerations:** Functional on tablets (iPad), not optimized for phones
- **Interaction Model:** Mouse/keyboard primary, touch-friendly where applicable

**Architecture Approach:**
- Single-page application (SPA) feel with minimal page loads
- Fast, responsive interface (interactions feel immediate even when AI processing takes minutes)
- Progressive loading for long-form intelligence reports
- Accessible via direct URL (own domain/subdomain)

**Authentication:**
- Simple email/password authentication for MVP
- User account required to access the application
- No complex role/permission system in MVP (all users have same access)

### Effortless Interactions

**What Should Feel Completely Natural:**

1. **Query Entry - Zero Learning Curve**
   - Single search bar, no complex forms or filters
   - Natural language questions work immediately (no syntax to learn)
   - System handles vague or broad questions gracefully (asks clarifying questions when needed)
   - Users leverage ChatGPT familiarity - if they can use ChatGPT, they can use this

2. **Mode Detection - Invisible Intelligence**
   - Users never think about "modes" or "report types"
   - System automatically determines the right intelligence format
   - No dropdown menus for "select report type"
   - Clarification feels conversational, not like an error state

3. **Citation Exploration - Trustworthy by Default**
   - Citations visible inline within narrative (not buried in footnotes)
   - Hover to preview source information
   - Click to explore source data (whatever data sources are available)
   - Visual cues show data freshness and coverage
   - No separate "references" section to hunt through

4. **Multi-Turn Conversations - Natural Follow-Ups**
   - Follow-up questions maintain context automatically
   - Users can refine, drill deeper, or pivot naturally
   - No "start new chat" friction between related questions
   - Conversation history visible for reference

5. **Report Export - One-Click Sharing**
   - Single "Export" button generates PDF or PPTX
   - No configuration dialogs or format choices to overwhelm users
   - Generated documents are presentation-ready immediately
   - Fast export (seconds, not minutes)

### Critical Success Moments

**Make-or-Break Interactions:**

1. **First Query Success (The "Aha" Moment)**
   - User's first question produces a high-quality, useful intelligence report
   - If first experience fails or confuses, user may not return
   - Success metric: First-time users complete first query and read report

2. **Trust Through Citations (The "I Can Verify This" Moment)**
   - User clicks first citation and sees credible source backing the claim
   - Builds confidence that intelligence is grounded, not hallucinated
   - Success metric: Users explore citations and feel reassured

3. **Speed Realization (The "This Would Have Taken Days" Moment)**
   - User receives comprehensive intelligence report in 3-5 minutes
   - Compares mentally to manual research (hours/days)
   - Success metric: Users return for second query within same session

4. **Quality Recognition (The "This Is Actually Good" Moment)**
   - User reads narrative and recognizes analyst-grade quality
   - Narrative structure, insights, and formatting meet professional standards
   - Success metric: Users export and share reports with colleagues

**Where Failure Would Ruin Experience:**
- Query takes >10 minutes without progress feedback (feels broken)
- Citations link to broken/missing data sources (trust destroyed)
- Narrative is generic, obvious, or unhelpful (value not delivered)
- Mode detection constantly asks clarifying questions (feels incompetent)
- Export fails or produces poorly formatted documents (sharing blocked)

### Experience Principles

**Guiding Principles for All UX Decisions:**

1. **"ChatGPT Simplicity, Bloomberg Authority"**
   - Interface is as simple as ChatGPT (search bar, conversation)
   - Output has the authority and rigor of professional research platforms
   - Balance approachability with credibility

2. **"Show, Don't Tell"**
   - Rather than explaining how the system works, let users experience it
   - Reduce instructional text, increase intuitive interaction
   - First intelligence report teaches users what's possible

3. **"Trust Through Transparency, Not Claims"**
   - Don't tell users "this is accurate" - show them the citations
   - Make verification easy, not an afterthought
   - Quality signals are embedded in the experience, not badges/labels

4. **"MVP Means Nail the Core, Skip the Nice-to-Haves"**
   - Focus: Query → Intelligence → Verification → Export
   - Defer: Advanced search, saved queries, collaboration features, dashboards
   - Every feature must justify its presence in MVP

5. **"Fast Feels Intelligent, Slow Feels Broken"**
   - Even when AI processing takes minutes, interface must feel responsive
   - Show progress, show reasoning, show what's happening
   - Never leave users staring at a blank screen wondering if it's working

## Desired Emotional Response

### Primary Emotional Goals

**Core Feeling: Confident Empowerment**
Users should feel empowered to tackle complex business questions they previously couldn't approach independently, while feeling confident in the quality and accuracy of the intelligence they receive.

**Primary Emotions:**

1. **Trust & Confidence**
   - Users trust the AI-generated intelligence enough to act on it
   - Citations and transparency build confidence in accuracy
   - Professional quality output reinforces credibility

2. **Efficiency & Relief**
   - Users feel relief from manual research burden
   - Sense of accomplishment from completing analysis in minutes vs days
   - Productive momentum from quick intelligence turnaround

3. **Competence & Empowerment**
   - Non-experts feel capable of generating professional intelligence
   - Experts feel amplified (10x productivity multiplier)
   - Users feel smarter and more capable than before

### Emotional Journey Mapping

**Discovery Phase (First Visit):**
- **Target Emotion:** Intrigued curiosity with cautious optimism
- **Design Support:** Clear value proposition, simple interface that looks trustworthy

**First Query (Critical Moment):**
- **Target Emotion:** Hopeful anticipation
- **Design Support:** Clear progress indicators, no anxiety-inducing blank screens

**Receiving Intelligence (Aha Moment):**
- **Target Emotion:** Pleasant surprise and impressed satisfaction
- **Design Support:** High-quality formatted output, professional presentation, clear structure

**Exploring Citations (Trust Building):**
- **Target Emotion:** Reassurance and verification satisfaction
- **Design Support:** Easy citation exploration, credible sources, transparent data linkage

**Follow-Up Queries (Momentum Building):**
- **Target Emotion:** Growing confidence and mastery
- **Design Support:** Natural conversation flow, context retention, increasingly sophisticated queries

**Returning User (Habit Formation):**
- **Target Emotion:** Comfortable competence
- **Design Support:** Familiar patterns, reliable quality, consistent experience

### Micro-Emotions

**Confidence Over Confusion:**
- System should feel intelligent and helpful, never cryptic or confusing
- Mode detection and clarification questions should feel natural, not like system errors
- Clear feedback at every stage eliminates uncertainty

**Trust Over Skepticism:**
- Every claim backed by citation builds cumulative trust
- Transparency in data sources and limitations prevents skepticism
- Quality consistency across queries reinforces reliability

**Accomplishment Over Frustration:**
- Successfully completing a query delivers sense of achievement
- Clear progress indicators prevent frustration during processing
- Helpful error messages maintain positive feelings even when things fail

**Control Over Helplessness:**
- Users feel in control of the intelligence generation process
- Ability to refine, drill deeper, or pivot maintains agency
- Export and sharing options extend user control beyond the platform

### Design Implications

**To Create Trust & Confidence:**
- Inline citations visible throughout narrative (not hidden)
- Professional formatting and structure matching analyst-grade quality
- Data freshness indicators and source credibility signals
- Quality indicators that show system self-assessment

**To Create Efficiency & Relief:**
- Fast, responsive interface even during AI processing
- Progress indicators showing what's happening ("Analyzing market data...", "Generating insights...")
- One-click export for immediate sharing
- Multi-turn conversations eliminate repetitive context-setting

**To Create Competence & Empowerment:**
- Zero learning curve (ChatGPT-familiar interface)
- System handles complexity invisibly (automatic mode detection)
- High-quality outputs make users look good to colleagues/executives
- Educational aspect - users learn strategic frameworks through consistent report structures

**To Avoid Negative Emotions:**
- Never leave users wondering if system is working (show progress)
- Never present broken citations or missing data (destroys trust instantly)
- Never force users through complex configuration (increases anxiety)
- Never make users feel stupid for asking "wrong" questions (graceful handling)

### Emotional Design Principles

1. **"Reassurance Through Transparency"**
   - Show what's happening, show sources, show limitations
   - Users feel secure when they understand the process
   - Transparency builds trust faster than claims of accuracy

2. **"Professional Delight, Not Playful Fun"**
   - This is a serious business tool, not entertainment
   - Delight comes from quality and efficiency, not animations or gamification
   - Satisfaction from accomplishment, not superficial engagement

3. **"Progressive Trust Building"**
   - First experience establishes credibility
   - Each successful interaction builds cumulative trust
   - Citation exploration reinforces confidence over time
   - Consistency across sessions solidifies reliability

4. **"Confidence Through Simplicity"**
   - Simple interfaces reduce anxiety
   - Complexity hidden behind clean UX increases confidence
   - Users feel smart when product feels easy

5. **"Speed Equals Intelligence"**
   - Fast responses feel competent and capable
   - Slow responses without feedback feel broken
   - Progress indicators maintain positive emotional state during processing

## UX Pattern Analysis & Inspiration

### Inspiring Products Analysis

**1. ChatGPT (OpenAI)**

**What They Do Well:**
- Single input field as primary interface - zero cognitive overhead
- Conversational UI feels natural and accessible
- Progressive disclosure (simple start, complexity revealed as needed)
- Clear visual distinction between user input and AI response
- Multi-turn conversations maintain context seamlessly
- Regenerate/edit options give users control
- Markdown rendering makes structured content readable

**Key Lesson:** Conversational interfaces lower barriers to entry. Users don't need training when the interface mimics natural communication.

**2. Perplexity AI**

**What They Do Well:**
- Inline citations integrated into narrative (numbered superscripts)
- Sources panel shows all citations in one place
- Hover previews for quick source verification
- Follow-up question suggestions guide exploration
- Clean, professional aesthetic (not playful)
- Speed emphasis (feels fast even when processing)
- Export functionality integrated naturally

**Key Lesson:** Trust comes from transparent sourcing. Citations as first-class UI elements, not afterthoughts.

**3. Bloomberg Terminal**

**What They Do Well:**
- Information density without feeling cluttered
- Professional, data-rich presentation builds credibility
- Keyboard shortcuts for power users
- Consistent data formatting across all views
- Status indicators show data freshness
- Black/dark theme reduces eye strain for long sessions
- Command-line style input for power users (but not required)

**Key Lesson:** Professional users value information density and efficiency over minimalism. Authority through consistent, structured presentation.

**4. Notion**

**What They Do Well:**
- Clean, modern aesthetic that feels effortless
- Progressive disclosure (simple by default, powerful when needed)
- Excellent use of whitespace for readability
- Smooth, fast interactions (no loading spinners for UI changes)
- Contextual actions appear on hover (reduce visual clutter)
- Export to multiple formats seamlessly
- Consistent design language across all features

**Key Lesson:** Modern SaaS users expect speed and polish. Every interaction should feel instant even when backend processing takes time.

**5. Linear (Project Management)**

**What They Do Well:**
- Keyboard-first design for power users
- Lightning-fast performance (optimistic UI updates)
- Clean, minimal interface with strong information hierarchy
- Command palette (Cmd+K) for quick actions
- Clear status indicators and progress feedback
- No loading states for UI interactions (feels instant)
- Consistent shortcuts across entire app

**Key Lesson:** Speed and responsiveness signal quality. Users equate fast interfaces with intelligent systems.

### Transferable UX Patterns

**Navigation & Information Architecture:**

1. **Single Input Field Primacy (ChatGPT)**
   - Application: Main search bar as dominant UI element
   - Benefit: Reduces decision paralysis, clear call-to-action
   - Implementation: Full-width search bar, prominent placement, autofocus on load

2. **Command Palette Pattern (Linear/Notion)**
   - Application: Cmd+K to access key functions (new query, export, settings)
   - Benefit: Power users can work faster, discoverability for casual users
   - Implementation: Keyboard shortcut overlay showing available commands

3. **Sidebar Navigation for Secondary Functions (Notion)**
   - Application: Left sidebar for history, saved reports, settings
   - Benefit: Keeps main area focused on core task, persistent access to utilities
   - Implementation: Collapsible sidebar, clear hierarchy, contextual sections

**Interaction Patterns:**

1. **Inline Citations with Hover Previews (Perplexity)**
   - Application: Superscript numbers in narrative text, hover shows source preview
   - Benefit: Trust through transparency, verification without leaving context
   - Implementation: Numbered citations [1], hover card with source metadata, click to expand

2. **Progressive Disclosure of Complexity (ChatGPT/Notion)**
   - Application: Simple interface by default, advanced options revealed contextually
   - Benefit: Novices aren't overwhelmed, experts access power features naturally
   - Implementation: Basic query interface, advanced filters on demand, export options contextual

3. **Optimistic UI Updates (Linear)**
   - Application: UI responds instantly even while backend processes
   - Benefit: System feels fast and responsive, reduces perceived latency
   - Implementation: Show query in conversation immediately, display "generating..." state while processing

4. **Multi-Turn Context Retention (ChatGPT)**
   - Application: Follow-up questions reference previous context automatically
   - Benefit: Natural conversation flow, users don't repeat themselves
   - Implementation: Conversation thread view, clear query/response pairs, context preserved

5. **Suggested Follow-Up Questions (Perplexity)**
   - Application: After delivering intelligence, suggest related queries
   - Benefit: Guides exploration, teaches users what's possible, increases engagement
   - Implementation: 3-4 suggested questions below each report

**Visual & Content Patterns:**

1. **Professional Data-Rich Presentation (Bloomberg)**
   - Application: Structured intelligence reports with clear sections, data tables, charts
   - Benefit: Analyst-grade credibility, information density professionals expect
   - Implementation: Consistent section headers, formatted data tables, embedded visualizations

2. **Markdown Rendering for Structure (ChatGPT/Notion)**
   - Application: Headers, lists, bold/italic for emphasis, code blocks for data
   - Benefit: Readable long-form content, scannable structure, professional formatting
   - Implementation: Clean markdown rendering, consistent typography, visual hierarchy

3. **Status and Progress Indicators (Linear/Bloomberg)**
   - Application: Show what's happening during AI processing
   - Benefit: Reduces anxiety, maintains trust, signals intelligence
   - Implementation: Progress messages ("Analyzing market data...", "Generating insights...", "Validating citations...")

4. **Data Freshness Signals (Bloomberg)**
   - Application: Show when data was last updated, currency indicators
   - Benefit: Users understand data limitations, trust through transparency
   - Implementation: Date stamps on citations, "Data as of [date]" indicators

**Trust & Verification Patterns:**

1. **Transparent Sourcing (Perplexity)**
   - Application: Every claim linked to verifiable source
   - Benefit: Builds trust through verifiability, enables validation
   - Implementation: Inline citation numbers, sources panel, click to explore source

2. **Export as Core Feature (Notion/Perplexity)**
   - Application: One-click export to PDF/PPTX
   - Benefit: Enables sharing, extends value beyond platform, professional workflow integration
   - Implementation: Export button in header, fast generation, presentation-ready formatting

### Anti-Patterns to Avoid

**Interaction Anti-Patterns:**

1. **Complex Query Builders (Traditional BI Tools)**
   - Problem: Forces users to understand system architecture before asking questions
   - Why Avoid: Contradicts "ChatGPT simplicity" principle, creates barriers to entry
   - Alternative: Natural language input with invisible intelligence

2. **Modal Dialogs for Configuration (Legacy Enterprise Software)**
   - Problem: Interrupts flow, forces decisions, creates cognitive overhead
   - Why Avoid: Slows users down, feels bureaucratic, conflicts with "effortless" goal
   - Alternative: Sensible defaults with inline configuration when needed

3. **Separate "Advanced" Mode (Many Tools)**
   - Problem: Creates two-tier experience, forces users to choose mode
   - Why Avoid: Progressive disclosure better serves both novices and experts
   - Alternative: Contextual power features that appear when needed

4. **Loading Spinners Without Context (Generic Apps)**
   - Problem: Users don't know what's happening or how long it will take
   - Why Avoid: Creates anxiety, feels unresponsive, damages trust
   - Alternative: Specific progress messages with reasoning visibility

5. **Hidden Citations or Footnotes (Traditional Reports)**
   - Problem: Verification requires scrolling, citations feel like afterthought
   - Why Avoid: Makes trust-building harder, conflicts with transparency principle
   - Alternative: Inline citations with hover previews

**Visual Anti-Patterns:**

1. **Playful/Gamified UI (Consumer Apps)**
   - Problem: Undermines professional credibility, feels unserious
   - Why Avoid: Business intelligence demands authority, not entertainment
   - Alternative: Professional delight through quality and efficiency

2. **Excessive White Space/Minimalism (Some Modern Apps)**
   - Problem: Professional users need information density
   - Why Avoid: Forces scrolling, reduces at-a-glance comprehension
   - Alternative: Bloomberg-style structured density with clear hierarchy

3. **Inconsistent Data Formatting (Poor BI Tools)**
   - Problem: Users can't quickly parse numbers, dates, formats vary
   - Why Avoid: Damages credibility, makes data harder to understand
   - Alternative: Strict formatting standards for all data types

4. **Badges, Banners, Upsells (SaaS Products)**
   - Problem: Clutters interface, distracts from core task, feels commercial
   - Why Avoid: Conflicts with professional focus, reduces trust
   - Alternative: Clean interface focused on user's intelligence needs

**Content Anti-Patterns:**

1. **Generic AI Disclaimers (Many AI Tools)**
   - Problem: "AI may make mistakes" feels like hedge, reduces confidence
   - Why Avoid: Better to show limitations through coverage cues than broad disclaimers
   - Alternative: Specific data gaps flagged inline, confident tone where data supports it

2. **Verbose Explanations (Overdesigned Onboarding)**
   - Problem: Users don't read long instructions, delays value delivery
   - Why Avoid: "Show, don't tell" principle - let users experience the product
   - Alternative: First query teaches by example

3. **Hidden Intelligence Rationale (Black Box AI)**
   - Problem: Users can't understand why system made certain choices
   - Why Avoid: Contradicts transparency principle, limits trust
   - Alternative: Show reasoning through citations and mode detection visibility

### Design Inspiration Strategy

**What to Adopt Directly:**

1. **ChatGPT's Conversational Interface**
   - Single input field as primary interaction
   - Multi-turn context retention
   - Clear visual distinction between user and system
   - Reason: Proven, familiar, eliminates learning curve

2. **Perplexity's Citation Integration**
   - Inline numbered citations throughout narrative
   - Hover previews for quick verification
   - Sources panel for comprehensive view
   - Reason: Solves trust problem elegantly, core to value proposition

3. **Linear's Speed and Responsiveness**
   - Optimistic UI updates
   - No loading states for UI interactions
   - Fast feels intelligent principle
   - Reason: Speed signals quality, reduces perceived latency

4. **Bloomberg's Professional Presentation**
   - Structured data formatting
   - Information density without clutter
   - Status and freshness indicators
   - Reason: Matches professional user expectations, builds credibility

**What to Adapt for Our Context:**

1. **Command Palette (Simplified for MVP)**
   - Adopt: Keyboard shortcuts for common actions
   - Adapt: Fewer commands initially (new query, export), expand later
   - Reason: MVP focus on core experience, defer advanced shortcuts

2. **Follow-Up Questions (Contextual Suggestions)**
   - Adopt: Suggest related queries after reports
   - Adapt: Mode-specific suggestions (Mode 1 might suggest deeper category dive)
   - Reason: Guides users while teaching system capabilities

3. **Sidebar Navigation (Minimal MVP Version)**
   - Adopt: Sidebar for history and settings
   - Adapt: Simplified version without complex organization/folders initially
   - Reason: Core utility without over-engineering for MVP

**What to Explicitly Avoid:**

1. **Bloomberg's Visual Complexity**
   - Avoid: Dense, dark interface with multiple simultaneous panels
   - Reason: Start simpler, add density based on user feedback
   - Alternative: Single focused panel with clean layout

2. **ChatGPT's Playful Tone**
   - Avoid: Casual language, conversational filler
   - Reason: Business intelligence demands professional credibility
   - Alternative: Clear, confident, analyst-grade tone

3. **Notion's Feature Breadth**
   - Avoid: Collaboration, commenting, databases, templates
   - Reason: MVP must nail core intelligence generation first
   - Alternative: Defer collaboration features to post-MVP

4. **Perplexity's Multi-Source Aggregation Display**
   - Avoid: Showing multiple conflicting sources for same data point
   - Reason: Adds complexity; our data has single authoritative source (knowledge graph)
   - Alternative: Single citation per claim, clear data lineage

**Strategic Synthesis:**

**Design Philosophy = "ChatGPT Simplicity + Perplexity Citations + Bloomberg Authority"**

- Start with ChatGPT's accessible interface
- Layer in Perplexity's transparent citation model
- Present with Bloomberg's professional credibility
- Execute with Linear's speed and polish
- Structure with Notion's information clarity

This combination serves both novice and expert users while maintaining trust through transparency and delivering intelligence with professional authority.

## Design System Foundation

### Design System Choice

**Primary System: Tailwind CSS + shadcn/ui**

**Component Strategy:**
- **Tailwind CSS** as utility-first CSS framework for styling
- **shadcn/ui** for base component library (copy/paste, owned components)
- **React** as UI framework
- **TypeScript** for type safety

**Rationale:** This combination provides rapid MVP development velocity while maintaining full customization control and professional polish. No heavy framework dependencies, complete ownership of component code, and flexibility to implement both ChatGPT-style conversational UI and Bloomberg-style data-rich presentations.

### Rationale for Selection

**1. MVP Velocity Without Compromising Quality**
- Tailwind's utility-first approach eliminates CSS file context switching
- shadcn/ui provides production-ready components without dependency lock-in
- Copy/paste component model means we own and control all UI code
- Fast iteration cycles critical for standalone MVP development

**2. Design Flexibility for Dual Aesthetic Requirements**
- Must support "ChatGPT Simplicity + Bloomberg Authority" design philosophy
- Tailwind enables both minimal conversation interfaces AND dense data presentations
- No prescribed design language (avoiding Material Design or other opinionated systems)
- Easy to implement Perplexity-style citation hover cards, progress indicators, and professional formatting

**3. Professional SaaS Aesthetic Alignment**
- Modern, clean foundation matches Linear/Notion inspiration sources
- Straightforward to create professional business intelligence UI
- Avoids playful/consumer app aesthetics (aligns with emotional design principles)
- Supports information density without visual clutter

**4. Developer Experience & Team Efficiency**
- Excellent TypeScript/React ecosystem integration
- Comprehensive documentation and active community
- Component customization without fighting framework constraints
- Performance-optimized by default (critical for "speed equals intelligence" principle)

**5. Technical Advantages for Intelligence Assistant**
- Lightweight bundle size (fast initial load)
- Easy to implement custom components (citation tooltips, progress indicators, mode-specific layouts)
- Responsive design utilities for desktop-first with tablet support
- Dark mode support built-in (option for future Bloomberg-style dark theme)

**6. No Framework Lock-In**
- Components are owned code, not npm dependencies
- Can migrate or replace individual components without ecosystem disruption
- Freedom to evolve design system as product matures beyond MVP
- Reduces technical debt risk for standalone application

### Implementation Approach

**Phase 1: Foundation Setup**

1. **Install Tailwind CSS**
   - Configure design tokens (colors, spacing, typography)
   - Set up custom theme aligned with professional intelligence aesthetic
   - Configure for desktop-first responsive breakpoints

2. **Initialize shadcn/ui**
   - Install CLI and configure component directory structure
   - Copy base components needed for MVP (Button, Input, Card, Dialog, Tooltip, etc.)
   - Customize default styles to match brand direction

3. **Establish Design Tokens**
   - Color palette: Professional blues/grays with accent colors for citations, status
   - Typography scale: Clear hierarchy for headers, body text, data displays
   - Spacing system: Consistent rhythm for layouts
   - Border radius: Subtle, modern (not too rounded, maintains professional feel)

**Phase 2: Core Components Development**

**Conversational UI Components:**
- `SearchBar` - Primary query input (full-width, prominent, autofocus)
- `ConversationThread` - Query/response pairs with clear visual distinction
- `MessageBubble` - User queries and AI responses with appropriate styling
- `TypingIndicator` - Progress feedback during AI processing

**Intelligence Display Components:**
- `IntelligenceReport` - Structured report container with sections
- `ReportSection` - Collapsible sections with headers (Mode 1's 5 sections, etc.)
- `Citation` - Inline superscript with hover preview and click to expand
- `CitationCard` - Hover preview showing source metadata
- `DataTable` - Formatted tables for market data, competitive analysis
- `ProgressIndicator` - Contextual messages ("Analyzing market data...", "Generating insights...")

**Navigation & Layout Components:**
- `AppShell` - Main layout with sidebar, header, content area
- `Sidebar` - History, saved reports, settings navigation
- `Header` - App branding, user menu, quick actions
- `CommandPalette` - Cmd+K overlay for power user actions

**Utility Components:**
- `ExportButton` - PDF/PPTX export with loading states
- `ErrorMessage` - Graceful error handling with helpful messaging
- `EmptyState` - First-time user guidance and example queries
- `Tooltip` - Contextual help and information previews

**Phase 3: Specialized Components**

**Mode-Specific Components:**
- `Mode1Report` - Market Overview structure (5 sections, top 5 competitors)
- `Mode2Report` - Category Deep Dive structure (adaptive sections, call-out boxes)
- `Mode3Report` - Regulatory Impact structure (before/after comparison, infographics)
- `VisualizationEmbed` - Container for charts and infographics

**Trust & Verification Components:**
- `SourcesPanel` - Comprehensive citation list
- `QualityIndicator` - Confidence signals (subtle, non-judgmental)
- `CoverageFlag` - Data gap notifications
- `DataFreshnessTag` - Last updated timestamps

### Customization Strategy

**Visual Identity Customization:**

**Color System:**
- **Primary:** Professional blue (trust, authority, intelligence)
- **Secondary:** Neutral grays (backgrounds, borders, subtle UI)
- **Accent:** Highlight color for citations, interactive elements
- **Semantic Colors:** Success (green), warning (amber), error (red), info (blue)
- **Surface Colors:** Clean whites/light grays for main content, subtle contrasts for depth

**Typography Strategy:**
- **Headings:** Clear, authoritative sans-serif (Inter, System UI)
- **Body Text:** Readable, professional (same family, appropriate weights)
- **Data Display:** Monospace for numbers, tabular data alignment
- **Code/Technical:** Monospace for any technical content or data structures

**Spacing & Layout:**
- Desktop-first with generous whitespace (not excessive minimalism)
- Information density balanced with readability (Bloomberg inspiration without visual complexity)
- Consistent grid system for alignment and rhythm
- Responsive breakpoints: Desktop (1280px+), Tablet (768px-1279px)

**Component Style Customization:**

**Buttons:**
- Primary: Solid fill, clear call-to-action (query submission, export)
- Secondary: Outlined, supporting actions
- Ghost: Minimal, tertiary actions
- Sizes: Default (standard actions), small (inline actions), large (primary CTAs)

**Cards:**
- Subtle shadows for depth without heavy borders
- Clean, professional appearance (not playful rounded corners)
- Clear content hierarchy within cards

**Inputs:**
- Single-line for search bar (prominent, generous sizing)
- Clear focus states (subtle, professional)
- No distracting animations or effects

**Interactive Elements:**
- Hover states: Subtle, fast transitions (feels responsive)
- Click feedback: Immediate visual acknowledgment
- Loading states: Progress indicators with context (never blank spinners)

**Citation Styling:**
- Superscript numbers [1] in subtle accent color
- Hover cards: Clean, readable source preview
- Click targets: Large enough for easy interaction
- Visual connection: Clear link between citation and narrative

**Data Visualization Integration:**
- Consistent color palette across charts
- Professional, business-intelligence aesthetic (not decorative)
- Clear labels, legends, axis formatting
- Responsive sizing for different screen widths

**Accessibility Considerations:**
- WCAG AA compliance minimum (AAA where feasible)
- Keyboard navigation for all interactive elements
- Focus indicators clear and visible
- Color contrast ratios meet standards
- Screen reader support for all content
- Alt text for visualizations and charts

**Performance Optimization:**
- Lazy loading for non-critical components
- Code splitting for mode-specific components
- Optimized bundle size (Tailwind purging unused styles)
- Fast Time to Interactive (TTI) for query input
- Smooth scrolling and animations (60fps)

**Design System Documentation:**
- Component usage guidelines
- Example implementations for common patterns
- Accessibility requirements per component
- Responsive behavior documentation
- Code snippets for consistent implementation

**Evolution Strategy:**
- Start with MVP core components
- Add complexity based on user feedback
- Maintain design token consistency as system grows
- Regular design system audits for consistency
- Component library expansion driven by actual needs (not speculative)

## 2. Core User Experience

### 2.1 Defining Experience

**The Core Interaction:** "Natural Language Query → Verified Intelligence Report"

**User's One-Sentence Description:**
"I just type my business question like I'm talking to an analyst, and it gives me a complete intelligence report with sources I can verify."

**What Makes This Defining:**
This single interaction collapses weeks of manual research into minutes. Users don't navigate databases, build queries, or stitch together multiple reports. They ask naturally, and the system delivers complete, verifiable intelligence. The magic is in the compression of complexity - sophisticated multi-agent orchestration, knowledge graph queries, and YAML-driven business rules all hidden behind ChatGPT-style simplicity.

**Core Experience Flow:**
1. User sees prominent search bar (autofocused, inviting)
2. User types natural language question (no special syntax)
3. System instantly acknowledges query (optimistic UI)
4. Progress indicators show intelligence generation ("Analyzing market data...", "Generating insights...")
5. Structured intelligence report appears (formatted, sectioned, cited)
6. User explores citations inline (hover previews, click to verify)
7. User asks follow-up or exports report (natural continuation or completion)

**Why This Experience Defines Success:**
- **Accessibility:** Non-experts can generate professional intelligence
- **Trust:** Citations enable verification without blind faith
- **Speed:** Minutes vs days/weeks creates "this is better" realization
- **Naturalness:** ChatGPT familiarity eliminates learning curve
- **Completeness:** Full intelligence report, not partial data dumps

### 2.2 User Mental Model

**How Users Currently Think About This Task:**

**Traditional Approach (What Users Know):**
1. Open research platform (Passport, Bloomberg, competitor tools)
2. Navigate complex taxonomy/database structure
3. Build queries with specific filters and parameters
4. Extract data into spreadsheets
5. Cross-reference multiple reports manually
6. Synthesize findings into narrative
7. Create citations and references
8. Format presentation
9. Validate with colleagues
10. Present to stakeholders

**Time Required:** Days to weeks
**Skill Required:** Expert knowledge of research platform
**Pain Points:** Manual, time-consuming, requires specialist knowledge, error-prone

**ChatGPT Mental Model (What Users Bring):**
- Single input field = ask any question
- Conversational interface = natural language works
- Multi-turn = follow-ups maintain context
- Fast responses = answers in seconds/minutes
- Markdown formatting = structured, readable output
- Copy/paste friendly = easy to share

**Intelligence Report Mental Model (What Professionals Expect):**
- Executive summary at top
- Clear sections with headers
- Data tables and visualizations
- Citations and sources
- Professional formatting
- Downloadable/shareable formats (PDF, PPTX)

**User's Hybrid Expectation:**
"ChatGPT ease + analyst-grade intelligence quality + verifiable sources"

**Potential Confusion Points:**
1. **Mode Detection Ambiguity:**
   - Users might not understand why they get different report formats
   - Mitigation: Make mode detection invisible, clarification conversational

2. **Processing Time Expectations:**
   - ChatGPT users expect 5-10 second responses
   - Intelligence reports take 3-5 minutes
   - Mitigation: Clear progress indicators, show what's happening

3. **Citation Verification Workflow:**
   - Users might not know citations are interactive
   - Mitigation: Visual cues (different color, hover state), subtle onboarding

4. **Query Formulation:**
   - Users might over-specify or under-specify queries
   - Mitigation: Handle both gracefully, ask clarifying questions when needed

5. **Report Completeness:**
   - Users might expect instant follow-up generation
   - Mitigation: Set expectations that each report takes minutes, but context is preserved

**Mental Model Advantages:**
- ChatGPT popularity means users already trained on conversational AI
- Professional users understand intelligence report structures
- Existing Passport users know the domain (market intelligence)
- Business professionals understand citation importance

### 2.3 Success Criteria

**Core Experience Success Indicators:**

**1. First Query Completion (Critical Success Moment)**
- **Success:** User's first question produces high-quality, useful intelligence report
- **Measurement:** User completes first query, reads report, explores citations
- **Failure Signal:** User abandons before report completion or immediately leaves after viewing
- **Target:** >80% first-time users complete first query and read report

**2. Citation Interaction (Trust Building)**
- **Success:** User clicks citations to verify sources, feels reassured
- **Measurement:** Citation click rate, time spent on source exploration
- **Failure Signal:** User ignores citations (doesn't trust or doesn't need verification)
- **Target:** >50% of users explore at least one citation per report

**3. Speed Realization (Value Recognition)**
- **Success:** User receives report in <5 minutes, recognizes time saved vs manual approach
- **Measurement:** Actual generation time, user return for second query within session
- **Failure Signal:** Processing takes >10 minutes, user doesn't return
- **Target:** 95% of queries complete in <5 minutes, >60% users ask second question same session

**4. Quality Recognition (Output Validation)**
- **Success:** User reads narrative, recognizes analyst-grade quality, exports/shares
- **Measurement:** Export rate, session duration, qualitative feedback
- **Failure Signal:** User dismisses as generic/unhelpful, doesn't export
- **Target:** >40% of reports exported, average quality rating >4/5

**What Makes Users Say "This Just Works":**
- Query accepted and acknowledged instantly (no loading delay before feedback)
- Progress indicators show specific activity (not just spinners)
- Report appears formatted and professional (not plain text dump)
- Citations visible and verifiable (not hidden or broken links)
- Follow-up questions maintain context naturally (no repetition)
- Export generates clean documents (presentation-ready immediately)

**When Users Feel Smart/Accomplished:**
- Asking complex question and getting comprehensive answer
- Discovering insight in intelligence report they hadn't considered
- Verifying citation and confirming data quality
- Generating multiple reports in time previously needed for one
- Sharing professional intelligence with colleagues/executives

**Feedback Signals for "Doing It Right":**
- Query acknowledged immediately (optimistic UI confirmation)
- Progress messages show system is working intelligently
- Report structure appears organized and complete
- Citations appear inline with narrative (verifiability visible)
- Export completes quickly with professional formatting
- Follow-up questions accepted naturally (context preserved)

**How Fast Should It Feel:**
- **Query input:** Instant acknowledgment (<100ms)
- **Mode detection:** Invisible (no perceived delay)
- **Progress start:** Immediate (<1 second to first progress message)
- **Report generation:** 3-5 minutes average, feels active (progress updates every 10-15 seconds)
- **Citation interaction:** Instant hover preview (<100ms)
- **Export generation:** <10 seconds for PDF/PPTX
- **Follow-up query:** Instant acknowledgment, context retained

**What Should Happen Automatically (No User Intervention):**
- Mode detection from query structure (no "select report type")
- Context retention across follow-up questions (no "remind me what we discussed")
- Citation attribution during narrative generation (not added afterward)
- Quality validation before presentation (internal scoring)
- Data freshness indicators (automatic date stamps)
- Professional formatting and structure (no manual layout)
- Source linking (automatic citation → data source connection)

### 2.4 Novel UX Patterns

**Pattern Classification: Primarily Established, Strategic Innovation**

**Established Patterns (Leverage Familiarity):**

1. **Conversational Interface (ChatGPT Pattern)**
   - **Proven:** Users already trained on ChatGPT interaction model
   - **Our Adoption:** Single input field, multi-turn context, message bubbles
   - **Benefit:** Zero learning curve, immediate user competence

2. **Inline Citations (Perplexity Pattern)**
   - **Proven:** Numbered superscripts for verifiable sources
   - **Our Adoption:** [1], [2] inline citations with hover previews
   - **Benefit:** Trust through transparency, familiar verification pattern

3. **Structured Reports (Bloomberg/Traditional BI Pattern)**
   - **Proven:** Sectioned intelligence reports with headers, data tables
   - **Our Adoption:** Mode-specific section structures (Mode 1's 5 sections, etc.)
   - **Benefit:** Professional credibility, matches analyst expectations

4. **Progress Indicators (Standard SaaS Pattern)**
   - **Proven:** Contextual loading messages showing activity
   - **Our Adoption:** Specific messages ("Analyzing market data...", "Generating insights...")
   - **Benefit:** Reduces anxiety, maintains trust during processing

**Novel/Innovative Patterns:**

1. **Invisible Mode Routing**
   - **Innovation:** Automatic report type detection without user mode selection
   - **Novel Aspect:** Three distinct intelligence formats (Market Overview, Category Deep Dive, Regulatory Impact) delivered based on query structure, not user configuration
   - **Why Novel:** Most BI tools require users to select report type/template; we infer intent
   - **Teaching Strategy:** Make mode detection feel natural through clear report structure; users learn mode patterns through consistent experience
   - **Risk Mitigation:** Clarification questions when confidence <85%, but phrase conversationally

2. **Progressive Intelligence Disclosure**
   - **Innovation:** Reports appear section-by-section as generated (not all-at-once)
   - **Novel Aspect:** User can start reading Executive Summary while Competitive Landscape still generating
   - **Why Novel:** Traditional reports load completely or not at all; we stream intelligence
   - **Teaching Strategy:** Visual indicators show "generating next section..." at bottom
   - **Risk Mitigation:** Ensure partial reports are clearly marked as incomplete

3. **Contextual Citation Density**
   - **Innovation:** Citation frequency adapts to claim type (more for quantitative, fewer for qualitative context)
   - **Novel Aspect:** Not every sentence cited (unlike academic writing), but every data point/claim has verifiable source
   - **Why Novel:** Balance between citation saturation (academic) and citation absence (typical BI)
   - **Teaching Strategy:** Users learn through experience that data = citation, context = narrative
   - **Risk Mitigation:** Clear visual distinction between cited claims and narrative context

**Unique Twist on Established Patterns:**

**ChatGPT Interface + Professional Intelligence Output**
- **Familiar:** Conversational search bar interface
- **Twist:** Output isn't conversational response, it's structured intelligence report
- **Why It Works:** Input familiarity reduces friction; output professionalism builds credibility
- **User Experience:** "ChatGPT ease to ask, analyst quality to receive"

**Perplexity Citations + Bloomberg Authority**
- **Familiar:** Inline numbered citations with hover previews
- **Twist:** Citations link to proprietary knowledge graph data, not web sources
- **Why It Works:** Citation pattern is familiar; data authority is higher (curated intelligence vs open web)
- **User Experience:** "Perplexity transparency with enterprise-grade data quality"

### 2.5 Experience Mechanics

**Core Experience: Natural Language Query → Verified Intelligence Report**

#### 1. Initiation: "How does the user start?"

**Visual Trigger:**
- Prominent, full-width search bar in center of empty state
- Placeholder text: "Ask a question about market intelligence..." (subtle guidance)
- Autofocused on page load (cursor ready, user can start typing immediately)
- Example queries below search bar (educate through examples):
  - "Soft drinks industry in France"
  - "Bottled Water in Brazil - packaging trends"
  - "UK sugar tax impact on soft drinks"

**Interaction Initiation:**
- User clicks into search bar (if not autofocused)
- User begins typing (natural language, no special syntax)
- Search bar expands subtly on focus (visual feedback)
- Submit on Enter key or click "Generate Intelligence" button

**Alternative Entry Points:**
- "New Query" button in header (when viewing previous report)
- Suggested follow-up questions below current report (contextual continuation)
- Command palette (Cmd/Ctrl+K) for power users

**Mental Preparation:**
- No forms, filters, or dropdowns to configure
- No mode selection required (system infers)
- User thinks about business question, not system mechanics

#### 2. Interaction: "What does the user do?"

**Primary User Action:**
- Type natural language query in search bar
- Press Enter or click "Generate Intelligence"

**System Immediate Response (Optimistic UI):**
- Query appears in conversation thread instantly (<100ms)
- Search bar clears, ready for follow-up
- Progress indicator appears immediately: "Understanding your question..."
- Timeline estimate shown: "Typically takes 3-5 minutes"

**System Processing (Visible Intelligence):**
- Progress messages update every 10-15 seconds:
  - "Detecting report type..." (1-2 sec)
  - "Analyzing market data..." (30-45 sec)
  - "Retrieving competitive intelligence..." (30-45 sec)
  - "Generating insights..." (60-90 sec)
  - "Validating citations..." (20-30 sec)
  - "Finalizing report..." (10-15 sec)

**User During Processing:**
- Can read progress messages (stay engaged)
- Can navigate away and return (processing continues)
- Can cancel if needed ("Cancel generation" option)
- Cannot submit new query until current completes (or cancel first)

**Controls:**
- Primary control: Query input field
- Secondary controls: Cancel generation, start new query
- No sliders, toggles, or complex configurations

#### 3. Feedback: "What tells users they're succeeding?"

**Success Signals:**

**Immediate Acknowledgment:**
- Query appears in conversation thread (confirmation of receipt)
- Progress indicator starts showing activity (system is working)
- Visual distinction between user query and system processing (different styling)

**Progressive Feedback:**
- Specific progress messages (not just "loading...")
- Activity indicators (animated icons showing intelligence generation)
- Time remaining updated (if estimable)

**Report Appearance:**
- Executive Summary appears first (fastest section)
- Additional sections load progressively (streaming intelligence)
- Visual indicator: "Generating [Section Name]..." at bottom
- Professional formatting applied (clean, structured, readable)

**Citation Visibility:**
- Inline citations appear with narrative (numbered superscripts [1])
- Hover over citation shows preview (immediate feedback)
- Citation count displayed at bottom: "12 sources cited"

**Quality Signals:**
- Structured sections with clear headers
- Data tables formatted cleanly
- Visualizations embedded (if applicable)
- Professional tone and analyst-grade writing

**What Happens If Mistake:**

**Query Unclear/Ambiguous:**
- System asks clarifying question conversationally
- Example: "I can generate either a Market Overview or Category Deep Dive. Which would you prefer?"
- User selects from options or rephrases query
- No error state, just conversation

**Processing Fails:**
- Clear error message: "I couldn't generate this report. [Specific reason]"
- Suggestions: "Try rephrasing your question" or "Check if this market is in our database"
- Option to retry or contact support
- Error doesn't feel like user's fault (system takes responsibility)

**Data Coverage Gaps:**
- Report generates but includes coverage flags
- Example: "Limited data available for [region/category]. Results may be incomplete."
- Citations show data limitations transparently
- User understands scope without feeling failed

**Low Quality Score:**
- System internally detects quality below threshold
- Either iterates automatically (invisible to user) or presents with caveat
- User sees: "This report has limited insights due to sparse data"
- Still delivers value, sets appropriate expectations

#### 4. Completion: "How do users know they're done?"

**Successful Outcome Signals:**

**Visual Completion:**
- Final section appears (no more "Generating..." indicators)
- Report footer shows completion metadata:
  - "Generated on [date/time]"
  - "[N] sources cited"
  - Quality indicator (if shown): "High confidence" or similar
- Export button becomes active/prominent

**Emotional Completion:**
- User finishes reading report (scrolls to bottom)
- User explores citations (verification complete)
- User feels satisfied ("I got what I needed")
- Sense of accomplishment ("That was fast and useful")

**System Completion:**
- Progress indicator disappears
- Report is fully loaded and formatted
- All citations linked and verifiable
- Export functionality ready

**What's Next? (Natural Continuation):**

**Immediate Next Actions:**
1. **Export Report**
   - Prominent "Export" button in header
   - Click opens format choice (PDF or PPTX)
   - Generates in <10 seconds
   - Downloads automatically

2. **Ask Follow-Up Question**
   - Search bar remains accessible (sticky header)
   - Context preserved from previous query
   - Suggested follow-ups below report:
     - "Tell me more about [specific competitor]"
     - "Show me [adjacent category]"
     - "What are the trends in [related market]?"

3. **Explore Citations**
   - Click any citation number
   - Opens source panel with full metadata
   - Option to view source data directly (if available)
   - Return to narrative easily

4. **Save for Later**
   - Report automatically saved to history (sidebar)
   - Option to bookmark/favorite important reports
   - Access from sidebar anytime

**Session Continuation vs. Completion:**
- **Continue:** User asks follow-up (same mode, related topic)
- **Complete:** User exports and closes tab (task finished)
- **Pause:** User navigates to history, views previous report
- **Restart:** User clicks "New Query" (fresh session, no context)

**Long-term Next:**
- Return to app for next intelligence need (different topic)
- Share exported report with colleagues
- Use intelligence for decision-making
- Build confidence in tool over time (habit formation)

## Visual Design Foundation

### Color System

**Primary Palette: Professional Intelligence**

**Brand Colors:**
- **Primary Blue:** `#2563EB` (Blue-600) - Trust, intelligence, authority
  - Use: Primary actions, links, key UI elements
  - Rationale: Professional, trustworthy, widely associated with business intelligence
  
- **Primary Dark:** `#1E40AF` (Blue-700) - Hover states, emphasis
- **Primary Light:** `#DBEAFE` (Blue-50) - Backgrounds, subtle highlights

**Neutral Grays:**
- **Gray-900:** `#111827` - Primary text, headers
- **Gray-700:** `#374151` - Secondary text, subheaders
- **Gray-500:** `#6B7280` - Tertiary text, metadata
- **Gray-300:** `#D1D5DB` - Borders, dividers
- **Gray-100:** `#F3F4F6` - Backgrounds, surfaces
- **Gray-50:** `#F9FAFB` - Page background, subtle contrast

**Semantic Colors:**
- **Success:** `#10B981` (Green-500) - Confirmations, completed states
- **Warning:** `#F59E0B` (Amber-500) - Cautions, data gaps
- **Error:** `#EF4444` (Red-500) - Errors, failures
- **Info:** `#3B82F6` (Blue-500) - Informational messages, tooltips

**Accent Color (Citations & Interactive):**
- **Accent Orange:** `#F97316` (Orange-500) - Citation highlights, interactive elements
  - Use: Citation superscripts, hover states on data points
  - Rationale: Stands out from blue/gray scheme, draws attention to verifiable sources

**Accessibility Compliance:**
- All text meets WCAG AA contrast ratios (4.5:1 for normal text, 3:1 for large text)
- Primary Blue on White: 7.5:1 (AAA)
- Gray-900 on White: 16.6:1 (AAA)
- Color never used as sole indicator (icons, labels, text supplement)

### Typography System

**Font Family: Inter (Modern, Professional, Readable)**

**Rationale:**
- Excellent readability at all sizes
- Professional SaaS aesthetic (Linear, Stripe, GitHub)
- Great number legibility (critical for data display)
- Variable font support (performance optimized)

**Type Scale:**
- **H1:** 36px (2.25rem) / Bold (700) - Report titles
- **H2:** 30px (1.875rem) / Semibold (600) - Section headers
- **H3:** 24px (1.5rem) / Semibold (600) - Subsections
- **Body:** 16px (1rem) / Regular (400) - Primary content
- **Small:** 14px (0.875rem) / Regular (400) - Metadata, citations

**Data Display:**
- Tabular numbers for consistent alignment
- Monospace for technical data where needed

### Spacing & Layout Foundation

**Spacing Scale: 8px Base Unit (Tailwind Default)**

**Layout Principles:**
- **Information Density Balance:** Bloomberg-style density with Notion-style clarity
- **Consistent Rhythm:** 48px between sections, 24px between components, 16px within components
- **Responsive Scaling:** Desktop-first, reduce spacing 25% on tablets

**App Layout:**
- **Main Content:** Max-width 1000px (optimal reading)
- **Sidebar:** 280px (collapsible for focus)
- **Search Bar:** Max-width 800px (comfortable query entry)
- **Margins:** 32px breathing room

**Component Spacing:**
- Cards: 24-32px padding
- Forms: 40px input height, 16px field spacing
- Buttons: 12px × 8px padding (default)
- Navigation: 40px item height (touch-friendly)

### Accessibility Considerations

- WCAG AA compliant (AAA where possible)
- Keyboard navigation for all interactive elements
- Screen reader support with semantic HTML and ARIA labels
- Minimum 40px touch targets
- Respects prefers-reduced-motion
- Focus indicators on all interactive elements

## User Journey Maps

### Primary User Journey: First-Time Intelligence Generation

**Journey: New User → First Intelligence Report → Trust Building**

**1. Discovery & Landing (Entry Point)**
- User arrives via direct URL or referral
- Sees clean interface with prominent search bar
- Example queries provide immediate context
- Value proposition clear: "Ask questions, get intelligence"

**2. First Query (Critical Moment)**
- User types natural language question
- System immediately acknowledges (optimistic UI)
- Progress indicators show activity ("Analyzing market data...")
- User remains engaged during 3-5 minute generation

**3. Report Receipt (Aha Moment)**
- Structured intelligence report appears
- Professional formatting immediately visible
- Citations inline throughout narrative
- User recognizes analyst-grade quality

**4. Citation Exploration (Trust Building)**
- User hovers over citation, sees preview
- Clicks to explore source data
- Verifies claim accuracy
- Trust established through transparency

**5. Follow-Up or Export (Value Confirmation)**
- User either asks follow-up question OR exports report
- Context maintained for follow-ups
- Export generates presentation-ready document
- User realizes value ("This is much faster than manual research")

**6. Return Visit (Habit Formation)**
- User returns for next intelligence need
- Familiar with interaction pattern
- Increased confidence in system
- Becomes regular user

### Secondary Journey: Expert User Power Workflow

**Journey: Experienced User → Multiple Reports → Complex Analysis**

**1. Quick Entry**
- Command palette (Cmd+K) for instant access
- Recent queries in sidebar for reference
- Muscle memory for keyboard shortcuts

**2. Rapid Querying**
- Natural language query without hesitation
- Context from previous session preserved
- Multiple queries in single session

**3. Cross-Report Analysis**
- Reviews multiple intelligence reports
- Compares insights across reports
- Builds comprehensive strategic view

**4. Export & Share**
- Bulk export multiple reports
- Shares with team members
- Uses intelligence for decision presentations

## Component Strategy

### Core Components (MVP Priority)

**Conversational Interface:**
1. **SearchBar** - Primary query input with autofocus, placeholder guidance
2. **ConversationThread** - Query/response pairs with clear visual distinction
3. **ProgressIndicator** - Contextual processing messages with activity feedback

**Intelligence Display:**
4. **IntelligenceReport** - Container with mode-specific structure
5. **ReportSection** - Collapsible sections with headers and content
6. **Citation** - Inline superscript with hover preview, click to expand
7. **CitationCard** - Hover overlay showing source metadata
8. **DataTable** - Formatted tables with proper alignment and styling

**Navigation & Layout:**
9. **AppShell** - Main layout structure (header, sidebar, content)
10. **Sidebar** - History navigation, saved reports access
11. **Header** - App branding, user menu, export action

**Utility:**
12. **ExportButton** - PDF/PPTX generation with loading states
13. **ErrorMessage** - Clear, helpful error communication
14. **EmptyState** - First-time user guidance with examples

### Component Patterns

**Progressive Disclosure:**
- Simple by default, complexity revealed contextually
- Example: Citations visible but non-intrusive, hover for details

**Optimistic UI:**
- Immediate visual feedback before server response
- Example: Query appears in thread instantly, processing begins

**Loading States:**
- Never blank spinners, always contextual messages
- Example: "Analyzing market data..." not just "Loading..."

**Error Handling:**
- Graceful degradation with helpful guidance
- Example: "Try rephrasing" not "Error 500"

## Key UX Patterns

### Natural Language Query Pattern
- **Implementation:** Single search bar, no syntax required
- **Benefit:** Zero learning curve, ChatGPT familiarity
- **Details:** Full-width input, autofocus, example queries below

### Inline Citation Pattern
- **Implementation:** Numbered superscripts [1] throughout narrative
- **Benefit:** Trust through transparency, Perplexity familiarity
- **Details:** Hover preview, click to expand, accent color distinction

### Progressive Report Loading Pattern
- **Implementation:** Sections stream as generated
- **Benefit:** Reduces perceived latency, maintains engagement
- **Details:** Executive summary first, subsequent sections follow

### Contextual Progress Pattern
- **Implementation:** Specific activity messages during processing
- **Benefit:** User understands what's happening, feels intelligent
- **Details:** "Analyzing market data...", "Generating insights...", "Validating citations..."

### Mode Detection Invisibility Pattern
- **Implementation:** Automatic report type inference
- **Benefit:** No cognitive overhead for mode selection
- **Details:** Clarification only when confidence <85%, conversational phrasing

### Command Palette Pattern (Power Users)
- **Implementation:** Cmd/Ctrl+K for quick actions
- **Benefit:** Keyboard efficiency for frequent users
- **Details:** New query, export, settings access

## Implementation Next Steps

### Phase 1: Foundation (Weeks 1-2)
**Goal:** Technical foundation and design system setup

**Deliverables:**
- Initialize React + TypeScript + Tailwind project
- Install and configure shadcn/ui components
- Set up design tokens (colors, typography, spacing)
- Create base layout components (AppShell, Header, Sidebar)
- Implement authentication flow (simple email/password)

**Success Criteria:**
- App loads with design system applied
- Users can log in/out
- Basic navigation functional

### Phase 2: Core Experience (Weeks 3-5)
**Goal:** Implement primary user flow (query → intelligence report)

**Deliverables:**
- SearchBar component with autofocus and examples
- Query submission and backend integration
- ProgressIndicator with contextual messages
- IntelligenceReport display with sectioned structure
- Citation components (inline superscripts, hover previews)
- Basic export functionality (PDF generation)

**Success Criteria:**
- Users can submit queries
- Intelligence reports display formatted
- Citations are interactive
- Export generates downloadable PDF

### Phase 3: Trust & Polish (Weeks 6-7)
**Goal:** Build trust through transparency and professional polish

**Deliverables:**
- Enhanced citation exploration (source panel, metadata)
- Multi-turn conversation with context retention
- Sidebar history and saved reports
- Error handling and graceful degradation
- Loading states and optimistic UI refinements
- Accessibility audit and fixes

**Success Criteria:**
- Citation workflow complete and intuitive
- Follow-up questions maintain context
- All interactions feel polished
- WCAG AA compliance verified

### Phase 4: Beta & Iteration (Week 8+)
**Goal:** User testing and refinement

**Deliverables:**
- Beta testing with target users (analysts, category managers)
- User feedback collection and analysis
- Iteration on pain points and confusion areas
- Performance optimization
- Documentation and onboarding materials

**Success Criteria:**
- >80% first-query completion rate
- >50% citation exploration rate
- >40% export rate
- Positive user feedback on speed and quality

## Success Metrics & Validation

### Product Metrics
- **First Query Completion:** >80% of new users complete first query
- **Citation Interaction:** >50% explore at least one citation
- **Speed Target:** 95% of queries complete in <5 minutes
- **Export Rate:** >40% of reports exported
- **Return Rate:** >60% ask second question same session

### User Experience Metrics
- **Task Completion Rate:** >90% successfully generate needed intelligence
- **Time on Task:** Average <10 minutes per intelligence need (vs hours/days manually)
- **Error Rate:** <5% queries fail or produce unusable reports
- **User Satisfaction:** >4.0/5.0 average rating

### Trust Metrics
- **Citation Click Rate:** >50% of users verify sources
- **Quality Confidence:** >80% users trust intelligence enough to act on it
- **Sharing Behavior:** >40% share reports with colleagues
- **Repeat Usage:** >70% return within 7 days

## Conclusion

This UX design specification provides a comprehensive foundation for building the AI-Powered Intelligence Assistant. The design philosophy—"ChatGPT Simplicity + Perplexity Citations + Bloomberg Authority"—ensures the product is both accessible and professional.

**Key Design Principles:**
1. Natural language interface eliminates learning curve
2. Inline citations build trust through transparency
3. Contextual progress indicators maintain engagement during processing
4. Professional formatting establishes credibility
5. MVP focus ensures core experience excellence before feature expansion

**Critical Success Factors:**
- First query must succeed (aha moment)
- Citations must be verifiable (trust building)
- Speed must feel fast even when processing takes minutes (progress feedback)
- Quality must match analyst-grade expectations (professional output)

**Design System Foundation:**
- Tailwind CSS + shadcn/ui for rapid development with full control
- Professional blue/gray color palette with accent orange for citations
- Inter typography for readability and modern aesthetic
- 8px spacing system for consistent rhythm
- WCAG AA accessibility compliance

This specification serves as the blueprint for implementation, ensuring all design decisions align with user needs, emotional goals, and technical requirements. The standalone MVP approach allows rapid iteration and validation before potential Passport integration.

**Next Steps:** Begin Phase 1 implementation (Foundation) and iterate based on user feedback throughout development.

---

**UX Design Specification Complete**
**Document Generated:** 2026-01-21
**For:** euromonitor-multi-agent-architecture (AI-Powered Intelligence Assistant)
