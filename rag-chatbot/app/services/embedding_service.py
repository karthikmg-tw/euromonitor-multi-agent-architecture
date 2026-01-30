"""
Embedding Service: Generate embeddings using sentence-transformers
"""
from sentence_transformers import SentenceTransformer
from typing import List
import logging
import numpy as np

logger = logging.getLogger(__name__)


class EmbeddingService:
    """Service for generating text embeddings using sentence-transformers."""

    def __init__(self, model_name: str = "sentence-transformers/all-mpnet-base-v2"):
        """
        Initialize the embedding service.

        Args:
            model_name: The sentence-transformer model to use (768 dimensions)
        """
        logger.info(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)
        logger.info("Embedding model loaded successfully")

    def embed_query(self, text: str) -> np.ndarray:
        """
        Generate embedding for a single query text.

        Args:
            text: Query text to embed

        Returns:
            Numpy array of shape (768,)
        """
        embedding = self.model.encode(text, convert_to_numpy=True)
        return embedding

    def embed_batch(self, texts: List[str]) -> np.ndarray:
        """
        Generate embeddings for multiple texts.

        Args:
            texts: List of texts to embed

        Returns:
            Numpy array of shape (num_texts, 768)
        """
        embeddings = self.model.encode(texts, convert_to_numpy=True, show_progress_bar=True)
        return embeddings
