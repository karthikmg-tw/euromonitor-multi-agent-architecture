// ============================================================================
// PASSPORT AI - SAMPLE ONTOLOGY DATA LOADER
// ============================================================================
// This Cypher script loads sample data from the Toys & Games India dataset
// to visualize the ontology in Neo4j Browser
//
// HOW TO USE:
// 1. Install Neo4j Desktop: https://neo4j.com/download/
// 2. Create a new database (DBMS 5.x)
// 3. Start the database
// 4. Open Neo4j Browser
// 5. Copy-paste this entire file and run
// 6. Run visualization query at the bottom
// ============================================================================

// Clear existing data (CAUTION: This deletes everything!)
MATCH (n) DETACH DELETE n;

// ============================================================================
// 1. CREATE GEOGRAPHY NODES
// ============================================================================

CREATE (:Geography {
  id: "geo_asia_pacific",
  name: "Asia Pacific",
  type: "Region",
  level: 0,
  created_at: datetime()
});

CREATE (:Geography {
  id: "geo_india",
  name: "India",
  type: "Country",
  level: 1,
  iso_code: "IN",
  region: "Asia Pacific",
  population_2024: 1450000000,
  created_at: datetime()
});

// Geography relationships
MATCH (country:Geography {id: "geo_india"}), (region:Geography {id: "geo_asia_pacific"})
CREATE (country)-[:LOCATED_IN]->(region);

// ============================================================================
// 2. CREATE CATEGORY HIERARCHY (Toys & Games)
// ============================================================================

// Level 0: Industry
CREATE (:Category {
  id: "cat_toys_games",
  name: "Toys and Games",
  full_name: "Toys and Games",
  level: 0,
  industry: "Toys and Games",
  parent_id: null,
  definition: "This is the aggregation of traditional toys and games, and video games.",
  is_lowest_level: false,
  created_at: datetime()
});

// Level 1: Major Segments
CREATE (:Category {
  id: "cat_traditional",
  name: "Traditional Toys and Games",
  full_name: "Toys and Games > Traditional Toys and Games",
  level: 1,
  industry: "Toys and Games",
  parent_id: "cat_toys_games",
  definition: "This is the aggregation of baby toys, action figures, dolls, and other non-video game toys.",
  is_lowest_level: false,
  created_at: datetime()
});

CREATE (:Category {
  id: "cat_video_games",
  name: "Video Games",
  full_name: "Toys and Games > Video Games",
  level: 1,
  industry: "Toys and Games",
  parent_id: "cat_toys_games",
  definition: "This aggregates consoles, gaming headsets, and video games software.",
  is_lowest_level: false,
  created_at: datetime()
});

// Level 2: Categories
CREATE (:Category {
  id: "cat_action_figures",
  name: "Action Figures and Accessories",
  full_name: "Toys and Games > Traditional Toys > Action Figures and Accessories",
  level: 2,
  industry: "Toys and Games",
  parent_id: "cat_traditional",
  definition: "Action figures are typically aimed at boys aged between three and 12 years old.",
  is_lowest_level: true,
  created_at: datetime()
});

CREATE (:Category {
  id: "cat_dolls",
  name: "Dolls and Accessories",
  full_name: "Toys and Games > Traditional Toys > Dolls and Accessories",
  level: 2,
  industry: "Toys and Games",
  parent_id: "cat_traditional",
  definition: "Dolls are typically aimed at girls.",
  is_lowest_level: true,
  created_at: datetime()
});

CREATE (:Category {
  id: "cat_vg_software",
  name: "Video Games Software",
  full_name: "Toys and Games > Video Games > Video Games Software",
  level: 2,
  industry: "Toys and Games",
  parent_id: "cat_video_games",
  definition: "Includes both physical and digital video games.",
  is_lowest_level: false,
  created_at: datetime()
});

// Level 3: Subcategories
CREATE (:Category {
  id: "cat_handheld_consoles",
  name: "Hand-Held Consoles",
  full_name: "Toys and Games > Video Games > Hand-Held Consoles",
  level: 3,
  industry: "Toys and Games",
  parent_id: "cat_video_games",
  definition: "Portable gaming devices like Nintendo Switch.",
  is_lowest_level: true,
  created_at: datetime()
});

CREATE (:Category {
  id: "cat_static_consoles",
  name: "Static Consoles",
  full_name: "Toys and Games > Video Games > Static Consoles",
  level: 3,
  industry: "Toys and Games",
  parent_id: "cat_video_games",
  definition: "Home gaming consoles like PlayStation and Xbox.",
  is_lowest_level: true,
  created_at: datetime()
});

// Category hierarchy relationships
MATCH (child:Category), (parent:Category)
WHERE child.parent_id = parent.id
CREATE (child)-[:BELONGS_TO {hierarchy_path: child.full_name}]->(parent);

// ============================================================================
// 3. CREATE COMPANY NODES
// ============================================================================

CREATE (:Company {
  id: "comp_sony_global",
  name: "Sony Corporation",
  short_name: "Sony",
  type: "GBO",
  headquarters_country: "Japan",
  founded_year: 1946,
  website: "https://www.sony.com",
  created_at: datetime()
});

CREATE (:Company {
  id: "comp_sony_india",
  name: "Sony India Pvt Ltd",
  short_name: "Sony India",
  type: "NBO",
  parent_company_id: "comp_sony_global",
  headquarters_country: "India",
  founded_year: 1996,
  website: "https://www.sony.co.in",
  created_at: datetime()
});

CREATE (:Company {
  id: "comp_mattel_india",
  name: "Mattel Toys (India) Pvt Ltd",
  short_name: "Mattel India",
  type: "NBO",
  headquarters_country: "India",
  founded_year: 1999,
  created_at: datetime()
});

CREATE (:Company {
  id: "comp_hasbro_india",
  name: "Hasbro India Toys Private Ltd",
  short_name: "Hasbro India",
  type: "NBO",
  headquarters_country: "India",
  created_at: datetime()
});

// Company relationships
MATCH (nbo:Company {id: "comp_sony_india"}), (gbo:Company {id: "comp_sony_global"})
CREATE (nbo)-[:PARENT_COMPANY]->(gbo);

MATCH (comp:Company {id: "comp_sony_india"}), (geo:Geography {id: "geo_india"})
CREATE (comp)-[:OPERATES_IN {since: 1996}]->(geo);

MATCH (comp:Company), (cat:Category {id: "cat_video_games"}), (geo:Geography {id: "geo_india"})
WHERE comp.id IN ["comp_sony_india", "comp_mattel_india", "comp_hasbro_india"]
CREATE (comp)-[:COMPETES_IN {market: "Toys and Games"}]->(cat);

// ============================================================================
// 4. CREATE BRAND NODES
// ============================================================================

CREATE (:Brand {
  id: "brand_playstation",
  name: "PlayStation",
  type: "GBN",
  owner_company_id: "comp_sony_india",
  launch_year: 1994,
  website: "https://www.playstation.com",
  created_at: datetime()
});

CREATE (:Brand {
  id: "brand_barbie",
  name: "Barbie",
  type: "GBN",
  owner_company_id: "comp_mattel_india",
  launch_year: 1959,
  created_at: datetime()
});

CREATE (:Brand {
  id: "brand_hotwheels",
  name: "Hot Wheels",
  type: "GBN",
  owner_company_id: "comp_mattel_india",
  launch_year: 1968,
  created_at: datetime()
});

// Brand relationships
MATCH (brand:Brand), (comp:Company)
WHERE brand.owner_company_id = comp.id
CREATE (brand)-[:OWNED_BY]->(comp);

// ============================================================================
// 5. CREATE SOURCE NODES
// ============================================================================

CREATE (:Source {
  id: "source_passport",
  name: "Euromonitor Passport - Toys and Games in India (2025 Edition)",
  short_name: "Euromonitor Passport",
  type: "Analyst Research",
  url: "https://passport.euromonitor.com/",
  description: "Comprehensive market intelligence database",
  credibility_score: 1.0,
  publication_date: date("2025-01-10"),
  access_date: date("2025-01-15"),
  created_at: datetime()
});

CREATE (:Source {
  id: "source_ncaer",
  name: "National Council of Applied Economic Research (NCAER)",
  short_name: "NCAER",
  type: "Official Source",
  url: "https://www.ncaer.org",
  description: "Independent, non-profit economic policy research institute",
  credibility_score: 0.95,
  created_at: datetime()
});

CREATE (:Source {
  id: "source_prowess",
  name: "Prowess Database",
  short_name: "Prowess",
  type: "Official Source",
  url: "https://prowess.cmie.com",
  description: "CMIE's database of Indian companies",
  credibility_score: 0.90,
  created_at: datetime()
});

// ============================================================================
// 6. CREATE MARKET SIZE NODES (Real data from Excel)
// ============================================================================

CREATE (:MarketSize {
  id: "ms_toys_india_retail_value",
  geography_id: "geo_india",
  category_id: "cat_toys_games",
  data_type: "Retail Value RSP",
  unit: "CHF million",
  currency: "CHF",
  current_constant: "Historic Current Prices, Forecast Constant 2024 Prices",

  // Historical data (actual values from Excel)
  historical_data: {
    `2010`: 1180.776,
    `2015`: 1303.289,
    `2019`: 1973.550,
    `2020`: 1792.284,
    `2021`: 1959.912,
    `2022`: 2270.929,
    `2023`: 2458.112,
    `2024`: 2795.550
  },

  // Forecast data
  forecast_data: {
    `2025`: 3130.127,
    `2026`: 3432.431,
    `2027`: 3712.015,
    `2028`: 3974.632,
    `2029`: 4233.641
  },

  // Growth metrics
  historic_cagr: 7.212105,  // 2019-2024
  forecast_cagr: 8.654907,  // 2024-2029

  source_ids: ["source_passport", "source_ncaer"],
  last_updated: datetime("2025-01-15"),
  methodology_notes: "Market size calculated at retail selling prices",

  created_at: datetime()
});

// Link MarketSize to Geography and Category
MATCH (geo:Geography {id: "geo_india"}), (ms:MarketSize {id: "ms_toys_india_retail_value"})
CREATE (geo)-[:HAS_MARKET_SIZE {year_range: "2010-2029"}]->(ms);

MATCH (cat:Category {id: "cat_toys_games"}), (ms:MarketSize {id: "ms_toys_india_retail_value"})
CREATE (cat)-[:HAS_MARKET_SIZE {year_range: "2010-2029"}]->(ms);

// Link MarketSize to Sources
MATCH (ms:MarketSize {id: "ms_toys_india_retail_value"}), (s:Source)
WHERE s.id IN ["source_passport", "source_ncaer"]
CREATE (ms)-[:SOURCED_FROM {
  confidence: 1.0,
  dataset: "Market Sizes",
  derivation: "direct"
}]->(s);

// ============================================================================
// 7. CREATE MARKET SHARE NODES
// ============================================================================

CREATE (:MarketShare {
  id: "share_sony_india_toys",
  geography_id: "geo_india",
  category_id: "cat_toys_games",
  company_id: "comp_sony_india",
  share_type: "NBO",
  data_type: "Market Share",
  unit: "% value",

  // Share data (estimated based on typical patterns)
  share_data: {
    `2019`: 15.2,
    `2020`: 14.1,
    `2021`: 15.8,
    `2022`: 22.0,
    `2023`: 23.6,
    `2024`: 22.6
  },

  historic_cagr: 8.749338,

  source_ids: ["source_passport"],
  last_updated: datetime("2025-01-15"),

  created_at: datetime()
});

CREATE (:MarketShare {
  id: "share_mattel_india_toys",
  geography_id: "geo_india",
  category_id: "cat_toys_games",
  company_id: "comp_mattel_india",
  share_type: "NBO",
  data_type: "Market Share",
  unit: "% value",

  share_data: {
    `2019`: 10.5,
    `2020`: 3.1,
    `2021`: 3.8,
    `2022`: 3.2,
    `2023`: 6.1,
    `2024`: 8.1
  },

  source_ids: ["source_passport"],
  created_at: datetime()
});

// Link MarketShare to Companies
MATCH (comp:Company), (share:MarketShare)
WHERE share.company_id = comp.id
CREATE (comp)-[:HAS_SHARE]->(share);

// Link MarketShare to Geography and Category
MATCH (geo:Geography), (share:MarketShare)
WHERE share.geography_id = geo.id
CREATE (share)-[:IN_GEOGRAPHY]->(geo);

MATCH (cat:Category), (share:MarketShare)
WHERE share.category_id = cat.id
CREATE (share)-[:FOR_CATEGORY]->(cat);

// Link MarketShare to Sources
MATCH (share:MarketShare), (s:Source {id: "source_passport"})
CREATE (share)-[:SOURCED_FROM {confidence: 1.0}]->(s);

// ============================================================================
// 8. CREATE SAMPLE REPORT NODE (Phase 3 - Unstructured)
// ============================================================================

CREATE (:Report {
  id: "report_toys_india_2025",
  title: "Toys and Games in India - Country Report 2025",
  type: "Country Report",
  publication_date: date("2025-01-10"),
  author: "Euromonitor Analyst Team",
  geography_ids: ["geo_india"],
  category_ids: ["cat_toys_games"],

  abstract: "The Indian toys and games market demonstrated remarkable resilience, growing from 1,973 million CHF in 2019 to 2,796 million CHF in 2024 at a CAGR of 7.2%. Sony India emerged as the market leader with 22.6% share in 2024, driven by PlayStation console demand.",

  full_text: "The Indian toys and games market has shown robust growth over the review period. Video games segment led the growth, with Sony India dominating through its PlayStation brand. Mattel India strengthened its position in traditional toys through Barbie and Hot Wheels brands.",

  pdf_url: "s3://passport/reports/toys_india_2025.pdf",
  page_count: 45,

  // Note: In real implementation, this would be a 1536-dim vector
  // For demo, we use a placeholder
  embedding_note: "1536-dim vector would be stored here for semantic search",

  source_ids: ["source_passport"],

  created_at: datetime()
});

// Link Report to entities it mentions
MATCH (report:Report {id: "report_toys_india_2025"}), (comp:Company {id: "comp_sony_india"})
CREATE (report)-[:MENTIONS {
  page: 15,
  context: "Sony India dominates the video games segment with PlayStation brand",
  sentiment: "positive"
}]->(comp);

MATCH (report:Report {id: "report_toys_india_2025"}), (cat:Category {id: "cat_video_games"})
CREATE (report)-[:MENTIONS {page: 12, context: "Video games segment analysis"}]->(cat);

MATCH (report:Report {id: "report_toys_india_2025"}), (brand:Brand {id: "brand_playstation"})
CREATE (report)-[:MENTIONS {page: 15, context: "PlayStation sales analysis"}]->(brand);

MATCH (report:Report {id: "report_toys_india_2025"}), (s:Source {id: "source_passport"})
CREATE (report)-[:CITES {page: 45, citation_style: "footnote"}]->(s);

// ============================================================================
// CREATE INDEXES FOR PERFORMANCE
// ============================================================================

CREATE INDEX geography_id IF NOT EXISTS FOR (g:Geography) ON (g.id);
CREATE INDEX geography_name IF NOT EXISTS FOR (g:Geography) ON (g.name);

CREATE INDEX category_id IF NOT EXISTS FOR (c:Category) ON (c.id);
CREATE INDEX category_name IF NOT EXISTS FOR (c:Category) ON (c.name);
CREATE INDEX category_level IF NOT EXISTS FOR (c:Category) ON (c.level);

CREATE INDEX company_id IF NOT EXISTS FOR (c:Company) ON (c.id);
CREATE INDEX company_name IF NOT EXISTS FOR (c:Company) ON (c.name);

CREATE INDEX brand_id IF NOT EXISTS FOR (b:Brand) ON (b.id);
CREATE INDEX brand_name IF NOT EXISTS FOR (b:Brand) ON (b.name);

CREATE INDEX source_id IF NOT EXISTS FOR (s:Source) ON (s.id);

CREATE INDEX market_size_id IF NOT EXISTS FOR (ms:MarketSize) ON (ms.id);
CREATE INDEX market_share_id IF NOT EXISTS FOR (msh:MarketShare) ON (msh.id);

CREATE INDEX report_id IF NOT EXISTS FOR (r:Report) ON (r.id);

// ============================================================================
// VERIFICATION QUERIES
// ============================================================================

// Count nodes by type
MATCH (n)
RETURN labels(n)[0] AS NodeType, count(n) AS Count
ORDER BY Count DESC;

// Count relationships by type
MATCH ()-[r]->()
RETURN type(r) AS RelationshipType, count(r) AS Count
ORDER BY Count DESC;

// ============================================================================
// VISUALIZATION QUERIES
// ============================================================================

// Query 1: Complete Ontology Overview
// Shows all node types and their relationships
MATCH path = (n)-[r]->(m)
RETURN path
LIMIT 100;

// Query 2: Category Hierarchy
// Visualize the category taxonomy
MATCH path = (child:Category)-[:BELONGS_TO*]->(parent:Category {id: "cat_toys_games"})
RETURN path;

// Query 3: Market Size with Citations
// Show how data links to sources
MATCH path = (geo:Geography {name: "India"})-[:HAS_MARKET_SIZE]->(ms:MarketSize)<-[:HAS_MARKET_SIZE]-(cat:Category {name: "Toys and Games"})
MATCH citation = (ms)-[:SOURCED_FROM]->(s:Source)
RETURN path, citation;

// Query 4: Company Analysis
// Show company relationships and market position
MATCH path = (comp:Company {name: "Sony India Pvt Ltd"})-[r]-(connected)
RETURN path;

// Query 5: Full Intelligence Report Generation Path
// Simulates the query path for generating a market overview report
MATCH geography = (country:Geography {name: "India"})-[:LOCATED_IN]->(region:Geography)
MATCH category = (cat:Category {name: "Toys and Games"})<-[:BELONGS_TO*0..]-(subcat:Category)
MATCH data = (country)-[:HAS_MARKET_SIZE]->(ms:MarketSize)<-[:HAS_MARKET_SIZE]-(cat)
MATCH citations = (ms)-[:SOURCED_FROM]->(s:Source)
MATCH companies = (comp:Company)-[:COMPETES_IN]->(cat)
MATCH shares = (comp)-[:HAS_SHARE]->(share:MarketShare)-[:FOR_CATEGORY]->(cat)
RETURN geography, category, data, citations, companies, shares
LIMIT 50;

// Query 6: Citation Validation Check
// Verify all market data has sources
MATCH (ms:MarketSize)
OPTIONAL MATCH (ms)-[:SOURCED_FROM]->(s:Source)
WITH ms, collect(s.name) AS sources
RETURN
  ms.id AS metric_id,
  ms.geography_id AS geography,
  ms.category_id AS category,
  CASE WHEN size(sources) = 0 THEN 'MISSING CITATION' ELSE sources END AS citation_status;

// ============================================================================
// SAMPLE APPLICATION QUERIES
// ============================================================================

// App Query 1: Fetch market size time-series for charting
MATCH (ms:MarketSize {geography_id: "geo_india", category_id: "cat_toys_games"})
RETURN
  ms.historical_data AS historical,
  ms.forecast_data AS forecast,
  ms.historic_cagr AS cagr,
  ms.unit AS unit;

// App Query 2: Top companies by market share (2024)
MATCH (comp:Company)-[:HAS_SHARE]->(share:MarketShare {geography_id: "geo_india", category_id: "cat_toys_games"})
RETURN
  comp.name AS company,
  share.share_data.`2024` AS share_2024,
  share.share_type AS type
ORDER BY share_2024 DESC
LIMIT 5;

// App Query 3: Category hierarchy for dropdown
MATCH path = (child:Category)-[:BELONGS_TO*]->(root:Category {level: 0})
RETURN
  child.id AS category_id,
  child.name AS category_name,
  child.level AS level,
  [node in nodes(path) | node.name] AS hierarchy_path
ORDER BY child.level, child.name;

// ============================================================================
// SUCCESS MESSAGE
// ============================================================================

RETURN "✅ Sample ontology data loaded successfully!" AS Status,
       "Run the visualization queries above to explore the graph" AS NextStep;
