# ⚡ Quick Start

Get the RAG Chatbot running in 5 minutes.

## 1. Setup (First Time Only)

```bash
cd rag-chatbot

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create config file
cp .env.example .env

# Edit .env and add your Anthropic API key
# Change: ANTHROPIC_API_KEY=your_anthropic_api_key_here
# To:     ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
```

## 2. Verify Setup

```bash
python test_setup.py
```

Should see all ✅ checks pass.

## 3. Start the Chatbot

```bash
./start.sh
```

Or manually (two terminals):

**Terminal 1:**
```bash
source venv/bin/activate
python -m uvicorn app.main:app --port 8000
```

**Terminal 2:**
```bash
source venv/bin/activate
python ui/gradio_app.py
```

## 4. Open Browser

Navigate to: **http://localhost:7860**

## 5. Ask Questions!

Try:
- "What is driving growth in Asia Pacific toys market?"
- "Tell me about kidults"
- "How is China performing?"

---

## Daily Usage

After first-time setup, just run:

```bash
cd rag-chatbot
./start.sh
```

Stop with `Ctrl+C`

---

## Troubleshooting One-Liners

```bash
# Check backend is running
curl http://localhost:8000/health

# Kill stuck processes
lsof -ti:8000 | xargs kill -9  # Backend
lsof -ti:7860 | xargs kill -9  # UI

# Reinstall dependencies
pip install --force-reinstall -r requirements.txt

# Check Python version (need 3.9+)
python3 --version

# Verify API key is set
grep ANTHROPIC_API_KEY .env

# Check data files exist
ls -lh "../output/ontology/market research/"
```

---

## File Locations

- **Backend:** `app/main.py`
- **UI:** `ui/gradio_app.py`
- **Config:** `.env`
- **Data:** `../output/ontology/market research/`

---

**Need more help?** See README.md or SETUP.md
