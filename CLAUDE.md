# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository contains multiple FastMCP example servers for testing purposes. Each example demonstrates different FastMCP capabilities and patterns.

## Development Setup

This project uses `uv` for Python package management. All commands should be run with `uv run` prefix.

### Common Commands

```bash
# Install dependencies
uv sync

# Install dev dependencies (includes testing tools)
uv sync --group dev

# Run a specific example server
uv run python echo_server.py

# Run tests
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Run a specific test file
uv run pytest test_echo_server.py

# Add a new dependency
uv add <package-name>

# Update dependencies
uv sync --upgrade
```

## Project Structure

Each FastMCP example should be a standalone Python file in the root directory following the pattern `<example_name>_server.py`. Examples should be minimal and focused on demonstrating specific FastMCP features.

## Creating New Examples

When adding new FastMCP examples:
1. Create a new file named `<feature>_server.py` in the root directory
2. Import FastMCP and create a server instance with a descriptive name
3. Implement tools using the `@mcp.tool` decorator
4. Include type hints for all function parameters and return values
5. Add a brief docstring to each tool function
6. Use `if __name__ == "__main__": mcp.run()` pattern for direct execution

## FastMCP Patterns

- Server creation: `mcp = FastMCP("Server Name")`
- Tool definition: Use `@mcp.tool` decorator on functions
- Type hints are required for tool parameters
- Tools should have clear, descriptive docstrings
- Default transport is STDIO when using `mcp.run()`

## Python Version

This project requires Python 3.12 or higher. The `.python-version` file specifies the exact version for consistency.

## Testing

Tests follow FastMCP's in-memory testing pattern:
- Test files should be named `test_<example_name>.py`
- Import the server instance directly from the example module
- Use `from fastmcp import Client` for testing
- Tests use pytest with asyncio support (configured in pyproject.toml)