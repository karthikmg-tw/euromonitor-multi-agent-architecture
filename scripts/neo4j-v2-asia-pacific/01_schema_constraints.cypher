// ============================================
// SCHEMA CONSTRAINTS & INDEXES
// Euromonitor Asia Pacific Knowledge Graph v2
// ============================================
// Author: Winston (Architect Agent) + Karthikmg
// Date: 2026-01-23
// Purpose: Define schema constraints and indexes for optimal query performance
// ============================================

// ============================================
// STEP 1: DROP EXISTING CONSTRAINTS (if reloading)
// ============================================
// Uncomment these if you need to reload from scratch
// DROP CONSTRAINT geography_id_unique IF EXISTS;
// DROP CONSTRAINT category_id_unique IF EXISTS;
// DROP CONSTRAINT company_name_unique IF EXISTS;
// DROP CONSTRAINT brand_name_unique IF EXISTS;

// ============================================
// STEP 2: UNIQUENESS CONSTRAINTS
// ============================================

// Geography
CREATE CONSTRAINT geography_id_unique IF NOT EXISTS
FOR (g:Geography) REQUIRE g.id IS UNIQUE;

CREATE CONSTRAINT country_iso_unique IF NOT EXISTS
FOR (c:Country) REQUIRE c.iso_code IS UNIQUE;

// Category
CREATE CONSTRAINT category_id_unique IF NOT EXISTS
FOR (c:Category) REQUIRE c.id IS UNIQUE;

// Company
CREATE CONSTRAINT company_id_unique IF NOT EXISTS
FOR (c:Company) REQUIRE c.id IS UNIQUE;

// Brand
CREATE CONSTRAINT brand_id_unique IF NOT EXISTS
FOR (b:Brand) REQUIRE b.id IS UNIQUE;

// Trend
CREATE CONSTRAINT trend_id_unique IF NOT EXISTS
FOR (t:Trend) REQUIRE t.id IS UNIQUE;

// Insight
CREATE CONSTRAINT insight_id_unique IF NOT EXISTS
FOR (i:Insight) REQUIRE i.id IS UNIQUE;

// ============================================
// STEP 3: PROPERTY EXISTENCE CONSTRAINTS
// ============================================

// Geography - must have name
CREATE CONSTRAINT geography_name_exists IF NOT EXISTS
FOR (g:Geography) REQUIRE g.name IS NOT NULL;

// Category - must have name and level
CREATE CONSTRAINT category_name_exists IF NOT EXISTS
FOR (c:Category) REQUIRE c.name IS NOT NULL;

// Company - must have name
CREATE CONSTRAINT company_name_exists IF NOT EXISTS
FOR (c:Company) REQUIRE c.name IS NOT NULL;

// ============================================
// STEP 4: PERFORMANCE INDEXES
// ============================================

// Geography indexes
CREATE INDEX geography_name_idx IF NOT EXISTS
FOR (g:Geography) ON (g.name);

CREATE INDEX geography_type_idx IF NOT EXISTS
FOR (g:Geography) ON (g.type);

CREATE INDEX country_region_idx IF NOT EXISTS
FOR (c:Country) ON (c.region);

// Category indexes
CREATE INDEX category_name_idx IF NOT EXISTS
FOR (c:Category) ON (c.name);

CREATE INDEX category_level_idx IF NOT EXISTS
FOR (c:Category) ON (c.level);

CREATE INDEX category_parent_idx IF NOT EXISTS
FOR (c:Category) ON (c.parent_id);

// Company indexes
CREATE INDEX company_name_idx IF NOT EXISTS
FOR (c:Company) ON (c.name);

CREATE INDEX company_type_idx IF NOT EXISTS
FOR (c:Company) ON (c.type);

CREATE INDEX company_market_idx IF NOT EXISTS
FOR (c:Company) ON (c.primary_market);

// Brand indexes
CREATE INDEX brand_name_idx IF NOT EXISTS
FOR (b:Brand) ON (b.name);

CREATE INDEX brand_owner_idx IF NOT EXISTS
FOR (b:Brand) ON (b.owner_company_id);

// Trend indexes
CREATE INDEX trend_name_idx IF NOT EXISTS
FOR (t:Trend) ON (t.trend_name);

CREATE INDEX trend_geography_idx IF NOT EXISTS
FOR (t:Trend) ON (t.geography);

// Insight indexes
CREATE INDEX insight_type_idx IF NOT EXISTS
FOR (i:Insight) ON (i.type);

CREATE INDEX insight_geography_idx IF NOT EXISTS
FOR (i:Insight) ON (i.geography);

// ============================================
// STEP 5: FULL-TEXT SEARCH INDEXES
// ============================================

// Text search on geography names
CREATE TEXT INDEX geography_text_search IF NOT EXISTS
FOR (g:Geography) ON (g.name);

// Text search on category names and descriptions
CREATE TEXT INDEX category_text_search IF NOT EXISTS
FOR (c:Category) ON (c.name);

// Text search on company names
CREATE TEXT INDEX company_text_search IF NOT EXISTS
FOR (c:Company) ON (c.name);

// Text search on trends
CREATE TEXT INDEX trend_name_text_search IF NOT EXISTS
FOR (t:Trend) ON (t.trend_name);

CREATE TEXT INDEX trend_description_text_search IF NOT EXISTS
FOR (t:Trend) ON (t.description);

// Text search on insights
CREATE TEXT INDEX insight_text_search IF NOT EXISTS
FOR (i:Insight) ON (i.insight);

// ============================================
// VERIFICATION
// ============================================

// Run this query to verify all constraints were created:
// SHOW CONSTRAINTS;

// Run this query to verify all indexes were created:
// SHOW INDEXES;

// ============================================
// END OF SCHEMA DEFINITION
// ============================================
