# Knowledge Graph Ontology Design
## Passport AI Intelligence Assistant - Deep Technical Architecture

**Author:** Winston (Architect Agent) + Karthikmg
**Date:** 2026-01-23
**Status:** Design Phase - Ontology Modeling

---

## Executive Summary

This document defines the **complete ontology** (node types, relationship types, properties, and constraints) for the Passport AI Intelligence Assistant Knowledge Graph, based on reverse-engineering real Euromonitor Passport data (Toys & Games India dataset).

**Key Decisions:**
1. **Hybrid Graph + Vector Architecture:** Neo4j with vector search plugin for unified structured + semantic search
2. **Citation-First Design:** Every data point traceable to source
3. **Temporal Modeling:** Time-series data as properties vs relationships (decision documented below)
4. **4-Phase Construction:** Pilot → Structured → Unstructured → Citations

---

## Table of Contents

1. [Passport Data Model Analysis](#1-passport-data-model-analysis)
2. [Core Ontology Design](#2-core-ontology-design)
3. [Node Types & Properties](#3-node-types--properties)
4. [Relationship Types](#4-relationship-types)
5. [Temporal Data Modeling](#5-temporal-data-modeling)
6. [Citation Graph Design](#6-citation-graph-design)
7. [Unstructured Data Integration](#7-unstructured-data-integration)
8. [Alternative Architectures Evaluated](#8-alternative-architectures-evaluated)
9. [Implementation Recommendations](#9-implementation-recommendations)

---

## 1. Passport Data Model Analysis

### Real Data Structure (from Toys & Games India)

**Source File:** `docs/data-samples/Toys_and_Games_in_India(Full_Dataset).xlsx`

**20 Sheets Identified:**
1. **Market Sizes** (1435 rows): Time-series market data by category/geography
2. **Market Size Unit Price** (88 rows): Average unit prices over time
3. **Company Share NBO** (638 rows): National Brand Owner market shares
4. **Company Share GBO**: Global Brand Owner market shares
5. **Brand Share LBN** (695 rows): Local Brand Name market shares
6. **Brand Share GBN**: Global Brand Name market shares
7. **Channel** (distribution channel analysis)
8. **Analysis by Licensing**: Licensing-specific metrics
9. **Blind Collectables**: Subcategory-specific analysis
10. **Video Games Software by Format**: Format-specific breakdown
11. **Brand Definitions** (metadata): Brand → Company mappings
12. **Category Definitions** (51 categories): Category taxonomy with hierarchy levels 0-5
13. **Channel Definitions**: Channel/outlet taxonomy
14. **Calculation Variables**: Methodology notes
15. **Sources** (140 sources): Citation metadata

### Core Entities Identified

**1. Geography Hierarchy**
```
Region (e.g., "Asia Pacific")
  └─ Country (e.g., "India")
```

**2. Category Taxonomy (6 levels: 0-5)**
```
Industry (Level 0, e.g., "Toys and Games")
  ├─ Major Segment (Level 1, e.g., "Traditional Toys and Games", "Video Games")
  │   ├─ Category (Level 2, e.g., "Action Figures", "Arts and Crafts", "Video Games Software")
  │   │   ├─ Subcategory (Level 3, e.g., "Hand-Held Consoles", "Static Consoles")
  │   │   │   ├─ Sub-Subcategory (Level 4, e.g., "Console Games (Physical)", "Computer Games (Digital)")
  │   │   │   │   └─ Granular (Level 5, e.g., "Console Games (Physical)" nested)
```

**3. Company & Brand Hierarchy**
```
Global Brand Owner (GBO)
  └─ National Brand Owner (NBO, e.g., "Sony India Pvt Ltd")
      ├─ Global Brand Name (GBN)
      │   └─ Local Brand Name (LBN, e.g., "PlayStation")
```

**4. Distribution Channels**
```
Channel Type (e.g., "Retail", "Ecommerce")
  └─ Outlet (e.g., "Amazon India", "Reliance Retail")
```

**5. Time-Series Data**
- Historical: 2010-2024 (actual data)
- Forecast: 2025-2029 (projections)
- Metrics: Market size (CHF million), Unit prices (INR), Market shares (%)

**6. Sources & Citations**
- Official sources (e.g., "NCAER", "Prowess Database")
- Company reports
- Trade publications
- Euromonitor analyst research

---

## 2. Core Ontology Design

### Design Principles

1. **Preserve Passport Taxonomy:** Map 1:1 to existing Passport structure (no abstraction layers)
2. **Citation Transparency:** Every data node links to source(s)
3. **Query Performance:** Index heavily-queried properties (geography, category, year)
4. **Temporal Flexibility:** Support both time-series queries and snapshot queries
5. **Extensibility:** Design for future categories/geographies without schema changes

### Ontology Overview

**11 Core Node Labels:**
1. `Geography` (Region, Country)
2. `Category` (Industry, Segment, Category, Subcategory - all levels)
3. `Company` (NBO and GBO)
4. `Brand` (LBN and GBN)
5. `Channel` (Distribution outlets)
6. `MarketData` (Time-series data points)
7. `MarketSize` (Specific metric type)
8. `MarketShare` (Company/brand share data)
9. `UnitPrice` (Price data)
10. `Source` (Citation sources)
11. `Report` (Unstructured documents - Phase 3)

**12 Core Relationship Types:**
1. `LOCATED_IN` (Country → Region)
2. `BELONGS_TO` (Category → Parent Category)
3. `HAS_DATA` (Geography + Category → MarketData)
4. `MEASURED_IN` (MarketData → Unit)
5. `SOURCED_FROM` (MarketData → Source)
6. `OWNED_BY` (Brand → Company)
7. `OPERATES_IN` (Company → Geography)
8. `COMPETES_IN` (Company → Category + Geography)
9. `DISTRIBUTED_VIA` (Category → Channel in Geography)
10. `HAS_SHARE` (Company/Brand → MarketShare)
11. `MENTIONS` (Report → Category/Company/Brand - Phase 3)
12. `CITES` (Report → Source - Phase 3)

---

## 3. Node Types & Properties

### 3.1 Geography Nodes

**Label:** `(:Geography)`

**Properties:**
```cypher
{
  id: "geo_india",                    // Unique identifier
  name: "India",                      // Display name
  type: "Country",                    // "Region", "Country", "State", "City"
  level: 1,                           // Hierarchy level (0=Region, 1=Country, etc.)
  iso_code: "IN",                     // ISO 3166 country code
  region: "Asia Pacific",             // Parent region name
  population_2024: 1450000000,        // Current population (for per-capita calculations)
  created_at: datetime(),
  updated_at: datetime()
}
```

**Indexes:**
```cypher
CREATE INDEX geography_id FOR (g:Geography) ON (g.id);
CREATE INDEX geography_name FOR (g:Geography) ON (g.name);
CREATE TEXT INDEX geography_search FOR (g:Geography) ON (g.name);
```

**Sample Cypher:**
```cypher
CREATE (:Geography {
  id: "geo_india",
  name: "India",
  type: "Country",
  level: 1,
  iso_code: "IN",
  region: "Asia Pacific",
  population_2024: 1450000000
})
```

---

### 3.2 Category Nodes

**Label:** `(:Category)`

**Properties:**
```cypher
{
  id: "cat_toys_games",               // Unique identifier
  name: "Toys and Games",             // Display name
  full_name: "Toys and Games",        // Full path name (for disambiguation)
  level: 0,                           // Hierarchy level (0-5)
  industry: "Toys and Games",         // Root industry
  parent_id: null,                    // Parent category ID (null for root)
  definition: "This is the aggregation of traditional...", // From Category Definitions sheet
  is_lowest_level: false,             // Whether this is a leaf node
  created_at: datetime(),
  updated_at: datetime()
}
```

**Indexes:**
```cypher
CREATE INDEX category_id FOR (c:Category) ON (c.id);
CREATE INDEX category_name FOR (c:Category) ON (c.name);
CREATE INDEX category_level FOR (c:Category) ON (c.level);
CREATE TEXT INDEX category_search FOR (c:Category) ON (c.name, c.definition);
```

**Example Hierarchy:**
```cypher
// Level 0: Industry
CREATE (:Category {id: "cat_toys_games", name: "Toys and Games", level: 0, parent_id: null})

// Level 1: Major Segments
CREATE (:Category {id: "cat_traditional", name: "Traditional Toys and Games", level: 1, parent_id: "cat_toys_games"})
CREATE (:Category {id: "cat_video_games", name: "Video Games", level: 1, parent_id: "cat_toys_games"})

// Level 2: Categories
CREATE (:Category {id: "cat_action_figures", name: "Action Figures and Accessories", level: 2, parent_id: "cat_traditional"})
CREATE (:Category {id: "cat_arts_crafts", name: "Arts and Crafts", level: 2, parent_id: "cat_traditional"})
CREATE (:Category {id: "cat_vg_software", name: "Video Games Software", level: 2, parent_id: "cat_video_games"})

// Level 3: Subcategories
CREATE (:Category {id: "cat_vg_handheld", name: "Hand-Held Consoles", level: 3, parent_id: "cat_video_games"})
CREATE (:Category {id: "cat_vg_static", name: "Static Consoles", level: 3, parent_id: "cat_video_games"})
```

---

### 3.3 Company Nodes

**Label:** `(:Company)`

**Properties:**
```cypher
{
  id: "comp_sony_india",              // Unique identifier
  name: "Sony India Pvt Ltd",         // Full legal name
  short_name: "Sony India",           // Short/display name
  type: "NBO",                        // "NBO" (National) or "GBO" (Global)
  parent_company_id: "comp_sony_global", // GBO parent (if NBO)
  headquarters_country: "India",      // Where company is based
  founded_year: 1996,
  website: "https://www.sony.co.in",
  created_at: datetime(),
  updated_at: datetime()
}
```

**Indexes:**
```cypher
CREATE INDEX company_id FOR (c:Company) ON (c.id);
CREATE INDEX company_name FOR (c:Company) ON (c.name);
CREATE INDEX company_type FOR (c:Company) ON (c.type);
CREATE TEXT INDEX company_search FOR (c:Company) ON (c.name, c.short_name);
```

---

### 3.4 Brand Nodes

**Label:** `(:Brand)`

**Properties:**
```cypher
{
  id: "brand_playstation",            // Unique identifier
  name: "PlayStation",                // Brand name
  type: "GBN",                        // "LBN" (Local) or "GBN" (Global)
  owner_company_id: "comp_sony_india", // Owning company (NBO or GBO)
  parent_brand_id: "brand_playstation_global", // GBN parent (if LBN)
  launch_year: 1994,
  website: "https://www.playstation.com",
  created_at: datetime(),
  updated_at: datetime()
}
```

**Indexes:**
```cypher
CREATE INDEX brand_id FOR (b:Brand) ON (b.id);
CREATE INDEX brand_name FOR (b:Brand) ON (b.name);
CREATE INDEX brand_type FOR (b:Brand) ON (b.type);
CREATE TEXT INDEX brand_search FOR (b:Brand) ON (b.name);
```

---

### 3.5 Channel Nodes

**Label:** `(:Channel)`

**Properties:**
```cypher
{
  id: "channel_amazon_india",         // Unique identifier
  name: "Amazon India",               // Channel/outlet name
  type: "Ecommerce",                  // "Retail", "Ecommerce", "Specialty", etc.
  parent_channel_id: "channel_ecommerce_generic", // Parent channel type
  geography_id: "geo_india",          // Where this channel operates
  created_at: datetime(),
  updated_at: datetime()
}
```

---

### 3.6 MarketData Nodes (Abstract)

**DESIGN DECISION:** Time-series data modeling approach

**Option A: Properties (RECOMMENDED)**
- Store time-series as JSON/Map property on relationship
- Example: `{2020: 1792.28, 2021: 1959.91, 2022: 2270.93, ...}`
- **Pros:** Compact, fast range queries, simple schema
- **Cons:** Less flexible for complex temporal queries

**Option B: Separate Nodes per Year**
- Create `(:MarketSize {year: 2020, value: 1792.28})` nodes
- **Pros:** Maximum query flexibility, easier to add metadata per year
- **Cons:** 20x more nodes (20 years × all data points), complex queries

**CHOSEN: Option A (Properties)** - See Section 5 for detailed rationale

**Label:** `(:MarketSize)` (subtype of MarketData)

**Properties:**
```cypher
{
  id: "ms_toys_india_retail_value",   // Unique identifier
  geography_id: "geo_india",          // Geography reference
  category_id: "cat_toys_games",      // Category reference
  data_type: "Retail Value RSP",      // Type of metric
  unit: "CHF million",                // Unit of measurement
  currency: "CHF",                    // Currency code
  current_constant: "Historic Current Prices, Forecast Constant 2024", // Pricing basis

  // Time-series data (20 years)
  historical_data: {                  // Map/JSON of year → value
    "2010": 1180.776,
    "2011": 1145.577,
    "2012": 1217.729,
    // ... 2013-2023
    "2024": 2795.550
  },
  forecast_data: {                    // Forecast values
    "2025": 3130.127,
    "2026": 3432.431,
    "2027": 3712.015,
    "2028": 3974.632,
    "2029": 4233.641
  },

  // Growth metrics
  historic_cagr: 7.212105,            // 2019-2024 CAGR
  forecast_cagr: 8.654907,            // 2024-2029 CAGR

  // Per-capita data (optional)
  per_capita_data: {                  // Map of year → per capita value
    "2024": 1.927,                    // CHF per person
    "2025": 2.138,
    // ...
  },

  // Metadata
  source_ids: ["source_ncaer", "source_prowess"], // Citation sources
  last_updated: datetime("2025-01-15"),
  methodology_notes: "Calculated using...",

  created_at: datetime(),
  updated_at: datetime()
}
```

**Indexes:**
```cypher
CREATE INDEX market_size_id FOR (ms:MarketSize) ON (ms.id);
CREATE INDEX market_size_geo FOR (ms:MarketSize) ON (ms.geography_id);
CREATE INDEX market_size_cat FOR (ms:MarketSize) ON (ms.category_id);
CREATE COMPOSITE INDEX market_size_geo_cat FOR (ms:MarketSize) ON (ms.geography_id, ms.category_id);
```

---

### 3.7 MarketShare Nodes

**Label:** `(:MarketShare)` (subtype of MarketData)

**Properties:**
```cypher
{
  id: "share_sony_india_toys",        // Unique identifier
  geography_id: "geo_india",          // Geography
  category_id: "cat_toys_games",      // Category
  company_id: "comp_sony_india",      // Company (for company share)
  brand_id: "brand_playstation",      // Brand (for brand share, optional)
  share_type: "NBO",                  // "NBO", "GBO", "LBN", "GBN"
  data_type: "Market Share",
  unit: "% value",

  // Time-series share data (percentages)
  share_data: {                       // Map of year → share %
    "2015": 15.2,
    "2016": 14.8,
    // ... 2017-2023
    "2024": 18.5
  },

  // Growth metrics
  historic_cagr: 8.749338,            // 2019-2024 CAGR

  source_ids: ["source_company_reports"],
  last_updated: datetime("2025-01-15"),

  created_at: datetime(),
  updated_at: datetime()
}
```

---

### 3.8 Source Nodes

**Label:** `(:Source)`

**Properties:**
```cypher
{
  id: "source_ncaer",                 // Unique identifier
  name: "National Council of Applied Economic Research (NCAER)", // Full name
  short_name: "NCAER",                // Abbreviation
  type: "Official Source",            // "Official Source", "Company Report", "Trade Publication", "Analyst Research"
  url: "https://www.ncaer.org",       // Website
  description: "Independent, non-profit economic policy research institute",
  credibility_score: 0.95,            // 0-1 score for source quality (internal)

  // Citation metadata
  access_date: date("2025-01-15"),    // When Euromonitor accessed this source
  publication_date: date("2024-12-01"), // When source published data

  created_at: datetime(),
  updated_at: datetime()
}
```

**Indexes:**
```cypher
CREATE INDEX source_id FOR (s:Source) ON (s.id);
CREATE INDEX source_name FOR (s:Source) ON (s.name);
CREATE TEXT INDEX source_search FOR (s:Source) ON (s.name, s.description);
```

---

### 3.9 Report Nodes (Phase 3 - Unstructured Data)

**Label:** `(:Report)`

**Properties:**
```cypher
{
  id: "report_toys_india_2025",       // Unique identifier
  title: "Toys and Games in India",   // Report title
  type: "Country Report",             // "Country Report", "Category Report", "Regulatory Brief"
  publication_date: date("2025-01-10"),
  author: "Euromonitor Analyst Team",
  geography_ids: ["geo_india"],       // Geographies covered
  category_ids: ["cat_toys_games"],   // Categories covered

  // Document content
  abstract: "Overview of the Indian toys market...", // Summary
  full_text: "The Indian toys and games market...", // Full text (for search)
  pdf_url: "s3://passport/reports/toys_india_2025.pdf", // File location
  page_count: 45,

  // Vector embedding (Phase 3)
  embedding: [0.123, 0.456, ...],     // 1536-dim vector (Claude/OpenAI embeddings)

  // Metadata
  source_ids: ["source_euromonitor"],  // Authoring organization
  related_report_ids: ["report_toys_asia_2025"], // Related reports

  created_at: datetime(),
  updated_at: datetime()
}
```

**Vector Index (Phase 3):**
```cypher
CREATE VECTOR INDEX report_embedding FOR (r:Report) ON (r.embedding)
OPTIONS {indexConfig: {
  `vector.dimensions`: 1536,
  `vector.similarity_function`: 'cosine'
}};
```

---

## 4. Relationship Types

### 4.1 Geography Relationships

**`LOCATED_IN`**
```cypher
// Country → Region
(:Geography {type: "Country"})-[:LOCATED_IN]->(:Geography {type: "Region"})

Example:
(:Geography {name: "India"})-[:LOCATED_IN]->(:Geography {name: "Asia Pacific"})
```

---

### 4.2 Category Relationships

**`BELONGS_TO`** (Child → Parent in hierarchy)
```cypher
(:Category {level: n})-[:BELONGS_TO]->(:Category {level: n-1})

Example:
(:Category {name: "Video Games", level: 1})-[:BELONGS_TO]->(:Category {name: "Toys and Games", level: 0})
(:Category {name: "Hand-Held Consoles", level: 3})-[:BELONGS_TO]->(:Category {name: "Video Games", level: 1})
```

**Properties on BELONGS_TO:**
```cypher
{
  hierarchy_path: "Toys and Games > Video Games > Hand-Held Consoles", // Full path
  created_at: datetime()
}
```

---

### 4.3 Data Relationships

**`HAS_MARKET_SIZE`** (Geography + Category → MarketSize data)
```cypher
(:Geography)-[:HAS_MARKET_SIZE]->(:MarketSize)<-[:HAS_MARKET_SIZE]-(:Category)

Example:
(:Geography {name: "India"})-[:HAS_MARKET_SIZE {year_range: "2010-2029"}]->
  (:MarketSize {id: "ms_toys_india_retail_value"})
  <-[:HAS_MARKET_SIZE]-(:Category {name: "Toys and Games"})
```

**Alternative pattern (denormalized):**
```cypher
(:Geography)-[:HAS_DATA {
  data_type: "MarketSize",
  unit: "CHF million",
  years: {2024: 2795.55, 2025: 3130.13, ...}
}]->(:Category)
```

**DECISION:** Use `(:MarketSize)` nodes with bidirectional `HAS_MARKET_SIZE` relationships for:
- Better citation tracking (one MarketSize → many Sources)
- Easier to query specific metrics
- Cleaner separation of concerns

---

### 4.4 Company & Brand Relationships

**`OWNED_BY`** (Brand → Company)
```cypher
(:Brand {name: "PlayStation"})-[:OWNED_BY {since: 1994}]->(:Company {name: "Sony India Pvt Ltd"})
```

**`PARENT_COMPANY`** (NBO → GBO)
```cypher
(:Company {type: "NBO", name: "Sony India Pvt Ltd"})-[:PARENT_COMPANY]->(:Company {type: "GBO", name: "Sony Corporation"})
```

**`COMPETES_IN`** (Company → Category + Geography)
```cypher
(:Company {name: "Sony India"})-[:COMPETES_IN {
  market_share_2024: 18.5,
  rank: 1
}]->(:Category {name: "Video Games"})

// AND

(:Company {name: "Sony India"})-[:OPERATES_IN {since: 1996}]->(:Geography {name: "India"})
```

---

### 4.5 Citation Relationships

**`SOURCED_FROM`** (Data → Source)
```cypher
(:MarketSize {id: "ms_toys_india"})-[:SOURCED_FROM {
  confidence: 0.95,
  page_reference: "Page 12",
  accessed_date: date("2025-01-15")
}]->(:Source {name: "NCAER"})
```

**Multiple sources:**
```cypher
(:MarketSize)-[:SOURCED_FROM]->(:Source {name: "NCAER"})
(:MarketSize)-[:SOURCED_FROM]->(:Source {name: "Prowess Database"})
```

---

### 4.6 Unstructured Content Relationships (Phase 3)

**`MENTIONS`** (Report → Entity)
```cypher
(:Report {title: "Toys in India"})-[:MENTIONS {
  page: 15,
  context: "Sony India dominates the video games segment...",
  sentiment: "positive"
}]->(:Company {name: "Sony India"})

(:Report)-[:MENTIONS]->(:Category)
(:Report)-[:MENTIONS]->(:Brand)
(:Report)-[:MENTIONS]->(:Geography)
```

**`CITES`** (Report → Source)
```cypher
(:Report)-[:CITES {page: 45, citation_style: "footnote"}]->(:Source {name: "NCAER"})
```

---

## 5. Temporal Data Modeling

### The Time-Series Problem

**Question:** How do we store 20 years of data (2010-2029) for each metric?

**Option 1: Properties on Nodes (RECOMMENDED)**
```cypher
(:MarketSize {
  geography_id: "geo_india",
  category_id: "cat_toys_games",
  data: {
    "2010": 1180.78,
    "2011": 1145.58,
    // ... 18 more years
    "2029": 4233.64
  }
})
```

**Option 2: Properties on Relationships**
```cypher
(:Geography)-[:HAS_DATA {
  years: {2010: 1180.78, 2011: 1145.58, ...}
}]->(:Category)
```

**Option 3: Separate Nodes per Year**
```cypher
(:MarketSize {year: 2010, value: 1180.78})-[:FOR_YEAR]->(:Year {year: 2010})
(:MarketSize {year: 2011, value: 1145.58})-[:FOR_YEAR]->(:Year {year: 2011})
// ... 20 separate nodes per metric
```

### Decision Matrix

| Criterion | Option 1 (Node Props) | Option 2 (Rel Props) | Option 3 (Year Nodes) |
|-----------|----------------------|---------------------|----------------------|
| **Storage Efficiency** | ✅ Excellent (compact) | ✅ Excellent | ❌ Poor (20x nodes) |
| **Query Speed (single metric)** | ✅ Fast (1 lookup) | ✅ Fast | ⚠️ Medium (traverse) |
| **Query Speed (time range)** | ✅ Fast (JSON slice) | ✅ Fast | ❌ Slow (many nodes) |
| **Citation Tracking** | ✅ Easy (node → sources) | ⚠️ Harder (rel props) | ✅ Easy |
| **Schema Simplicity** | ✅ Simple | ✅ Simple | ❌ Complex |
| **Temporal Query Flexibility** | ⚠️ Limited (no native time queries) | ⚠️ Limited | ✅ Maximum (Cypher temporal) |
| **Extensibility (add years)** | ✅ Easy (update map) | ✅ Easy | ⚠️ Medium (new nodes) |

### DECISION: Option 1 (Properties on Nodes)

**Rationale:**
1. **Storage:** Passport has millions of data points. 20x node explosion is prohibitive.
2. **Query patterns:** Most queries fetch full time-series for charting ("Show me market size 2010-2029"), not individual years.
3. **Citation:** Need `(:MarketSize)-[:SOURCED_FROM]->(:Source)` relationships, which are cleaner with node-based approach.
4. **Neo4j Performance:** Map properties are performant for <100 key-value pairs.

**Trade-off Accepted:** Less flexible for complex temporal queries (e.g., "Find all categories where 2023 value > 2022 value by >10%"). We can compensate with:
- Pre-computed growth metrics (historic_cagr, forecast_cagr as properties)
- Application-layer filtering if needed

**Example Query:**
```cypher
// Fetch full time-series for a geography + category
MATCH (g:Geography {name: "India"})-[:HAS_MARKET_SIZE]->(ms:MarketSize)<-[:HAS_MARKET_SIZE]-(c:Category {name: "Toys and Games"})
RETURN ms.historical_data, ms.forecast_data
```

---

## 6. Citation Graph Design

### 100% Accuracy Requirement

**Problem Statement:** Every AI-generated claim must be traceable to a Passport source with 100% accuracy.

**Example Claim:**
> "The Indian toys and games market grew from 1,973 million CHF in 2019 to 2,796 million CHF in 2024, a CAGR of 7.2%."

**Required Citation:**
- **Source:** Euromonitor Passport - Market Sizes, Toys and Games in India (2025 Edition)
- **Metric:** Retail Value RSP (CHF million)
- **Data:** 2019=1973.55, 2024=2795.55
- **CAGR Calculation:** Verified as 7.21% (matches published CAGR)

### Citation Graph Structure

**`Source` → `MarketSize` → `Narrative Claim`**

**1. Source Node (already defined)**
```cypher
(:Source {
  id: "source_passport_toys_india_2025",
  name: "Euromonitor Passport - Toys and Games in India",
  edition: "2025",
  type: "Analyst Research",
  publication_date: date("2025-01-10"),
  url: "https://passport.euromonitor.com/...",
  access_date: date("2025-01-15")
})
```

**2. MarketSize Node (with source linkage)**
```cypher
(:MarketSize {id: "ms_toys_india"})-[:SOURCED_FROM {
  dataset: "Market Sizes",
  sheet: "Market Sizes",
  row_number: 3,
  confidence: 1.0,  // 100% confidence (primary data)
  derivation: "direct"  // "direct" vs "calculated" (e.g., CAGR)
}]->(:Source {id: "source_passport_toys_india_2025"})
```

**3. Citation Validation**

When AI generates narrative, Citation Specialist agent:
1. **Extracts claim:** "market grew to 2,796 million CHF in 2024"
2. **Identifies metric:** Market size, India, Toys and Games, 2024
3. **Queries KG:**
   ```cypher
   MATCH (ms:MarketSize {geography_id: "geo_india", category_id: "cat_toys_games"})
   RETURN ms.historical_data["2024"] AS value_2024, ms.source_ids
   ```
4. **Validates:** value_2024 = 2795.55 ≈ 2796 (rounded) ✅
5. **Fetches sources:**
   ```cypher
   MATCH (ms:MarketSize {id: "ms_toys_india"})-[r:SOURCED_FROM]->(s:Source)
   RETURN s.name, s.url, r.dataset, r.confidence
   ```
6. **Generates citation:** [1] Euromonitor Passport, Market Sizes, Toys and Games in India (2025)

**4. Citation Object (stored with generated report)**
```json
{
  "claim": "The Indian toys market grew to 2,796 million CHF in 2024",
  "metric_id": "ms_toys_india",
  "data_point": {
    "year": 2024,
    "value": 2795.55,
    "unit": "CHF million",
    "rounded_display": 2796
  },
  "sources": [
    {
      "source_id": "source_passport_toys_india_2025",
      "name": "Euromonitor Passport - Toys and Games in India (2025)",
      "url": "https://passport.euromonitor.com/...",
      "dataset": "Market Sizes",
      "confidence": 1.0
    }
  ],
  "validation_status": "verified",
  "validated_at": "2025-01-23T10:30:00Z"
}
```

### Derived Metrics (e.g., CAGR)

**Challenge:** CAGR is calculated, not directly from Passport. How to cite?

**Solution:** Calculate and validate against Passport's published CAGR.

```cypher
// Passport provides pre-calculated CAGR
(:MarketSize {
  historic_cagr: 7.212105,  // Passport-published CAGR 2019-2024
  data: {2019: 1973.55, 2024: 2795.55}
})

// AI calculates: CAGR = ((2795.55 / 1973.55)^(1/5)) - 1 = 7.21%
// Validation: AI_CAGR ≈ Passport_CAGR (within 0.01% tolerance) ✅
```

**Citation:**
> "7.2% CAGR (2019-2024)" [1]
> [1] Euromonitor Passport, calculated from Market Sizes data

**Relationship:**
```cypher
(:MarketSize)-[:SOURCED_FROM {
  derivation: "calculated_cagr",
  formula: "((value_2024 / value_2019)^(1/5)) - 1",
  validation: "matches_passport_published_cagr",
  tolerance: 0.01
}]->(:Source)
```

### Broken Link Detection

**Automated Validation:**
```cypher
// Find MarketSize nodes with missing sources
MATCH (ms:MarketSize)
WHERE size(ms.source_ids) = 0
RETURN ms.id, ms.geography_id, ms.category_id
// Alert: Critical - Uncited data detected

// Validate source URLs (periodic job)
MATCH (s:Source)
WHERE s.url IS NOT NULL
CALL apoc.load.html(s.url) YIELD value  // Attempt to fetch
WITH s, value
WHERE value IS NULL
SET s.url_status = 'broken', s.last_checked = datetime()
RETURN s.id, s.name, s.url
// Alert: Warning - Broken citation link
```

---

## 7. Unstructured Data Integration

### Phase 3: Adding Reports, Documents, PDFs

**Goal:** Enable semantic search across unstructured Passport content (country reports, category analyses, regulatory briefs).

### Architecture

**Hybrid: Neo4j Graph + Vector Index**

**Option A: Neo4j Vector Search Plugin (RECOMMENDED)**
- Single database for structured + unstructured
- `(:Report)` nodes with `embedding` vector property
- Native vector index: `CREATE VECTOR INDEX report_embedding ...`
- Pros: Unified queries, no sync issues
- Cons: Neo4j vector search less mature than Pinecone/Weaviate

**Option B: Separate Vector DB (Pinecone/Weaviate)**
- Neo4j for structured, Pinecone for embeddings
- Sync `report_id` between systems
- Pros: Best-in-class vector search
- Cons: Dual data stores, sync complexity

**CHOSEN: Option A (Neo4j Vector Plugin)** for MVP - Rationale in Section 8.

### Report Node Design (repeated from Section 3.9)

```cypher
(:Report {
  id: "report_toys_india_2025",
  title: "Toys and Games in India",
  full_text: "The Indian toys market...",  // For embedding
  embedding: [0.123, 0.456, ...],  // 1536-dim Claude embeddings
  geography_ids: ["geo_india"],
  category_ids: ["cat_toys_games"]
})
```

### Structured + Unstructured Query Pattern

**User Query:** "What are the regulatory changes affecting toys in India?"

**Query Flow:**
1. **Semantic Search (Vector):**
   ```cypher
   CALL db.index.vector.queryNodes('report_embedding', 10, $query_embedding)
   YIELD node AS report, score
   WHERE score > 0.75
   RETURN report.title, report.abstract
   ```
2. **Filter by Metadata:**
   ```cypher
   MATCH (report:Report)
   WHERE "geo_india" IN report.geography_ids
     AND "cat_toys_games" IN report.category_ids
   CALL db.index.vector.queryNodes('report_embedding', 5, $query_embedding)
   YIELD node, score
   WHERE node.id = report.id AND score > 0.75
   RETURN report
   ```
3. **Retrieve Related Structured Data:**
   ```cypher
   MATCH (report:Report)-[:MENTIONS]->(c:Category {id: "cat_toys_games"})
   MATCH (g:Geography {id: "geo_india"})-[:HAS_MARKET_SIZE]->(ms:MarketSize)<-[:HAS_MARKET_SIZE]-(c)
   RETURN report, ms.historical_data, ms.source_ids
   ```

### Embedding Generation Strategy

**Tool:** Claude 3.5 Sonnet Embeddings API (or OpenAI `text-embedding-3-large`)

**Process:**
1. **Extract text from PDFs:** PyPDF2 or Apache Tika
2. **Chunk documents:** 1000-token chunks with 200-token overlap
3. **Generate embeddings:** Batch API calls (cost: ~$0.0001/1K tokens)
4. **Store in Neo4j:**
   ```cypher
   CREATE (r:Report {
     id: $report_id,
     chunk_index: $chunk_index,
     text: $chunk_text,
     embedding: $embedding_vector
   })
   ```
5. **Link to entities:**
   ```cypher
   // NER extraction: identify mentioned companies, categories
   MATCH (r:Report {id: $report_id})
   MATCH (c:Company {name: $mentioned_company})
   MERGE (r)-[:MENTIONS {page: $page}]->(c)
   ```

**Cost Estimate:**
- Assume 1,000 reports × 50 pages × 500 tokens/page = 25M tokens
- Embedding cost: 25M tokens × $0.0001/1K = $2.50 (one-time)
- Storage: 25M tokens ÷ 1000 tokens/chunk × 1536 dims × 4 bytes = 150 MB vectors

---

## 8. Alternative Architectures Evaluated

### Option 1: Neo4j + Vector Plugin (CURRENT CHOICE)

**Pros:**
- ✅ Unified data model (structured + unstructured in one DB)
- ✅ No data sync issues between systems
- ✅ Native graph + vector queries (e.g., "Find reports mentioning companies in this category")
- ✅ Simpler infrastructure (one database)
- ✅ Lower operational overhead

**Cons:**
- ⚠️ Neo4j vector search less mature than Pinecone/Weaviate
- ⚠️ Performance at scale unclear (millions of embeddings)
- ⚠️ Smaller ecosystem (fewer tools, examples)

**Verdict:** **RECOMMENDED for MVP** - Simplicity wins. Can migrate to Pinecone later if needed.

---

### Option 2: Neo4j + Pinecone

**Pros:**
- ✅ Best-in-class vector search (Pinecone optimized for speed)
- ✅ Proven scalability (billions of vectors)
- ✅ Rich ecosystem (LangChain integrations, monitoring)

**Cons:**
- ❌ Dual data stores (sync complexity)
- ❌ Need to maintain `report_id` mapping between Neo4j and Pinecone
- ❌ Harder to do hybrid queries (e.g., "reports about companies in India with >10% market share")
- ❌ Additional cost (~$70/month Pinecone starter)

**Verdict:** **Consider for Phase 5+** if Neo4j vector performance inadequate.

---

### Option 3: PostgreSQL + pgvector (No Graph)

**Pros:**
- ✅ Simpler stack (Postgres already in architecture for users/queries)
- ✅ pgvector extension mature and performant
- ✅ Relational model familiar to developers

**Cons:**
- ❌ No native graph traversal (relationships require complex joins)
- ❌ Hard to model category hierarchy (recursive CTEs, ugly)
- ❌ Worse for cross-content queries (e.g., "companies competing in related categories")
- ❌ Citation graph awkward (many-to-many tables)

**Verdict:** **NOT RECOMMENDED** - Graph structure is core to Passport's taxonomy. Forcing into relational is anti-pattern.

---

### Option 4: Weaviate (Graph + Vector in One)

**Pros:**
- ✅ Purpose-built for hybrid search (structured + semantic)
- ✅ Excellent vector performance
- ✅ Graph-like references between objects
- ✅ Auto-vectorization of text fields

**Cons:**
- ⚠️ Weaker graph query capabilities vs Neo4j (not full Cypher)
- ⚠️ Less familiar to team (new technology)
- ⚠️ Harder to preserve exact Passport taxonomy (Weaviate's schema less flexible)
- ⚠️ Smaller community than Neo4j

**Verdict:** **STRONG ALTERNATIVE** - Worth a deeper evaluation if Neo4j vector plugin disappoints. Revisit in Phase 2 after Neo4j proof-of-concept.

---

### Recommendation Summary

**Phase 1-4 (MVP):** Neo4j + Vector Plugin
- Simplicity, unified model, faster to build

**Phase 5+ (Production):** Re-evaluate if:
- Vector search performance <500ms for 95th percentile
- Need >10M report chunks (Neo4j limit unclear)
- Want advanced vector features (filters, hybrid search scoring)

**Migration path:** Neo4j → Weaviate or Neo4j + Pinecone (dual system)

---

## 9. Implementation Recommendations

### 9.1 Schema Validation

**Enforce constraints:**
```cypher
// Uniqueness
CREATE CONSTRAINT geography_id_unique FOR (g:Geography) REQUIRE g.id IS UNIQUE;
CREATE CONSTRAINT category_id_unique FOR (c:Category) REQUIRE c.id IS UNIQUE;
CREATE CONSTRAINT company_id_unique FOR (c:Company) REQUIRE c.id IS UNIQUE;
CREATE CONSTRAINT brand_id_unique FOR (b:Brand) REQUIRE b.id IS UNIQUE;
CREATE CONSTRAINT source_id_unique FOR (s:Source) REQUIRE s.id IS UNIQUE;
CREATE CONSTRAINT market_size_id_unique FOR (ms:MarketSize) REQUIRE ms.id IS UNIQUE;

// Required properties
CREATE CONSTRAINT geography_name_exists FOR (g:Geography) REQUIRE g.name IS NOT NULL;
CREATE CONSTRAINT category_name_exists FOR (c:Category) REQUIRE c.name IS NOT NULL;

// Relationship validation
// Ensure MarketSize always has at least one source
// (Enforce in application layer - Neo4j doesn't support "must have relationship" constraints)
```

### 9.2 Query Optimization

**Indexes (already listed per node type)**

**Common Query Patterns:**
```cypher
// 1. Fetch market size for geography + category (Mode 1)
MATCH (g:Geography {name: $geography})-[:HAS_MARKET_SIZE]->(ms:MarketSize)<-[:HAS_MARKET_SIZE]-(c:Category {name: $category})
RETURN ms.historical_data, ms.forecast_data, ms.source_ids

// 2. Top 5 companies in category + geography
MATCH (comp:Company)-[:COMPETES_IN]->(c:Category {name: $category}),
      (comp)-[:OPERATES_IN]->(g:Geography {name: $geography})
OPTIONAL MATCH (comp)-[:HAS_SHARE]->(share:MarketShare)
WHERE share.category_id = c.id AND share.geography_id = g.id
RETURN comp.name, share.share_data["2024"] AS share_2024
ORDER BY share_2024 DESC
LIMIT 5

// 3. Citation validation
MATCH (ms:MarketSize {id: $metric_id})-[:SOURCED_FROM]->(s:Source)
RETURN s.name, s.url, s.type

// 4. Semantic search + structured filter (Phase 3)
CALL db.index.vector.queryNodes('report_embedding', 10, $query_embedding)
YIELD node AS report, score
WHERE score > 0.75
  AND $geography_id IN report.geography_ids
  AND $category_id IN report.category_ids
MATCH (report)-[:MENTIONS]->(entity)
RETURN report, entity, score
ORDER BY score DESC
```

### 9.3 Data Ingestion Pipeline

**Phase 1: Pilot (Week 1-2)**
1. Manual Excel parsing (Python pandas)
2. Create Geography, Category nodes (53 categories for Toys & Games)
3. Create MarketSize nodes for Toys & Games in India
4. Link to Source nodes
5. Validate: Query market size 2024, check CAGR calculation

**Phase 2: Structured Data (Week 3-5)**
1. Automate Excel → Neo4j ETL (Python script + Neo4j driver)
2. Process all industries, all geographies
3. Add Company, Brand nodes
4. Add MarketShare nodes
5. Validate: >95% Passport corpus coverage

**Phase 3: Unstructured (Week 6-8)**
1. Extract text from PDFs (sample: 10 reports)
2. Generate embeddings (Claude API)
3. Create Report nodes with vectors
4. Create vector index
5. Test semantic search

**Phase 4: Citations (Week 8)**
1. Index all Source nodes
2. Validate MarketSize → Source links
3. Implement citation validation logic (Citation Specialist agent)
4. Test: Generate report, validate 100% citation accuracy

### 9.4 Maintenance

**Incremental Updates:**
- Passport publishes monthly updates → Detect changes → MERGE into Neo4j
- Invalidate cache (Redis) for affected geography + category combinations

**Full Refresh:**
- Quarterly: Rebuild entire KG (blue/green deployment)
- Backup old instance, build new, validate, switch traffic

**Monitoring:**
- Coverage dashboard: Track % of Passport data in KG
- Citation health: % of MarketSize nodes with sources
- Query performance: p95 latency for common queries

---

## Conclusion

This ontology design provides a **complete blueprint** for building the Passport AI Knowledge Graph:

✅ **11 node types** covering structured + unstructured data
✅ **12 relationship types** with clear semantics
✅ **Temporal modeling** (map properties) optimized for time-series
✅ **Citation graph** enabling 100% accuracy validation
✅ **Hybrid architecture** (Neo4j + vectors) for semantic + structured search
✅ **4-phase construction plan** from pilot to production
✅ **Alternative architectures evaluated** with migration paths

**Next Steps:**
1. Validate this design with Euromonitor stakeholders
2. Build Phase 1 pilot (Toys & Games India)
3. Performance test queries with realistic data volume
4. Iterate based on findings

---

**Document Version:** 1.0
**Last Updated:** 2026-01-23
**Authors:** Winston (Architect) + Karthikmg
**Review Status:** Draft - Pending Stakeholder Review
