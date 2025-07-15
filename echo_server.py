from fastmcp import FastMCP

mcp = FastMCP("Echo Server")

@mcp.tool
def echo(message: str) -> str:
    """Repeat the input message back to the caller."""
    return message

if __name__ == "__main__":
    mcp.run()# Build trigger: 1752592586
# Build trigger: 1752592707
# Build trigger: 1752593811
