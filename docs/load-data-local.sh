#!/bin/bash
# Load ontology data into local Neo4j instance
# Usage: ./load-data-local.sh

echo "🔄 Loading Passport AI ontology data into Neo4j..."

# Check if cypher-shell is available
if ! command -v cypher-shell &> /dev/null; then
    echo "❌ cypher-shell not found in PATH"
    echo ""
    echo "Try one of these:"
    echo "  1. Add Neo4j bin to PATH: export PATH=\$PATH:/path/to/neo4j/bin"
    echo "  2. Use full path: /path/to/neo4j/bin/cypher-shell < docs/sample-data-loader.cypher"
    echo "  3. Copy-paste script into Neo4j Browser at http://localhost:7474"
    exit 1
fi

# Load the Cypher script
cypher-shell -u neo4j -p your_password < docs/sample-data-loader.cypher

echo ""
echo "✅ Data loading complete!"
echo "🌐 Open Neo4j Browser: http://localhost:7474"
echo "🔍 Run visualization queries from the script"
