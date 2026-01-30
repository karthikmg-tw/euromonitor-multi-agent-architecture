"""
Hybrid Search: Combines vector similarity with keyword matching
"""
from typing import List, Dict, Tuple
import logging
import difflib

logger = logging.getLogger(__name__)


class HybridSearchService:
    """Combines semantic vector search with keyword matching for better recall."""

    def __init__(self, graph_service, vector_search_service):
        self.graph = graph_service
        self.vector_search = vector_search_service

    def search(
        self,
        query: str,
        query_embedding,
        top_k: int = 5,
        min_similarity: float = 0.3
    ) -> List[Tuple[str, float, str]]:
        """
        Hybrid search combining vector similarity and keyword matching.

        Returns: List of (hash, similarity_score, match_type)
        """
        results = {}

        # 1. Vector search
        vector_results = self.vector_search.search(
            query_embedding,
            top_k=top_k,
            min_similarity=min_similarity
        )

        for hash_val, similarity in vector_results:
            if hash_val not in results or results[hash_val][0] < similarity:
                results[hash_val] = (similarity, "vector")

        # 2. Keyword search in graph (exact and fuzzy matching)
        query_lower = query.lower().strip()
        query_words = set(query_lower.split())

        keyword_matches = []

        for entity in self.graph.entities_by_id.values():
            label = entity.get('label', '').lower()
            aliases = [a.lower() for a in entity.get('aliases', [])]
            description = entity.get('description', '').lower()

            score = 0
            match_type = None

            # Exact label match - highest priority
            if query_lower == label:
                score = 1.0
                match_type = "exact_label"
            # Label contains query or query contains label
            elif query_lower in label or label in query_lower:
                score = 0.9
                match_type = "label_substring"
            # Exact alias match
            elif query_lower in aliases:
                score = 0.95
                match_type = "exact_alias"
            # Any alias contains query
            elif any(query_lower in alias or alias in query_lower for alias in aliases):
                score = 0.85
                match_type = "alias_substring"
            # Fuzzy match using edit distance for word variations (kidulting → kidults)
            if score == 0:
                for check_label in [label] + aliases:
                    # Use difflib for similarity ratio
                    similarity = difflib.SequenceMatcher(None, query_lower, check_label).ratio()
                    if similarity >= 0.75:  # 75% similarity threshold
                        score = 0.88 * similarity  # Scale by similarity
                        match_type = "fuzzy_match"
                        break

            # Description contains query
            if score == 0 and query_lower in description:
                score = 0.6
                match_type = "description"

            # Word overlap
            if score == 0:
                label_words = set(label.split())
                overlap = len(query_words & label_words)
                if overlap > 0:
                    score = 0.3 + (overlap * 0.1)
                    match_type = "word_overlap"

            if score > 0:
                # Generate hash for this entity
                from hashlib import sha256
                label_hash = sha256(entity['label'].encode('utf-8')).hexdigest()
                keyword_matches.append((label_hash, score, match_type))

        # Merge keyword matches with vector results
        for hash_val, score, match_type in keyword_matches:
            if hash_val not in results or results[hash_val][0] < score:
                results[hash_val] = (score, match_type)

        # Sort by score descending and take top_k
        sorted_results = sorted(
            [(h, s, t) for h, (s, t) in results.items()],
            key=lambda x: x[1],
            reverse=True
        )[:top_k]

        logger.info(f"Hybrid search: {len(vector_results)} vector + {len(keyword_matches)} keyword = {len(sorted_results)} total")

        return sorted_results
