# Neo4j Schema: Euromonitor Toys & Games Data

## Overview
This document describes the graph schema for integrating Euromonitor International market intelligence data into our Neo4j ontology.

## Design Philosophy: Hybrid Approach

**Phase 1 (Core)**: Essential entities for immediate analysis
**Phase 2+ (Incremental)**: Detailed metrics added as needed

---

## Node Types

### 1. Region
Represents geographic regions for market analysis.

```cypher
(:Region {
  name: string,
  description: string,
  data_source: string,
  report_date: date
})
```

**Example**: Asia Pacific

---

### 2. Country
Individual countries within regions.

```cypher
(:Country {
  name: string,
  iso_code: string,

  // Core metrics (Phase 1)
  market_size_2023: float,
  market_rank_apac: int,
  key_insight: string,

  // Detailed metrics (Phase 2)
  market_size_2018: float,
  cagr_2018_2023: float,
  forecast_size_2028: float,
  video_games_size: float,
  traditional_toys_size: float,
  video_games_share: float,
  ecommerce_share: float,
  // ... additional metrics as needed
})
```

**Relationships**:
- `(Country)-[:LOCATED_IN]->(Region)`

---

### 3. Industry
Top-level industry classification.

```cypher
(:Industry {
  name: string,
  description: string
})
```

**Example**: Toys and Games

---

### 4. Category
Product categories and subcategories.

```cypher
(:Category {
  name: string,
  parent_industry: string,
  parent_category: string (optional),
  type: string
})
```

**Examples**: Video Games, Mobile Games, Construction

**Relationships**:
- `(Category)-[:PART_OF]->(Industry)`
- `(SubCategory)-[:SUBCATEGORY_OF]->(Category)`

---

### 5. Company
Market players and competitors.

```cypher
(:Company {
  name: string,
  hq_country: string,
  primary_category: string,
  rank_apac: int,

  // Phase 2 metrics
  regional_market_share: float,
  flagship_products: [string],
  strategy_2023: string,
  competitive_advantage: string
})
```

**Relationships**:
- `(Company)-[:HEADQUARTERED_IN]->(Country)`
- `(Company)-[:COMPETES_IN]->(Category)`

---

### 6. Brand
Consumer-facing brands owned by companies.

```cypher
(:Brand {
  name: string,
  category: string,
  target_demographic: string,
  market_position: string
})
```

**Relationships**:
- `(Brand)-[:OWNED_BY]->(Company)`

---

### 7. Product
Specific products or titles.

```cypher
(:Product {
  name: string,
  type: string,
  genre: string (optional),
  release_year: int (optional)
})
```

**Examples**: Honor of Kings, Pokémon cards, LEGO Star Wars sets

**Relationships**:
- `(Product)-[:PUBLISHED_BY]->(Company)`
- `(Product)-[:BELONGS_TO]->(Brand)`

---

### 8. Trend
Market trends and consumer behavior patterns.

```cypher
(:Trend {
  name: string,
  description: string,
  impact: string, // 'high', 'medium', 'low'

  // Phase 2
  affected_countries: [string],
  primary_categories: [string],
  growth_outlook: string
})
```

**Examples**: Kidults Segment Growth, E-sports Growth

**Relationships**:
- `(Trend)-[:IMPACTS]->(Country)`
- `(Trend)-[:EMERGING_IN]->(Country)`
- `(Trend)-[:AFFECTS]->(Category)`

---

### 9. DistributionChannel
Sales and distribution channels.

```cypher
(:DistributionChannel {
  name: string,
  growth_trend: string,
  dominant_in: string (optional)
})
```

**Examples**: Retail E-Commerce, Appliances and Electronics Specialists

**Relationships**:
- `(Category)-[:SOLD_THROUGH]->(DistributionChannel)`

---

### 10. MarketSegment (Phase 2)
Specific market segment analysis (category + country combination).

```cypher
(:MarketSegment {
  name: string,
  country: string,
  category: string,
  leader: string,
  competition_intensity: string,
  local_players_gaining: boolean
})
```

**Relationships**:
- `(Company)-[:COMPETES_IN]->(MarketSegment)`

---

### 11. Forecast (Phase 2)
Future projections and predictions.

```cypher
(:Forecast {
  country: string,
  forecast_period: string,
  expected_cagr: float,
  expected_size_2028: float,
  driver_video_games: string,
  challenge_1: string,
  opportunity_1: string
})
```

**Relationships**:
- `(Forecast)-[:PROJECTS]->(Country)`

---

### 12. ChannelPerformance (Phase 2)
Detailed channel performance by country/year.

```cypher
(:ChannelPerformance {
  country: string,
  channel: string,
  year: int,
  overall_share: float,
  video_games_share: float,
  traditional_toys_share: float
})
```

**Relationships**:
- `(ChannelPerformance)-[:MEASURES]->(Country)`

---

## Relationship Types Summary

| Relationship | From | To | Meaning |
|-------------|------|-----|---------|
| `LOCATED_IN` | Country | Region | Geographic containment |
| `PART_OF` | Category | Industry | Category hierarchy |
| `SUBCATEGORY_OF` | Category | Category | Category nesting |
| `HEADQUARTERED_IN` | Company | Country | Company location |
| `COMPETES_IN` | Company | Category/MarketSegment | Market participation |
| `OWNED_BY` | Brand/Product | Company | Ownership |
| `PUBLISHED_BY` | Product | Company | Product publisher |
| `IMPACTS` | Trend | Country/Category | Trend influence |
| `EMERGING_IN` | Trend | Country | Trend origin |
| `SOLD_THROUGH` | Category | DistributionChannel | Distribution method |
| `PROJECTS` | Forecast | Country | Future prediction |
| `MEASURES` | Performance | Country | Performance tracking |

---

## Querying Patterns

### Get market overview for a country
```cypher
MATCH (c:Country {name: 'China'})-[:LOCATED_IN]->(r:Region)
OPTIONAL MATCH (comp:Company)-[:HEADQUARTERED_IN]->(c)
OPTIONAL MATCH (trend:Trend)-[:IMPACTS|EMERGING_IN]->(c)
RETURN c, r, collect(DISTINCT comp) as companies, collect(DISTINCT trend) as trends
```

### Find competitive landscape in a category
```cypher
MATCH (cat:Category {name: 'Video Games'})
MATCH (comp:Company)-[:COMPETES_IN]->(cat)
RETURN comp.name, comp.rank_apac, comp.primary_category
ORDER BY comp.rank_apac
```

### Identify trends affecting multiple markets
```cypher
MATCH (t:Trend)-[:IMPACTS]->(c:Country)
WITH t, collect(c.name) as affected_countries, count(c) as country_count
WHERE country_count > 2
RETURN t.name, t.description, affected_countries, country_count
ORDER BY country_count DESC
```

### Get company's market presence
```cypher
MATCH (comp:Company {name: 'Tencent Holdings Ltd'})
MATCH (comp)-[:HEADQUARTERED_IN]->(hq:Country)
MATCH (comp)-[:COMPETES_IN]->(cat:Category)
OPTIONAL MATCH (prod:Product)-[:PUBLISHED_BY]->(comp)
RETURN comp, hq, collect(DISTINCT cat) as categories, collect(DISTINCT prod) as products
```

---

## Data Loading Sequence

### Phase 1: Core Foundation (Execute first)
```bash
# Load core entities
cat 01_core_entities.cypher | cypher-shell -u neo4j -p password
```

**Contains**:
- Region (Asia Pacific)
- 11 Countries with basic metrics
- Industry and top-level categories
- Top 10 companies
- 6 key trends
- 4 distribution channels

**Enables**: High-level market analysis, competitive landscape overview

---

### Phase 2: Detailed Metrics (Incremental)
```bash
# Load detailed framework (examples included)
cat 02_detailed_metrics_framework.cypher | cypher-shell -u neo4j -p password
```

**Contains**:
- Detailed country metrics (China example)
- Company performance data (Tencent example)
- Market segment analysis
- Channel performance
- Forecast data
- Templates for adding more

**Enables**: Deep-dive analysis, forecasting, segment-specific insights

---

### Phase 3+: Continuous Expansion
Use templates in `02_detailed_metrics_framework.cypher` to add:
- Additional company details
- More products and brands
- Country-specific competitive dynamics
- Historical time series data
- Consumer demographic information

---

## Integration with Existing Ontology

This schema integrates with existing ontology nodes:

**Potential connections**:
- `(DataSource)` → Can reference Euromonitor reports
- `(GeographicLocation)` → Links to Country nodes
- `(Organization)` → Can map to Company nodes
- `(MarketIntelligence)` → High-level insights from trends

**Recommended approach**: Keep Euromonitor data in dedicated subgraph, create linking relationships as needed.

---

## Maintenance & Updates

### Adding New Reports
1. Extract core entities (countries, companies, categories)
2. Update market_size and metrics with new year data
3. Add new trends or update existing trend properties
4. Create new Forecast nodes for updated projections

### Quality Checks
```cypher
// Check for orphaned nodes
MATCH (n)
WHERE NOT (n)--()
RETURN labels(n), count(*)

// Verify country data completeness
MATCH (c:Country)
WHERE c.market_size_2023 IS NULL
RETURN c.name

// Check relationship coverage
MATCH (comp:Company)
WHERE NOT (comp)-[:HEADQUARTERED_IN]->()
RETURN comp.name
```

---

## Next Steps

1. ✅ Execute `01_core_entities.cypher`
2. ✅ Execute `02_detailed_metrics_framework.cypher`
3. ⏸️ Validate data in Neo4j Browser
4. ⏸️ Extract additional detailed data from PDF pages 28-49 (country snapshots)
5. ⏸️ Create brand and product nodes for top companies
6. ⏸️ Add time-series historical data for trend analysis
7. ⏸️ Integrate with LLM for natural language querying

---

## Source Attribution
All data sourced from:
- **Euromonitor International**: Toys and Games in Asia Pacific (June 2024)
- Report available at: `/Users/karthikmg/Documents/euromonitor-multi-agent-architecture/docs/data-samples/Toys_and_Games_in_Asia_Pacific.pdf`
