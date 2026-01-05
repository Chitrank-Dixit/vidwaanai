from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from typing import Dict, Any
import uuid
import logging

from src.api.models import (
    QueryRequest,
    QueryResponse,
    ErrorResponse,
    SessionCreateRequest,
    SessionResponse,
)
from functools import lru_cache
from src.core.agent_service import AgentService

# Initialize Router
agent_router = APIRouter(prefix="/api/v1/agent", tags=["Agent"])

# Dependency to get AgentService (Singleton pattern typically better, but for now instantiation is okay or we cache it)
# Ideally we set this up in main.py lifespan or lru_cache


@lru_cache()
def get_agent_service() -> AgentService:
    return AgentService()


@agent_router.post(
    "/query",
    response_model=QueryResponse,
    summary="Query the agent",
    description="Submit a question and get an answer with sources and reasoning",
    responses={
        200: {"description": "Successful query"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"},
    },
)
async def query_agent(
    request: QueryRequest, service: AgentService = Depends(get_agent_service)
) -> QueryResponse:
    """
    Main endpoint: Backend sends question, Agent returns answer.
    """
    try:
        # Process the query through the RAG pipeline
        result = service.process_query(
            question=request.question, session_id=request.session_id
        )

        # Map dict result to Pydantic model
        return QueryResponse(
            answer=result["answer"],
            confidence=result["confidence"],
            sources=result["sources"],
            reasoning_trace=result["reasoning_trace"],
            session_id=result["session_id"],
            timestamp=datetime.utcfromtimestamp(result["timestamp"]),
            processing_time_ms=result["processing_time_ms"],
        )

    except Exception as e:
        # Log error in service
        import traceback

        error_trace = traceback.format_exc()
        logger = logging.getLogger(__name__)
        logger.error(f"Error processing query: {str(e)}")
        logger.error(f"Traceback:\n{error_trace}")

        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")


@agent_router.get(
    "/health",
    summary="Check agent health",
    description="Verify that all components are operational",
)
async def health_check(
    service: AgentService = Depends(get_agent_service),
) -> Dict[str, Any]:
    """
    Health check endpoint.
    """
    # Simple check for now. TODO: Check DB/LLM connection status dynamically
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow(),
        "components": {
            "api": "ready",
            "llm": "ready",  # Assume ready if service init worked
        },
    }


# Session Management (Stub implementation for Phase 1 MVP)
@agent_router.post(
    "/session/create",
    response_model=SessionResponse,
    summary="Create new conversation session",
)
async def create_session(request: SessionCreateRequest) -> SessionResponse:
    """Create a new session ID."""
    s_id = str(uuid.uuid4())
    return SessionResponse(
        session_id=s_id,
        title=request.title or "New Conversation",
        created_at=datetime.utcnow(),
    )
