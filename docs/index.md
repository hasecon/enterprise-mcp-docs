# Enterprise MCP Documentation Server

<div align="center">
  <img src="assets/logo.png" alt="Enterprise MCP Docs Logo" width="200">
  
  **Multi-tool documentation provider for Claude Code and other MCP clients**
  
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/hasecon/enterprise-mcp-docs/blob/main/LICENSE)
  [![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
  [![MCP](https://img.shields.io/badge/MCP-compatible-green.svg)](https://modelcontextprotocol.io/)
  [![Build](https://img.shields.io/github/actions/workflow/status/hasecon/enterprise-mcp-docs/ci.yml)](https://github.com/hasecon/enterprise-mcp-docs/actions)
  
</div>

## What is Enterprise MCP Documentation Server?

Enterprise MCP Documentation Server is a powerful, self-hosted [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that provides up-to-date documentation for enterprise and development tools directly to AI coding assistants like Claude Code, Cursor, and Windsurf.

Unlike traditional approaches that rely on stale training data, this server fetches and processes live documentation from official sources, ensuring your AI assistant always has accurate, current information.

## 🚀 Key Features

### 🔍 **Eliminate AI Hallucinations**
Stop getting outdated API examples and non-existent functions. Our server provides real, current documentation.

### 🏢 **Enterprise Tool Support**
Built specifically for enterprise environments with support for:
- **Infrastructure**: Proxmox, Docker, Kubernetes
- **Security**: Nessus, vulnerability management
- **Service Management**: TopDesk, incident management
- **Collaboration**: Confluence, team documentation
- **Development**: Python, Git, automation tools

### 🔒 **Privacy-First Architecture**
- **Self-hosted**: Keep sensitive documentation on your infrastructure
- **No external API calls** for your private/internal documentation
- **Air-gapped deployment** support for secure environments

### ⚡ **High Performance**
- **Redis caching** for lightning-fast responses
- **Vector similarity search** for relevant results
- **Smart preprocessing** eliminates noise and improves accuracy
- **Concurrent processing** for multiple documentation sources

### 🧩 **Modular & Extensible**
- **Plugin architecture** for easy provider additions
- **Community-driven** provider ecosystem
- **Custom tool support** for your internal documentation
- **Context7 integration** for popular programming libraries

## 🎯 Use Cases

### For Development Teams
```
"How do I configure Elasticsearch clustering with security?"
"Show me Docker Compose best practices for microservices"
"What are the latest Python async/await patterns?"
```

### For DevOps Engineers
```
"How do I set up Proxmox high availability?"
"What are the current Docker security recommendations?"
"Show me n8n workflow error handling examples"
```

### For Security Teams
```
"How do I configure Nessus scan policies for compliance?"
"What are the latest vulnerability assessment procedures?"
"Show me security hardening for Proxmox clusters"
```

### For Enterprise Users
```
"How do I create TopDesk automation workflows?"
"What are the Confluence API best practices?"
"Show me integration patterns for enterprise tools"
```

## 🛠️ Supported Tools

| Category | Tools | Status | Documentation |
|----------|-------|---------|---------------|
| **Search & Analytics** | Elasticsearch | ✅ Complete | [📖 Docs](tools/elasticsearch.md) |
| **Containerization** | Docker, Docker Compose | ✅ Complete | [📖 Docs](tools/docker.md) |
| **Programming** | Python 3.9+ | ✅ Complete | [📖 Docs](tools/python.md) |
| **Automation** | n8n, Ollama | ✅ Complete | [📖 Docs](tools/n8n.md) |
| **Virtualization** | Proxmox VE | ✅ Complete | [📖 Docs](tools/proxmox.md) |
| **Security** | Nessus Professional | ✅ Complete | [📖 Docs](tools/nessus.md) |
| **Service Management** | TopDesk | ✅ Complete | [📖 Docs](tools/topdesk.md) |
| **Collaboration** | Confluence | ✅ Complete | [📖 Docs](tools/confluence.md) |
| **Version Control** | Git, GitHub | 🚧 Planned | [📋 Roadmap](#roadmap) |
| **Infrastructure** | Terraform, Ansible | 🚧 Planned | [📋 Roadmap](#roadmap) |

## 🏃‍♂️ Quick Start

### 1. Install

=== "pip (Recommended)"

    ```bash
    pip install enterprise-mcp-docs
    ```

=== "Docker"

    ```bash
    docker run -p 8000:8000 hasecon/enterprise-mcp-docs
    ```

=== "From Source"

    ```bash
    git clone https://github.com/hasecon/enterprise-mcp-docs.git
    cd enterprise-mcp-docs
    pip install -e .
    ```

### 2. Configure

```bash
# Copy and edit configuration
cp config/default.json config/local.json
cp .env.example .env
```

### 3. Initialize Documentation

```bash
# Crawl documentation for enabled tools
enterprise-mcp-docs crawl --all
```

### 4. Start Server

```bash
enterprise-mcp-docs serve
```

### 5. Connect to Claude Code

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

## 🎉 Start Using

Once configured, ask Claude Code questions like:

!!! example "Example Queries"

    === "Elasticsearch"
        ```
        How do I create an Elasticsearch mapping for user data with proper field types?
        ```

    === "Docker"
        ```
        Show me Docker Compose configuration for a web app with Redis and PostgreSQL.
        ```

    === "Proxmox"
        ```
        How do I configure Proxmox clustering with shared storage for high availability?
        ```

    === "Python"
        ```
        What are the best practices for async/await in Python 3.11+ with error handling?
        ```

## 📚 Next Steps

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } **Quick Start**

    ---

    Get up and running in 5 minutes

    [:octicons-arrow-right-24: Installation Guide](getting-started/installation.md)

-   :material-cog:{ .lg .middle } **Configuration**

    ---

    Configure tools and customize settings

    [:octicons-arrow-right-24: Configuration Guide](getting-started/configuration.md)

-   :material-tools:{ .lg .middle } **Supported Tools**

    ---

    Explore supported enterprise tools

    [:octicons-arrow-right-24: Tools Overview](tools/index.md)

-   :material-code-braces:{ .lg .middle } **Development**

    ---

    Add custom providers and contribute

    [:octicons-arrow-right-24: Developer Guide](development/contributing.md)

</div>

## 🚀 Roadmap

- [ ] **Context7 Integration** - Hybrid approach for popular dev libraries
- [ ] **Web UI Dashboard** - Visual documentation browsing and management
- [ ] **Custom Embedding Models** - Support for domain-specific embeddings
- [ ] **Multi-language Support** - Documentation in multiple languages
- [ ] **API Rate Limiting** - Advanced rate limiting and quota management
- [ ] **Metrics & Monitoring** - Comprehensive observability stack
- [ ] **Cloud Deployment** - One-click cloud deployments
- [ ] **Enterprise SSO** - Integration with enterprise authentication

## 🤝 Community

Join our growing community:

- 💬 [GitHub Discussions](https://github.com/hasecon/enterprise-mcp-docs/discussions)
- 🐛 [Report Issues](https://github.com/hasecon/enterprise-mcp-docs/issues)
- 📧 [Email Support](mailto:info@hasecon.nl)
- 🌟 [Star the Project](https://github.com/hasecon/enterprise-mcp-docs)

## 📄 License

This project is licensed under the [MIT License](https://github.com/hasecon/enterprise-mcp-docs/blob/main/LICENSE) - see the license file for details.

---

<div align="center">

**Ready to eliminate AI hallucinations and get accurate, up-to-date documentation?**

[Get Started →](getting-started/installation.md){ .md-button .md-button--primary }
[View on GitHub →](https://github.com/hasecon/enterprise-mcp-docs){ .md-button }

</div>