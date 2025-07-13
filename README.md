# Enterprise MCP Documentation Server

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![MCP](https://img.shields.io/badge/MCP-compatible-green.svg)
![Build](https://img.shields.io/github/actions/workflow/status/hasecon/enterprise-mcp-docs/ci.yml)

**Multi-tool documentation provider for Claude Code, Cursor, and other MCP clients**

[Installation](#installation) • [Configuration](#configuration) • [Usage](#usage) • [Contributing](#contributing)

</div>

## 🚀 Overview

Enterprise MCP Documentation Server is a powerful, self-hosted Model Context Protocol (MCP) server that provides up-to-date documentation for enterprise and development tools directly to AI coding assistants like Claude Code, Cursor, and Windsurf.

Unlike traditional approaches that rely on stale training data, this server fetches and processes live documentation from official sources, ensuring your AI assistant always has accurate, current information.

### Why This Project?

🔍 **No More Hallucinations**: Stop getting outdated API examples  
🏢 **Enterprise Ready**: Supports internal tools like Proxmox, Nessus, TopDesk  
🔒 **Privacy First**: Self-hosted, no data leaves your infrastructure  
⚡ **Smart Caching**: Redis-backed performance optimization  
🧩 **Modular Design**: Easy to extend with new tools  
🎯 **Context7 Compatible**: Integrates with existing solutions  

## 🛠️ Supported Tools

| Category | Tools | Status |
|----------|-------|---------|
| **Search & Analytics** | Elasticsearch | ✅ Complete |
| **Containerization** | Docker, Docker Compose | ✅ Complete |
| **Programming** | Python 3.x Documentation | ✅ Complete |
| **Automation** | n8n Workflows | ✅ Complete |
| **AI/ML** | Ollama | ✅ Complete |
| **Virtualization** | Proxmox VE | ✅ Complete |
| **Security** | Nessus Professional | ✅ Complete |
| **Service Management** | TopDesk | ✅ Complete |
| **Collaboration** | Confluence | ✅ Complete |
| **Version Control** | Git, GitHub | 🚧 Planned |
| **Infrastructure** | Terraform, Ansible | 🚧 Planned |

## 📋 Requirements

- Python 3.9+
- Redis (for caching)
- 4GB+ RAM (for embeddings)
- Internet access (for documentation crawling)

## 🔧 Installation

### Option 1: pip install (Recommended)

```bash
pip install enterprise-mcp-docs
```

### Option 2: Docker

```bash
# Using docker-compose (includes Redis)
git clone https://github.com/hasecon/enterprise-mcp-docs.git
cd enterprise-mcp-docs
docker-compose up -d
```

### Option 3: From Source

```bash
git clone https://github.com/hasecon/enterprise-mcp-docs.git
cd enterprise-mcp-docs
pip install -e .
```

## ⚙️ Configuration

### 1. Basic Setup

```bash
# Copy configuration template
cp config/default.json config/local.json

# Set environment variables
cp .env.example .env
```

### 2. Configure Tools

Edit `config/local.json`:

```json
{
  "tools": {
    "elasticsearch": {
      "provider": "Elasticsearch",
      "base_url": "https://www.elastic.co/guide/en/elasticsearch/reference/current/",
      "sections": ["getting-started", "search", "mapping", "query-dsl"],
      "cache_ttl": 3600,
      "enabled": true
    },
    "docker": {
      "provider": "Docker", 
      "base_url": "https://docs.docker.com/",
      "sections": ["get-started", "build", "compose"],
      "cache_ttl": 7200,
      "enabled": true
    }
  },
  "vector_db": {
    "enabled": true,
    "embedding_model": "all-MiniLM-L6-v2"
  },
  "cache": {
    "redis_url": "redis://localhost:6379",
    "ttl": 3600
  }
}
```

### 3. Initialize Documentation

```bash
# Crawl all enabled tools
enterprise-mcp-docs crawl --all

# Or crawl specific tools
enterprise-mcp-docs crawl --tool elasticsearch
enterprise-mcp-docs crawl --tool docker
```

## 🚦 Usage

### Start the MCP Server

```bash
# Start server
enterprise-mcp-docs serve

# Or with custom config
enterprise-mcp-docs serve --config config/production.json
```

### Claude Code Integration

Add to your Claude Code configuration:

```json
{
  "mcpServers": {
    "enterprise-docs": {
      "command": "python",
      "args": ["-m", "enterprise_mcp_docs.server"],
      "env": {}
    }
  }
}
```

### Cursor Integration

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "enterprise-docs": {
      "command": "enterprise-mcp-docs",
      "args": ["serve"]
    }
  }
}
```

### Example Queries

Once configured, you can ask Claude Code:

```
How do I create an Elasticsearch mapping for user data?
Show me Docker Compose syntax for a web application with Redis.
What are the best practices for n8n workflow error handling?
How do I configure Proxmox clustering with shared storage?
```

## 🔌 Adding New Providers

1. **Create Provider Class**

```python
# src/enterprise_mcp_docs/providers/mytool.py
from .base import BaseProvider

class MyToolProvider(BaseProvider):
    async def crawl_docs(self):
        # Implement crawling logic
        docs = []
        # ... fetch and process docs
        await self.add_to_vector_db(docs)
        return docs
```

2. **Add Configuration**

```json
{
  "tools": {
    "mytool": {
      "provider": "MyTool",
      "base_url": "https://mytool.com/docs/",
      "sections": ["api", "guides"],
      "cache_ttl": 3600,
      "enabled": true
    }
  }
}
```

3. **Test and Submit PR!**

## 🧪 Development

### Setup Development Environment

```bash
git clone https://github.com/hasecon/enterprise-mcp-docs.git
cd enterprise-mcp-docs

# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=enterprise_mcp_docs

# Run specific test types
pytest -m unit
pytest -m integration
```

### Code Quality

```bash
# Format code
black src/ tests/
isort src/ tests/

# Type checking
mypy src/

# Linting
flake8 src/ tests/
```

## 🐳 Docker Deployment

### Development

```bash
docker-compose -f docker-compose.dev.yml up
```

### Production

```bash
docker-compose -f docker-compose.prod.yml up -d
```

## 📊 Monitoring

The server exposes metrics on `/metrics` endpoint:

- Documentation fetch success/failure rates
- Cache hit ratios
- Search query performance
- Vector similarity scores

## 🤝 Contributing

We love contributions! Here's how to help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Contributors

- [Hasecon](https://github.com/hasecon) - Initial work

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Context7](https://context7.com/) for inspiration on documentation processing
- [MCP Team](https://github.com/modelcontextprotocol) for the protocol
- [Upstash](https://upstash.com/) for Redis expertise
- All contributors and community members

## 📞 Support

- 📖 [Documentation](https://hasecon.github.io/enterprise-mcp-docs)
- 🐛 [Issues](https://github.com/hasecon/enterprise-mcp-docs/issues)
- 💬 [Discussions](https://github.com/hasecon/enterprise-mcp-docs/discussions)
- 📧 [Email](mailto:contact@hasecon.nl)

---

<div align="center">

**[⭐ Star this project](https://github.com/hasecon/enterprise-mcp-docs) if you find it useful!**

Made with ❤️ for the developer community

</div>