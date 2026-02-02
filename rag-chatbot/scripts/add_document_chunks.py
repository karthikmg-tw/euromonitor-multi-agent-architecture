"""
Script to add document chunks to the knowledge graph.

This script:
1. Loads the source document (TXT file)
2. Chunks the text intelligently
3. Generates embeddings for chunks
4. Links chunks to entities (entity mention detection)
5. Updates graph.json with chunk nodes
6. Updates embeddings.json with chunk embeddings
"""

import json
import hashlib
import re
from pathlib import Path
from typing import List, Dict, Tuple
import argparse
from datetime import datetime

# Imports for text processing and embeddings
from sentence_transformers import SentenceTransformer


class DocumentChunker:
    """Intelligent document chunking with context preservation."""

    def __init__(self, chunk_size=500, chunk_overlap=100):
        """
        Initialize chunker.

        Args:
            chunk_size: Target size in characters
            chunk_overlap: Overlap between chunks in characters
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_text(self, text: str, source_file: str) -> List[Dict]:
        """
        Chunk text into semantic units.

        Args:
            text: Full document text
            source_file: Name of source file

        Returns:
            List of chunk dictionaries
        """
        chunks = []

        # Split by paragraphs first (preserve semantic boundaries)
        paragraphs = text.split('\n\n')

        current_chunk = ""
        chunk_id = 0
        para_id = 0

        for para in paragraphs:
            para = para.strip()
            if not para:
                continue

            # If adding this paragraph exceeds chunk_size, save current chunk
            if len(current_chunk) + len(para) > self.chunk_size and current_chunk:
                chunks.append({
                    "id": f"chunk_{source_file}_{chunk_id:04d}",
                    "type": "DocumentChunk",
                    "text": current_chunk.strip(),
                    "source_file": source_file,
                    "chunk_index": chunk_id,
                    "paragraph_start": para_id - current_chunk.count('\n\n'),
                    "char_count": len(current_chunk)
                })

                # Start new chunk with overlap
                overlap_text = self._get_overlap(current_chunk, self.chunk_overlap)
                current_chunk = overlap_text + "\n\n" + para
                chunk_id += 1
            else:
                # Add paragraph to current chunk
                if current_chunk:
                    current_chunk += "\n\n" + para
                else:
                    current_chunk = para

            para_id += 1

        # Add final chunk
        if current_chunk:
            chunks.append({
                "id": f"chunk_{source_file}_{chunk_id:04d}",
                "type": "DocumentChunk",
                "text": current_chunk.strip(),
                "source_file": source_file,
                "chunk_index": chunk_id,
                "paragraph_start": para_id - current_chunk.count('\n\n'),
                "char_count": len(current_chunk)
            })

        return chunks

    def _get_overlap(self, text: str, overlap_size: int) -> str:
        """Get last N characters, breaking at sentence boundary."""
        if len(text) <= overlap_size:
            return text

        # Try to break at sentence boundary
        overlap_text = text[-overlap_size:]
        sentence_break = overlap_text.rfind('. ')

        if sentence_break > 0:
            return overlap_text[sentence_break+2:]

        return overlap_text


class EntityLinker:
    """Link document chunks to graph entities."""

    def __init__(self, entities: List[Dict]):
        """
        Initialize linker with entities.

        Args:
            entities: List of entity dictionaries from graph
        """
        self.entities = entities
        self._build_lookup_index()

    def _build_lookup_index(self):
        """Build index for fast entity matching."""
        self.entity_patterns = []

        for entity in self.entities:
            # Create patterns from label and aliases
            patterns = [entity['label']]
            patterns.extend(entity.get('aliases', []))

            # Create regex patterns (case-insensitive, word boundaries)
            for pattern_text in patterns:
                # Escape special regex characters
                escaped = re.escape(pattern_text)
                # Word boundary regex
                regex_pattern = r'\b' + escaped + r'\b'

                self.entity_patterns.append({
                    'entity_id': entity['id'],
                    'entity_label': entity['label'],
                    'pattern': re.compile(regex_pattern, re.IGNORECASE)
                })

    def link_chunk_to_entities(self, chunk: Dict) -> List[str]:
        """
        Find entities mentioned in chunk.

        Args:
            chunk: Chunk dictionary

        Returns:
            List of entity IDs mentioned in chunk
        """
        mentioned_entities = set()
        chunk_text = chunk['text']

        for pattern_info in self.entity_patterns:
            if pattern_info['pattern'].search(chunk_text):
                mentioned_entities.add(pattern_info['entity_id'])

        return list(mentioned_entities)


class ChunkProcessor:
    """Main processor for adding chunks to graph."""

    def __init__(
        self,
        graph_path: str,
        embeddings_path: str,
        document_path: str,
        model_name: str = 'all-mpnet-base-v2'
    ):
        """
        Initialize processor.

        Args:
            graph_path: Path to graph.json
            embeddings_path: Path to embeddings.json
            document_path: Path to source document (TXT)
            model_name: Sentence transformer model name
        """
        self.graph_path = Path(graph_path)
        self.embeddings_path = Path(embeddings_path)
        self.document_path = Path(document_path)

        # Load graph and embeddings
        print(f"Loading graph from {self.graph_path}")
        with open(self.graph_path, 'r') as f:
            self.graph = json.load(f)

        print(f"Loading embeddings from {self.embeddings_path}")
        with open(self.embeddings_path, 'r') as f:
            self.embeddings = json.load(f)

        # Load embedding model
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)

        # Initialize components
        self.chunker = DocumentChunker(chunk_size=500, chunk_overlap=100)
        self.linker = EntityLinker(self.graph['entities'])

    def generate_hash(self, text: str) -> str:
        """Generate SHA-256 hash for text."""
        return hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]

    def process_document(self) -> Dict:
        """
        Process document and add chunks to graph.

        Returns:
            Statistics dictionary
        """
        print(f"\n{'='*60}")
        print(f"Processing document: {self.document_path.name}")
        print(f"{'='*60}\n")

        # Read document
        print("Step 1: Reading document...")
        with open(self.document_path, 'r', encoding='utf-8') as f:
            document_text = f.read()
        print(f"  Document length: {len(document_text):,} characters")

        # Chunk document
        print("\nStep 2: Chunking document...")
        chunks = self.chunker.chunk_text(document_text, self.document_path.stem)
        print(f"  Created {len(chunks)} chunks")
        print(f"  Average chunk size: {sum(c['char_count'] for c in chunks) / len(chunks):.0f} chars")

        # Generate embeddings
        print("\nStep 3: Generating embeddings...")
        chunk_texts = [chunk['text'] for chunk in chunks]
        embeddings = self.model.encode(
            chunk_texts,
            show_progress_bar=True,
            batch_size=32
        )
        print(f"  Generated {len(embeddings)} embeddings")

        # Add embeddings to chunks and embeddings dict
        print("\nStep 4: Adding embedding hashes...")
        for i, chunk in enumerate(chunks):
            # Generate hash from chunk text
            chunk_hash = self.generate_hash(chunk['text'])
            chunk['embedding_hash'] = chunk_hash

            # Store embedding
            self.embeddings[chunk_hash] = embeddings[i].tolist()

        # Link chunks to entities
        print("\nStep 5: Linking chunks to entities...")
        total_links = 0
        for chunk in chunks:
            mentioned_entities = self.linker.link_chunk_to_entities(chunk)
            chunk['mentions_entities'] = mentioned_entities
            total_links += len(mentioned_entities)

        print(f"  Created {total_links} chunk→entity links")
        print(f"  Average {total_links/len(chunks):.1f} entities per chunk")

        # Create relationships
        print("\nStep 6: Creating relationships...")
        new_relationships = []
        for chunk in chunks:
            for entity_id in chunk['mentions_entities']:
                new_relationships.append({
                    "id": f"rel_{chunk['id']}_{entity_id}",
                    "from_": chunk['id'],
                    "to": entity_id,
                    "type": "MENTIONS",
                    "properties": {
                        "detected_at": datetime.utcnow().isoformat() + 'Z'
                    }
                })

        print(f"  Created {len(new_relationships)} MENTIONS relationships")

        # Update graph
        print("\nStep 7: Updating graph...")

        # Add chunks to graph (as a new key)
        if 'chunks' not in self.graph:
            self.graph['chunks'] = []

        self.graph['chunks'].extend(chunks)

        # Add relationships
        if 'relationships' not in self.graph:
            self.graph['relationships'] = []

        self.graph['relationships'].extend(new_relationships)

        # Update metadata
        if 'metadata' not in self.graph:
            self.graph['metadata'] = {}

        self.graph['metadata']['last_chunk_update'] = datetime.utcnow().isoformat() + 'Z'
        self.graph['metadata']['total_chunks'] = len(self.graph['chunks'])
        self.graph['metadata']['total_entities'] = len(self.graph['entities'])
        self.graph['metadata']['total_relationships'] = len(self.graph['relationships'])

        # Save updated graph
        print("\nStep 8: Saving updated graph...")
        backup_path = self.graph_path.with_suffix('.json.backup')
        print(f"  Creating backup: {backup_path}")
        with open(backup_path, 'w') as f:
            json.dump(self.graph, f, indent=2)

        print(f"  Saving graph: {self.graph_path}")
        with open(self.graph_path, 'w') as f:
            json.dump(self.graph, f, indent=2)

        # Save updated embeddings
        print(f"\nStep 9: Saving updated embeddings...")
        embeddings_backup = self.embeddings_path.with_suffix('.json.backup')
        print(f"  Creating backup: {embeddings_backup}")
        with open(embeddings_backup, 'w') as f:
            json.dump(self.embeddings, f)

        print(f"  Saving embeddings: {self.embeddings_path}")
        with open(self.embeddings_path, 'w') as f:
            json.dump(self.embeddings, f)

        # Statistics
        stats = {
            'document': self.document_path.name,
            'chunks_created': len(chunks),
            'embeddings_generated': len(chunks),
            'entity_links': total_links,
            'relationships_created': len(new_relationships),
            'total_graph_nodes': len(self.graph['entities']) + len(self.graph['chunks']),
            'total_embeddings': len(self.embeddings)
        }

        print(f"\n{'='*60}")
        print("PROCESSING COMPLETE!")
        print(f"{'='*60}")
        print(f"\nStatistics:")
        print(f"  Document: {stats['document']}")
        print(f"  Chunks created: {stats['chunks_created']}")
        print(f"  Entity links: {stats['entity_links']}")
        print(f"  Total graph nodes: {stats['total_graph_nodes']}")
        print(f"  Total embeddings: {stats['total_embeddings']}")
        print(f"\nBackups created:")
        print(f"  {backup_path}")
        print(f"  {embeddings_backup}")

        return stats


def main():
    parser = argparse.ArgumentParser(
        description='Add document chunks to knowledge graph'
    )
    parser.add_argument(
        '--graph',
        type=str,
        default='../output/ontology/market research/graph.json',
        help='Path to graph.json'
    )
    parser.add_argument(
        '--embeddings',
        type=str,
        default='../output/ontology/market research/embeddings/embeddings.json',
        help='Path to embeddings.json'
    )
    parser.add_argument(
        '--document',
        type=str,
        default='../docs/data-samples/Toys_and_Games_in_Asia_Pacific.txt',
        help='Path to source document (TXT)'
    )
    parser.add_argument(
        '--model',
        type=str,
        default='all-mpnet-base-v2',
        help='Sentence transformer model name'
    )

    args = parser.parse_args()

    # Process document
    processor = ChunkProcessor(
        graph_path=args.graph,
        embeddings_path=args.embeddings,
        document_path=args.document,
        model_name=args.model
    )

    stats = processor.process_document()

    print(f"\n✅ Done! Your graph now includes document chunks.")
    print(f"\nNext steps:")
    print(f"  1. Review the updated graph.json")
    print(f"  2. Test the RAG system with dual-source search")
    print(f"  3. Compare answer quality (entity-only vs hybrid)")


if __name__ == "__main__":
    main()
