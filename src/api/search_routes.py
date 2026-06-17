from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel

from src.api.dependencies import get_agent_service
from src.core.agent_service import AgentService

search_router = APIRouter(prefix="/api/v1/search", tags=["Search"])


class SearchResult(BaseModel):
    id: str
    text: str
    translation: str | None = None
    source: str
    score: float
    retrieval_method: str | None = "hybrid"
    metadata: dict[str, Any] | None = None


class SearchResponse(BaseModel):
    results: list[SearchResult]
    count: int
    strategy: str


@search_router.get(
    "/hybrid",
    response_model=SearchResponse,
    summary="Hybrid Search (Vector + Keyword)",
    description="Search for mantras using Semantic + Keyword search with RRF or Weighted fusion.",
)
async def hybrid_search(
    q: str,
    limit: int = Query(10, ge=1, le=50),
    strategy: str = Query("hybrid", pattern="^(hybrid|vector|keyword)$"),
    fusion: str = Query("weighted", pattern="^(weighted|rrf)$"),
    service: AgentService = Depends(get_agent_service),
) -> SearchResponse:
    """
    Perform hybrid search using the Agent's retriever.
    """
    try:
        # Access the hybrid retriever directly from the agent service
        # This assumes AgentService exposes self.retriever.search or we access internal
        # We modified AgentService to have self.retriever

        results = service.retriever.search(
            query=q, top_k=limit, strategy=strategy, fusion_method=fusion
        )

        formatted_results = []
        for r in results:
            formatted_results.append(
                SearchResult(
                    id=str(r.get("id")),
                    text=r.get("text", ""),
                    translation=r.get("translation"),
                    source=r.get("source", "Unknown"),
                    score=r.get("score", 0.0),
                    retrieval_method=r.get("fusion_method", strategy),
                    metadata=r,
                )
            )

        return SearchResponse(
            results=formatted_results, count=len(formatted_results), strategy=strategy
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
