import logging
import os
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    import measured
    logger.info(f"measured version: {measured.__version__}")
except ImportError:
    logger.info("Could not import measured")

mcp = FastMCP("Echo Server")

@mcp.tool
def echo(message: str) -> str:
    """Repeat the input message back to the caller."""
    headers = get_http_headers()
    hello_env = os.getenv("HELLO")
    goodbye_env = os.getenv("GOODBYE")
    logger.info(f"Echo server received: {message}")
    logger.info(f"Request headers: {dict(headers)}")
    logger.info(f"HELLO={hello_env}")
    logger.info(f"GOODBYE={goodbye_env}")
    return message

if __name__ == "__main__":
    mcp.run()
