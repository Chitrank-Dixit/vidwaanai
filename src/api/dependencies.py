from functools import lru_cache
from src.core.agent_service import AgentService


@lru_cache()
def get_agent_service() -> AgentService:
    return AgentService()
