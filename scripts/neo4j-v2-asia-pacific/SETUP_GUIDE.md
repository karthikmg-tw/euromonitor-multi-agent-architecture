# Quick Setup Guide - Neo4j v2 Asia Pacific

## What We Just Created

A complete **ETL pipeline** for your Euromonitor Asia Pacific Knowledge Graph:

### 📂 Python Extraction Layer
- **`extract_asia_pacific_data.py`** - Parses unstructured text reports into structured JSON
- Already executed ✅ - Generated `extracted_data.json` with:
  - 11 countries
  - 27 categories
  - 10 companies
  - 8 brands
  - 6 market insights
  - 6 major trends

### 📊 Neo4j Loading Layer
Four Cypher files ready to load:

1. **`01_schema_constraints.cypher`** - Sets up indexes, constraints, uniqueness rules
2. **`02_core_entities.cypher`** - Creates geography (11 countries) + category taxonomy (28 nodes)
3. **`03_companies_brands.cypher`** - Creates companies, brands, and their relationships
4. **`04_insights_trends.cypher`** - Creates market insights and trends with impact relationships

## How to Load Into Neo4j

### Option A: One-Command Load (Easiest)

```bash
cd scripts/neo4j-v2-asia-pacific
./load_all.sh
```

The script will:
- Test connection to Neo4j
- Ask if you want to clear existing data
- Load all 4 files in sequence
- Verify the graph was created
- Show node/relationship counts

**Note:** You'll be prompted for your Neo4j password

### Option B: Manual Load via Neo4j Browser

1. Open http://localhost:7474
2. Copy-paste each `.cypher` file into the query editor (in order: 01, 02, 03, 04)
3. Run each one

### Option C: Command Line (Manual)

```bash
cd scripts/neo4j-v2-asia-pacific

# Load each file
cypher-shell -u neo4j -p YOUR_PASSWORD < 01_schema_constraints.cypher
cypher-shell -u neo4j -p YOUR_PASSWORD < 02_core_entities.cypher
cypher-shell -u neo4j -p YOUR_PASSWORD < 03_companies_brands.cypher
cypher-shell -u neo4j -p YOUR_PASSWORD < 04_insights_trends.cypher
```

## Verification After Loading

### 1. Check Node Counts
```cypher
MATCH (n)
RETURN labels(n)[0] AS type, count(n) AS count
ORDER BY count DESC;
```

**Expected counts:**
- Category: 28
- Country: 11
- Insight: 14
- Company: 10
- Brand: 8
- Trend: 6
- Region: 1

### 2. Visualize the Region Structure
```cypher
MATCH path = (c:Country)-[:LOCATED_IN]->(r:Region)
RETURN path;
```

You should see all 11 countries connected to Asia Pacific region.

### 3. Check Category Hierarchy
```cypher
MATCH (root:Category {level: 0})
OPTIONAL MATCH path = (child:Category)-[:BELONGS_TO*]->(root)
RETURN root.name, child.name, child.level, length(path) as depth
ORDER BY depth, child.name
LIMIT 20;
```

### 4. Explore Companies and Trends
```cypher
// Companies affected by trends
MATCH (t:Trend)-[r:BENEFITS_COMPANY]->(c:Company)
RETURN t.trend_name, c.name, r.type as impact;
```

### 5. Find China-Specific Insights
```cypher
MATCH (i:Insight)-[:ABOUT_GEOGRAPHY]->(g:Country {name: 'China'})
RETURN i.insight, i.year;
```

## Key Features of This Graph

### ✅ Complete Asia Pacific Coverage
- China (market leader)
- Japan (2nd largest)
- South Korea
- India (high growth)
- Indonesia, Thailand, Malaysia, Philippines, Singapore, Taiwan, Hong Kong

### ✅ Full Category Taxonomy (4 Levels)
```
Toys and Games (L0)
├── Traditional Toys and Games (L1)
│   ├── Baby and Infant (L2)
│   ├── Construction (L2)
│   ├── Games and Puzzles (L2)
│   └── ... 12 more categories
└── Video Games (L1)
    ├── Video Games Hardware (L2)
    │   ├── Hand-Held Consoles (L3)
    │   └── Static Consoles (L3)
    └── Video Games Software (L2)
        ├── Mobile Games (L3)
        ├── Console Games (L3)
        └── ...
```

### ✅ Competitive Landscape
- **Tencent** (Regional leader, Video Games)
- **NetEase** (Top 4, Mobile Games)
- **miHoYo** (Genshin Impact, Honkai: Star Rail)
- **LEGO** (Traditional toys leader, losing share to local Chinese brands)
- **Nintendo** (Top brand, Switch & Pokémon)
- **Sony** (PlayStation, gaining share)
- **Local Chinese brands** (Sembo, Enlighten, Bloks - benefiting from cultural identity trend)

### ✅ Market Trends Captured
1. **Kidults** - Adults as key target (declining birth rates)
2. **Cultural Identity** - Chinese consumers preferring local themes
3. **Gender-Neutral Toys** - Blurring traditional categories
4. **Experiential Retail** - Offline stores creating experiences
5. **Cross-Platform Gaming** - Mobile expanding to console/PC
6. **E-Sports** - Competitive gaming rise (especially India)

### ✅ Relationship Types
- `LOCATED_IN` - Geography hierarchy
- `BELONGS_TO` - Category taxonomy
- `OWNED_BY` - Brand ownership
- `COMPETES_IN` - Company-category focus
- `OPERATES_IN` - Company-geography presence
- `IMPACTS_GEOGRAPHY` - Trend-geography relationships
- `IMPACTS_CATEGORY` - Trend-category relationships
- `BENEFITS_COMPANY` - Trend impact (positive/negative)

## Comparison: v1 vs v2

| Feature | v1 (old) | v2 (new) |
|---------|----------|----------|
| **Countries** | 4 partial | 11 complete |
| **Categories** | 6 basic | 28 full hierarchy |
| **Companies** | Basic data | 10 with relationships |
| **Insights** | Properties | 14 separate nodes |
| **Trends** | None | 6 with impact links |
| **Extraction** | Manual | Automated Python |
| **Ontology** | Ad-hoc | Design doc aligned |

## What You Can Do Now

### Immediate Actions
1. ✅ **Load the graph** (use `./load_all.sh`)
2. ✅ **Run validation queries** (see above)
3. ✅ **Explore in Neo4j Browser** (visualizations)

### Next Phase Options

**Phase 2a: Add Market Metrics**
- Market sizes (historical + forecast)
- Market shares (company/brand)
- Unit prices
- CAGR calculations

**Phase 2b: Add More Geographies**
- Expand beyond Asia Pacific
- Add North America, Europe, etc.

**Phase 3: Unstructured Data**
- Parse full report PDFs
- Generate embeddings (Claude/OpenAI)
- Add vector search capability

**Phase 4: Citations**
- Add Source nodes
- Link all data to sources
- Enable 100% citation accuracy

## Troubleshooting

**"Connection refused" when loading:**
```bash
# Check if Neo4j is running
neo4j status

# Start it if not
neo4j start
```

**"Authentication failed":**
- Update password in `load_all.sh`
- Or set environment variable: `export NEO4J_PASSWORD=your_password`

**Want to start fresh?**
```cypher
// In Neo4j Browser, delete everything:
MATCH (n) DETACH DELETE n;

// Then reload:
cd scripts/neo4j-v2-asia-pacific && ./load_all.sh
```

**Python script failed?**
```bash
# Check Python version (need 3.x)
python3 --version

# Re-run extraction
cd scripts/python-v2
python3 extract_asia_pacific_data.py
```

## Files Created

```
scripts/
├── python-v2/
│   └── extract_asia_pacific_data.py         # ✅ Created & executed
│
└── neo4j-v2-asia-pacific/
    ├── README.md                             # ✅ Full documentation
    ├── SETUP_GUIDE.md                        # ✅ This file
    ├── 01_schema_constraints.cypher          # ✅ Schema setup
    ├── 02_core_entities.cypher               # ✅ Geography & categories
    ├── 03_companies_brands.cypher            # ✅ Companies & brands
    ├── 04_insights_trends.cypher             # ✅ Insights & trends
    ├── load_all.sh                           # ✅ Master loader script
    └── extracted_data.json                   # ✅ Generated data
```

## Support

- **Architecture Questions:** See `docs/knowledge-graph-ontology-design.md`
- **Query Examples:** See `README.md` in this folder
- **Validation Queries:** Listed in this guide above

---

**Ready to load?** Run: `./load_all.sh`

**After loading:** Open http://localhost:7474 and explore!
