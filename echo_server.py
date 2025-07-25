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
# Build trigger: 1752855005
# Build trigger: 1752857662
# Build trigger: 1752858333
# Build trigger: 1752858893
# Build trigger: 1752867113
# Build trigger: 1752867578
# Build trigger: 1752867773
# Build trigger: 1752868329
# Build trigger: 1752868385
# Build trigger: 1752869271
# Build trigger: 1752869538
# Build trigger: 1752871002
# Build trigger: 1752872341
# Build trigger: 1753103932
# Build trigger: 1753107657
# Build trigger: 1753107865
# Build trigger: 1753114345
# Build trigger: 1753192682
# Build trigger: 1753192721
# Build trigger: 1753192817
# Build trigger: 1753192908
# Build trigger: 1753194158
# Build trigger: 1753194424
# Build trigger: 1753204906
# Build trigger: 1753205310
# Build trigger: 1753205415
