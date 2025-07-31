import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP("Echo Server")

@mcp.tool()
def echo(message: str) -> str:
    """Repeat the input message back to the caller."""
    return "from a v1 server: " + message

if __name__ == "__main__":
    mcp.run()
