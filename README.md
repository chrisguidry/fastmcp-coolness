# FastMCP Echo Server

A minimal FastMCP server that echoes messages back to the caller.

## Setup

```bash
uv sync
```

## Run

```bash
uv run python echo_server.py
```

The server provides a single tool called `echo` that takes a message and returns the same message.