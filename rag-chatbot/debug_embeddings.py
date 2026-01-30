#!/usr/bin/env python3
"""
Debug script to figure out how embeddings were generated
"""
import json
import hashlib

# Load graph
with open('../output/ontology/market research/graph.json') as f:
    graph = json.load(f)

# Load embeddings
with open('../output/ontology/market research/embeddings/embeddings.json') as f:
    embeddings = json.load(f)

print(f"Total entities: {len(graph['entities'])}")
print(f"Total embeddings: {len(embeddings)}")
print()

# Get first entity
entity = graph['entities'][0]
print(f"Sample entity:")
print(f"  ID: {entity['id']}")
print(f"  Label: {entity['label']}")
print(f"  Description: {entity.get('description', '')[:100]}...")
print()

# Try different text combinations to generate hash
text_combinations = [
    ("description only", entity.get('description', '')),
    ("label only", entity.get('label', '')),
    ("label + description", f"{entity.get('label', '')}. {entity.get('description', '')}"),
    ("label: description", f"{entity.get('label', '')}: {entity.get('description', '')}"),
]

print("Testing hash combinations:")
embedding_hashes = list(embeddings.keys())
for name, text in text_combinations:
    text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
    match = text_hash in embeddings
    print(f"  {name:20s}: {text_hash[:16]}... {'✅ MATCH!' if match else '❌'}")

print()
print("First 3 embedding hashes:")
for i, h in enumerate(embedding_hashes[:3]):
    print(f"  {i+1}. {h[:16]}...")
