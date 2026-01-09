# Agent Integration Guide

This guide explains how to connect AI agents (like Claude) to the VidwaanAI MCP Server.

## Prerequisites
- VidwaanAI MCP Server running (default port 3000 or via stdio)
- MCP Client (e.g., Claude Desktop, or custom client)

## Connecting with Claude Desktop

1. **Configure Claude Desktop**:
   Edit your `claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "vidwaan-ai": {
         "command": "docker",
         "args": [
           "run",
           "-i",
           "--rm",
           "mcp-server"
         ]
       }
     }
   }
   ```
   *Note: This assumes you have built the `mcp-server` image.*

2. **Restart Claude Desktop**.

3. **Verify Connection**:
   Look for the connection indicator in Claude Desktop.

## Using Tools

Once connected, you can ask Claude to perform tasks like:
- "Search for documents about Mahabharata in Hindi"
- "Who is Arjuna? Check the knowledge graph."
- "Summarize these search results."

Claude will automatically discover the available tools and use them to answer your request.

## Best Practices for Agents

- **Always detect language first**: Use `detect_language` to understand the user's intent.
- **Cite sources**: When generating answers, refer to the documents returned by search.
- **Use Hybrid Search**: For complex queries, hybrid search often yields better results.
