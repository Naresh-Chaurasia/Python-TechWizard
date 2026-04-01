# Basic MCP Server Template

A minimal MCP server implementation that you can use as a starting point.

## Features

- Tool registration and handling
- Resource management
- Error handling
- Logging support

## Setup

```bash
# Copy this template
cp -r templates/basic-mcp-server my-server
cd my-server

# Install dependencies
pip install -r requirements.txt

# Run the server
python server.py
```

## Configuration

Edit `config.json` to customize your server:
```json
{
  "name": "my-server",
  "version": "1.0.0",
  "description": "My custom MCP server"
}
```

## Adding Tools

1. Define your tool in `tools.py`
2. Register it in `server.py`
3. Test with the client

Example tool:
```python
from mcp import types

async def my_tool(arguments: dict) -> types.CallToolResult:
    # Your tool logic here
    return types.CallToolResult(
        content=[types.TextContent(type="text", text="Success!")]
    )
```