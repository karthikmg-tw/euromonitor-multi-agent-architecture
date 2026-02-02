#!/usr/bin/env python3
"""
Interactive RAG Chatbot Tester (Python version)
Usage: python test_chat.py
"""

import requests
import json
from typing import Optional

API_URL = "http://localhost:8000/chat"
HEALTH_URL = "http://localhost:8000/health"

# ANSI colors
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
NC = '\033[0m'


def check_backend():
    """Check if backend is running."""
    try:
        response = requests.get(HEALTH_URL, timeout=2)
        return response.status_code == 200
    except:
        return False


def test_query(
    query: str,
    entity_weight: float = 1.0,
    chunk_weight: float = 1.0,
    top_k: int = 7,
    show_sources: bool = False
):
    """Test a query and display results."""
    print(f"{BLUE}{'━' * 60}{NC}")
    print(f"{YELLOW}Query:{NC} {query}")
    print(f"{YELLOW}Weights:{NC} entity={entity_weight}, chunk={chunk_weight}, top_k={top_k}")
    print(f"{BLUE}{'━' * 60}{NC}\n")

    # Make request
    payload = {
        "query": query,
        "entity_weight": entity_weight,
        "chunk_weight": chunk_weight,
        "top_k": top_k,
        "debug": True
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()

        # Display answer
        print(f"{GREEN}Answer:{NC}")
        print(result['answer'])
        print()

        # Display debug info
        if 'debug' in result and result['debug']:
            debug = result['debug']
            entity_count = debug.get('entity_count', 0)
            chunk_count = debug.get('chunk_count', 0)
            breakdown = debug.get('top_results_breakdown', {})
            top_entities = breakdown.get('entities', 0)
            top_chunks = breakdown.get('chunks', 0)

            print(f"{YELLOW}📊 Debug Info:{NC}")
            print(f"  Retrieved: {entity_count} entities, {chunk_count} chunks")
            print(f"  Top results: {top_entities} entities, {top_chunks} chunks")
            print()

        # Display sources if requested
        if show_sources and 'sources' in result:
            print(f"{YELLOW}📚 Sources:{NC}")
            for i, source in enumerate(result['sources'][:5], 1):
                if source['type'] == 'entity':
                    print(f"  {i}. [ENTITY] {source.get('label', 'N/A')} ({source.get('entity_type', 'N/A')})")
                else:
                    print(f"  {i}. [CHUNK] {source.get('source_file', 'N/A')} (chunk {source.get('chunk_index', '?')})")
            print()

    except requests.exceptions.RequestException as e:
        print(f"{RED}❌ Error: {e}{NC}\n")


def main():
    """Main interactive loop."""
    print("=" * 60)
    print("  RAG Chatbot Interactive Tester (Python)")
    print("=" * 60)
    print()

    # Check backend
    if not check_backend():
        print(f"{RED}❌ Backend not running on port 8000{NC}")
        print("Start it with: cd rag-chatbot && python -m uvicorn app.main:app --port 8000")
        return

    print(f"{GREEN}✅ Backend is running{NC}\n")

    # Sample queries
    sample_queries = [
        ("What are kidults?", 1.0, 1.0, 5, "Balanced - factual query"),
        ("Why is China important for toys?", 0.7, 1.5, 7, "Chunk-focused - exploratory"),
        ("What is LEGO?", 1.5, 0.7, 5, "Entity-focused - definition"),
        ("How do mobile games compare to traditional toys?", 1.0, 1.0, 7, "Balanced - comparative"),
    ]

    while True:
        print(f"{YELLOW}{'━' * 60}{NC}")
        print("Choose an option:")
        print("  1) Run sample queries")
        print("  2) Custom query (balanced)")
        print("  3) Custom query (entity-focused)")
        print("  4) Custom query (chunk-focused)")
        print("  5) Compare weights side-by-side")
        print("  6) Custom query with advanced options")
        print("  q) Quit")
        print()

        choice = input("Your choice: ").strip()
        print()

        if choice == '1':
            print("Running sample queries...\n")
            for query, ew, cw, k, desc in sample_queries:
                print(f"{BLUE}[{desc}]{NC}")
                test_query(query, ew, cw, k)
                print()

        elif choice == '2':
            query = input("Enter your query: ").strip()
            if query:
                test_query(query, 1.0, 1.0, 7, show_sources=True)

        elif choice == '3':
            query = input("Enter your query: ").strip()
            if query:
                test_query(query, 1.5, 0.7, 5, show_sources=True)

        elif choice == '4':
            query = input("Enter your query: ").strip()
            if query:
                test_query(query, 0.7, 1.5, 7, show_sources=True)

        elif choice == '5':
            query = input("Enter your query: ").strip()
            if query:
                print("\n=== BALANCED WEIGHTS ===")
                test_query(query, 1.0, 1.0, 7)
                print("\n=== ENTITY-FOCUSED ===")
                test_query(query, 1.5, 0.7, 5)
                print("\n=== CHUNK-FOCUSED ===")
                test_query(query, 0.7, 1.5, 7)

        elif choice == '6':
            query = input("Enter your query: ").strip()
            if not query:
                continue
            try:
                ew = float(input("Entity weight (default 1.0): ").strip() or "1.0")
                cw = float(input("Chunk weight (default 1.0): ").strip() or "1.0")
                k = int(input("Top K (default 7): ").strip() or "7")
                test_query(query, ew, cw, k, show_sources=True)
            except ValueError:
                print(f"{RED}Invalid input{NC}\n")

        elif choice.lower() == 'q':
            print("Goodbye!")
            break

        else:
            print(f"{RED}Invalid choice{NC}\n")

        input("\nPress Enter to continue...")
        print()


if __name__ == "__main__":
    main()
