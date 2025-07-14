# Frequently Asked Questions

This page answers the most common questions about Enterprise MCP Documentation Server.

## 🚀 Getting Started

??? question "What is Enterprise MCP Documentation Server and why do I need it?"

    Enterprise MCP Documentation Server is a self-hosted documentation provider that gives AI coding assistants like Claude Code access to accurate, up-to-date documentation for enterprise and development tools.
    
    **Why you need it:**
    - ❌ **Without it:** Claude gives you outdated examples, hallucinates APIs, and can't help with enterprise tools
    - ✅ **With it:** Claude provides current, accurate documentation for Elasticsearch, Docker, Proxmox, Nessus, TopDesk, and more
    
    Think of it as giving your AI assistant a constantly updated library of technical documentation.

??? question "How is this different from Context7?"

    | Feature | Enterprise MCP Docs | Context7 |
    |---------|-------------------|----------|
    | **Focus** | Enterprise + internal tools | Popular dev libraries only |
    | **Hosting** | Self-hosted (privacy) | Cloud-only |
    | **Customization** | Fully customizable | Limited to supported tools |
    | **Cost** | Free & open source | Freemium model |
    | **Data Control** | Complete control | Data goes to external service |
    
    **Use both:** You can configure our server to use Context7 for popular libraries while handling enterprise tools internally.

??? question "Which AI coding assistants does this work with?"

    Enterprise MCP Documentation Server works with any MCP-compatible client:
    
    **Confirmed Working:**
    - ✅ **Claude Code** (Anthropic's official CLI tool)
    - ✅ **Cursor** (AI-first code editor)
    - ✅ **Windsurf** (AI-powered IDE)
    - ✅ **Cline** (VS Code extension)
    
    **Upcoming Support:**
    - 🚧 **Continue** (VS Code extension)
    - 🚧 **Copilot Chat** (GitHub integration planned)
    - 🚧 **Custom integrations** via API

??? question "Do I need to be a developer to use this?"

    **For basic usage:** No! If you're comfortable with command-line tools, you can set this up using our one-command installer.
    
    **For advanced usage:** Some technical knowledge helps for:
    - Custom configurations
    - Adding new documentation sources
    - Production deployments
    
    **Getting help:** Our community is very helpful for non-developers!

## 🔧 Troubleshooting

??? question "Claude Code can't connect to the MCP server. What's wrong?"

    **Step 1: Check server is running**
    ```bash
    curl http://localhost:8000/health
    # Should return: {"status": "healthy"}
    ```
    
    **Step 2: Verify Claude Code configuration**
    ```bash
    cat ~/.config/claude-code/mcp.json
    # Check the file exists and has correct syntax
    ```
    
    **Step 3: Test MCP connection**
    ```bash
    claude-code --test-mcp enterprise-docs
    ```
    
    **Step 4: Check logs**
    ```bash
    tail -f logs/mcp-server.log
    ```
    
    **Common fixes:**
    - Restart Claude Code
    - Check file permissions on mcp.json
    - Verify Python path in configuration

??? question "The server starts but Claude gets no search results. Why?"

    **Most common cause:** Documentation wasn't crawled yet.
    
    **Check documentation status:**
    ```bash
    enterprise-mcp-docs status
    ls -la data/docs/  # Should contain tool folders
    ```
    
    **Fix: Crawl documentation**
    ```bash
    enterprise-mcp-docs crawl --all --verbose
    ```
    
    **Other causes:**
    - Vector database not initialized
    - Redis connection issues
    - Configuration errors

## 🔒 Security & Privacy

??? question "Is my documentation data secure?"

    **Yes!** Security is a core design principle:
    
    **Self-hosted:** All data stays on your infrastructure
    **No external calls:** Internal documentation never leaves your network
    **Access control:** Configure authentication and rate limiting
    **Encryption:** Support for TLS/SSL encryption
    **Audit logging:** Track all access and changes
    
    **For sensitive environments:** Deploy in air-gapped networks with no internet access.

??? question "Can I use this in a corporate/regulated environment?"

    **Absolutely!** This was designed for enterprise use:
    
    **Compliance features:**
    - Self-hosted deployment
    - Audit logging and monitoring
    - Role-based access control
    - Data retention policies
    - Air-gapped deployment support
    
    **Regulatory compliance:**
    - GDPR-compliant (data stays local)
    - SOC 2 ready (with proper configuration)
    - HIPAA-compatible (healthcare environments)
    - FedRAMP considerations (government use)

## 🏢 Enterprise & Team Usage

??? question "Can multiple team members use the same MCP server?"

    **Yes!** This is the recommended approach for teams:
    
    **Shared deployment:**
    - One server serves multiple developers
    - Shared documentation cache
    - Consistent results across team
    - Reduced resource usage
    
    **Team configuration:**
    ```json
    {
      "mcpServers": {
        "enterprise-docs": {
          "command": "python",
          "args": ["-m", "enterprise_mcp_docs.server"],
          "env": {
            "MCP_SERVER_URL": "https://mcp.company.com"
          }
        }
      }
    }
    ```

??? question "How do I deploy this for my entire organization?"

    **Deployment options:**
    
    **1. Centralized deployment** (Recommended)
    - Single server for entire organization
    - Load balancer for high availability
    - Shared cache and documentation
    
    **2. Team-based deployment**
    - One server per team/department
    - Team-specific documentation
    - Easier management and customization
    
    **3. Hybrid approach**
    - Central server for common tools
    - Team servers for specialized tools
    
    **See our [Production Deployment Guide](deployment/production.md) for details.**

## 🔄 Updates & Maintenance

??? question "How do I update to a new version?"

    **Update methods:**
    
    **pip installation:**
    ```bash
    pip install --upgrade enterprise-mcp-docs
    ```
    
    **Docker:**
    ```bash
    docker pull hasecon/enterprise-mcp-docs:latest
    docker-compose up -d
    ```
    
    **From source:**
    ```bash
    git pull origin main
    pip install -e .
    ```
    
    **Migration:** Most updates are backward compatible. Check the [changelog](changelog.md) for breaking changes.

??? question "Do I need to maintain this myself?"

    **Minimal maintenance required:**
    
    **Automatic:**
    - Documentation crawling
    - Cache management  
    - Health monitoring
    
    **Periodic (monthly):**
    - Check for software updates
    - Review logs for errors
    - Monitor disk usage
    
    **As needed:**
    - Add new tools
    - Adjust configuration
    - Scale resources
    
    **Managed options:**
    - Docker deployment for easier updates
    - Cloud hosting for automatic scaling
    - Commercial support available

## 💬 Community & Support

??? question "Where can I get help?"

    **Community support:**
    - 💬 [GitHub Discussions](https://github.com/hasecon/enterprise-mcp-docs/discussions) - General questions
    - 🐛 [GitHub Issues](https://github.com/hasecon/enterprise-mcp-docs/issues) - Bug reports
    - 📧 [Email](mailto:info@hasecon.nl) - Direct contact
    
    **Documentation:**
    - 📚 [Complete docs](https://hasecon.github.io/enterprise-mcp-docs)
    - 📚 [Examples](https://github.com/hasecon/enterprise-mcp-docs/tree/main/examples)
    
    **Commercial support:**
    - Priority response times
    - Custom development
    - Training and consulting

??? question "Can I request support for a new tool?"

    **Absolutely!** We love adding new tools:
    
    **How to request:**
    1. [Create a tool request](https://github.com/hasecon/enterprise-mcp-docs/issues/new?template=tool-request.md)
    2. Include tool name, documentation URL, and use case
    3. Community votes on requests
    4. Popular requests get prioritized
    
    **Or build it yourself:**
    - [Provider development guide](development/adding-providers.md)
    - Community review and integration
    - Recognition in the project

---

!!! question "Still have questions?"
    
    Don't see your question here? We're happy to help!
    
    [Ask on GitHub Discussions →](https://github.com/hasecon/enterprise-mcp-docs/discussions){ .md-button .md-button--primary }
    [Report an Issue →](https://github.com/hasecon/enterprise-mcp-docs/issues/new){ .md-button }
    [Contact Us →](mailto:info@hasecon.nl){ .md-button }