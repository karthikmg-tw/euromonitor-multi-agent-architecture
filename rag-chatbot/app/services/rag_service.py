"""
RAG Service: Orchestrate retrieval and generation pipeline
"""
from typing import Dict, List, Tuple
import logging

from .graph_service import GraphService
from .vector_search import VectorSearchService
from .embedding_service import EmbeddingService
from .llm_service import LLMService
from .hybrid_search import HybridSearchService

logger = logging.getLogger(__name__)


class RAGService:
    """
    RAG (Retrieval-Augmented Generation) orchestrator.

    Coordinates: query embedding → hybrid search → context retrieval → response generation
    """

    def __init__(
        self,
        graph_service: GraphService,
        vector_search: VectorSearchService,
        embedding_service: EmbeddingService,
        llm_service: LLMService
    ):
        self.graph = graph_service
        self.vector_search = vector_search
        self.embeddings = embedding_service
        self.llm = llm_service
        self.hybrid_search = HybridSearchService(graph_service, vector_search)
        logger.info("RAG service initialized with hybrid search")

    def query(
        self,
        user_query: str,
        top_k: int = 5,
        include_relationships: bool = True,
        min_similarity: float = 0.3
    ) -> Dict:
        """
        Process a user query through the full RAG pipeline.

        Args:
            user_query: User's natural language question
            top_k: Number of similar entities to retrieve
            include_relationships: Whether to include entity relationships in context
            min_similarity: Minimum cosine similarity threshold (0.0-1.0)

        Returns:
            Dictionary with:
                - answer: Generated response
                - sources: List of source entities used
                - debug: Debug information (similarities, entity IDs, etc.)
        """
        logger.info(f"Processing query: {user_query}")

        # Step 1: Generate query embedding
        logger.debug("Generating query embedding...")
        query_embedding = self.embeddings.embed_query(user_query)

        # Step 2: Hybrid search (vector + keyword matching)
        logger.debug(f"Hybrid search for top {top_k} entities...")
        similar_results = self.hybrid_search.search(
            query=user_query,
            query_embedding=query_embedding,
            top_k=top_k,
            min_similarity=min_similarity
        )

        # Extract just hash and score for compatibility
        similar_results = [(h, s) for h, s, _ in similar_results]

        if not similar_results:
            logger.warning("No similar entities found")
            return {
                "answer": "I couldn't find any relevant information in the knowledge graph to answer your question. Please try rephrasing or asking about topics related to toys and games in Asia Pacific.",
                "sources": [],
                "debug": {
                    "num_results": 0,
                    "query": user_query
                }
            }

        # Step 3: Retrieve entities from graph
        logger.debug(f"Retrieving {len(similar_results)} entities from graph...")
        context_entities = []
        debug_info = []

        for text_hash, similarity in similar_results:
            entity = self.graph.get_entity_by_hash(text_hash)
            if entity:
                context_entities.append(entity)
                debug_info.append({
                    "entity_id": entity['id'],
                    "label": entity['label'],
                    "type": entity['type'],
                    "similarity": similarity
                })
            else:
                # Entity not found - might be from relationship or other text
                # Just skip silently as vector search might return non-entity embeddings
                pass

        # Step 4: Retrieve relationships (optional)
        relationships = []
        if include_relationships and context_entities:
            logger.debug("Retrieving relationships...")
            for entity in context_entities:
                entity_rels = self.graph.get_relationships_for_entity(entity['id'])
                relationships.extend(entity_rels)

            # Deduplicate relationships
            seen = set()
            unique_rels = []
            for rel in relationships:
                rel_id = rel.get('id')
                if rel_id not in seen:
                    seen.add(rel_id)
                    unique_rels.append(rel)
            relationships = unique_rels

        logger.debug(f"Found {len(relationships)} relationships")

        # Step 5: Generate response using LLM
        logger.debug("Generating response...")
        answer = self.llm.generate_response(
            query=user_query,
            context_entities=context_entities,
            relationships=relationships
        )

        # Step 6: Format sources for citation
        sources = []
        for entity in context_entities:
            source_info = {
                "entity_id": entity['id'],
                "label": entity['label'],
                "type": entity['type'],
                "description": entity.get('description', ''),
                "source_urls": entity.get('properties', {}).get('source_urls', 'N/A')
            }
            sources.append(source_info)

        return {
            "answer": answer,
            "sources": sources,
            "debug": {
                "num_entities": len(context_entities),
                "num_relationships": len(relationships),
                "similarities": debug_info,
                "query": user_query
            }
        }

    def get_entity_info(self, entity_id: str) -> Dict:
        """
        Get detailed information about a specific entity.

        Args:
            entity_id: Entity ID to look up

        Returns:
            Entity information including related entities
        """
        entity = self.graph.get_entity_by_id(entity_id)
        if not entity:
            return {"error": f"Entity {entity_id} not found"}

        # Get relationships
        relationships = self.graph.get_relationships_for_entity(entity_id)

        # Get related entities
        related = self.graph.get_related_entities(entity_id, max_depth=1)

        return {
            "entity": entity,
            "relationships": relationships,
            "related_entities": related
        }
