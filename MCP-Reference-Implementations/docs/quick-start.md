# Quick Start Guide

## Prerequisites

- Python 3.8+ or Node.js 16+
- Basic understanding of JSON-RPC
- API keys for AI services (if using AI-powered features)

## Installation

### Option 1: Clone and Run Examples
```bash
git clone <repository-url>
cd MCP-Showcase
cd examples/basic
python simple_server.py
```

### Option 2: Use Template
```bash
cp templates/basic-mcp-server my-mcp-server
cd my-mcp-server
npm install  # or pip install -r requirements.txt
```

## Your First MCP Server

### 1. Basic Python Server
```python
import asyncio
import sys
from mcp import types
from mcp.server import Server

app = Server("my-first-server")

@app.list_tools()
async def list_tools():
    return [
        types.Tool(
            name="echo",
            description="Echo back the input text",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "echo":
        return types.CallToolResult(
            content=[types.TextContent(type="text", text=arguments["text"])]
        )

async def main():
    async with app.run() as server:
        await server.communicate()

if __name__ == "__main__":
    asyncio.run(main())
```

### 2. Running the Server
```bash
python my_server.py
```

### 3. Testing with Claude Desktop
Add to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "my-first-server": {
      "command": "python",
      "args": ["path/to/my_server.py"]
    }
  }
}
```

## Next Steps

1. **Explore Examples**: Check out `examples/` for more complex implementations
2. **Read Architecture**: Understand the MCP protocol details
3. **Build Custom**: Create your own MCP server for specific needs
4. **Integrate**: Connect with existing tools and services

## Troubleshooting

### Common Issues

1. **Connection Failed**: Check if server is running and accessible
2. **Tool Not Found**: Verify tool registration and spelling
3. **Permission Denied**: Check file permissions and API keys

### Debug Tips

- Enable logging: `export MCP_LOG_LEVEL=debug`
- Use MCP CLI tools for testing
- Check JSON-RPC messages with Wireshark or similar

## Resources

- [MCP Specification](https://modelcontextprotocol.io/)
- [Community Discord](https://discord.gg/mcp)
- [GitHub Issues](https://github.com/modelcontextprotocol/issues)