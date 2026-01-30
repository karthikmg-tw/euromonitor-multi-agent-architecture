# RAG Chatbot Architecture Documentation

## Table of Contents
- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Knowledge Graph](#knowledge-graph)
- [Hash-Based Entity Mapping](#hash-based-entity-mapping)
- [RAG Pipeline](#rag-pipeline)
- [Technical Stack](#technical-stack)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Performance Optimization](#performance-optimization)
- [Troubleshooting](#troubleshooting)

---

## Overview

This RAG (Retrieval-Augmented Generation) chatbot is designed to answer questions about the Asia Pacific toys and games market using a knowledge graph-based approach. It combines semantic search with large language models to provide accurate, source-cited responses.

### Key Capabilities
- **Natural Language Queries**: Ask questions in plain English
- **Knowledge Graph Reasoning**: Traverse entity relationships for context
- **Source Attribution**: Every answer includes citations to source entities
- **Real-time Processing**: Sub-30 second response times
- **Scalable Architecture**: Handles concurrent users efficiently

---

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│              (React Frontend - Port 5173)                    │
│  - Modern ChatGPT-style interface                           │
│  - Real-time messaging                                       │
│  - Collapsible source citations                             │
└─────────────────┬───────────────────────────────────────────┘
                  │ HTTP/REST
                  │
┌─────────────────▼───────────────────────────────────────────┐
│                   FastAPI Backend (Port 8000)                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              RAG Service (Orchestrator)               │  │
│  └───┬──────────────────────────────────────────────┬───┘  │
│      │                                               │       │
│  ┌───▼────────────┐  ┌──────────────┐  ┌───────────▼────┐ │
│  │ Embedding      │  │ Vector       │  │ Graph          │ │
│  │ Service        │  │ Search       │  │ Service        │ │
│  │                │  │ Service      │  │                │ │
│  │ - Query        │  │ - Cosine     │  │ - Entity       │ │
│  │   embedding    │  │   similarity │  │   retrieval    │ │
│  │ - sentence-    │  │ - Top-K      │  │ - Relationship │ │
│  │   transformers │  │   results    │  │   traversal    │ │
│  └────────────────┘  └──────────────┘  └────────────────┘ │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              LLM Service (Claude 3.5)                 │  │
│  │  - Context synthesis                                  │  │
│  │  - Response generation                                │  │
│  │  - Citation formatting                                │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                  ▲
                  │
          ┌───────┴────────┐
          │                │
    ┌─────▼─────┐   ┌─────▼─────┐
    │ graph.json │   │embeddings │
    │            │   │  .json    │
    │ 85 entities│   │           │
    │115 relations│  │768-dim    │
    │17 types    │   │vectors    │
    └────────────┘   └───────────┘
         Data Layer
```

### Component Responsibilities

#### **Frontend (React + TypeScript)**
- User interface rendering
- Message state management
- Real-time updates via HTTP polling
- Collapsible source display
- Health monitoring

#### **Backend (FastAPI + Python)**
- Request routing and validation
- RAG pipeline orchestration
- Error handling and logging
- CORS management
- Health check endpoints

#### **Data Layer**
- **graph.json**: Knowledge graph with entities and relationships
- **embeddings.json**: Pre-computed 768-dimensional vectors
- **schema.json**: Entity type definitions and constraints

---

## Knowledge Graph

### Structure

The knowledge graph is a property graph consisting of:

#### **Entities (Nodes)**
Each entity represents a concept, product, company, or market element.

**Entity Schema:**
```json
{
  "id": "unique-identifier",
  "label": "Human-readable name",
  "type": "EntityType",
  "description": "Detailed description",
  "aliases": ["Alternative names"],
  "properties": {
    "source_urls": "https://source.com/page",
    "additional_metadata": "..."
  },
  "embedding_hash": "hash-for-vector-lookup"
}
```

#### **Entity Types (17 total)**
- **Market**: Geographic markets (e.g., Asia Pacific Toys Market)
- **Location**: Countries and regions (e.g., China, Japan)
- **Category**: Product categories (e.g., Construction Toys)
- **Trend**: Market trends (e.g., Digital Integration)
- **Company**: Manufacturers and retailers (e.g., LEGO, Mattel)
- **Brand**: Product brands
- **Product**: Specific products
- **ConsumerSegment**: Target demographics (e.g., Kidults)
- **DistributionChannel**: Sales channels
- **Regulation**: Legal frameworks
- **Organization**: Industry bodies
- **Event**: Market events
- **Technology**: Tech innovations
- **Material**: Product materials
- **Design**: Design patterns
- **Feature**: Product features
- **Metric**: Market metrics

#### **Relationships (Edges)**
Relationships connect entities and provide semantic meaning.

**Relationship Types:**
- `HAS_TREND`: Market → Trend
- `LOCATED_IN`: Entity → Location
- `COMPETES_WITH`: Company → Company
- `TARGETS`: Product → ConsumerSegment
- `USES_CHANNEL`: Company → DistributionChannel
- `MANUFACTURES`: Company → Product
- `BELONGS_TO`: Product → Category
- `INFLUENCED_BY`: Market → Trend
- `OPERATES_IN`: Company → Market

**Relationship Schema:**
```json
{
  "id": "relationship-id",
  "source": "source-entity-id",
  "target": "target-entity-id",
  "type": "RELATIONSHIP_TYPE",
  "properties": {
    "strength": 0.8,
    "since": "2020"
  }
}
```

### Example Graph Fragment

```
[Asia Pacific Toys Market]
    ├─ HAS_TREND → [Digital Integration]
    ├─ HAS_TREND → [Kidults Phenomenon]
    ├─ LOCATED_IN → [China]
    │   └─ OPERATES_IN ← [LEGO]
    │       ├─ MANUFACTURES → [LEGO Sets]
    │       └─ TARGETS → [Kidults]
    └─ HAS_CATEGORY → [Construction Toys]
        └─ BELONGS_TO ← [LEGO Sets]
```

---

## Hash-Based Entity Mapping

### The Architecture Problem

When building a RAG system with separate vector search and knowledge graph components, we face a critical challenge: **How do we connect embeddings to their source entities?**

**The Setup:**
- **Vector Database**: Stores 768-dimensional embeddings for semantic search
- **Knowledge Graph**: Stores rich entity objects with descriptions, relationships, properties
- **The Problem**: Vector search returns embedding IDs, but we need full entity objects

### Why We Need Hashes

#### **Problem 1: Decoupled Storage**

Vector embeddings and graph data are stored separately:

```
embeddings.json:
{
  "???": [0.234, -0.112, 0.445, ..., 0.567]  # 768 dimensions
}

graph.json:
{
  "entities": [
    {
      "id": "digital-integration-trend",
      "label": "Digital Integration",
      "description": "The integration of...",
      ...
    }
  ]
}
```

**Question:** What identifier (???) should we use to link the embedding to the entity?

#### **Problem 2: Why Not Use Entity ID Directly?**

You might think: "Just use the entity ID!"

```json
// Naive approach - DON'T DO THIS
{
  "digital-integration-trend": [0.234, -0.112, ...]
}
```

**Issues with this approach:**

1. **Entity ID Changes**: If you rename an entity ID in the graph, embeddings become orphaned
2. **No Embedding Tracking**: Can't tell if embedding is stale (entity description changed)
3. **Debugging Nightmare**: No way to verify embedding matches current entity content
4. **Collision Risk**: Entity IDs might conflict with system IDs
5. **Regeneration Problem**: When regenerating embeddings, how do you know which ones to update?

### The Hash Solution

Instead, we use **content-based hashing** - generating a deterministic hash from the entity's text content.

#### **What Gets Hashed?**

```python
def generate_entity_hash(entity):
    """Generate a deterministic hash from entity content."""

    # Combine all text that was embedded
    text_to_hash = " ".join([
        entity.get("label", ""),
        entity.get("description", ""),
        " ".join(entity.get("aliases", [])),
        str(entity.get("properties", {}))
    ])

    # Generate SHA-256 hash
    hash_object = hashlib.sha256(text_to_hash.encode('utf-8'))
    return hash_object.hexdigest()[:16]  # Use first 16 chars for brevity

# Example output: "a3f2c8e9d1b4f6a7"
```

**Key Properties of Hashes:**

1. **Deterministic**: Same content → Same hash (always)
2. **Content-Dependent**: Different content → Different hash (almost always)
3. **Fixed Length**: Always 16 characters (or 64 if using full SHA-256)
4. **Collision Resistant**: Virtually impossible for two different texts to produce same hash
5. **One-Way**: Can't reverse hash back to original text

### Complete Data Flow with Hashes

#### **1. Embedding Generation (Offline)**

When creating the embeddings file:

```python
def create_embeddings(graph):
    embeddings = {}

    for entity in graph["entities"]:
        # 1. Combine text for embedding
        text = f"{entity['label']} {entity['description']}"

        # 2. Generate embedding vector
        vector = model.encode(text)  # 768 dimensions

        # 3. Generate content hash
        entity_hash = generate_entity_hash(entity)

        # 4. Store in entity for future lookup
        entity["embedding_hash"] = entity_hash

        # 5. Store embedding with hash as key
        embeddings[entity_hash] = vector.tolist()

    return embeddings

# Result stored in embeddings.json:
{
  "a3f2c8e9d1b4f6a7": [0.234, -0.112, 0.445, ...],  # Digital Integration
  "b7e4d2f1c9a8e5b3": [0.567, 0.234, -0.334, ...],  # Licensed Toys
  "c8f3e2d1b5a9f6c4": [-0.112, 0.445, 0.223, ...]   # Traditional Toys
}

# Entity in graph.json includes hash:
{
  "id": "digital-integration-trend",
  "label": "Digital Integration",
  "description": "The integration of...",
  "embedding_hash": "a3f2c8e9d1b4f6a7"  # ← Link to embedding
}
```

#### **2. Query Time (Online)**

When a user asks a question:

```python
# Step 1: User query
user_query = "What trends are affecting toys?"

# Step 2: Embed query (same model as entities)
query_vector = model.encode(user_query)  # [0.234, -0.112, ...]

# Step 3: Vector search returns HASHES with similarity scores
vector_results = vector_search(query_vector, embeddings)
# Returns: [
#   ("a3f2c8e9d1b4f6a7", 0.87),  # Best match
#   ("b7e4d2f1c9a8e5b3", 0.82),  # Second best
#   ("c8f3e2d1b5a9f6c4", 0.76)   # Third best
# ]

# Step 4: Lookup entities by hash
entities = []
for hash_id, similarity in vector_results:
    # Find entity with matching embedding_hash
    entity = graph.get_entity_by_hash(hash_id)
    if entity:
        entities.append({
            "entity": entity,
            "similarity": similarity
        })

# Step 5: Now we have full entity objects!
# [
#   {
#     "entity": {
#       "id": "digital-integration-trend",
#       "label": "Digital Integration",
#       "description": "The integration of...",
#       "embedding_hash": "a3f2c8e9d1b4f6a7"
#     },
#     "similarity": 0.87
#   },
#   ...
# ]
```

### Hash Lookup Implementation

**Efficient O(1) Lookup:**

```python
class GraphService:
    def __init__(self, graph_path):
        self.graph = self.load_graph(graph_path)

        # Build hash index for O(1) lookup
        self.hash_to_entity = {}
        for entity in self.graph["entities"]:
            hash_id = entity.get("embedding_hash")
            if hash_id:
                self.hash_to_entity[hash_id] = entity

    def get_entity_by_hash(self, hash_id: str):
        """O(1) lookup of entity by embedding hash."""
        return self.hash_to_entity.get(hash_id)
```

**Without Hash Index (Slow - O(n)):**
```python
# BAD: Linear search through all entities
for entity in graph["entities"]:
    if entity.get("embedding_hash") == hash_id:
        return entity  # Must check every entity!
```

**With Hash Index (Fast - O(1)):**
```python
# GOOD: Direct dictionary lookup
return hash_to_entity[hash_id]  # Instant!
```

### Why Hashes Are Superior

#### **1. Content Integrity**

Hash changes if content changes:

```python
# Original entity
entity_v1 = {
    "label": "Digital Integration",
    "description": "Basic digital features"
}
hash_v1 = "a3f2c8e9"  # Hash of above

# Updated entity (description improved)
entity_v2 = {
    "label": "Digital Integration",
    "description": "Advanced AR and app integration with IoT"
}
hash_v2 = "f7b2e8c4"  # Different hash!

# When regenerating embeddings:
if entity["embedding_hash"] != generate_hash(entity):
    # Content changed - regenerate embedding
    new_embedding = model.encode(entity)
    embeddings[generate_hash(entity)] = new_embedding
```

**Benefit:** Automatic staleness detection for embeddings.

#### **2. Collision Avoidance**

```python
# SHA-256 has 2^256 possible hashes
# For 1 million entities, collision probability: ~10^-60
# More likely to win lottery 10 times in a row than get collision

# Even with birthday paradox:
# Need ~2^128 hashes before 50% collision chance
# = 340,282,366,920,938,463,463,374,607,431,768,211,456 entities
# (your graph has 126 entities)
```

**Benefit:** Effectively zero collision risk in practice.

#### **3. Debugging & Validation**

```python
def validate_embeddings(graph, embeddings):
    """Verify all embeddings match current entity content."""

    issues = []
    for entity in graph["entities"]:
        stored_hash = entity.get("embedding_hash")
        current_hash = generate_entity_hash(entity)

        if stored_hash != current_hash:
            issues.append({
                "entity_id": entity["id"],
                "problem": "Content changed, embedding stale",
                "stored_hash": stored_hash,
                "current_hash": current_hash
            })

        if stored_hash not in embeddings:
            issues.append({
                "entity_id": entity["id"],
                "problem": "Embedding missing",
                "hash": stored_hash
            })

    return issues

# Output:
# [
#   {
#     "entity_id": "digital-integration",
#     "problem": "Content changed, embedding stale",
#     "stored_hash": "old_hash_123",
#     "current_hash": "new_hash_456"
#   }
# ]
```

**Benefit:** Easy to detect and fix data inconsistencies.

#### **4. Flexible Entity IDs**

```python
# Can change entity IDs without breaking embeddings
# Old graph:
{
  "id": "trend_digital_integration",  # Old naming convention
  "embedding_hash": "a3f2c8e9"
}

# New graph (renamed ID):
{
  "id": "digital-integration-trend",  # New naming convention
  "embedding_hash": "a3f2c8e9"  # SAME HASH - still works!
}

# Embedding file unchanged:
{
  "a3f2c8e9": [0.234, -0.112, ...]  # Still valid
}
```

**Benefit:** Refactor entity IDs without regenerating embeddings.

### Alternative Approaches (and Why They're Worse)

#### **Alternative 1: Use Entity ID as Key**

```json
{
  "digital-integration-trend": [0.234, -0.112, ...]
}
```

**Problems:**
- ❌ Can't detect stale embeddings
- ❌ Breaking changes if IDs renamed
- ❌ No content verification

#### **Alternative 2: Sequential Integer IDs**

```json
{
  "0": [0.234, -0.112, ...],
  "1": [0.567, 0.234, ...],
  "2": [-0.112, 0.445, ...]
}
```

**Problems:**
- ❌ Need separate mapping file (entity_id → integer)
- ❌ Fragile - insert new entity breaks all subsequent IDs
- ❌ Can't detect content changes

#### **Alternative 3: UUID**

```json
{
  "550e8400-e29b-41d4-a716-446655440000": [0.234, -0.112, ...]
}
```

**Problems:**
- ❌ Random - not content-dependent
- ❌ Same entity, different embeddings = different UUIDs
- ❌ Can't verify embedding matches content

### Hash File Structure

**Complete embeddings.json:**
```json
{
  "a3f2c8e9d1b4f6a7": [0.234, -0.112, 0.445, ..., 0.567],
  "b7e4d2f1c9a8e5b3": [0.567, 0.234, -0.334, ..., 0.123],
  "c8f3e2d1b5a9f6c4": [-0.112, 0.445, 0.223, ..., -0.234],
  ...
  // 126 entries total (one per entity)
}
```

**Complete entity with hash:**
```json
{
  "id": "digital-integration-trend",
  "label": "Digital Integration",
  "type": "Trend",
  "description": "The integration of digital technologies into traditional toys...",
  "aliases": ["Digital Features", "Smart Toys"],
  "properties": {
    "source_urls": "https://euromonitor.com/...",
    "impact": "high"
  },
  "embedding_hash": "a3f2c8e9d1b4f6a7"  // ← Links to embeddings.json
}
```

### Performance Implications

**Memory Usage:**
```python
# Hash size: 16 bytes (16 characters)
# 126 entities × 16 bytes = 2,016 bytes (2 KB) for all hashes

# Compare to storing full entity objects in vector DB:
# Average entity JSON: ~500 bytes
# 126 entities × 500 bytes = 63,000 bytes (63 KB)

# Hash = 32x more memory efficient
```

**Lookup Speed:**
```python
# Hash table lookup: O(1) - constant time
# 1 entity or 1 million entities = same speed

# vs. Linear search: O(n) - scales with data
# 126 entities: ~63 comparisons on average
# 1,000,000 entities: ~500,000 comparisons on average
```

### Summary

**Why Hashes:**
1. ✅ **Deterministic**: Same content → same hash
2. ✅ **Content-Based**: Detects when embeddings are stale
3. ✅ **Efficient**: O(1) lookups, minimal memory
4. ✅ **Collision-Safe**: Effectively zero collision risk
5. ✅ **Flexible**: Can change entity IDs without breaking embeddings
6. ✅ **Debuggable**: Easy to validate data consistency

**The Flow:**
```
Content → Hash → Embedding
  ↓        ↓        ↓
Entity  Links   Vector DB
  ↑        ↑        ↑
  └────────┴────────┘
    O(1) lookup
```

Hashes are the elegant bridge between semantic search (vectors) and structured knowledge (graph), enabling fast, reliable, and maintainable RAG systems.

---

## RAG Pipeline

### Step-by-Step Process

#### **1. Query Embedding**

**Input:** User's natural language question
```python
query = "What trends are affecting traditional toys?"
```

**Process:**
- Load sentence-transformers model: `all-mpnet-base-v2`
- Generate 768-dimensional embedding vector
- Normalize vector for cosine similarity

**Output:** Query vector `[0.234, -0.112, ..., 0.567]` (768 dimensions)

**Why this works:**
- Semantic similarity captures meaning, not just keywords
- Same model used for query and entity embeddings
- Works across paraphrases and synonyms

---

#### **2. Vector Search**

**Input:** Query embedding + configuration
```python
{
  "query_embedding": [...],
  "top_k": 5,
  "min_similarity": 0.05
}
```

**Process:**
```python
# Cosine similarity calculation
similarity(query, entity) = dot(query, entity) / (||query|| * ||entity||)

# For each entity embedding:
for entity_hash, entity_embedding in embeddings.items():
    score = cosine_similarity(query_embedding, entity_embedding)
    if score >= min_similarity:
        results.append((entity_hash, score))

# Sort by similarity (descending)
results.sort(key=lambda x: x[1], reverse=True)
return results[:top_k]
```

**Output:** Top-K entity hashes with similarity scores
```python
[
  ("hash123", 0.87),  # Digital Integration trend
  ("hash456", 0.82),  # Licensed Toys trend
  ("hash789", 0.76),  # Traditional Toys category
  ("hash012", 0.71),  # Sustainability trend
  ("hash345", 0.68)   # Asia Pacific Market
]
```

**Why this works:**
- Cosine similarity measures semantic closeness
- Top-K ensures we get the most relevant entities
- Threshold filters out noise

---

#### **3. Entity Retrieval**

**Input:** Entity hashes from vector search

**Process:**
```python
# Load graph.json
graph = load_graph()

# Retrieve full entity objects
entities = []
for entity_hash, similarity in search_results:
    entity = graph.get_entity_by_hash(entity_hash)
    if entity:
        entities.append({
            "entity": entity,
            "similarity": similarity
        })
```

**Output:** Full entity objects with metadata
```python
[
  {
    "id": "digital-integration-trend",
    "label": "Digital Integration",
    "type": "Trend",
    "description": "The integration of digital technologies into traditional toys...",
    "properties": {
      "source_urls": "https://euromonitor.com/..."
    }
  },
  ...
]
```

---

#### **4. Relationship Traversal**

**Input:** Retrieved entities

**Process:**
```python
# For each entity, find connected entities (1-hop)
relationships = []
for entity in entities:
    # Find outgoing relationships
    outgoing = graph.get_relationships_from(entity.id)
    relationships.extend(outgoing)

    # Find incoming relationships
    incoming = graph.get_relationships_to(entity.id)
    relationships.extend(incoming)

# Deduplicate
unique_relationships = remove_duplicates(relationships)
```

**Output:** Enriched context with relationships
```python
{
  "entities": [...],
  "relationships": [
    {
      "source": "asia-pacific-market",
      "target": "digital-integration-trend",
      "type": "HAS_TREND"
    },
    {
      "source": "lego",
      "target": "digital-integration-trend",
      "type": "ADOPTS"
    }
  ]
}
```

**Why this works:**
- Relationships provide context
- 1-hop traversal captures immediate connections
- Avoids overwhelming the LLM with too much data

---

#### **5. Context Synthesis**

**Input:** Entities + Relationships

**Process:**
```python
def build_context(entities, relationships):
    context = "# Relevant Information\n\n"

    # Add entity information
    for entity in entities:
        context += f"## {entity['label']} ({entity['type']})\n"
        context += f"{entity['description']}\n\n"

        if entity.get('aliases'):
            context += f"Also known as: {', '.join(entity['aliases'])}\n\n"

    # Add relationship information
    if relationships:
        context += "# Relationships\n\n"
        for rel in relationships:
            context += f"- {rel['source']} {rel['type']} {rel['target']}\n"

    return context
```

**Output:** Structured context string
```markdown
# Relevant Information

## Digital Integration (Trend)
The integration of digital technologies into traditional toys, including AR, apps, and smart features...

## Licensed Toys (Trend)
Growing demand for toys based on popular media franchises...

# Relationships
- Asia Pacific Market HAS_TREND Digital Integration
- LEGO ADOPTS Digital Integration
- Traditional Toys INFLUENCED_BY Digital Integration
```

---

#### **6. LLM Response Generation**

**Input:** User query + Context + System prompt

**System Prompt:**
```
You are a market research analyst specializing in the Asia Pacific toys and games industry.

Rules:
1. Answer based ONLY on the provided context
2. Cite specific entities when making claims
3. If information is not in context, say so
4. Be concise but comprehensive
5. Use professional, analytical language

Context:
{context}

User Question:
{query}

Provide a detailed answer with specific references to the entities mentioned in the context.
```

**Process:**
```python
response = claude.complete(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    system=system_prompt,
    messages=[{
        "role": "user",
        "content": query
    }]
)
```

**Output:** Natural language response
```
The Asia Pacific toys market is being significantly influenced by several key trends:

**Digital Integration** is transforming traditional toys by incorporating AR, apps, and smart features. Companies like LEGO are actively adopting these technologies to enhance play experiences.

**Licensed Toys** continue to drive growth, with increasing demand for products based on popular media franchises...
```

---

#### **7. Source Formatting**

**Input:** Entities used in response

**Process:**
```python
sources = []
for entity in retrieved_entities:
    source = {
        "entity_id": entity["id"],
        "label": entity["label"],
        "type": entity["type"],
        "description": entity["description"][:200],
        "source_urls": entity["properties"].get("source_urls", "N/A")
    }
    sources.append(source)

return {
    "answer": response_text,
    "sources": sources
}
```

**Output:** Complete response with citations
```json
{
  "answer": "The Asia Pacific toys market is being...",
  "sources": [
    {
      "entity_id": "digital-integration",
      "label": "Digital Integration",
      "type": "Trend",
      "description": "The integration of digital technologies...",
      "source_urls": "https://euromonitor.com/..."
    }
  ]
}
```

---

## Technical Stack

### Backend

**Framework: FastAPI 0.109.0**
- Async request handling
- Automatic API documentation (Swagger/OpenAPI)
- Pydantic validation
- CORS middleware

**ML/AI Libraries:**
- `sentence-transformers 2.3.1`: Embedding generation
- `numpy 1.26.3`: Vector operations
- `anthropic 0.18.0`: Claude API client

**Data Processing:**
- `python-dotenv 1.0.0`: Environment management
- `requests 2.31.0`: HTTP client

### Frontend

**Framework: React 18 + TypeScript**
- Component-based architecture
- Type-safe development
- Hot module replacement (Vite)

**Build Tools:**
- `Vite 7.3.1`: Fast dev server & bundler
- `TypeScript 5.x`: Type checking
- `Tailwind CSS 4.x`: Utility-first CSS

**HTTP Client:**
- `axios`: API communication

### Embedding Model

**Model: `sentence-transformers/all-mpnet-base-v2`**
- **Architecture**: MPNet (Masked and Permuted Pre-training)
- **Dimensions**: 768
- **Max Sequence Length**: 384 tokens
- **Performance**: 69.6 on Semantic Textual Similarity benchmark
- **Size**: ~420MB

**Why this model:**
- High quality sentence embeddings
- Good balance of speed and accuracy
- Widely used and well-tested
- Pre-trained on large corpus

### LLM: Claude 3.5 Sonnet

**Model ID**: `claude-3-5-sonnet-20241022`
- **Context Window**: 200K tokens
- **Output**: Up to 8K tokens
- **Strengths**:
  - Accurate citation
  - Complex reasoning
  - Concise responses
  - Professional tone

---

## API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### **GET /health**
Health check endpoint

**Response:**
```json
{
  "status": "ok",
  "version": "1.0.0",
  "services": {
    "graph": "loaded",
    "vector_search": "loaded",
    "embeddings": "loaded",
    "llm": "ready"
  }
}
```

---

#### **POST /chat**
Main chat endpoint for RAG queries

**Request Body:**
```json
{
  "query": "What trends are affecting toys?",
  "top_k": 5,
  "include_relationships": true,
  "min_similarity": 0.05,
  "debug": false
}
```

**Parameters:**
- `query` (required): User's question
- `top_k` (optional, default: 5): Number of entities to retrieve
- `include_relationships` (optional, default: true): Include graph relationships
- `min_similarity` (optional, default: 0.05): Minimum cosine similarity threshold
- `debug` (optional, default: false): Include debug information

**Response:**
```json
{
  "answer": "The Asia Pacific toys market...",
  "sources": [
    {
      "entity_id": "digital-integration",
      "label": "Digital Integration",
      "type": "Trend",
      "description": "Integration of digital technologies...",
      "source_urls": "https://euromonitor.com/..."
    }
  ],
  "debug": {
    "num_entities": 5,
    "num_relationships": 12,
    "similarities": [
      {"entity_id": "...", "similarity": 0.87}
    ]
  }
}
```

**Error Responses:**
```json
// 503 Service Unavailable
{
  "detail": "Services not initialized"
}

// 500 Internal Server Error
{
  "detail": "Error processing request: ..."
}
```

---

#### **POST /entity**
Get detailed information about a specific entity

**Request Body:**
```json
{
  "entity_id": "digital-integration"
}
```

**Response:**
```json
{
  "entity": {
    "id": "digital-integration",
    "label": "Digital Integration",
    "type": "Trend",
    "description": "...",
    "properties": {...}
  },
  "relationships": [...],
  "related_entities": [...]
}
```

---

## Deployment

### Prerequisites
- Python 3.9+
- Node.js 18+
- 8GB RAM minimum
- Anthropic API key

### Backend Setup

```bash
# Navigate to backend directory
cd rag-chatbot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API key and paths

# Start backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd rag-chatbot/frontend

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

### Production Deployment

**Backend (Gunicorn + Uvicorn):**
```bash
gunicorn app.main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
```

**Frontend (Nginx):**
```bash
# Build frontend
npm run build

# Serve with Nginx
# Copy dist/ to /var/www/html/
```

### Docker Deployment

**Backend Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Frontend Dockerfile:**
```dockerfile
FROM node:18 AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
```

**Docker Compose:**
```yaml
version: '3.8'

services:
  backend:
    build: ./rag-chatbot
    ports:
      - "8000:8000"
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    volumes:
      - ./output:/app/output

  frontend:
    build: ./rag-chatbot/frontend
    ports:
      - "80:80"
    depends_on:
      - backend
```

---

## Performance Optimization

### Current Performance

**Response Times:**
- Embedding generation: ~100ms
- Vector search: ~50ms
- Entity retrieval: ~20ms
- LLM generation: ~2-5 seconds
- **Total**: ~2.5-5.5 seconds per query

**Throughput:**
- Concurrent users: 10-20 (single instance)
- Queries per minute: ~60-100

### Optimization Strategies

#### **1. Caching**

**Query Caching:**
```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def get_embedding(query: str):
    return embedding_service.embed(query)
```

**Benefits:**
- Repeated queries: 0ms embedding time
- Common questions served instantly

#### **2. Batch Processing**

For multiple queries:
```python
# Batch embed multiple queries
embeddings = model.encode([query1, query2, query3], batch_size=32)
```

#### **3. Index Optimization**

**FAISS for Vector Search:**
```python
import faiss

# Build FAISS index
dimension = 768
index = faiss.IndexFlatIP(dimension)  # Inner product = cosine for normalized vectors
index.add(embeddings_matrix)

# Search
D, I = index.search(query_embedding, k=top_k)
```

**Benefits:**
- 10-100x faster search
- Scales to millions of vectors

#### **4. Model Optimization**

**Quantization:**
- Reduce model size by 4x
- Minimal accuracy loss
- Faster inference

#### **5. Response Streaming**

Stream LLM responses:
```python
async def stream_response(query):
    async for chunk in claude.stream(prompt):
        yield chunk
```

**Benefits:**
- Lower perceived latency
- Better UX

---

## Troubleshooting

### Common Issues

#### **Issue: "Services not initialized"**

**Cause:** Graph/embeddings files not loaded

**Solution:**
```bash
# Check file paths in .env
ls -la output/ontology/market\ research/

# Verify paths match .env configuration
GRAPH_PATH=../output/ontology/market research/graph.json
EMBEDDINGS_PATH=../output/ontology/market research/embeddings/embeddings.json
```

---

#### **Issue: "Cannot connect to backend"**

**Cause:** CORS or backend not running

**Solution:**
```bash
# Check backend is running
curl http://localhost:8000/health

# Verify CORS is enabled in main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

#### **Issue: Slow first query**

**Cause:** Model loading on first request

**Solution:**
```python
# Warm up model on startup
@app.on_event("startup")
async def warmup():
    embedding_service.embed("warmup query")
```

---

#### **Issue: Out of memory**

**Cause:** Loading large graph or model

**Solution:**
- Increase RAM allocation
- Use model quantization
- Stream large responses
- Implement pagination for results

---

#### **Issue: Inaccurate responses**

**Cause:** Irrelevant entities retrieved

**Solutions:**
1. **Increase min_similarity** (0.05 → 0.3)
2. **Decrease top_k** (10 → 3)
3. **Improve query** (more specific)
4. **Enhance entity descriptions** in graph
5. **Update embeddings** with better model

---

## Data Pipeline

### Creating/Updating the Knowledge Graph

```bash
# 1. Extract data from source
python scripts/extract_data.py --input raw_data.xlsx --output entities.json

# 2. Create graph
python scripts/create_graph.py --entities entities.json --output graph.json

# 3. Generate embeddings
python scripts/generate_embeddings.py --graph graph.json --output embeddings.json

# 4. Validate
python scripts/validate_graph.py --graph graph.json --embeddings embeddings.json
```

---

## Security Considerations

### API Key Management
- Store API keys in environment variables
- Never commit .env files
- Use secret management in production (AWS Secrets Manager, Vault)

### Input Validation
- Sanitize user queries
- Limit query length (max 500 chars)
- Rate limiting (max 60 requests/minute)

### Data Privacy
- No PII in knowledge graph
- Log sanitization
- GDPR compliance for user data

---

## Future Enhancements

### Planned Features

**Multi-hop Reasoning:**
- Traverse 2-3 hops in graph
- More complex question answering

**Conversation Memory:**
- Store chat history
- Context-aware follow-ups

**Advanced Search:**
- Hybrid search (BM25 + vector)
- Reranking with cross-encoders

**Analytics:**
- Query analytics
- Popular topics
- User feedback loop

**Knowledge Graph Expansion:**
- Auto-entity extraction from documents
- Relationship inference
- Temporal reasoning

---

## Conclusion

This RAG chatbot demonstrates a production-ready approach to knowledge graph-based question answering. By combining semantic search, graph traversal, and large language models, it provides accurate, well-cited responses to domain-specific queries.

The architecture is modular, scalable, and maintainable, making it suitable for enterprise deployment and future enhancements.

---

## Additional Resources

- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **Sentence Transformers**: https://www.sbert.net/
- **Claude API**: https://docs.anthropic.com/
- **React Documentation**: https://react.dev/

---

**Last Updated**: January 30, 2026
**Version**: 1.0.0
**Maintained By**: Development Team
