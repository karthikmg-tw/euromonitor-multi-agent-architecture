#!/bin/bash
# ============================================
# Neo4j v2 Asia Pacific - Master Loader Script
# ============================================
# Author: Winston (Architect Agent) + Karthikmg
# Date: 2026-01-23
# ============================================

set -e  # Exit on error

echo "=========================================="
echo "Neo4j v2 Asia Pacific - Knowledge Graph Loader"
echo "=========================================="
echo ""

# Configuration
NEO4J_USER="${NEO4J_USER:-neo4j}"
NEO4J_PASSWORD="${NEO4J_PASSWORD:-karthikmg@5963}"
NEO4J_HOST="${NEO4J_HOST:-localhost}"
NEO4J_PORT="${NEO4J_PORT:-7687}"

# Check if cypher-shell is available
if ! command -v cypher-shell &> /dev/null; then
    echo "❌ ERROR: cypher-shell not found"
    echo "Please install Neo4j or add cypher-shell to your PATH"
    exit 1
fi

# Test connection
echo "🔌 Testing Neo4j connection..."
if ! cypher-shell -u "$NEO4J_USER" -p "$NEO4J_PASSWORD" -a "bolt://$NEO4J_HOST:$NEO4J_PORT" "RETURN 1;" > /dev/null 2>&1; then
    echo "❌ ERROR: Cannot connect to Neo4j"
    echo "   Make sure Neo4j is running on bolt://$NEO4J_HOST:$NEO4J_PORT"
    echo "   Check your credentials (user: $NEO4J_USER)"
    exit 1
fi
echo "✅ Connected to Neo4j"
echo ""

# Optional: Clear existing data
read -p "⚠️  Do you want to clear existing data? (yes/no): " CLEAR_DATA
if [ "$CLEAR_DATA" = "yes" ]; then
    echo "🗑️  Clearing existing data..."
    cypher-shell -u "$NEO4J_USER" -p "$NEO4J_PASSWORD" -a "bolt://$NEO4J_HOST:$NEO4J_PORT" \
        "MATCH (n) DETACH DELETE n;"
    echo "✅ Data cleared"
    echo ""
fi

# Load files in order
FILES=(
    "01_schema_constraints.cypher"
    "02_core_entities.cypher"
    "03_companies_brands.cypher"
    "04_insights_trends.cypher"
)

TOTAL=${#FILES[@]}
CURRENT=0

for FILE in "${FILES[@]}"; do
    CURRENT=$((CURRENT + 1))
    echo "[$CURRENT/$TOTAL] Loading $FILE..."

    if [ ! -f "$FILE" ]; then
        echo "❌ ERROR: File not found: $FILE"
        exit 1
    fi

    if cypher-shell -u "$NEO4J_USER" -p "$NEO4J_PASSWORD" -a "bolt://$NEO4J_HOST:$NEO4J_PORT" \
        --format plain < "$FILE" > /dev/null 2>&1; then
        echo "✅ Loaded $FILE"
    else
        echo "❌ ERROR loading $FILE"
        echo "   Check the file for syntax errors"
        exit 1
    fi
    echo ""
done

echo "=========================================="
echo "✅ All files loaded successfully!"
echo "=========================================="
echo ""

# Verification
echo "📊 Verifying graph..."
echo ""

echo "Node counts:"
cypher-shell -u "$NEO4J_USER" -p "$NEO4J_PASSWORD" -a "bolt://$NEO4J_HOST:$NEO4J_PORT" \
    "MATCH (n) RETURN labels(n)[0] AS type, count(n) AS count ORDER BY count DESC;" || true

echo ""
echo "Relationship counts:"
cypher-shell -u "$NEO4J_USER" -p "$NEO4J_PASSWORD" -a "bolt://$NEO4J_HOST:$NEO4J_PORT" \
    "MATCH ()-[r]->() RETURN type(r) AS relationship, count(r) AS count ORDER BY count DESC;" || true

echo ""
echo "=========================================="
echo "🎉 Knowledge Graph v2 loaded successfully!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "  1. Open Neo4j Browser: http://localhost:7474"
echo "  2. Run validation queries from README.md"
echo "  3. Visualize the graph structure"
echo ""
echo "Quick visualization query:"
echo "  MATCH (c:Country)-[:LOCATED_IN]->(r:Region)"
echo "  RETURN c, r LIMIT 25;"
echo ""
