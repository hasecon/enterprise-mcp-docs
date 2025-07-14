# Quick Start Guide

Get up and running with Enterprise MCP Documentation Server in 5 minutes! This guide assumes you've already [installed](installation.md) and [configured](configuration.md) the basic setup.

## 🚀 Step 1: Start the Server

First, let's start the MCP server:

=== "Command Line"

    ```bash
    # Start the server
    enterprise-mcp-docs serve
    
    # Or with custom configuration
    enterprise-mcp-docs serve --config config/local.json
    
    # Or in background
    enterprise-mcp-docs serve --daemon
    ```

=== "Docker"

    ```bash
    # Using docker-compose
    docker-compose up -d
    
    # Check status
    docker-compose ps
    
    # View logs
    docker-compose logs -f mcp-server
    ```

=== "Python Module"

    ```bash
    # Run as Python module
    python -m enterprise_mcp_docs.server
    
    # With configuration
    python -m enterprise_mcp_docs.server --config config/local.json
    ```

### Verify Server is Running

```bash
# Check health endpoint
curl http://localhost:8000/health

# Expected response:
{
  "status": "healthy",
  "version": "0.1.0",
  "components": {
    "redis": "ok",
    "vector_db": "ok"
  }
}
```

## 📚 Step 2: Crawl Documentation

Initialize your documentation database by crawling the enabled tools:

### Quick Crawl (Essential Tools)

```bash
# Crawl the most important tools first
enterprise-mcp-docs crawl --tool elasticsearch
enterprise-mcp-docs crawl --tool docker  
enterprise-mcp-docs crawl --tool python
```

### Full Crawl (All Tools)

```bash
# Crawl all enabled tools (this may take 10-30 minutes)
enterprise-mcp-docs crawl --all

# Monitor progress
tail -f logs/mcp-server.log
```

!!! tip "Crawling Tips"
    
    - Initial crawling takes time - be patient!
    - Start with essential tools you use daily
    - Run crawling during off-hours to avoid rate limiting
    - Monitor logs for any crawling errors

## 🔌 Step 3: Connect to Claude Code

Now let's connect the MCP server to Claude Code:

### 1. Add MCP Server Configuration

Add the following to your `~/.config/claude-code/mcp.json`:

```json
{
  "mcpServers": {
    "enterprise-docs": {
      "command": "python",
      "args": ["-m", "enterprise_mcp_docs.server"],
      "env": {
        "CONFIG_FILE": "/path/to/your/config/local.json"
      }
    }
  }
}
```

### 2. Restart Claude Code

```bash
# Restart Claude Code to load the new MCP server
# (Method depends on how you installed Claude Code)
```

## ✅ Step 4: Test the Integration

Let's verify everything is working:

### Test Basic Queries

Try these example queries in Claude Code:

!!! example "Test Queries"

    === "Elasticsearch"
        ```
        How do I create an Elasticsearch index with custom mapping for user data?
        ```

    === "Docker"
        ```
        Show me a Docker Compose file for a web application with PostgreSQL and Redis.
        ```

    === "Python"
        ```
        What are the best practices for async/await in Python 3.11+ with proper error handling?
        ```

### Verify Documentation Sources

Check that Claude is using the MCP server:

```
Can you find the latest Elasticsearch documentation on creating indices? 
Please show me the exact documentation source you're using.
```

You should see responses that reference current, accurate documentation from the official sources.

## 🎯 Step 5: Your First Real Query

Now let's try a real-world scenario:

!!! example "Real-World Example"

    **Query in Claude Code:**
    ```
    I need to set up a complete development environment with:
    - Elasticsearch for search
    - Redis for caching  
    - PostgreSQL for data storage
    - Docker for containerization
    
    Can you provide Docker Compose configuration and explain how to configure Elasticsearch with proper security settings?
    ```

    **Expected Result:**
    Claude should provide accurate, up-to-date configuration examples using the latest documentation from your MCP server.

## 🚀 Next Steps

After successful setup:

1. **[Explore Supported Tools](../tools/index.md)** - Learn about all available documentation sources
2. **[Optimize Configuration](configuration.md)** - Fine-tune settings for your environment  
3. **[Add Custom Tools](../development/adding-providers.md)** - Add your own documentation sources

---

!!! success "Quick Start Complete!"
    
    You're now ready to leverage the power of accurate, up-to-date documentation in your AI-assisted development workflow! 🚀
    
    [Explore Tools →](../tools/index.md){ .md-button .md-button--primary }
    [User Guide →](../user-guide/claude-code.md){ .md-button }