# 🚀 Setup Guide

Complete setup instructions for the RAG Chatbot.

## Prerequisites

- **Python 3.9+** installed
- **Anthropic API key** (get one at https://console.anthropic.com/)
- Your ontology files in `../output/ontology/market research/`

## Step-by-Step Setup

### 1. Navigate to Project Directory

```bash
cd /Users/karthikmg/Documents/euromonitor-multi-agent-architecture/rag-chatbot
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

### 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install:
- FastAPI (backend framework)
- Anthropic SDK (Claude API)
- sentence-transformers (embeddings)
- Gradio (UI)
- Other dependencies

**Note:** First-time installation downloads the sentence-transformer model (~420MB). This is normal and only happens once.

### 5. Configure Environment Variables

```bash
cp .env.example .env
```

Then edit `.env` with your preferred editor:

```bash
# macOS
open .env

# Linux
nano .env

# Windows
notepad .env
```

Update the file:
```env
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
GRAPH_PATH=../output/ontology/market research/graph.json
EMBEDDINGS_PATH=../output/ontology/market research/embeddings/embeddings.json
SCHEMA_PATH=../output/ontology/market research/schema.json
```

### 6. Verify Data Files

Check that your ontology files exist:

```bash
ls -lh "../output/ontology/market research/"
```

You should see:
- `graph.json` (~120KB)
- `schema.json` (~36KB)
- `embeddings/embeddings.json` (~1.2MB)

### 7. Test Installation

Test that everything is installed correctly:

```bash
python -c "import fastapi, anthropic, sentence_transformers, gradio; print('✅ All packages installed')"
```

## Running the Chatbot

### Option 1: Using the Startup Script (Recommended)

```bash
./start.sh
```

This starts both backend and UI automatically.

### Option 2: Manual Start (Two Terminals)

**Terminal 1 - Backend:**
```bash
cd rag-chatbot
source venv/bin/activate
python -m uvicorn app.main:app --reload --port 8000
```

**Terminal 2 - UI:**
```bash
cd rag-chatbot
source venv/bin/activate
python ui/gradio_app.py
```

### 8. Access the Chatbot

Open your browser and go to:

**http://localhost:7860**

You should see the Gradio chat interface!

## Verification Checklist

- [ ] Virtual environment created and activated
- [ ] All dependencies installed
- [ ] `.env` file created with valid API key
- [ ] Data files exist and paths are correct
- [ ] Backend starts without errors
- [ ] UI starts without errors
- [ ] Can access http://localhost:7860
- [ ] Backend health check passes: http://localhost:8000/health

## Common Issues

### "ModuleNotFoundError"
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt` again

### "Missing required environment variables"
- Check `.env` file exists
- Verify ANTHROPIC_API_KEY is set
- Verify paths are correct (relative to rag-chatbot/)

### "Cannot connect to backend API"
- Ensure backend is running on port 8000
- Check terminal for error messages
- Try `curl http://localhost:8000/health`

### "File not found" for graph.json
- Check that paths in `.env` are correct
- Verify ontology files exist in output/ directory
- Use relative paths from rag-chatbot/ directory

### Port already in use
- Kill existing processes:
  ```bash
  lsof -ti:8000 | xargs kill -9  # Kill backend
  lsof -ti:7860 | xargs kill -9  # Kill UI
  ```

## Next Steps

Once running, try these example queries:

1. "What is driving growth in the Asia Pacific toys market?"
2. "Tell me about the kidults consumer segment"
3. "What trends are affecting traditional toys and games?"
4. "How is China's toys and games market performing?"

See the main README.md for more details!
