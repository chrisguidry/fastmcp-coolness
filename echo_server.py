import logging
from fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP("Echo Server")

@mcp.tool
def echo(message: str) -> str:
    """Repeat the input message back to the caller."""
    logger.info(f"Echo server received: {message}")
    return message

if __name__ == "__main__":
    mcp.run()# Build trigger: 1752592586
# Build trigger: 1752592707
# Build trigger: 1752593811
# Build trigger: 1752594205
# Build trigger: 1752594675
# Build trigger: 1752596365
# Build trigger: 1752596912
# Build trigger: 1752597551
# Build trigger: 1752597732
# Build trigger: 1752598183
# Build trigger: 1752766064
# Build trigger: 1752767293
# Build trigger: 1752767418
# Build trigger: 1752768461
# Build trigger: 1752768708
# Build trigger: 1752769369
# Build trigger: 1752788949
# Build trigger: 1752789087
# Build trigger: 1752789325
# Build trigger: 1752847156
# Build trigger: 1752847545
# Build trigger: 1752847832
# Build trigger: 1752847897
# Build trigger: 1752849869
# Build trigger: 1752849930
# Build trigger: 1752849940
# Build trigger: 1752850047
# Build trigger: 1752850574
# Build trigger: 1752850707
# Build trigger: 1752850904
