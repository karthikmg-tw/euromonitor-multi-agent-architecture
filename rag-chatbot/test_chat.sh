#!/bin/bash
# Interactive RAG Chatbot Tester
# Usage: ./test_chat.sh

set -e

API_URL="http://localhost:8000/chat"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=========================================="
echo "  RAG Chatbot Interactive Tester"
echo "=========================================="
echo ""

# Check if server is running
if ! curl -s http://localhost:8000/health > /dev/null; then
    echo "❌ Backend not running on port 8000"
    echo "Start it with: cd rag-chatbot && python -m uvicorn app.main:app --port 8000"
    exit 1
fi

echo "✅ Backend is running"
echo ""

# Function to test a query
test_query() {
    local query="$1"
    local entity_weight="${2:-1.0}"
    local chunk_weight="${3:-1.0}"
    local top_k="${4:-7}"

    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}Query:${NC} $query"
    echo -e "${YELLOW}Weights:${NC} entity=$entity_weight, chunk=$chunk_weight, top_k=$top_k"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""

    # Make request
    response=$(curl -s -X POST "$API_URL" \
        -H "Content-Type: application/json" \
        -d "{
            \"query\": \"$query\",
            \"entity_weight\": $entity_weight,
            \"chunk_weight\": $chunk_weight,
            \"top_k\": $top_k,
            \"debug\": true
        }")

    # Extract and display answer
    answer=$(echo "$response" | jq -r '.answer')
    echo -e "${GREEN}Answer:${NC}"
    echo "$answer"
    echo ""

    # Display debug info
    entity_count=$(echo "$response" | jq -r '.debug.entity_count // 0')
    chunk_count=$(echo "$response" | jq -r '.debug.chunk_count // 0')
    top_entities=$(echo "$response" | jq -r '.debug.top_results_breakdown.entities // 0')
    top_chunks=$(echo "$response" | jq -r '.debug.top_results_breakdown.chunks // 0')

    echo -e "${YELLOW}📊 Debug Info:${NC}"
    echo "  Retrieved: $entity_count entities, $chunk_count chunks"
    echo "  Top results: $top_entities entities, $top_chunks chunks"
    echo ""
}

# Interactive mode
while true; do
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo "Choose an option:"
    echo "  1) Quick test queries"
    echo "  2) Custom query (balanced)"
    echo "  3) Custom query (entity-focused)"
    echo "  4) Custom query (chunk-focused)"
    echo "  5) Compare weights side-by-side"
    echo "  q) Quit"
    echo ""
    read -p "Your choice: " choice
    echo ""

    case $choice in
        1)
            echo "Running quick test queries..."
            echo ""
            test_query "What are kidults?" 1.0 1.0 5
            test_query "Why is China important for toys?" 0.7 1.5 7
            test_query "What is LEGO?" 1.5 0.7 5
            ;;
        2)
            read -p "Enter your query: " query
            test_query "$query" 1.0 1.0 7
            ;;
        3)
            read -p "Enter your query: " query
            test_query "$query" 1.5 0.7 5
            ;;
        4)
            read -p "Enter your query: " query
            test_query "$query" 0.7 1.5 7
            ;;
        5)
            read -p "Enter your query: " query
            echo ""
            echo "=== BALANCED WEIGHTS ==="
            test_query "$query" 1.0 1.0 7
            echo ""
            echo "=== ENTITY-FOCUSED ==="
            test_query "$query" 1.5 0.7 5
            echo ""
            echo "=== CHUNK-FOCUSED ==="
            test_query "$query" 0.7 1.5 7
            ;;
        q|Q)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice"
            ;;
    esac

    echo ""
    read -p "Press Enter to continue..."
    echo ""
done
