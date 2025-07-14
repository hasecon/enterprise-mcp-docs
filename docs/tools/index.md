# Supported Tools Overview

Enterprise MCP Documentation Server provides comprehensive documentation support for a wide range of enterprise and development tools. This page gives you an overview of all supported tools and their current status.

## 🎯 Quick Overview

<div class="grid cards" markdown>

-   :material-magnify:{ .lg .middle } **Search & Analytics**

    ---

    **Elasticsearch** - Full-text search and analytics
    
    **Status:** ✅ Complete  
    **Sections:** 11 sections, 500+ pages

    [:octicons-arrow-right-24: Documentation](elasticsearch.md)

-   :material-docker:{ .lg .middle } **Containerization**

    ---

    **Docker** - Container platform and orchestration
    
    **Status:** ✅ Complete  
    **Sections:** 8 sections, 300+ pages

    [:octicons-arrow-right-24: Documentation](docker.md)

-   :material-language-python:{ .lg .middle } **Programming**

    ---

    **Python** - Programming language documentation
    
    **Status:** ✅ Complete  
    **Sections:** 12 sections, 1000+ pages

    [:octicons-arrow-right-24: Documentation](python.md)

-   :material-server:{ .lg .middle } **Virtualization**

    ---

    **Proxmox VE** - Virtualization management platform
    
    **Status:** ✅ Complete  
    **Sections:** 9 sections, 200+ pages

    [:octicons-arrow-right-24: Documentation](proxmox.md)

</div>

## 📊 Complete Tool Matrix

### Production Ready ✅

| Tool | Category | Sections | Pages | Last Updated | Configuration |
|------|----------|----------|-------|--------------|---------------|
| **[Elasticsearch](elasticsearch.md)** | Search & Analytics | 11 | 500+ | Daily | [Setup →](../configuration/tools.md#elasticsearch) |
| **[Docker](docker.md)** | Containerization | 8 | 300+ | Daily | [Setup →](../configuration/tools.md#docker) |
| **[Python](python.md)** | Programming | 12 | 1000+ | Weekly | [Setup →](../configuration/tools.md#python) |
| **[Proxmox VE](proxmox.md)** | Virtualization | 9 | 200+ | Weekly | [Setup →](../configuration/tools.md#proxmox) |
| **[Nessus](nessus.md)** | Security | 6 | 150+ | Monthly | [Setup →](../configuration/tools.md#nessus) |
| **[TopDesk](topdesk.md)** | Service Management | 4 | 100+ | Monthly | [Setup →](../configuration/tools.md#topdesk) |
| **[Confluence](confluence.md)** | Collaboration | 5 | 80+ | Weekly | [Setup →](../configuration/tools.md#confluence) |
| **[n8n](n8n.md)** | Automation | 6 | 120+ | Weekly | [Setup →](../configuration/tools.md#n8n) |
| **[Ollama](ollama.md)** | AI/ML | 4 | 60+ | Weekly | [Setup →](../configuration/tools.md#ollama) |

### In Development 🚧

| Tool | Category | Expected | Status | Progress |
|------|----------|----------|---------|----------|
| **Git** | Version Control | Q2 2025 | 🚧 In Progress | 75% |
| **GitHub** | Code Hosting | Q2 2025 | 🚧 In Progress | 60% |
| **Terraform** | Infrastructure | Q2 2025 | 🚧 Planning | 25% |
| **Ansible** | Configuration | Q3 2025 | 🚧 Planning | 10% |
| **Kubernetes** | Orchestration | Q3 2025 | 📋 Planned | 0% |

### Community Requested 📋

| Tool | Category | Votes | Complexity | Timeline |
|------|----------|-------|------------|----------|
| **Grafana** | Monitoring | 45 | Medium | Q3 2025 |
| **Jenkins** | CI/CD | 38 | High | Q4 2025 |
| **MongoDB** | Database | 32 | Medium | Q3 2025 |
| **Nginx** | Web Server | 28 | Low | Q2 2025 |
| **Redis** | Cache/DB | 25 | Low | Q2 2025 |

[📝 Request New Tool →](https://github.com/hasecon/enterprise-mcp-docs/issues/new?template=tool-request.md){ .md-button }

## 🏢 Enterprise & Team Usage

### For Small Teams (1-10 developers)

**Recommended Starter Pack:**
- ✅ **Docker** - Containerization
- ✅ **Python** - Development
- ✅ **Elasticsearch** - Search (if needed)

**Configuration:**
```json
{
  "tools": {
    "docker": {"provider": "Docker", "enabled": true},
    "python": {"provider": "Python", "enabled": true}
  }
}
```

### For Medium Teams (10-50 developers)

**Recommended Enterprise Pack:**
- ✅ **Docker** - Containerization
- ✅ **Python** - Development  
- ✅ **Elasticsearch** - Search & Analytics
- ✅ **n8n** - Automation
- 🚧 **Git** - Version Control (when available)

### For Large Organizations (50+ developers)

**Recommended Full Stack:**
- ✅ **All Development Tools** - Docker, Python, Git
- 🚧 **Infrastructure** - Proxmox, Terraform, Kubernetes  
- ✅ **Security** - Nessus
- ✅ **Enterprise** - TopDesk, Confluence
- 📋 **Monitoring** - Elasticsearch, Grafana

## 🚀 Getting Started with Tools

### Quick Setup

1. **Choose Your Tools**
   
   Select the tools your team uses from the supported list above.

2. **Configure**
   
   Add tools to your configuration file:
   
   ```json
   {
     "tools": {
       "elasticsearch": {"provider": "Elasticsearch", "enabled": true},
       "docker": {"provider": "Docker", "enabled": true},
       "python": {"provider": "Python", "enabled": true}
     }
   }
   ```

3. **Crawl Documentation**
   
   Initialize documentation for your selected tools:
   
   ```bash
   enterprise-mcp-docs crawl --tool elasticsearch
   enterprise-mcp-docs crawl --tool docker  
   enterprise-mcp-docs crawl --tool python
   ```

4. **Start Using**
   
   Ask Claude Code questions about your tools:
   
   ```
   How do I set up Elasticsearch with Docker using Python client libraries?
   ```

## 🔧 Tool-Specific Features

### Advanced Search Capabilities

Different tools offer different search capabilities:

| Tool | Semantic Search | Code Examples | API Docs | Version Support |
|------|----------------|---------------|----------|------------------|
| **Elasticsearch** | ✅ Excellent | ✅ 200+ | ✅ Complete | ✅ 8.x, 7.x |
| **Docker** | ✅ Excellent | ✅ 150+ | ✅ Complete | ✅ Latest |
| **Python** | ✅ Excellent | ✅ 500+ | ✅ Complete | ✅ 3.12, 3.11, 3.10 |
| **Proxmox** | ✅ Good | ✅ 80+ | ✅ Partial | ✅ 8.x, 7.x |
| **n8n** | ✅ Good | ✅ 100+ | ✅ Complete | ✅ Latest |

## 🤝 Contributing New Tools

### Community Process

Want to add support for a new tool? Here's how:

1. **Check Existing Requests**
   
   Browse [existing tool requests](https://github.com/hasecon/enterprise-mcp-docs/labels/tool-request) to avoid duplicates.

2. **Create Tool Request**
   
   [Submit a new tool request](https://github.com/hasecon/enterprise-mcp-docs/issues/new?template=tool-request.md) with:
   - Tool name and category
   - Use case and business justification
   - Documentation URL and structure
   - Estimated user demand

3. **Community Voting**
   
   Tool requests are prioritized based on:
   - 👍 Community upvotes
   - 🏢 Enterprise demand
   - 🔧 Technical feasibility
   - 📚 Documentation quality

4. **Development**
   
   High-priority tools are added to the development roadmap or you can [contribute a provider yourself](../development/adding-providers.md).

### Development Providers

Want to build a provider yourself?

1. **[Follow the Provider Guide](../development/adding-providers.md)** - Complete tutorial
2. **Use the Provider Template** - Quick start template
3. **Submit Pull Request** - Community review process
4. **Celebrate** - Your tool is now available to everyone! 🎉

---

!!! tip "Getting the Most from Your Tools"
    
    - **Start small** with 2-3 essential tools
    - **Add gradually** as your team's needs grow
    - **Monitor usage** to optimize your tool selection
    - **Keep documentation fresh** with regular crawling
    - **Share feedback** to help improve tool support
    
    [Get Started →](../getting-started/quick-start.md){ .md-button .md-button--primary }
    [Request New Tool →](https://github.com/hasecon/enterprise-mcp-docs/issues/new?template=tool-request.md){ .md-button }