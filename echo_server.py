from fastmcp import FastMCP

mcp = FastMCP("Echo Server")

@mcp.tool
def echo(message: str) -> str:
    """Repeat the input message back to the caller."""
    return message

if __name__ == "__main__":
    mcp.run()