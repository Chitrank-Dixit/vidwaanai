import asyncio
import sys
from contextlib import asynccontextmanager
from typing import Any, Dict, List, Optional

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class VidwaanMCPClient:
    """
    A client for the VidwaanAI MCP Server.
    Wraps the MCP ClientSession to provide easy access to tools.
    """

    def __init__(self, server_script_path: str = "src/mcp/server.py"):
        # We want to run as a module to ensure imports work correctly
        # Ignore the path argument for now or use it if it's a path, but default to module execution
        self.server_params = StdioServerParameters(
            command=sys.executable,
            args=["-m", "src.mcp.server"],
            env=None,  # Inherit env
        )
        self.session: Optional[ClientSession] = None
        self._exit_stack = None

    @asynccontextmanager
    async def connect(self) -> Any:
        """
        Connects to the MCP server via stdio.
        """
        async with stdio_client(self.server_params) as (read, write):
            async with ClientSession(read, write) as session:
                self.session = session
                await session.initialize()
                yield self

    async def list_tools(self) -> List[Any]:
        """
        Lists available tools.
        """
        if not self.session:
            raise RuntimeError("Client not connected")
        result = await self.session.list_tools()
        return list(result.tools)

    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> Any:
        """
        Calls a tool by name with arguments.
        """
        if not self.session:
            raise RuntimeError("Client not connected")
        result = await self.session.call_tool(name, arguments)
        return result


async def main() -> None:
    # Example usage
    client = VidwaanMCPClient()
    async with client.connect() as c:
        print("Connected to MCP Server")

        tools = await c.list_tools()
        print(f"Found {len(tools)} tools")

        # Test language detection
        print("\nTesting detect_language...")
        result = await c.call_tool("detect_language", {"query": "नमस्ते भारत"})
        print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
