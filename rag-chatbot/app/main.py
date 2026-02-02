"""
FastAPI application for RAG Chatbot
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
import os
from dotenv import load_dotenv

from app.services.graph_service_v2 import GraphServiceV2
from app.services.vector_search import VectorSearchService
from app.services.embedding_service import EmbeddingService
from app.services.llm_service import LLMService
from app.services.rag_service_v2 import RAGServiceV2
from app.models.schemas import (
    ChatRequest,
    ChatResponse,
    SourceInfo,
    EntityRequest,
    EntityResponse,
    HealthResponse
)

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="RAG Chatbot API",
    description="Market Research RAG Chatbot using Knowledge Graph and Vector Embeddings",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global services (initialized on startup)
rag_service: RAGServiceV2 = None


@app.on_event("startup")
async def startup_event():
    """Initialize services on application startup."""
    global rag_service

    logger.info("Starting RAG Chatbot API...")

    # Get paths from environment
    graph_path = os.getenv("GRAPH_PATH")
    embeddings_path = os.getenv("EMBEDDINGS_PATH")
    schema_path = os.getenv("SCHEMA_PATH")
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

    # Validate paths
    if not all([graph_path, embeddings_path, schema_path, anthropic_api_key]):
        raise ValueError("Missing required environment variables. Check .env file.")

    # Initialize services (using V2 with chunk support)
    logger.info("Initializing Graph Service V2 (with chunks)...")
    graph_service = GraphServiceV2(graph_path, schema_path)

    logger.info("Initializing Vector Search Service...")
    vector_search = VectorSearchService(embeddings_path)

    logger.info("Initializing Embedding Service...")
    embedding_service = EmbeddingService()

    logger.info("Initializing LLM Service...")
    llm_service = LLMService(anthropic_api_key)

    logger.info("Initializing RAG Service V2 (dual-source)...")
    rag_service = RAGServiceV2(
        graph_service=graph_service,
        embedding_service=embedding_service,
        vector_search_service=vector_search,
        llm_service=llm_service
    )

    logger.info("✅ All services initialized successfully!")


@app.get("/", response_model=HealthResponse)
async def root():
    """Root endpoint - health check."""
    return {
        "status": "ok",
        "version": "1.0.0",
        "services": {
            "graph": "loaded",
            "vector_search": "loaded",
            "embeddings": "loaded",
            "llm": "ready"
        }
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return {
        "status": "ok",
        "version": "1.0.0",
        "services": {
            "graph": "loaded",
            "vector_search": "loaded",
            "embeddings": "loaded",
            "llm": "ready"
        }
    }


@app.post("/chat", response_model=ChatResponse, response_model_exclude_none=True)
async def chat(request: ChatRequest):
    """
    Main chat endpoint - answer questions using RAG pipeline.

    Args:
        request: ChatRequest with query and parameters

    Returns:
        ChatResponse with answer and sources
    """
    if rag_service is None:
        raise HTTPException(status_code=503, detail="Services not initialized")

    try:
        # Process query through RAG pipeline
        result = rag_service.query(
            user_query=request.query,
            top_k=request.top_k,
            entity_weight=request.entity_weight,
            chunk_weight=request.chunk_weight,
            include_relationships=request.include_relationships,
            min_similarity=request.min_similarity,
            debug=request.debug
        )

        # Format response
        sources = [SourceInfo(**source) for source in result['sources']]

        response = ChatResponse(
            answer=result['answer'],
            sources=sources,
            debug=result.get('debug') if request.debug else None
        )

        return response

    except Exception as e:
        logger.error(f"Error processing chat request: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")


@app.post("/entity", response_model=EntityResponse)
async def get_entity(request: EntityRequest):
    """
    Get detailed information about a specific entity.

    Args:
        request: EntityRequest with entity_id

    Returns:
        EntityResponse with entity details and relationships
    """
    if rag_service is None:
        raise HTTPException(status_code=503, detail="Services not initialized")

    try:
        result = rag_service.get_entity_info(request.entity_id)

        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])

        return EntityResponse(**result)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting entity info: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
