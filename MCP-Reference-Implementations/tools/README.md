# MCP Development Tools

Collection of utilities and tools for MCP development and testing.

## Available Tools

### 1. MCP Test Client
A simple client for testing MCP servers without Claude Desktop.

```bash
python tools/test_client.py --server path/to/server.py
```

### 2. MCP Server Generator
Generate boilerplate code for new MCP servers.

```bash
python tools/generate_server.py --name my-server --template basic
```

### 3. MCP Protocol Inspector
Inspect and debug MCP protocol messages.

```bash
python tools/protocol_inspector.py --port 3000
```

### 4. MCP Configuration Validator
Validate Claude Desktop configuration files.

```bash
python tools/validate_config.py --config ~/.config/claude/claude_desktop_config.json
```

## Usage

Each tool includes help documentation:
```bash
python tools/<tool_name>.py --help
```

## Contributing

Add new tools to this directory and update this README with:
- Tool description
- Usage examples
- Dependencies