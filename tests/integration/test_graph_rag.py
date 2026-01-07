
import pytest
from unittest.mock import MagicMock, patch
from src.core.agent_service import AgentService

@pytest.fixture
def mock_agent_deps():
    with patch("src.core.agent_service.DatabaseManager") as mock_db, \
         patch("src.core.agent_service.VedaEmbedder") as mock_embedder, \
         patch("src.core.agent_service.LMStudioClient") as mock_llm, \
         patch("src.core.agent_service.GraphBuilder") as mock_gb, \
         patch("src.core.agent_service.GraphRetriever") as mock_gr, \
         patch("src.core.agent_service.EntityExtractor") as mock_ee, \
         patch("src.core.agent_service.HybridRetrieverService") as mock_hrs:
         
         # Mock return values
         mock_service = AgentService()
         
         # Setup Hybrid Retriever
         mock_service.retriever.search.return_value = [
             {"id": 1, "source": "RV", "title": "Mantra 1", "content": "Fire is hot", "similarity": 0.9}
         ]
         
         # Setup Entity Extractor
         mock_service.entity_extractor.extract_from_query.return_value = [
             {"name": "Agni", "type": "Deity"}
         ]
         
         # Setup Graph Retriever
         mock_service.graph_retriever.get_context_subgraph.return_value = [
             {"source": "Agni", "relation": "IS_A", "target": "Deity"}
         ]
         mock_service.graph_retriever.format_subgraph_context.return_value = "Agni --[IS_A]--> Deity"
         
         # Setup LLM
         mock_service.llm_client.generate.return_value = "Agni is the fire god."
         
         yield mock_service

def test_process_query_with_graph_context(mock_agent_deps):
    agent = mock_agent_deps
    
    response = agent.process_query("Who is Agni?", session_id="test")
    
    # Verify Hybrid Search called
    agent.retriever.search.assert_called_once()
    
    # Verify Entity Extraction called
    agent.entity_extractor.extract_from_query.assert_called_with("Who is Agni?")
    
    # Verify Graph Retrieval called with extracted entity
    agent.graph_retriever.get_context_subgraph.assert_called_with(["Agni"])
    
    # Verify Prompt construction (implicitly via checking if generate was called)
    # To be more precise, we can check the call args of generate
    call_args_list = agent.llm_client.generate.call_args[0]
    system_prompt_arg = call_args_list[0]
    context_arg = call_args_list[1]
    
    assert "You are Vidwaan" in system_prompt_arg
    assert "Agni --[IS_A]--> Deity" in context_arg
    
    # Verify Response structure
    assert response["answer"] == "Agni is the fire god."
    assert "graph_retrieval" in [trace["action"] for trace in response["reasoning_trace"]]

def test_process_query_no_entities(mock_agent_deps):
    agent = mock_agent_deps
    agent.entity_extractor.extract_from_query.return_value = []
    
    response = agent.process_query("Hello", session_id="test")
    
    # Graph Retrieval should NOT be called
    agent.graph_retriever.get_context_subgraph.assert_not_called()
    
    # Context should not have graph section
    call_args_list = agent.llm_client.generate.call_args[0]
    context_arg = call_args_list[1]
    assert "Knowledge Graph Context:" not in context_arg
