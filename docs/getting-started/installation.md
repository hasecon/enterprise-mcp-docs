# Installation Guide

This guide will help you install and set up Enterprise MCP Documentation Server on your system.

## 📋 System Requirements

### Minimum Requirements

- **Python**: 3.9 or higher
- **Memory**: 4GB RAM (for vector embeddings)
- **Storage**: 2GB free space (for documentation cache)
- **Network**: Internet access for documentation crawling

### Recommended Requirements

- **Python**: 3.11 or higher  
- **Memory**: 8GB RAM or more
- **Storage**: 10GB free space
- **Redis**: For optimal caching performance
- **Docker**: For containerized deployment

### Supported Platforms

- ✅ **Linux** (Ubuntu 20.04+, CentOS 7+, Debian 10+)
- ✅ **macOS** (10.15+ / Big Sur+)
- ✅ **Windows** (10/11 with WSL2 recommended)
- ✅ **Docker** (Linux containers)

## 🚀 Installation Methods

Choose the installation method that best fits your environment:

=== "pip (Recommended)"

    ### Install from PyPI

    The easiest way to install Enterprise MCP Documentation Server:

    ```bash
    # Install the package
    pip install enterprise-mcp-docs
    
    # Verify installation
    enterprise-mcp-docs --version
    ```

    ### Install from PyPI with All Features

    ```bash
    # Install with all optional dependencies
    pip install enterprise-mcp-docs[monitoring,context7]
    ```

=== "Docker (Easiest)"

    ### Using Docker Compose (Recommended)

    ```bash
    # Clone the repository
    git clone https://github.com/hasecon/enterprise-mcp-docs.git
    cd enterprise-mcp-docs
    
    # Start all services
    docker-compose up -d
    
    # Check status
    docker-compose ps
    ```

    ### Using Docker Run

    ```bash
    # Pull the image
    docker pull hasecon/enterprise-mcp-docs:latest
    
    # Run with Redis
    docker network create mcp-network
    docker run -d --name redis --network mcp-network redis:7-alpine
    docker run -d \
      --name mcp-server \
      --network mcp-network \
      -p 8000:8000 \
      -e REDIS_URL=redis://redis:6379 \
      hasecon/enterprise-mcp-docs:latest
    ```

=== "From Source"

    ### Clone and Install

    ```bash
    # Clone the repository
    git clone https://github.com/hasecon/enterprise-mcp-docs.git
    cd enterprise-mcp-docs
    
    # Install in development mode
    pip install -e .
    
    # Or install with development dependencies
    pip install -e ".[dev]"
    ```

    ### Using the Setup Script

    ```bash
    # Make setup script executable
    chmod +x scripts/setup.sh
    
    # Run automated setup
    ./scripts/setup.sh
    
    # Or with development dependencies
    ./scripts/setup.sh --dev
    ```

## ⚙️ Initial Setup

### 1. Configuration Files

After installation, create your configuration files:

```bash
# Copy configuration template
cp config/default.json config/local.json

# Copy environment template  
cp .env.example .env
```

### 2. Environment Variables

Edit the `.env` file with your settings:

```bash
# Basic configuration
ENVIRONMENT=development
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=INFO

# Redis configuration (if using Redis)
REDIS_URL=redis://localhost:6379

# Vector database settings
EMBEDDING_MODEL=all-MiniLM-L6-v2
VECTOR_DB_PATH=./vector_store

# Documentation crawling
CRAWL_INTERVAL=86400  # 24 hours
MAX_CRAWL_WORKERS=4
```

### 3. Initial Documentation Crawl

```bash
# Crawl documentation for all enabled tools
enterprise-mcp-docs crawl --all

# Or crawl specific tools
enterprise-mcp-docs crawl --tool elasticsearch
enterprise-mcp-docs crawl --tool docker
enterprise-mcp-docs crawl --tool python
```

!!! tip "Performance Tip"
    Initial crawling can take 10-30 minutes depending on the number of tools enabled. Run this during off-hours or in the background.

## 🔧 Verification

### 1. Test Installation

```bash
# Check version
enterprise-mcp-docs --version

# Test configuration
enterprise-mcp-docs config check

# Test server startup
enterprise-mcp-docs serve --test-mode
```

### 2. Health Check

```bash
# Start the server
enterprise-mcp-docs serve &

# Check health endpoint
curl http://localhost:8000/health

# Expected response:
# {"status": "healthy", "version": "0.1.0", "components": {"redis": "ok", "vector_db": "ok"}}
```

## 🔌 MCP Client Integration

### Claude Code

Add to your Claude Code configuration file:

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

### Cursor

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "enterprise-docs": {
      "command": "enterprise-mcp-docs",
      "args": ["serve"],
      "env": {}
    }
  }
}
```

## 🚀 Next Steps

After successful installation:

1. **[Configure Tools](configuration.md)** - Set up documentation sources
2. **[Quick Start Guide](quick-start.md)** - Learn basic usage
3. **[User Guide](../user-guide/claude-code.md)** - Integrate with your AI assistant
4. **[Monitoring Setup](../deployment/monitoring.md)** - Set up monitoring and alerting

---

!!! success "Installation Complete!"
    
    Your Enterprise MCP Documentation Server is now installed and ready to use! 🎉
    
    [Continue to Configuration →](configuration.md){ .md-button .md-button--primary }