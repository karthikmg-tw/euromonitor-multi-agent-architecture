# 🤖 Market Research RAG Chatbot

A simple, practical RAG (Retrieval-Augmented Generation) chatbot built on top of your market research knowledge graph and ontology.

## 🏗️ Architecture

```
User Question
      ↓
Gradio UI (port 7860)
      ↓
FastAPI Backend (port 8000)
      ↓
┌─────────────────────────────────────┐
│     RAG Pipeline                    │
│                                     │
│  1. Embed Query                     │
│     → sentence-transformers         │
│     → 768-dim vector                │
│                                     │
│  2. Vector Search                   │
│     → Cosine similarity             │
│     → Top-K entities                │
│                                     │
│  3. Context Retrieval               │
│     → Load entities from graph.json │
│     → Traverse relationships        │
│                                     │
│  4. Response Generation             │
│     → Claude 3.5 Sonnet             │
│     → Context + Query → Answer      │
│                                     │
│  5. Citation Formatting             │
│     → Entity sources                │
└─────────────────────────────────────┘
      ↓
   Answer + Sources
```

## 📦 Tech Stack

- **Backend:** FastAPI
- **Embeddings:** sentence-transformers/all-mpnet-base-v2 (768 dims)
- **Vector Search:** NumPy cosine similarity
- **LLM:** Claude 3.5 Sonnet (Anthropic API)
- **UI:** Gradio
- **Data:** Knowledge graph from `output/ontology/market research/`

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.9+
- Anthropic API key

### 2. Installation

```bash
# Navigate to the rag-chatbot directory
cd rag-chatbot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the `rag-chatbot/` directory:

```bash
cp .env.example .env
```

Edit `.env` and add your API key:

```env
ANTHROPIC_API_KEY=your_actual_api_key_here
GRAPH_PATH=../output/ontology/market research/graph.json
EMBEDDINGS_PATH=../output/ontology/market research/embeddings/embeddings.json
SCHEMA_PATH=../output/ontology/market research/schema.json
```

### 4. Start the Backend

In one terminal:

```bash
cd rag-chatbot
source venv/bin/activate
python -m uvicorn app.main:app --reload --port 8000
```

You should see:
```
✅ All services initialized successfully!
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 5. Start the UI

In another terminal:

```bash
cd rag-chatbot
source venv/bin/activate
python ui/gradio_app.py
```

You should see:
```
Running on local URL:  http://0.0.0.0:7860
```

### 6. Open in Browser

Navigate to: **http://localhost:7860**

## 💬 Example Queries

Try asking:

- "What is driving growth in the Asia Pacific toys market?"
- "Tell me about the kidults consumer segment"
- "What trends are affecting traditional toys and games?"
- "How is China's toys and games market performing?"
- "What is the forecast for the Asia Pacific market?"
- "Who are the key competitors in construction toys?"
- "What role do licensed toys play in the market?"

## 🔧 Configuration Parameters

You can tune these parameters in the Gradio UI:

- **top_k** (1-10): Number of similar entities to retrieve
  - Higher = more context, but potentially less relevant
  - Default: 5

- **min_similarity** (0.0-1.0): Minimum cosine similarity threshold
  - Higher = only very similar entities
  - Lower = broader matching
  - Default: 0.3

## 📊 Data Overview

The chatbot uses your existing ontology:

- **126 entities** across 17 types:
  - Markets, Locations, Categories, Trends
  - Companies, Brands, Products
  - Consumer Segments, Distribution Channels
  - Regulations, Organizations, Events

- **768-dimensional embeddings** (all-mpnet-base-v2)

- **Relationships** between entities for context enrichment

## 🧪 Testing

### Test Backend Health

```bash
curl http://localhost:8000/health
```

Expected response:
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

### Test Chat API

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is driving growth in Asia Pacific?",
    "top_k": 5,
    "include_relationships": true,
    "min_similarity": 0.3
  }'
```

## 📁 Project Structure

```
rag-chatbot/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI application
│   ├── models/
│   │   └── schemas.py             # Pydantic models
│   └── services/
│       ├── graph_service.py       # Load & query graph.json
│       ├── embedding_service.py   # Generate embeddings
│       ├── vector_search.py       # Cosine similarity search
│       ├── llm_service.py         # Claude API integration
│       └── rag_service.py         # RAG orchestrator
├── ui/
│   └── gradio_app.py              # Gradio chat interface
├── requirements.txt
├── .env.example
├── .env                           # Your config (not committed)
└── README.md
```

## 🎯 How It Works

1. **User asks a question** in the Gradio UI

2. **Query embedding** generated using sentence-transformers
   - Same model as original embeddings (all-mpnet-base-v2)

3. **Vector search** finds top-K similar entities
   - Cosine similarity between query and entity embeddings

4. **Context retrieval** loads entities and relationships
   - Entity descriptions, properties, aliases
   - Relationships to other entities (1-hop traversal)

5. **LLM generates response** using Claude 3.5 Sonnet
   - Prompt includes retrieved context
   - System instructions enforce citation and accuracy

6. **Sources formatted** for display
   - Entity names, types, descriptions
   - Source URLs from properties

## 🔒 Security Notes

- The `.env` file contains your API key - **never commit it**
- Add `.env` to `.gitignore` (already done)
- Use environment variables in production

## 🐛 Troubleshooting

### "Cannot connect to backend API"
- Ensure FastAPI is running on port 8000
- Check terminal for error messages

### "Services not initialized"
- Verify paths in `.env` are correct
- Check that graph.json and embeddings.json exist

### "Missing required environment variables"
- Ensure ANTHROPIC_API_KEY is set in `.env`
- Check all path variables are set

### Slow responses
- First query loads the sentence-transformer model (~420MB)
- Subsequent queries are faster
- Consider increasing `min_similarity` to reduce context size

### Low-quality answers
- Try increasing `top_k` for more context
- Try lowering `min_similarity` for broader matching
- Check if query is related to available entities

## 📈 Future Enhancements

Potential improvements:

- [ ] Add conversation history (multi-turn chat)
- [ ] Implement caching for repeated queries
- [ ] Add export functionality (PDF, Markdown)
- [ ] Integrate feedback mechanism (thumbs up/down)
- [ ] Add entity type filtering in UI
- [ ] Support for multiple knowledge domains
- [ ] Advanced citation formatting with hover previews

## 📝 License

Internal use - Market Research Knowledge Graph

## 🙋 Support

For issues or questions, check the logs:
- Backend logs: Terminal running uvicorn
- UI logs: Terminal running gradio

---

**Built with boring, reliable technology that actually works.** 🏗️
