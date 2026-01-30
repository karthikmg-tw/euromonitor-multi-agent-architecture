"""
Pydantic models for API requests and responses
"""
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any


class ChatRequest(BaseModel):
    """Request model for chat endpoint."""
    query: str = Field(..., description="User's natural language question", min_length=1)
    top_k: int = Field(default=5, description="Number of similar entities to retrieve", ge=1, le=20)
    include_relationships: bool = Field(default=True, description="Include entity relationships in context")
    min_similarity: float = Field(default=0.3, description="Minimum similarity threshold", ge=0.0, le=1.0)
    debug: bool = Field(default=False, description="Include debug information in response")


class SourceInfo(BaseModel):
    """Information about a source entity."""
    entity_id: str
    label: str
    type: str
    description: str
    source_urls: str


class ChatResponse(BaseModel):
    """Response model for chat endpoint."""
    answer: str = Field(..., description="Generated answer to the question")
    sources: List[SourceInfo] = Field(..., description="Source entities used in the answer")
    debug: Optional[Dict[str, Any]] = Field(None, description="Debug information (if requested)")


class EntityRequest(BaseModel):
    """Request model for entity lookup."""
    entity_id: str = Field(..., description="Entity ID to look up")


class EntityResponse(BaseModel):
    """Response model for entity lookup."""
    entity: Dict[str, Any]
    relationships: List[Dict[str, Any]]
    related_entities: List[Dict[str, Any]]


class HealthResponse(BaseModel):
    """Response model for health check."""
    status: str
    version: str
    services: Dict[str, str]
