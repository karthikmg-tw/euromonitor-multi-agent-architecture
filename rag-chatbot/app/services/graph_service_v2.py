"""
Enhanced Graph Service: Handles both entities AND document chunks.

This version extends the original graph service to support:
- Entity nodes (original)
- Document chunk nodes (new)
- Unified hash-based lookup for both node types
- Relationship traversal including chunk→entity links
"""

import json
import hashlib
from typing import Dict, List, Optional, Union
import logging

logger = logging.getLogger(__name__)


class GraphServiceV2:
    """Enhanced service for loading and querying the unified knowledge graph."""

    def __init__(self, graph_path: str, schema_path: str = None):
        self.graph_path = graph_path
        self.schema_path = schema_path

        # Separate indexes for entities and chunks
        self.entities_by_id = {}
        self.entities_by_hash = {}
        self.chunks_by_id = {}
        self.chunks_by_hash = {}

        # Unified hash index (all nodes)
        self.nodes_by_hash = {}

        self.relationships = []
        self.schema = {}

        self._load_data()

    def _load_data(self):
        """Load graph and schema data."""
        logger.info(f"Loading unified graph from {self.graph_path}")

        # Load graph
        with open(self.graph_path, 'r') as f:
            graph_data = json.load(f)

        # Index entities
        for entity in graph_data.get('entities', []):
            entity_id = entity['id']
            self.entities_by_id[entity_id] = entity

            # Get embedding hash (if exists in entity)
            embedding_hash = entity.get('embedding_hash')

            if not embedding_hash:
                # Generate hash if not present (legacy support)
                text = self._get_entity_text(entity)
                embedding_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]
                entity['embedding_hash'] = embedding_hash

            self.entities_by_hash[embedding_hash] = entity
            self.nodes_by_hash[embedding_hash] = {
                'type': 'entity',
                'node': entity
            }

        # Index chunks (if they exist)
        for chunk in graph_data.get('chunks', []):
            chunk_id = chunk['id']
            self.chunks_by_id[chunk_id] = chunk

            # Get embedding hash
            embedding_hash = chunk.get('embedding_hash')

            if embedding_hash:
                self.chunks_by_hash[embedding_hash] = chunk
                self.nodes_by_hash[embedding_hash] = {
                    'type': 'chunk',
                    'node': chunk
                }

        # Store relationships
        self.relationships = graph_data.get('relationships', [])

        # Load schema (optional)
        if self.schema_path:
            with open(self.schema_path, 'r') as f:
                self.schema = json.load(f)

        logger.info(
            f"Loaded {len(self.entities_by_id)} entities, "
            f"{len(self.chunks_by_id)} chunks, "
            f"{len(self.relationships)} relationships"
        )

    def _get_entity_text(self, entity: Dict) -> str:
        """Get the text representation used for embeddings."""
        return entity.get('label', '').strip()

    # ==================== Hash-based Lookups ====================

    def get_node_by_hash(self, hash_id: str) -> Optional[Dict]:
        """
        Get any node (entity or chunk) by embedding hash.

        Returns:
            {
                'type': 'entity' | 'chunk',
                'node': {...}
            }
        """
        return self.nodes_by_hash.get(hash_id)

    def get_entity_by_hash(self, hash_id: str) -> Optional[Dict]:
        """Get entity by embedding hash."""
        return self.entities_by_hash.get(hash_id)

    def get_chunk_by_hash(self, hash_id: str) -> Optional[Dict]:
        """Get chunk by embedding hash."""
        return self.chunks_by_hash.get(hash_id)

    # ==================== ID-based Lookups ====================

    def get_entity_by_id(self, entity_id: str) -> Optional[Dict]:
        """Get entity by ID."""
        return self.entities_by_id.get(entity_id)

    def get_chunk_by_id(self, chunk_id: str) -> Optional[Dict]:
        """Get chunk by ID."""
        return self.chunks_by_id.get(chunk_id)

    def get_node_by_id(self, node_id: str) -> Optional[Dict]:
        """Get any node by ID (checks entities first, then chunks)."""
        node = self.entities_by_id.get(node_id)
        if node:
            return {'type': 'entity', 'node': node}

        node = self.chunks_by_id.get(node_id)
        if node:
            return {'type': 'chunk', 'node': node}

        return None

    # ==================== Relationship Queries ====================

    def get_relationships_for_node(
        self,
        node_id: str,
        rel_type: Optional[str] = None
    ) -> List[Dict]:
        """
        Get all relationships involving a node.

        Args:
            node_id: Node ID (entity or chunk)
            rel_type: Optional filter by relationship type

        Returns:
            List of relationships
        """
        related = []
        for rel in self.relationships:
            if rel_type and rel.get('type') != rel_type:
                continue

            if rel.get('from_') == node_id or rel.get('to') == node_id:
                related.append(rel)

        return related

    def get_chunks_mentioning_entity(self, entity_id: str) -> List[Dict]:
        """
        Get all chunks that mention an entity.

        Args:
            entity_id: Entity ID

        Returns:
            List of chunk dictionaries
        """
        chunks = []

        # Method 1: Via relationships (if MENTIONS relationships exist)
        for rel in self.relationships:
            if (rel.get('type') == 'MENTIONS' and
                rel.get('to') == entity_id):
                chunk_id = rel.get('from_')
                chunk = self.chunks_by_id.get(chunk_id)
                if chunk:
                    chunks.append(chunk)

        # Method 2: Via chunk properties (if mentions_entities exists)
        for chunk in self.chunks_by_id.values():
            if entity_id in chunk.get('mentions_entities', []):
                if chunk not in chunks:  # Avoid duplicates
                    chunks.append(chunk)

        return chunks

    def get_entities_mentioned_in_chunk(self, chunk_id: str) -> List[Dict]:
        """
        Get all entities mentioned in a chunk.

        Args:
            chunk_id: Chunk ID

        Returns:
            List of entity dictionaries
        """
        entities = []

        # Method 1: Via chunk property
        chunk = self.chunks_by_id.get(chunk_id)
        if chunk:
            entity_ids = chunk.get('mentions_entities', [])
            for entity_id in entity_ids:
                entity = self.entities_by_id.get(entity_id)
                if entity:
                    entities.append(entity)

        # Method 2: Via relationships (backup)
        if not entities:
            for rel in self.relationships:
                if (rel.get('type') == 'MENTIONS' and
                    rel.get('from_') == chunk_id):
                    entity_id = rel.get('to')
                    entity = self.entities_by_id.get(entity_id)
                    if entity:
                        entities.append(entity)

        return entities

    def get_related_entities(
        self,
        entity_id: str,
        max_depth: int = 1
    ) -> List[Dict]:
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

            # Get relationships (exclude chunk relationships)
            for rel in self.relationships:
                # Skip chunk→entity relationships
                if rel.get('type') == 'MENTIONS':
                    continue

                related_id = None

                if rel.get('from_') == current_id:
                    related_id = rel.get('to')
                elif rel.get('to') == current_id:
                    related_id = rel.get('from_')

                # Check if related_id is an entity (not a chunk)
                if related_id and related_id not in visited:
                    entity = self.entities_by_id.get(related_id)
                    if entity:
                        visited.add(related_id)
                        related_entities.append(entity)
                        queue.append((related_id, depth + 1))

        return related_entities

    # ==================== Type-based Queries ====================

    def get_entities_by_type(self, entity_type: str) -> List[Dict]:
        """Get all entities of a specific type."""
        return [
            entity for entity in self.entities_by_id.values()
            if entity.get('type') == entity_type
        ]

    def get_chunks_by_source(self, source_file: str) -> List[Dict]:
        """Get all chunks from a specific source file."""
        return [
            chunk for chunk in self.chunks_by_id.values()
            if chunk.get('source_file') == source_file
        ]

    # ==================== Search ====================

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

    def search_chunks(self, query: str, limit: int = 10) -> List[Dict]:
        """Simple keyword search in chunk text."""
        query_lower = query.lower()
        results = []

        for chunk in self.chunks_by_id.values():
            text = chunk.get('text', '').lower()

            if query_lower in text:
                results.append(chunk)

            if len(results) >= limit:
                break

        return results

    # ==================== Statistics ====================

    def get_statistics(self) -> Dict:
        """Get graph statistics."""
        return {
            'entities': len(self.entities_by_id),
            'chunks': len(self.chunks_by_id),
            'total_nodes': len(self.entities_by_id) + len(self.chunks_by_id),
            'relationships': len(self.relationships),
            'embeddings': len(self.nodes_by_hash),
            'entity_types': len(set(e.get('type') for e in self.entities_by_id.values())),
            'chunks_with_mentions': sum(
                1 for c in self.chunks_by_id.values()
                if c.get('mentions_entities')
            )
        }
