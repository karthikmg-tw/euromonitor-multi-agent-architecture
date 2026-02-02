"""
Enhanced RAG Service: Dual-source retrieval (Entities + Document Chunks)

This version performs:
1. Parallel search across entities and chunks
2. Reranking and deduplication
3. Context building from both sources
4. Enhanced citation with chunk sources
"""

from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)


class RAGServiceV2:
    """Enhanced RAG service with dual-source retrieval."""

    def __init__(
        self,
        graph_service,
        embedding_service,
        vector_search_service,
        llm_service
    ):
        """
        Initialize RAG service.

        Args:
            graph_service: GraphServiceV2 instance
            embedding_service: Embedding service
            vector_search_service: Vector search service
            llm_service: LLM service
        """
        self.graph = graph_service
        self.embedder = embedding_service
        self.vector_search = vector_search_service
        self.llm = llm_service

    def query(
        self,
        user_query: str,
        top_k: int = 7,
        entity_weight: float = 1.0,
        chunk_weight: float = 1.0,
        include_relationships: bool = True,
        min_similarity: float = 0.05,
        debug: bool = False
    ) -> Dict:
        """
        Process RAG query with dual-source retrieval.

        Args:
            user_query: User's question
            top_k: Total number of results to retrieve
            entity_weight: Weight for entity results (0-2, default 1.0)
            chunk_weight: Weight for chunk results (0-2, default 1.0)
            include_relationships: Whether to include graph relationships
            min_similarity: Minimum similarity threshold
            debug: Include debug information

        Returns:
            {
                'answer': str,
                'sources': List[Dict],
                'debug': Dict (optional)
            }
        """
        logger.info(f"Processing query: {user_query[:50]}...")

        # Step 1: Generate query embedding
        query_embedding = self.embedder.embed_query(user_query)

        # Step 2: Dual-source vector search
        search_results = self.vector_search.search(
            query_embedding,
            top_k=top_k * 2,  # Get more candidates for reranking
            min_similarity=min_similarity
        )

        # Step 3: Separate entities and chunks
        entity_results = []
        chunk_results = []

        for hash_id, similarity in search_results:
            node_info = self.graph.get_node_by_hash(hash_id)

            if not node_info:
                continue

            if node_info['type'] == 'entity':
                entity_results.append({
                    'node': node_info['node'],
                    'similarity': similarity * entity_weight,
                    'type': 'entity'
                })
            elif node_info['type'] == 'chunk':
                chunk_results.append({
                    'node': node_info['node'],
                    'similarity': similarity * chunk_weight,
                    'type': 'chunk'
                })

        # Step 4: Combine and rerank
        combined_results = entity_results + chunk_results
        combined_results.sort(key=lambda x: x['similarity'], reverse=True)

        # Step 5: Take top-K after reranking
        top_results = combined_results[:top_k]

        logger.info(
            f"Retrieved {len(entity_results)} entities, "
            f"{len(chunk_results)} chunks -> {len(top_results)} total"
        )

        # Step 6: Build enhanced context
        context = self._build_context(
            top_results,
            include_relationships=include_relationships
        )

        # Step 7: Generate response with LLM
        answer = self.llm.generate_simple_response(
            query=user_query,
            context=context
        )

        # Step 8: Format sources
        sources = self._format_sources(top_results)

        # Build response
        response = {
            'answer': answer,
            'sources': sources
        }

        # Add debug info if requested
        if debug:
            response['debug'] = {
                'entity_count': len(entity_results),
                'chunk_count': len(chunk_results),
                'top_results_breakdown': {
                    'entities': sum(1 for r in top_results if r['type'] == 'entity'),
                    'chunks': sum(1 for r in top_results if r['type'] == 'chunk')
                },
                'similarities': [
                    {
                        'type': r['type'],
                        'label': r['node'].get('label') or f"Chunk {r['node'].get('chunk_index')}",
                        'similarity': round(r['similarity'], 3)
                    }
                    for r in top_results
                ],
                'context_length': len(context)
            }

        return response

    def _build_context(
        self,
        results: List[Dict],
        include_relationships: bool
    ) -> str:
        """
        Build context from entities and chunks.

        Args:
            results: List of result dicts with node info
            include_relationships: Whether to include relationships

        Returns:
            Formatted context string
        """
        context = "# Retrieved Information\n\n"

        # Track which entities we've seen
        seen_entities = set()

        for i, result in enumerate(results, 1):
            node = result['node']
            node_type = result['type']
            similarity = result['similarity']

            if node_type == 'entity':
                entity_id = node['id']
                seen_entities.add(entity_id)

                # Entity header
                context += f"## Entity {i}: {node.get('label')} ({node.get('type')})\n"
                context += f"**Relevance:** {similarity:.2f}\n\n"

                # Description
                if node.get('description'):
                    context += f"{node['description']}\n\n"

                # Aliases
                if node.get('aliases'):
                    context += f"*Also known as:* {', '.join(node['aliases'])}\n\n"

                # Related chunks (if any)
                if include_relationships:
                    chunks = self.graph.get_chunks_mentioning_entity(entity_id)
                    if chunks:
                        context += f"*Mentioned in {len(chunks)} document section(s)*\n\n"

            elif node_type == 'chunk':
                # Chunk header
                context += f"## Document Excerpt {i}\n"
                context += f"**Source:** {node.get('source_file', 'Unknown')}\n"
                context += f"**Chunk:** {node.get('chunk_index', '?')}\n"
                context += f"**Relevance:** {similarity:.2f}\n\n"

                # Chunk text
                context += f"{node['text']}\n\n"

                # Mentioned entities
                mentioned = node.get('mentions_entities', [])
                if mentioned:
                    entity_labels = []
                    for entity_id in mentioned[:5]:  # Limit to 5
                        entity = self.graph.get_entity_by_id(entity_id)
                        if entity:
                            entity_labels.append(entity.get('label', entity_id))

                    context += f"*Mentions:* {', '.join(entity_labels)}\n\n"

            context += "---\n\n"

        # Add entity relationships (if requested)
        if include_relationships and seen_entities:
            relationship_context = self._add_relationship_context(seen_entities)
            if relationship_context:
                context += "# Entity Relationships\n\n"
                context += relationship_context

        return context

    def _add_relationship_context(self, entity_ids: set) -> str:
        """Add relationship information for entities."""
        context = ""
        relationships_added = 0

        for entity_id in list(entity_ids)[:3]:  # Limit to 3 entities
            entity = self.graph.get_entity_by_id(entity_id)
            if not entity:
                continue

            # Get related entities
            related = self.graph.get_related_entities(entity_id, max_depth=1)

            if related:
                context += f"**{entity.get('label')}** is connected to:\n"
                for rel_entity in related[:5]:  # Limit to 5 related
                    context += f"- {rel_entity.get('label')} ({rel_entity.get('type')})\n"
                    relationships_added += 1

                context += "\n"

        return context if relationships_added > 0 else ""

    def _format_sources(self, results: List[Dict]) -> List[Dict]:
        """
        Format sources for response with clean, type-specific fields.

        Returns structured sources without null fields for better display.
        """
        sources = []

        for result in results:
            node = result['node']
            node_type = result['type']
            similarity = result['similarity']

            if node_type == 'entity':
                # Entity source - only include entity-relevant fields
                source = {
                    'type': 'entity',
                    'entity_id': node['id'],
                    'label': node.get('label', 'Unknown'),
                    'entity_type': node.get('type', 'unknown'),
                    'description': node.get('description', 'No description available')[:200],
                    'source_urls': node.get('properties', {}).get('source_urls', None)
                }
                # Remove null fields
                source = {k: v for k, v in source.items() if v is not None}

            else:  # chunk
                # Chunk source - only include chunk-relevant fields
                text = node.get('text', '')
                # Clean preview: remove excessive whitespace and newlines
                preview = ' '.join(text[:250].split())
                if len(text) > 250:
                    preview += '...'

                # Get mentioned entity labels
                mentioned = []
                for eid in node.get('mentions_entities', [])[:5]:
                    entity = self.graph.get_entity_by_id(eid)
                    if entity:
                        mentioned.append(entity.get('label', eid))

                source = {
                    'type': 'chunk',
                    'chunk_id': node['id'],
                    'source_file': node.get('source_file', 'Unknown'),
                    'chunk_index': node.get('chunk_index', 0),
                    'text_preview': preview,
                    'mentioned_entities': mentioned if mentioned else None
                }
                # Remove null fields
                source = {k: v for k, v in source.items() if v is not None}

            sources.append(source)

        return sources
