"""
Graph Service: Load and query the knowledge graph from graph.json
"""
import json
import hashlib
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)


class GraphService:
    """Service for loading and querying the knowledge graph."""

    def __init__(self, graph_path: str, schema_path: str):
        self.graph_path = graph_path
        self.schema_path = schema_path
        self.entities_by_id = {}
        self.entities_by_hash = {}
        self.relationships = []
        self.schema = {}

        self._load_data()

    def _load_data(self):
        """Load graph and schema data."""
        logger.info(f"Loading graph from {self.graph_path}")

        # Load graph
        with open(self.graph_path, 'r') as f:
            graph_data = json.load(f)

        # Index entities by ID
        for entity in graph_data.get('entities', []):
            entity_id = entity['id']
            self.entities_by_id[entity_id] = entity

            # Create hash mapping
            # The embeddings are likely generated from: label + description
            text_for_embedding = self._get_entity_text(entity)
            text_hash = hashlib.sha256(text_for_embedding.encode('utf-8')).hexdigest()
            self.entities_by_hash[text_hash] = entity

        # Store relationships
        self.relationships = graph_data.get('relationships', [])

        # Load schema
        with open(self.schema_path, 'r') as f:
            self.schema = json.load(f)

        logger.info(f"Loaded {len(self.entities_by_id)} entities and {len(self.relationships)} relationships")

    def _get_entity_text(self, entity: Dict) -> str:
        """
        Get the text representation used for embeddings.
        This should match what was used during embedding generation.
        """
        # The embeddings were generated from entity labels
        label = entity.get('label', '')
        return label.strip()

    def get_entity_by_id(self, entity_id: str) -> Optional[Dict]:
        """Get entity by ID."""
        return self.entities_by_id.get(entity_id)

    def get_entity_by_hash(self, text_hash: str) -> Optional[Dict]:
        """Get entity by text hash."""
        return self.entities_by_hash.get(text_hash)

    def get_relationships_for_entity(self, entity_id: str) -> List[Dict]:
        """Get all relationships involving an entity."""
        related = []
        for rel in self.relationships:
            if rel.get('from_') == entity_id or rel.get('to') == entity_id:
                related.append(rel)
        return related

    def get_related_entities(self, entity_id: str, max_depth: int = 1) -> List[Dict]:
        """
        Get entities related to this entity (traversing the graph).

        Args:
            entity_id: Starting entity ID
            max_depth: How many hops to traverse (1 = direct neighbors only)

        Returns:
            List of related entities
        """
        if max_depth < 1:
            return []

        related_entities = []
        visited = {entity_id}
        queue = [(entity_id, 0)]

        while queue:
            current_id, depth = queue.pop(0)

            if depth >= max_depth:
                continue

            # Get relationships
            for rel in self.relationships:
                related_id = None

                if rel.get('from_') == current_id:
                    related_id = rel.get('to')
                elif rel.get('to') == current_id:
                    related_id = rel.get('from_')

                if related_id and related_id not in visited:
                    visited.add(related_id)
                    entity = self.get_entity_by_id(related_id)
                    if entity:
                        related_entities.append(entity)
                        queue.append((related_id, depth + 1))

        return related_entities

    def get_entities_by_type(self, entity_type: str) -> List[Dict]:
        """Get all entities of a specific type."""
        return [
            entity for entity in self.entities_by_id.values()
            if entity.get('type') == entity_type
        ]

    def search_entities(self, query: str, limit: int = 10) -> List[Dict]:
        """Simple keyword search in entity labels and descriptions."""
        query_lower = query.lower()
        results = []

        for entity in self.entities_by_id.values():
            label = entity.get('label', '').lower()
            description = entity.get('description', '').lower()
            aliases = [a.lower() for a in entity.get('aliases', [])]

            if (query_lower in label or
                query_lower in description or
                any(query_lower in alias for alias in aliases)):
                results.append(entity)

            if len(results) >= limit:
                break

        return results
