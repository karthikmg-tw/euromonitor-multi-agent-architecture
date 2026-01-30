#!/usr/bin/env python3
"""
Create a hash-to-entity mapping file
"""
import json
import hashlib

# Load graph
with open('../output/ontology/market research/graph.json') as f:
    graph = json.load(f)

# Load embeddings
with open('../output/ontology/market research/embeddings/embeddings.json') as f:
    embeddings = json.load(f)

# Build reverse mapping
hash_to_entity = {}

for entity in graph['entities']:
    entity_id = entity['id']
    label = entity['label']

    # Generate hash from label
    label_hash = hashlib.sha256(label.encode('utf-8')).hexdigest()

    # Check if this hash exists in embeddings
    if label_hash in embeddings:
        hash_to_entity[label_hash] = entity_id

print(f"Mapped {len(hash_to_entity)} hashes to entities")
print(f"Unmapped embeddings: {len(embeddings) - len(hash_to_entity)}")

# Save mapping
with open('hash_to_entity_mapping.json', 'w') as f:
    json.dump(hash_to_entity, f, indent=2)

print("Saved to hash_to_entity_mapping.json")
