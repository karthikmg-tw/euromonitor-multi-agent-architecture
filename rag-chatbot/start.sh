#!/bin/bash

# Startup script for RAG Chatbot
# This script starts both the FastAPI backend and Gradio UI

set -e  # Exit on error

echo "🚀 Starting RAG Chatbot..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run:"
    echo "   python3 -m venv venv"
    echo "   source venv/bin/activate"
    echo "   pip install -r requirements.txt"
    exit 1
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found. Please create it from .env.example:"
    echo "   cp .env.example .env"
    echo "   # Then edit .env and add your ANTHROPIC_API_KEY"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

echo "✅ Virtual environment activated"

# Check if API key is set
if ! grep -q "ANTHROPIC_API_KEY=sk-" .env; then
    echo "⚠️  Warning: ANTHROPIC_API_KEY may not be set properly in .env"
    echo "   Make sure it starts with 'sk-ant-'"
fi

# Start FastAPI backend in background
echo "🔧 Starting FastAPI backend on port 8000..."
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

# Wait for backend to start
echo "⏳ Waiting for backend to initialize..."
sleep 5

# Check if backend is running
if ! curl -s http://localhost:8000/health > /dev/null; then
    echo "❌ Backend failed to start. Check logs above."
    kill $BACKEND_PID 2>/dev/null || true
    exit 1
fi

echo "✅ Backend is running (PID: $BACKEND_PID)"

# Start Gradio UI
echo "🎨 Starting Gradio UI on port 7860..."
python ui/gradio_app.py &
UI_PID=$!

echo ""
echo "✨ RAG Chatbot is running!"
echo ""
echo "   Backend API:  http://localhost:8000"
echo "   Gradio UI:    http://localhost:7860"
echo ""
echo "Press Ctrl+C to stop both services..."
echo ""

# Wait for interrupt
trap "echo ''; echo '🛑 Stopping services...'; kill $BACKEND_PID $UI_PID 2>/dev/null; exit 0" INT

# Keep script running
wait
