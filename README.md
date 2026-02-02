# Euromonitor Multi-Agent Architecture

A comprehensive market research intelligence system that combines knowledge graphs, vector embeddings, and AI-powered chatbots to provide deep insights into the Asia Pacific toys and games market.

## Overview

This project implements a sophisticated RAG (Retrieval-Augmented Generation) system with dual-source retrieval capabilities, integrating structured knowledge graph data with semantic search to deliver accurate, well-cited market research insights.

### Key Components

- **RAG Chatbot**: Interactive AI assistant powered by Claude 3.5 Sonnet
- **Knowledge Graph**: Neo4j-based ontology with 126+ entities and relationships
- **Vector Search**: 768-dimensional semantic embeddings for intelligent retrieval
- **Euromonitor Integration**: Automated pipeline for ingesting market research data
- **Modern UI**: React-based ChatGPT-style interface

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    React Frontend (Port 5173)                │
│                 Modern chat interface with source citations  │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP/REST
┌────────────────────────▼────────────────────────────────────┐
│                 FastAPI Backend (Port 8000)                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Enhanced RAG Service                    │   │
│  │  - Dual-source retrieval (graph + embeddings)       │   │
│  │  - Hash-based entity mapping                        │   │
│  │  - Relationship traversal                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Embedding    │  │ Vector       │  │ Graph        │     │
│  │ Service      │  │ Search       │  │ Service      │     │
│  │ (all-mpnet)  │  │ (Cosine)     │  │ (Neo4j)      │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         LLM Service (Claude 3.5 Sonnet)              │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
                         │
              ┌──────────┴──────────┐
              │                     │
      ┌───────▼────────┐   ┌───────▼────────┐
      │  graph.json    │   │ embeddings.json│
      │  126 entities  │   │ 768-dim vectors│
      │  115 relations │   │ Hash-mapped    │
      └────────────────┘   └────────────────┘
```

## Quick Start

### Prerequisites

- Python 3.9+
- Node.js 18+
- Anthropic API key
- 8GB RAM minimum

### 1. Clone the Repository

```bash
git clone <repository-url>
cd euromonitor-multi-agent-architecture
```

### 2. Set Up the Backend

```bash
cd rag-chatbot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### 3. Start the Backend

```bash
# From rag-chatbot directory with venv activated
python -m uvicorn app.main:app --reload --port 8000
```

Expected output:
```
✅ All services initialized successfully!
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 4. Start the Frontend

In a new terminal:

```bash
cd rag-chatbot/frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Expected output:
```
VITE v7.3.1  ready in 432 ms
➜  Local:   http://localhost:5173/
```

### 5. Open in Browser

Navigate to: [http://localhost:5173](http://localhost:5173)

## Project Structure

```
euromonitor-multi-agent-architecture/
├── rag-chatbot/                    # Main RAG chatbot application
│   ├── app/                        # FastAPI backend
│   │   ├── main.py                 # API endpoints
│   │   ├── models/                 # Pydantic schemas
│   │   └── services/               # Core services
│   │       ├── rag_service.py      # Dual-source RAG orchestrator
│   │       ├── graph_service.py    # Knowledge graph operations
│   │       ├── embedding_service.py # Vector embedding generation
│   │       ├── vector_search.py    # Semantic search
│   │       └── llm_service.py      # Claude API integration
│   ├── frontend/                   # React UI
│   │   ├── src/
│   │   ├── package.json
│   │   └── vite.config.ts
│   ├── requirements.txt
│   ├── .env.example
│   ├── README.md                   # Chatbot user guide
│   ├── ARCHITECTURE.md             # Technical architecture deep-dive
│   ├── QUICK_START.md              # Setup instructions
│   └── TESTING_GUIDE.md            # Testing procedures
│
├── docs/                           # Documentation
│   ├── EUROMONITOR_INTEGRATION_SUMMARY.md  # Data integration guide
│   ├── knowledge-graph-ontology-design.md  # Ontology design
│   ├── neo4j-schema-euromonitor.md        # Neo4j schema
│   ├── HOW-TO-VISUALIZE.md                # Visualization guide
│   └── data-samples/                      # Sample data files
│
├── scripts/                        # Utilities
│   ├── neo4j-v2-asia-pacific/     # Neo4j data loaders
│   └── euromonitor_to_cypher.py   # Cypher generation utility
│
├── output/                         # Generated outputs
│   └── ontology/
│       └── market research/
│           ├── graph.json          # Knowledge graph data
│           ├── embeddings/
│           │   └── embeddings.json # Vector embeddings
│           └── schema.json         # Entity type definitions
│
├── ui/                            # Additional UI components
│
├── _bmad/                         # BMAD framework
│   ├── core/                      # Core workflows
│   ├── bmb/                       # Module builder
│   ├── bmm/                       # Module management
│   └── cis/                       # Innovation strategies
│
└── _bmad-output/                  # BMAD outputs
```

## Features

### Enhanced RAG Pipeline

- **Dual-Source Retrieval**: Combines knowledge graph traversal with vector similarity search
- **Hash-Based Mapping**: Efficient O(1) entity lookup using content-based hashing
- **Relationship Traversal**: Enriches context with 1-hop graph connections
- **Source Attribution**: Every answer includes citations to source entities

### Knowledge Graph

- **126+ entities** across 17 types (Markets, Companies, Trends, Products, etc.)
- **115+ relationships** modeling market dynamics
- **Rich metadata** including descriptions, aliases, and source URLs
- **Extensible schema** for continuous data integration

### Vector Search

- **768-dimensional embeddings** using sentence-transformers/all-mpnet-base-v2
- **Cosine similarity** for semantic matching
- **Configurable parameters**: top_k, min_similarity thresholds
- **Sub-second search** across entire knowledge base

### Modern UI

- **ChatGPT-style interface** with streaming responses
- **Collapsible source citations** for transparency
- **Real-time health monitoring** of backend services
- **Responsive design** for desktop and mobile

## Use Cases

### Market Analysis

```
Query: "What is driving growth in the Asia Pacific toys market?"

Response: The Asia Pacific toys market is being significantly influenced
by several key trends:

**Digital Integration** is transforming traditional toys by incorporating
AR, apps, and smart features. Companies like LEGO are actively adopting
these technologies...

Sources:
• Digital Integration (Trend)
• Asia Pacific Toys Market (Market)
• LEGO (Company)
```

### Competitive Intelligence

```
Query: "Who are the key competitors in construction toys?"

Response: The construction toys segment is highly competitive with
several major players:

**LEGO** dominates with its strong brand equity and digital integration...
```

### Trend Analysis

```
Query: "What consumer segments are driving market growth?"

Response: The **Kidults phenomenon** is a major growth driver, with
adults increasingly purchasing toys for themselves...
```

## Documentation

### For Users

- [RAG Chatbot User Guide](rag-chatbot/README.md) - Quick start and usage
- [Quick Start Guide](rag-chatbot/QUICK_START.md) - Setup instructions
- [Testing Guide](rag-chatbot/TESTING_GUIDE.md) - API testing and validation

### For Developers

- [Architecture Documentation](rag-chatbot/ARCHITECTURE.md) - Technical deep-dive
- [Dual Source Implementation](rag-chatbot/DUAL_SOURCE_IMPLEMENTATION.md) - RAG pipeline details
- [Knowledge Graph Ontology](docs/knowledge-graph-ontology-design.md) - Ontology design principles
- [Neo4j Schema](docs/neo4j-schema-euromonitor.md) - Database schema reference

### For Data Engineers

- [Euromonitor Integration](docs/EUROMONITOR_INTEGRATION_SUMMARY.md) - Data loading guide
- [Visualization Guide](docs/HOW-TO-VISUALIZE.md) - Graph visualization tools
- [Cypher Generator Utility](scripts/euromonitor_to_cypher.py) - Automated data loading

## Example Queries

Try these queries in the chatbot:

- "What is driving growth in the Asia Pacific toys market?"
- "Tell me about the kidults consumer segment"
- "What trends are affecting traditional toys and games?"
- "How is China's toys and games market performing?"
- "What is the forecast for the Asia Pacific market?"
- "Who are the key competitors in construction toys?"
- "What role do licensed toys play in the market?"

## Technology Stack

### Backend

- **FastAPI 0.109.0**: Modern async web framework
- **sentence-transformers 2.3.1**: State-of-the-art embeddings
- **anthropic 0.18.0**: Claude API client
- **numpy 1.26.3**: Numerical computing

### Frontend

- **React 18**: UI framework
- **TypeScript 5**: Type-safe JavaScript
- **Vite 7.3.1**: Fast build tool
- **Tailwind CSS 4**: Utility-first CSS
- **Axios**: HTTP client

### AI/ML

- **Embedding Model**: all-mpnet-base-v2 (768 dimensions)
- **LLM**: Claude 3.5 Sonnet (200K context window)
- **Vector Search**: Cosine similarity

### Data

- **Knowledge Graph**: JSON-based property graph
- **Vector Store**: Hash-mapped embeddings
- **Schema**: JSON schema definitions

## Performance

- **Response Time**: 2-5 seconds per query
- **Throughput**: 60-100 queries/minute (single instance)
- **Vector Search**: Sub-50ms
- **Embedding Generation**: ~100ms
- **LLM Response**: 2-5 seconds

## API Endpoints

### Health Check

```bash
curl http://localhost:8000/health
```

### Chat

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is driving growth in Asia Pacific?",
    "top_k": 5,
    "min_similarity": 0.3
  }'
```

## Configuration

### Environment Variables

Create `.env` file in `rag-chatbot/`:

```env
ANTHROPIC_API_KEY=your_api_key_here
GRAPH_PATH=../output/ontology/market research/graph.json
EMBEDDINGS_PATH=../output/ontology/market research/embeddings/embeddings.json
SCHEMA_PATH=../output/ontology/market research/schema.json
```

### Tunable Parameters

- **top_k** (1-10): Number of entities to retrieve (default: 5)
- **min_similarity** (0.0-1.0): Similarity threshold (default: 0.3)
- **include_relationships** (boolean): Include graph connections (default: true)

## Troubleshooting

### Backend Won't Start

```bash
# Check file paths
ls -la output/ontology/market\ research/

# Verify Python environment
which python
pip list
```

### Frontend Can't Connect

```bash
# Verify backend is running
curl http://localhost:8000/health

# Check CORS settings in app/main.py
```

### Slow First Query

The first query loads the embedding model (~420MB). Subsequent queries are faster.

### Inaccurate Responses

- Increase `min_similarity` (0.3 → 0.5) for more relevant matches
- Adjust `top_k` to change context size
- Check if query matches available entities

## Future Enhancements

### Planned Features

- [ ] Multi-turn conversation with history
- [ ] Query caching for common questions
- [ ] Export functionality (PDF, Markdown)
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Integration with additional data sources
- [ ] Automated data pipeline from PDFs
- [ ] Real-time data updates

## Contributing

### Adding New Data

1. Extract data from source documents
2. Generate Cypher statements using utility scripts
3. Load into knowledge graph
4. Regenerate embeddings if needed
5. Validate with test queries

### Extending the System

- Add new entity types in schema.json
- Update graph service for new relationships
- Enhance prompt engineering for better responses
- Implement additional retrieval strategies

## Security

- API keys stored in environment variables
- `.env` files excluded from version control
- Input validation on all endpoints
- Rate limiting recommended for production
- CORS configured for development (restrict in production)

## License

Internal use - Market Research Knowledge Graph

## Support

For issues or questions:

1. Check the relevant documentation:
   - User issues: [rag-chatbot/README.md](rag-chatbot/README.md)
   - Technical issues: [rag-chatbot/ARCHITECTURE.md](rag-chatbot/ARCHITECTURE.md)
   - Data issues: [docs/EUROMONITOR_INTEGRATION_SUMMARY.md](docs/EUROMONITOR_INTEGRATION_SUMMARY.md)

2. Review troubleshooting sections in documentation

3. Check logs:
   - Backend: Terminal running uvicorn
   - Frontend: Browser console and terminal running Vite

## Acknowledgments

Built with:
- **Anthropic Claude**: Advanced language understanding
- **Sentence Transformers**: High-quality embeddings
- **FastAPI**: Modern Python web framework
- **React**: Powerful UI library
- **Neo4j**: Graph database platform (ontology design)

---

**Version**: 1.0.0
**Last Updated**: February 2, 2026
**Status**: Production Ready ✅

Built with boring, reliable technology that actually works. 🏗️
