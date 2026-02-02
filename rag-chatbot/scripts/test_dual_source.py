"""
Test script for dual-source RAG (entities + chunks).

This script tests:
1. Graph loading with chunks
2. Dual-source search
3. Answer quality comparison
"""

import sys
from pathlib import Path
import json

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from app.services.graph_service_v2 import GraphServiceV2
from app.services.embedding_service import EmbeddingService
from app.services.vector_search import VectorSearchService
from app.services.rag_service_v2 import RAGServiceV2
from app.services.llm_service import LLMService


def test_graph_loading():
    """Test that graph loads with chunks."""
    print("="*60)
    print("TEST 1: Graph Loading")
    print("="*60)

    graph_path = "../output/ontology/market research/graph.json"
    schema_path = "../output/ontology/market research/schema.json"

    print(f"\nLoading graph from: {graph_path}")

    graph = GraphServiceV2(graph_path, schema_path)

    stats = graph.get_statistics()

    print(f"\nGraph Statistics:")
    print(f"  Entities: {stats['entities']}")
    print(f"  Chunks: {stats['chunks']}")
    print(f"  Total nodes: {stats['total_nodes']}")
    print(f"  Relationships: {stats['relationships']}")
    print(f"  Chunks with mentions: {stats['chunks_with_mentions']}")

    if stats['chunks'] > 0:
        print(f"\n✅ SUCCESS: Graph has {stats['chunks']} chunks")
    else:
        print(f"\n❌ FAIL: No chunks found in graph")
        print(f"   Did you run add_document_chunks.py first?")

    return graph, stats['chunks'] > 0


def test_hash_lookups(graph):
    """Test hash-based lookups."""
    print("\n" + "="*60)
    print("TEST 2: Hash-based Lookups")
    print("="*60)

    # Get a sample entity
    sample_entity = list(graph.entities_by_id.values())[0]
    entity_hash = sample_entity.get('embedding_hash')

    print(f"\nTest entity: {sample_entity.get('label')}")
    print(f"Entity hash: {entity_hash}")

    # Test lookup
    result = graph.get_node_by_hash(entity_hash)

    if result and result['type'] == 'entity':
        print(f"✅ Entity lookup successful")
    else:
        print(f"❌ Entity lookup failed")

    # Get a sample chunk (if exists)
    if graph.chunks_by_id:
        sample_chunk = list(graph.chunks_by_id.values())[0]
        chunk_hash = sample_chunk.get('embedding_hash')

        print(f"\nTest chunk: {sample_chunk.get('id')}")
        print(f"Chunk hash: {chunk_hash}")

        result = graph.get_node_by_hash(chunk_hash)

        if result and result['type'] == 'chunk':
            print(f"✅ Chunk lookup successful")
        else:
            print(f"❌ Chunk lookup failed")


def test_entity_chunk_links(graph):
    """Test entity↔chunk relationships."""
    print("\n" + "="*60)
    print("TEST 3: Entity-Chunk Relationships")
    print("="*60)

    # Pick an entity
    entity = list(graph.entities_by_id.values())[0]
    entity_id = entity['id']

    print(f"\nTest entity: {entity.get('label')}")

    # Find chunks mentioning this entity
    chunks = graph.get_chunks_mentioning_entity(entity_id)

    print(f"Chunks mentioning this entity: {len(chunks)}")

    if chunks:
        print(f"✅ Found {len(chunks)} chunks")
        print(f"\nSample chunk:")
        sample_chunk = chunks[0]
        print(f"  ID: {sample_chunk.get('id')}")
        print(f"  Text preview: {sample_chunk.get('text')[:100]}...")
    else:
        print(f"⚠️  No chunks mention this entity")


def test_dual_source_search():
    """Test dual-source vector search."""
    print("\n" + "="*60)
    print("TEST 4: Dual-Source Search")
    print("="*60)

    # Initialize services
    graph_path = "../output/ontology/market research/graph.json"
    embeddings_path = "../output/ontology/market research/embeddings/embeddings.json"

    print("\nInitializing services...")
    graph = GraphServiceV2(graph_path)
    embedder = EmbeddingService()
    vector_search = VectorSearchService(embeddings_path)

    # Test query
    test_query = "What trends are affecting toys in Asia Pacific?"
    print(f"\nTest query: {test_query}")

    # Generate embedding
    print("  Generating query embedding...")
    query_embedding = embedder.embed_query(test_query)

    # Search
    print("  Searching...")
    results = vector_search.search(
        query_embedding,
        top_k=10,
        min_similarity=0.05
    )

    print(f"  Found {len(results)} results")

    # Classify results
    entity_count = 0
    chunk_count = 0

    print("\nTop 10 results:")
    for i, (hash_id, similarity) in enumerate(results, 1):
        node_info = graph.get_node_by_hash(hash_id)

        if not node_info:
            print(f"  {i}. [UNKNOWN] {hash_id[:8]}... (sim: {similarity:.3f})")
            continue

        if node_info['type'] == 'entity':
            entity = node_info['node']
            print(f"  {i}. [ENTITY] {entity.get('label')} (sim: {similarity:.3f})")
            entity_count += 1
        else:
            chunk = node_info['node']
            print(f"  {i}. [CHUNK] {chunk.get('id')} (sim: {similarity:.3f})")
            chunk_count += 1

    print(f"\nBreakdown:")
    print(f"  Entities: {entity_count}")
    print(f"  Chunks: {chunk_count}")

    if chunk_count > 0:
        print(f"\n✅ SUCCESS: Dual-source search working!")
    else:
        print(f"\n⚠️  WARNING: No chunks in results")


def test_rag_query():
    """Test full RAG query."""
    print("\n" + "="*60)
    print("TEST 5: Full RAG Query")
    print("="*60)

    # Check for API key
    import os
    if not os.getenv('ANTHROPIC_API_KEY'):
        print("⚠️  SKIPPED: No ANTHROPIC_API_KEY found")
        print("   Set API key to test full RAG pipeline")
        return

    # Initialize services
    graph_path = "../output/ontology/market research/graph.json"
    embeddings_path = "../output/ontology/market research/embeddings/embeddings.json"

    print("\nInitializing services...")
    graph = GraphServiceV2(graph_path)
    embedder = EmbeddingService()
    vector_search = VectorSearchService(embeddings_path)
    llm = LLMService()

    rag = RAGServiceV2(
        graph_service=graph,
        embedding_service=embedder,
        vector_search_service=vector_search,
        llm_service=llm
    )

    # Test query
    test_query = "What is driving growth in the Asia Pacific toys market?"
    print(f"\nQuery: {test_query}")

    # Execute query
    print("\nProcessing... (this may take 5-10 seconds)")
    result = rag.query(
        user_query=test_query,
        top_k=7,
        debug=True
    )

    # Display results
    print("\n" + "-"*60)
    print("ANSWER:")
    print("-"*60)
    print(result['answer'])

    print("\n" + "-"*60)
    print("SOURCES:")
    print("-"*60)
    for i, source in enumerate(result['sources'], 1):
        if source['type'] == 'entity':
            print(f"{i}. [ENTITY] {source['label']} ({source['entity_type']})")
        else:
            print(f"{i}. [CHUNK] {source['source_file']} (chunk {source['chunk_index']})")

    print("\n" + "-"*60)
    print("DEBUG INFO:")
    print("-"*60)
    print(json.dumps(result['debug'], indent=2))

    print(f"\n✅ RAG query completed successfully!")


def main():
    """Run all tests."""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  DUAL-SOURCE RAG TEST SUITE".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")

    try:
        # Test 1: Graph loading
        graph, has_chunks = test_graph_loading()

        if not has_chunks:
            print("\n" + "!"*60)
            print("CRITICAL: No chunks found in graph!")
            print("Please run: python scripts/add_document_chunks.py")
            print("!"*60)
            return

        # Test 2: Hash lookups
        test_hash_lookups(graph)

        # Test 3: Entity-chunk links
        test_entity_chunk_links(graph)

        # Test 4: Dual-source search
        test_dual_source_search()

        # Test 5: Full RAG (if API key available)
        test_rag_query()

        # Summary
        print("\n" + "="*60)
        print("TEST SUMMARY")
        print("="*60)
        print("✅ All tests completed!")
        print("\nYour dual-source RAG system is ready to use.")
        print("\nNext steps:")
        print("  1. Update main.py to use GraphServiceV2 and RAGServiceV2")
        print("  2. Test with your frontend/UI")
        print("  3. Compare answer quality vs entity-only")

    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
