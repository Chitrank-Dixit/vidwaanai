from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Optional, List, Dict, Any
from pydantic import BaseModel

from src.graph.graph_manager import GraphManager
from src.graph.reasoning_service import GraphReasoningService

router = APIRouter(prefix="/api/kg", tags=["Knowledge Graph"])

# Dependency Injection
def get_graph_manager():
    gm = GraphManager()
    try:
        yield gm
    finally:
        gm.close()

def get_reasoning_service(gm: GraphManager = Depends(get_graph_manager)):
    return GraphReasoningService(gm)

# Types
class ReasonRequest(BaseModel):
    entity_id: str
    hops: int = 2

# Routes
@router.get("/entity/{entity_id}")
async def get_entity(
    entity_id: str, 
    depth: int = 1, 
    service: GraphReasoningService = Depends(get_reasoning_service)
):
    """Get entity details and neighborhood."""
    result = service.get_entity_details(entity_id, depth)
    if not result:
        raise HTTPException(status_code=404, detail="Entity not found")
    return result

@router.get("/search/entities")
async def search_entities(
    q: str, 
    limit: int = 10,
    service: GraphReasoningService = Depends(get_reasoning_service)
):
    """Search entities by name."""
    if not q:
        raise HTTPException(status_code=400, detail="Query string 'q' is required")
    return service.search_entities(q, limit)

@router.get("/path/{start_id}/{end_id}")
async def find_path(
    start_id: str, 
    end_id: str, 
    max_depth: int = 5,
    service: GraphReasoningService = Depends(get_reasoning_service)
):
    """Find shortest path between two entities."""
    return service.find_shortest_path(start_id, end_id, max_depth)

@router.post("/reason")
async def reason_about_entity(
    request: ReasonRequest,
    service: GraphReasoningService = Depends(get_reasoning_service)
):
    """Multi-hop reasoning about an entity."""
    return service.reason_about_entity(request.entity_id, request.hops)

@router.get("/hierarchy/{concept_id}")
async def get_hierarchy(
    concept_id: str,
    service: GraphReasoningService = Depends(get_reasoning_service)
):
    """Get concept hierarchy (parents/children)."""
    return service.get_hierarchy(concept_id)
