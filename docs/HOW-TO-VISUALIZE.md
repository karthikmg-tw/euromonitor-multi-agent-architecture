# How to Visualize the Passport AI Ontology

You now have **3 ways** to visualize the knowledge graph ontology. Choose based on your preference:

---

## ⚡ Option 1: Quick View (Mermaid Diagrams) - **FASTEST**

**No installation required!** View diagrams directly in your IDE or browser.

### Steps:

1. **In VS Code:**
   ```bash
   # Install extension (one-time)
   code --install-extension bierner.markdown-mermaid

   # Open the visualization file
   code docs/ontology-visualization.md

   # Preview: Cmd+Shift+V (Mac) or Ctrl+Shift+V (Windows)
   ```

2. **In Browser:**
   - Open: https://mermaid.live
   - Copy Mermaid code from `docs/ontology-visualization.md`
   - Paste and view interactive diagram

3. **In GitHub/GitLab:**
   - Push your repo
   - Open `docs/ontology-visualization.md` in the web UI
   - Diagrams render automatically

**Output:** Static diagrams showing:
- Core ontology structure
- Node types and properties
- Relationship types
- Example query paths

---

## 🎯 Option 2: Interactive Neo4j (Best for Exploration) - **RECOMMENDED**

**Best for:** Clicking around, exploring relationships, understanding data flow.

### Steps:

#### A. Install Neo4j Desktop (One-time setup)

```bash
# Download from: https://neo4j.com/download/
# Or via Homebrew (Mac):
brew install --cask neo4j
```

#### B. Create Database

1. Launch **Neo4j Desktop**
2. Click **"+ New"** → **"Create Project"**
3. Click **"Add"** → **"Local DBMS"**
4. Name: `passport-ai-ontology`
5. Password: `your_password` (remember this!)
6. Version: **5.x** (latest)
7. Click **"Create"**

#### C. Start Database

1. Click **"Start"** on your DBMS
2. Wait for status: ● Running
3. Click **"Open"** → **"Neo4j Browser"**

#### D. Load Sample Data

1. In Neo4j Browser, paste the entire contents of:
   ```
   docs/sample-data-loader.cypher
   ```
2. Press **Cmd+Enter** (Mac) or **Ctrl+Enter** (Windows) to run
3. Wait ~5 seconds for data loading
4. You should see: ✅ "Sample ontology data loaded successfully!"

#### E. Visualize!

Run these queries in Neo4j Browser (paste and Cmd+Enter):

**Query 1: Complete Ontology Overview**
```cypher
MATCH path = (n)-[r]->(m)
RETURN path
LIMIT 100;
```
*Shows all node types and relationships in one view*

**Query 2: Category Hierarchy**
```cypher
MATCH path = (child:Category)-[:BELONGS_TO*]->(parent:Category {id: "cat_toys_games"})
RETURN path;
```
*Visualize the 6-level category taxonomy*

**Query 3: Market Size with Citations**
```cypher
MATCH path = (geo:Geography {name: "India"})-[:HAS_MARKET_SIZE]->(ms:MarketSize)<-[:HAS_MARKET_SIZE]-(cat:Category {name: "Toys and Games"})
MATCH citation = (ms)-[:SOURCED_FROM]->(s:Source)
RETURN path, citation;
```
*See how market data links to sources for 100% citation accuracy*

**Query 4: Company Analysis**
```cypher
MATCH path = (comp:Company {name: "Sony India Pvt Ltd"})-[r]-(connected)
RETURN path;
```
*Explore all relationships for a company*

**Query 5: Full Intelligence Generation Path**
```cypher
MATCH geography = (country:Geography {name: "India"})-[:LOCATED_IN]->(region:Geography)
MATCH category = (cat:Category {name: "Toys and Games"})<-[:BELONGS_TO*0..]-(subcat:Category)
MATCH data = (country)-[:HAS_MARKET_SIZE]->(ms:MarketSize)<-[:HAS_MARKET_SIZE]-(cat)
MATCH citations = (ms)-[:SOURCED_FROM]->(s:Source)
MATCH companies = (comp:Company)-[:COMPETES_IN]->(cat)
MATCH shares = (comp)-[:HAS_SHARE]->(share:MarketShare)-[:FOR_CATEGORY]->(cat)
RETURN geography, category, data, citations, companies, shares
LIMIT 50;
```
*Simulates the complete data retrieval path for Mode 1 (Market Overview)*

### Neo4j Browser Features:

- **Click nodes** to expand relationships
- **Drag nodes** to rearrange layout
- **Double-click nodes** to see properties
- **Right-click → Expand** to load more connected nodes
- **Click relationship labels** to filter by type
- **Bottom panel** shows query results and data

---

## 🐍 Option 3: Python Visualization - **PROGRAMMATIC**

**Best for:** Saving static images, customizing layout, embedding in notebooks.

### Steps:

#### A. Install Dependencies

```bash
cd docs
pip install pyvis networkx
```

#### B. Run Visualizer

```bash
python visualize_ontology.py
```

This will:
1. Build the ontology graph
2. Print statistics (node counts, relationship counts)
3. Generate `ontology_visualization.html`
4. Auto-open in your default browser

#### C. Interact

- **Drag nodes** to rearrange
- **Hover nodes** for details (type, level, etc.)
- **Pan canvas** by clicking and dragging background
- **Zoom** with scroll wheel
- **Click nodes** to highlight connections

### Customize Layout

Edit `visualize_ontology.py` to:
- Change colors: `color="#hexcode"`
- Adjust node size: `size=30`
- Modify physics: Edit the `net.set_options()` section
- Add more nodes/edges: Follow the patterns in the script

---

## 📊 What You'll See

All three methods visualize the same ontology, showing:

### Node Types (Color-coded):
- **Blue boxes:** Geography (Region, Country)
- **Yellow ellipses:** Category (6-level hierarchy)
- **Purple stars:** Company (GBO, NBO)
- **Pink diamonds:** Brand (LBN, GBN)
- **Green boxes:** Market Data (MarketSize, MarketShare)
- **Orange triangles:** Source (Citations)
- **Dark green boxes:** Report (Unstructured content - Phase 3)

### Relationship Types:
- **LOCATED_IN** (blue): Geography hierarchy
- **BELONGS_TO** (orange): Category taxonomy
- **HAS_MARKET_SIZE** (green): Data linkage
- **SOURCED_FROM** (red): Citations
- **OWNED_BY** (pink): Brand ownership
- **COMPETES_IN** (purple): Market participation
- **MENTIONS** (dark green): Report references

### Real Data:
- **Market Size:** India Toys & Games = 2,795M CHF (2024)
- **CAGR:** 7.2% (2019-2024 historical)
- **Companies:** Sony India (22.6% share), Mattel India (8.1%)
- **Sources:** Euromonitor Passport, NCAER, Prowess DB

---

## 🎯 Recommended Flow

**For first-time exploration:**
1. Start with **Mermaid diagrams** (Option 1) to understand structure
2. Move to **Neo4j Browser** (Option 2) to explore interactively
3. Use **Python script** (Option 3) for custom visualizations or presentations

**For development:**
- Use **Neo4j** as your primary exploration tool
- Keep Neo4j Browser open while working on agent queries
- Test Cypher queries in Browser before coding them

---

## 🚀 Next Steps After Visualization

Once you've explored the ontology:

1. **Validate Design:**
   - Share `docs/ontology-visualization.md` with Euromonitor stakeholders
   - Walk through query paths for Mode 1, 2, 3
   - Confirm node/relationship structure matches their expectations

2. **Build Phase 1 Pilot:**
   - Expand `sample-data-loader.cypher` with full Toys & Games India data
   - Parse your Excel file programmatically (Python + pandas)
   - Load into Neo4j for performance testing

3. **Performance Test:**
   - Measure query latency with realistic data volume
   - Test with 1000+ categories, 100+ companies
   - Validate <500ms response time for typical queries

4. **Iterate:**
   - Refine ontology based on performance findings
   - Add missing relationships discovered during testing
   - Document schema changes

---

## 📚 Files Created

Your project now has:

```
docs/
├── knowledge-graph-ontology-design.md   # 70-page complete ontology spec
├── ontology-visualization.md            # Mermaid diagrams
├── sample-data-loader.cypher            # Neo4j data loader
├── visualize_ontology.py                # Python visualizer
└── HOW-TO-VISUALIZE.md                  # This guide

data-samples/
└── Toys_and_Games_in_India(Full_Dataset).xlsx  # Real Passport data
```

---

## ❓ Troubleshooting

### Neo4j won't start
- Check port 7687 is not in use: `lsof -i :7687`
- Restart Neo4j Desktop app
- Check logs in Neo4j Desktop → DBMS → "..." → "Terminal"

### Mermaid not rendering
- Update VS Code extension: "Markdown Preview Mermaid Support"
- Or use https://mermaid.live directly

### Python script errors
- Ensure pyvis installed: `pip list | grep pyvis`
- Check Python version: 3.7+ required
- Try: `pip install --upgrade pyvis networkx`

---

## 🎉 You're Ready!

You now have a **complete, visualized ontology** designed from real Passport data.

**Your next decision:**
- **A.** Validate with Euromonitor stakeholders
- **B.** Build Phase 1 pilot with full Toys & Games data
- **C.** Explore alternative architectures (Weaviate, pgvector)
- **D.** Design YAML business rules for Mode 1

What would you like to tackle next?
