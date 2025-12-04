import logging

from mcp.server.fastmcp import FastMCP

from src.mcp.tools.generation_tools import (
    generate_answer,
    summarize_results,
    translate_answer,
)
from src.mcp.tools.kg_tools import (
    find_related_documents,
    get_entity_context,
    query_knowledge_graph,
)
from src.mcp.tools.language_tools import (
    detect_language,
    get_supported_languages,
    preprocess_text,
)
from src.mcp.tools.pipeline_tools import (
    execute_rag_pipeline,
    get_pipeline_strategies,
    validate_pipeline_config,
)
from src.mcp.tools.reranking_tools import (
    calculate_relevance_score,
    get_reranking_models,
    rerank_results,
)
from src.mcp.tools.search_tools import (
    generate_embeddings,
    get_search_strategies,
    hybrid_search,
    search_documents,
)

# Initialize FastMCP server
mcp = FastMCP("VidwaanAI MCP Server")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp_server")

# Import tools to register them
# Note: We'll import these after defining the server to avoid circular imports if they need the mcp instance,
# but typically tools are defined as functions decorated with @mcp.tool()

# Register tools
mcp.add_tool(detect_language)
mcp.add_tool(preprocess_text)
mcp.add_tool(get_supported_languages)

mcp.add_tool(generate_embeddings)
mcp.add_tool(search_documents)
mcp.add_tool(hybrid_search)
mcp.add_tool(get_search_strategies)

mcp.add_tool(rerank_results)
mcp.add_tool(calculate_relevance_score)
mcp.add_tool(get_reranking_models)

mcp.add_tool(query_knowledge_graph)
mcp.add_tool(find_related_documents)
mcp.add_tool(get_entity_context)

mcp.add_tool(generate_answer)
mcp.add_tool(summarize_results)
mcp.add_tool(translate_answer)

mcp.add_tool(execute_rag_pipeline)
mcp.add_tool(get_pipeline_strategies)
mcp.add_tool(validate_pipeline_config)

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
