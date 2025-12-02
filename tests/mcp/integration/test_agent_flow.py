import pytest
import asyncio
import json
from src.mcp.client import VidwaanMCPClient

@pytest.mark.asyncio
async def test_tool_discovery():
    """
    Test that the client can connect and list tools.
    """
    client = VidwaanMCPClient()
    async with client.connect() as c:
        tools = await c.list_tools()
        assert len(tools) > 0
        tool_names = [t.name for t in tools]
        assert "detect_language" in tool_names
        assert "search_documents" in tool_names
        assert "execute_rag_pipeline" in tool_names

@pytest.mark.asyncio
async def test_simple_workflow():
    """
    Test a simple workflow: Detect Language -> Search
    """
    client = VidwaanMCPClient()
    async with client.connect() as c:
        # Step 1: Detect Language
        query = "नमस्ते"
        lang_result = await c.call_tool("detect_language", {"query": query})
        # MCP returns a CallToolResult, content is a list of TextContent or ImageContent
        # We need to parse the JSON from the text content if it's a string, 
        # but our tools return dicts which FastMCP handles.
        # FastMCP usually serializes the return value to JSON string in TextContent.
        
        # Let's inspect the structure in a real run, but for now assume standard MCP behavior
        # content[0].text should contain the JSON string of the result
        
        # Wait, FastMCP might return the dict directly if using python SDK client?
        # The SDK ClientSession.call_tool returns CallToolResult.
        # content is list[TextContent | ImageContent | EmbeddedResource]
        
        assert lang_result.content
        import json
        # The tool returns a dict, so it should be in text content as JSON
        lang_data = json.loads(lang_result.content[0].text)
        assert lang_data["language_code"] == "hi"
        
        # Step 2: Search
        search_result = await c.call_tool("search_documents", {
            "embedding": [0.1]*768, 
            "language": lang_data["language_code"]
        })
        search_data = json.loads(search_result.content[0].text)
        assert len(search_data) > 0

@pytest.mark.asyncio
async def test_rag_pipeline_workflow():
    """
    Test the full RAG pipeline tool.
    """
    client = VidwaanMCPClient()
    async with client.connect() as c:
        result = await c.call_tool("execute_rag_pipeline", {
            "query": "Who is Arjuna?",
            "config": {"strategy": "standard"}
        })
        data = json.loads(result.content[0].text)
        assert data["answer"] is not None
        assert "steps_executed" in data

if __name__ == "__main__":
    # Allow running this file directly
    asyncio.run(test_tool_discovery())
