import pytest
from fastmcp import Client

from echo_server import mcp


@pytest.fixture
def echo_server():
    """Fixture providing the echo server instance."""
    return mcp


async def test_echo_returns_input_message(echo_server):
    """Test that echo tool returns the exact input message."""
    async with Client(echo_server) as client:
        result = await client.call_tool("echo", {"message": "Hello, World!"})
        assert result.data == "Hello, World!"


async def test_echo_empty_string(echo_server):
    """Test that echo handles empty strings correctly."""
    async with Client(echo_server) as client:
        result = await client.call_tool("echo", {"message": ""})
        assert result.data == ""


async def test_echo_special_characters(echo_server):
    """Test that echo preserves special characters."""
    async with Client(echo_server) as client:
        special_message = "Hello 👋 \n\t{\"test\": true}"
        result = await client.call_tool("echo", {"message": special_message})
        assert result.data == special_message


async def test_echo_long_message(echo_server):
    """Test that echo handles long messages."""
    async with Client(echo_server) as client:
        long_message = "A" * 1_000
        result = await client.call_tool("echo", {"message": long_message})
        assert result.data == long_message


async def test_server_has_echo_tool(echo_server):
    """Test that the server exposes the echo tool."""
    async with Client(echo_server) as client:
        tools = await client.list_tools()
        tool_names = [tool.name for tool in tools]
        assert "echo" in tool_names
        
        echo_tool = next(tool for tool in tools if tool.name == "echo")
        assert echo_tool.description == "Repeat the input message back to the caller."