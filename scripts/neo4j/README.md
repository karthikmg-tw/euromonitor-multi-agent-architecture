# Neo4j Data Loading Scripts - Euromonitor Integration

## Overview
This directory contains Cypher scripts to load Euromonitor market intelligence data into Neo4j using a **hybrid approach**: core entities now, detailed metrics incrementally.

---

## Files

### 1. `01_core_entities.cypher`
**Purpose**: Foundation layer - essential entities for immediate analysis

**Contains**:
- 1 Region (Asia Pacific)
- 11 Countries with basic market data
- 1 Industry + 8 Categories/Subcategories
- 10 Top Companies (regional players)
- 6 Key Trends
- 4 Distribution Channels
- All fundamental relationships

**Execution time**: ~2 seconds
**Node count**: ~42 nodes
**Relationship count**: ~70 relationships

**Run**:
```bash
# Option 1: Using cypher-shell
cat 01_core_entities.cypher | cypher-shell -u neo4j -p your_password -d neo4j

# Option 2: Using Neo4j Browser
# Copy/paste script content into query window and execute
```

---

### 2. `02_detailed_metrics_framework.cypher`
**Purpose**: Demonstrates how to add granular data + provides templates

**Contains**:
- Detailed country metrics (China example with 30+ properties)
- Company performance data (Tencent example)
- Market segment analysis
- Channel performance metrics
- Forecast data structures
- Product nodes
- Templates for incremental additions

**Execution time**: ~1 second
**Node count**: +10 nodes
**Relationship count**: +15 relationships

**Run**:
```bash
cat 02_detailed_metrics_framework.cypher | cypher-shell -u neo4j -p your_password -d neo4j
```

---

## Quick Start

### Step 1: Load Core Data
```bash
cd /Users/karthikmg/Documents/euromonitor-multi-agent-architecture/scripts/neo4j

# Load foundation
cat 01_core_entities.cypher | cypher-shell -u neo4j -p password -d neo4j
```

**Verify**:
```cypher
// Check node counts
MATCH (n) RETURN labels(n)[0] as NodeType, count(*) as Count
ORDER BY Count DESC

// View Asia Pacific region with countries
MATCH (r:Region {name: 'Asia Pacific'})<-[:LOCATED_IN]-(c:Country)
RETURN r, c

// Top companies
MATCH (comp:Company)
WHERE comp.rank_apac <= 10
RETURN comp.name, comp.rank_apac, comp.hq_country
ORDER BY comp.rank_apac
```

---

### Step 2: Add Detailed Metrics
```bash
# Load examples and templates
cat 02_detailed_metrics_framework.cypher | cypher-shell -u neo4j -p password -d neo4j
```

**Verify**:
```cypher
// Check China's detailed metrics
MATCH (c:Country {iso_code: 'CN'})
RETURN c

// View company products
MATCH (comp:Company {name: 'Tencent Holdings Ltd'})
OPTIONAL MATCH (prod:Product)-[:PUBLISHED_BY]->(comp)
RETURN comp, collect(prod) as products

// Check forecast data
MATCH (f:Forecast)-[:PROJECTS]->(c:Country)
RETURN c.name, f.expected_cagr, f.expected_size_2028
```

---

## Incremental Data Loading Patterns

### Pattern 1: Add New Country Detail
```cypher
// Add detailed metrics to Japan
MATCH (japan:Country {iso_code: 'JP'})
SET japan += {
  market_size_2018: 16100,
  market_size_2023: 18500,
  cagr_2018_2023: 2.8,
  trading_cards_boom: true,
  key_category: 'Games and Puzzles',
  pokemon_cards_impact: 'Major driver of growth'
}
```

### Pattern 2: Add Company Performance by Country
```cypher
// Create performance node
CREATE (perf:CompanyPerformance {
  company: 'LEGO Group',
  country: 'CN',
  year: 2023,
  performance: 'First decline in many years',
  market_share: 0.05,
  challenge: 'Competition from local players',
  competitors: ['Bloks', 'Enlighten (Qman)', 'Sembo']
})

// Link to company and country
MATCH (comp:Company {name: 'LEGO Group'}),
      (country:Country {iso_code: 'CN'}),
      (perf:CompanyPerformance {company: 'LEGO Group', country: 'CN'})
CREATE (perf)-[:MEASURES]->(comp),
       (perf)-[:IN_MARKET]->(country)
```

### Pattern 3: Add Brand Information
```cypher
// Create brand
MERGE (pokemon:Brand {name: 'Pokémon'})
SET pokemon += {
  category: 'Trading Cards',
  target_demographic: 'Children and Kidults',
  market_position: 'Market leader in Japan',
  key_products: ['Pokémon Trading Cards', 'Pokémon video games']
}

// Link to company
MATCH (pokemon:Brand {name: 'Pokémon'}),
      (nintendo:Company {name: 'Nintendo Co Ltd'})
CREATE (pokemon)-[:OWNED_BY]->(nintendo)
```

### Pattern 4: Add Product Details
```cypher
// Create game product
MERGE (genshin:Product {name: 'Genshin Impact'})
SET genshin += {
  type: 'Mobile Game',
  genre: 'Action RPG',
  release_year: 2020,
  platforms: ['Mobile', 'PC', 'Console'],
  cross_platform: true,
  market_impact: 'Massive user base globally'
}

// Link to publisher
MATCH (genshin:Product {name: 'Genshin Impact'}),
      (mihoyo:Company {name: 'miHoYo Co Ltd'})
CREATE (genshin)-[:PUBLISHED_BY]->(mihoyo)
```

### Pattern 5: Add Historical Time Series
```cypher
// Create time series data
MERGE (chinaSales:TimeSeries {
  country: 'CN',
  metric: 'market_size',
  unit: 'USD_million'
})
SET chinaSales.data_points = [
  {year: 2018, value: 49900},
  {year: 2019, value: 52300},
  {year: 2020, value: 56800},
  {year: 2021, value: 59000},
  {year: 2022, value: 57200},
  {year: 2023, value: 60224}
]

// Link to country
MATCH (china:Country {iso_code: 'CN'}),
      (series:TimeSeries {country: 'CN', metric: 'market_size'})
CREATE (series)-[:TRACKS]->(china)
```

---

## Data Extraction Workflow

### From PDF to Cypher

**For Country Snapshots (Pages 28-49)**:

1. **Extract Key Metrics**:
   - Market size (historical and forecast)
   - Category breakdown
   - Top companies
   - Distribution channel share
   - Key trends

2. **Create Cypher**:
   ```cypher
   MATCH (country:Country {iso_code: 'XX'})
   SET country += {
     // paste extracted metrics
   }
   ```

3. **Add Relationships**:
   ```cypher
   // Link trends to country
   MATCH (trend:Trend {name: 'Trend Name'}),
         (country:Country {iso_code: 'XX'})
   CREATE (trend)-[:IMPACTS]->(country)
   ```

---

## Validation Queries

### Check Data Completeness
```cypher
// Countries without market size
MATCH (c:Country)
WHERE c.market_size_2023 IS NULL
RETURN c.name, c.iso_code

// Companies without HQ location
MATCH (comp:Company)
WHERE NOT (comp)-[:HEADQUARTERED_IN]->()
RETURN comp.name

// Orphaned nodes
MATCH (n)
WHERE NOT (n)--()
RETURN labels(n), count(*)
```

### Quality Checks
```cypher
// Verify all countries linked to region
MATCH (c:Country)
WHERE NOT (c)-[:LOCATED_IN]->(:Region)
RETURN c.name

// Check company-category relationships
MATCH (comp:Company)
WHERE NOT (comp)-[:COMPETES_IN]->(:Category)
RETURN comp.name

// Find duplicate nodes
MATCH (c:Country)
WITH c.name as name, collect(c) as nodes
WHERE size(nodes) > 1
RETURN name, size(nodes) as count
```

---

## Performance Tips

1. **Use MERGE for idempotency**: Can re-run scripts safely
2. **Batch operations**: Group related operations in single transaction
3. **Index key properties**:
   ```cypher
   CREATE INDEX country_iso IF NOT EXISTS FOR (c:Country) ON (c.iso_code);
   CREATE INDEX company_name IF NOT EXISTS FOR (c:Company) ON (c.name);
   CREATE INDEX category_name IF NOT EXISTS FOR (c:Category) ON (c.name);
   ```

4. **Use parameters for repeated values**:
   ```cypher
   :param iso_code => 'CN'
   MATCH (c:Country {iso_code: $iso_code})
   RETURN c
   ```

---

## Next Data to Add

**Priority 1** (High-value, medium effort):
- [ ] Japan detailed metrics (page 36-37)
- [ ] South Korea detailed metrics (page 44-45)
- [ ] India detailed metrics (page 32-33)
- [ ] Top 10 brands with ownership links

**Priority 2** (Complete picture):
- [ ] All country snapshots (pages 28-49)
- [ ] Company competitive positions by country
- [ ] Distribution channel performance by country
- [ ] Key products for top 20 companies

**Priority 3** (Nice to have):
- [ ] Historical time series (2018-2023)
- [ ] Forecast details (2024-2028)
- [ ] Consumer demographic data
- [ ] Pricing information

---

## Troubleshooting

### Script fails partway through
```cypher
// Check what was created
MATCH (n)
WHERE n.data_source = 'Euromonitor International'
RETURN labels(n), count(*)

// Clean up partial load if needed
MATCH (n)
WHERE n.data_source = 'Euromonitor International'
DETACH DELETE n
```

### Duplicate nodes created
```cypher
// Find duplicates
MATCH (c:Country)
WITH c.name as name, collect(c) as nodes
WHERE size(nodes) > 1
RETURN name, nodes

// Merge duplicates (careful!)
MATCH (c1:Country {name: 'China'})
MATCH (c2:Country {name: 'China'})
WHERE id(c1) < id(c2)
CALL apoc.refactor.mergeNodes([c1, c2], {properties: 'combine'})
YIELD node
RETURN node
```

---

## Support

For issues or questions:
1. Check schema documentation: `../../docs/neo4j-schema-euromonitor.md`
2. Review PDF source: `../../docs/data-samples/Toys_and_Games_in_Asia_Pacific.pdf`
3. Validate with queries above

---

**Last Updated**: 2026-01-23
**Data Source**: Euromonitor International, Toys and Games in Asia Pacific (June 2024)
