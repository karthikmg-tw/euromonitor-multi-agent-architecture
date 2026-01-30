"""
Vector Search Service: Perform similarity search over embeddings
"""
import json
import numpy as np
from typing import List, Tuple
import logging

logger = logging.getLogger(__name__)


class VectorSearchService:
    """Service for vector similarity search using cosine similarity."""

    def __init__(self, embeddings_path: str):
        """
        Initialize vector search service.

        Args:
            embeddings_path: Path to embeddings.json file
        """
        logger.info(f"Loading embeddings from {embeddings_path}")

        # Load embeddings
        with open(embeddings_path, 'r') as f:
            embeddings_data = json.load(f)

        # Convert to numpy arrays
        self.hashes = list(embeddings_data.keys())
        self.embeddings = np.array([embeddings_data[h] for h in self.hashes])

        # Normalize embeddings for cosine similarity
        # cosine_similarity(a, b) = dot(a_normalized, b_normalized)
        norms = np.linalg.norm(self.embeddings, axis=1, keepdims=True)
        self.normalized_embeddings = self.embeddings / norms

        logger.info(f"Loaded {len(self.hashes)} embeddings with dimension {self.embeddings.shape[1]}")

    def search(
        self,
        query_embedding: np.ndarray,
        top_k: int = 5,
        min_similarity: float = 0.0
    ) -> List[Tuple[str, float]]:
        """
        Search for most similar entities.

        Args:
            query_embedding: Query embedding vector (768,)
            top_k: Number of results to return
            min_similarity: Minimum similarity threshold (0.0 to 1.0)

        Returns:
            List of (hash, similarity_score) tuples, sorted by similarity (descending)
        """
        # Normalize query embedding
        query_normalized = query_embedding / np.linalg.norm(query_embedding)

        # Compute cosine similarities
        similarities = np.dot(self.normalized_embeddings, query_normalized)

        # Filter by minimum similarity
        if min_similarity > 0:
            valid_indices = np.where(similarities >= min_similarity)[0]
            similarities = similarities[valid_indices]
            valid_hashes = [self.hashes[i] for i in valid_indices]
        else:
            valid_hashes = self.hashes

        # Get top-k indices
        if len(similarities) == 0:
            return []

        top_k = min(top_k, len(similarities))
        top_k_indices = np.argsort(similarities)[-top_k:][::-1]

        # Return results
        results = [
            (valid_hashes[i], float(similarities[i]))
            for i in top_k_indices
        ]

        return results

    def get_embedding_by_hash(self, text_hash: str) -> np.ndarray:
        """Get embedding vector by hash."""
        try:
            idx = self.hashes.index(text_hash)
            return self.embeddings[idx]
        except ValueError:
            return None
