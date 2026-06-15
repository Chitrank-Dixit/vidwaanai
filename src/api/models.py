from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

# --- Request Models ---


class QueryRequest(BaseModel):
    """Request to query the agent."""

    question: str = Field(
        ...,
        min_length=3,
        max_length=5000,
        description="The user's question about Vedic scriptures.",
    )
    session_id: str | None = Field(
        None, description="Session ID for conversation history context."
    )
    context: dict[str, Any] | None = Field(
        None, description="Optional extra context or filters."
    )
    temperature: float | None = Field(
        0.7, ge=0.0, le=1.0, description="LLM sampling temperature."
    )
    max_tokens: int | None = Field(
        1000, ge=50, le=4096, description="Max tokens for the answer."
    )


class SessionCreateRequest(BaseModel):
    """Request to create a new multi-turn session."""

    title: str | None = Field(None, description="Optional title for the conversation.")
    metadata: dict[str, Any] | None = Field(
        None, description="Optional metadata for the session."
    )


# --- Response Models ---


class Source(BaseModel):
    """Source document (Verse/Sutra) used for the answer."""

    id: str
    title: str
    content: str
    confidence: float
    entity_type: str | None = None
    metadata: dict[str, Any] | None = None


class ReasoningStep(BaseModel):
    """A single step in the agent's chain of thought."""

    step: int
    action: str  # e.g., "vector_search", "graph_query", "llm_call"
    input: str
    output: str
    duration_ms: float


class QueryResponse(BaseModel):
    """The complete response from the agent."""

    answer: str
    confidence: float
    sources: list[Source]
    reasoning_trace: list[ReasoningStep]
    session_id: str
    timestamp: datetime
    processing_time_ms: float


class SessionResponse(BaseModel):
    """Session details."""

    session_id: str
    title: str
    created_at: datetime


class ErrorResponse(BaseModel):
    """Standard error response."""

    error_code: str
    error_message: str
    details: dict[str, Any] | None = None
    timestamp: datetime
