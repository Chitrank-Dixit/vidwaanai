from typing import Any, cast

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

from src.agent.vidwaan_agent import VidwaanAI
from src.core.config import settings
from src.graph.routes import router as graph_router

app = FastAPI(title="VidwaanAI API", description="API for VidwaanAI Agent")

app.include_router(graph_router)


# Dependency to get agent
def get_agent() -> VidwaanAI:
    # In a real app, we might want to reuse the agent instance or use a dependency injection framework
    # For now, we'll create a new one or use a singleton pattern if needed.
    # Since VidwaanAI init might be heavy (DB pool), singleton is better.
    if not hasattr(app.state, "agent"):
        app.state.agent = VidwaanAI(
            db_url=settings.DATABASE_URL,
            openai_key=settings.OPENAI_API_KEY or "",
            lmstudio_url=settings.lmstudio_base_url,
            enable_graph_rag=settings.ENABLE_GRAPH_RAG,
            neo4j_uri=settings.NEO4J_URI,
            neo4j_user=settings.NEO4J_USER,
            neo4j_password=settings.NEO4J_PASSWORD,
        )
    return cast(VidwaanAI, app.state.agent)


class QueryRequest(BaseModel):
    text: str
    language: str | None = "en"
    scripture_filter: str | None = None


class QueryResponse(BaseModel):
    answer: str
    retrieved_verses: list[dict[str, Any]]
    language: str
    confidence: dict[str, Any]
    timestamp: str


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest, agent: VidwaanAI = Depends(get_agent)) -> Any:
    try:
        response = agent.query(
            question=request.text,
            language=request.language or "en",
            scripture_filter=request.scripture_filter,
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
