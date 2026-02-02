"""
Pydantic models for API requests and responses
"""
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any


class ChatRequest(BaseModel):
    """Request model for chat endpoint."""
    query: str = Field(..., description="User's natural language question", min_length=1)
    top_k: int = Field(default=7, description="Total number of results to retrieve (entities + chunks)", ge=1, le=20)
    entity_weight: float = Field(default=1.0, description="Weight for entity results (0.5-2.0)", ge=0.1, le=2.0)
    chunk_weight: float = Field(default=1.0, description="Weight for chunk results (0.5-2.0)", ge=0.1, le=2.0)
    include_relationships: bool = Field(default=True, description="Include entity relationships in context")
    min_similarity: float = Field(default=0.05, description="Minimum similarity threshold", ge=0.0, le=1.0)
    debug: bool = Field(default=False, description="Include debug information in response")


class SourceInfo(BaseModel):
    """Information about a source (entity or document chunk)."""
    type: str  # 'entity' or 'chunk'

    # Entity fields
    entity_id: Optional[str] = None
    label: Optional[str] = None
    entity_type: Optional[str] = None
    description: Optional[str] = None
    source_urls: Optional[str] = None

    # Chunk fields
    chunk_id: Optional[str] = None
    source_file: Optional[str] = None
    chunk_index: Optional[int] = None
    text_preview: Optional[str] = None
    mentioned_entities: Optional[List[str]] = None

    class Config:
        # Exclude None values from JSON output for cleaner display
        json_encoders = {type(None): lambda v: None}

    def dict(self, **kwargs):
        """Override dict to exclude None values."""
        kwargs.setdefault('exclude_none', True)
        return super().dict(**kwargs)


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
