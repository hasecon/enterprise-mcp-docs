# Enterprise MCP Documentation Server - Project Insights

## Project Overview

### Core Concept
Enterprise MCP Documentation Server is een self-hosted Model Context Protocol (MCP) server die actuele documentatie van enterprise en development tools direct beschikbaar maakt voor AI coding assistants zoals Claude Code, Cursor, en Windsurf.

### Belangrijkste Kenmerken
- **Live Documentation Fetching**: Haalt actuele documentatie op van officiële bronnen (geen verouderde training data)
- **Enterprise Ready**: Ondersteunt tools zoals Proxmox, Nessus, TopDesk, Confluence
- **Privacy First**: Self-hosted oplossing, data blijft binnen je eigen infrastructuur  
- **Smart Caching**: Redis-backed performance optimalisatie
- **Modular Design**: Eenvoudig uit te breiden met nieuwe tools
- **Context7 Compatible**: Kan geïntegreerd worden met bestaande oplossingen

## Technische Architectuur

### Core Components
1. **MCP Server**: Hoofdserver die het Model Context Protocol implementeert
2. **Documentation Providers**: Modulaire providers voor verschillende tools (Elasticsearch, Docker, Python, etc.)
3. **Vector Database**: Voor semantische zoekfunctionaliteit in documentatie
4. **Redis Cache**: Voor performance optimalisatie
5. **Crawling Engine**: Voor het ophalen en verwerken van documentatie

### Belangrijke Directories
- `/src/enterprise_mcp_docs/` - Hoofdcode van de applicatie
- `/config/` - Configuratiebestanden (default.json, local.json)
- `/docs/` - Project documentatie (MkDocs formaat)
- `/tests/` - Unit en integration tests
- `/scripts/` - Setup en utility scripts
- `/docker/` - Docker configuratie bestanden

## Ondersteunde Tools

### Production Ready (✅)
1. **Elasticsearch** - Full-text search en analytics (11 secties, 500+ pagina's)
2. **Docker** - Container platform en orchestration (8 secties, 300+ pagina's)
3. **Python** - Programming language documentatie (12 secties, 1000+ pagina's)
4. **Proxmox VE** - Virtualization management platform (9 secties, 200+ pagina's)
5. **Nessus** - Security vulnerability management (6 secties, 150+ pagina's)
6. **TopDesk** - Service management (4 secties, 100+ pagina's)
7. **Confluence** - Team collaboration (5 secties, 80+ pagina's)
8. **n8n** - Workflow automation (6 secties, 120+ pagina's)
9. **Ollama** - AI/ML platform (4 secties, 60+ pagina's)

### In Development (🚧)
- Git, GitHub (Version Control)
- Terraform, Ansible (Infrastructure as Code)
- Kubernetes (Container Orchestration)

## Installation & Setup

### System Requirements
- **Minimum**: Python 3.9+, 4GB RAM, 2GB storage
- **Recommended**: Python 3.11+, 8GB RAM, 10GB storage, Redis

### Installation Methods
1. **pip install** (Recommended): `pip install enterprise-mcp-docs`
2. **Docker**: Met docker-compose voor complete setup inclusief Redis
3. **From Source**: Voor development doeleinden

### Key Configuration Steps
1. Copy configuration: `cp config/default.json config/local.json`
2. Set environment variables: `cp .env.example .env`
3. Crawl documentation: `enterprise-mcp-docs crawl --all`
4. Start server: `enterprise-mcp-docs serve`

## Integration met AI Assistants

### Claude Code Configuration
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

### Cursor Configuration
Toevoegen aan `.cursor/mcp.json` met vergelijkbare configuratie.

## Development Insights

### Provider Architecture
- Elke tool heeft zijn eigen provider class die erft van `BaseProvider`
- Providers implementeren `crawl_docs()` methode voor documentatie ophalen
- Documentatie wordt opgeslagen in vector database voor semantische search
- Caching via Redis voor performance

### Belangrijke Commands
- `enterprise-mcp-docs --version` - Check versie
- `enterprise-mcp-docs config check` - Test configuratie
- `enterprise-mcp-docs crawl --tool [naam]` - Crawl specifieke tool
- `enterprise-mcp-docs serve` - Start MCP server
- `enterprise-mcp-docs status` - Check documentatie status

## Use Cases & Benefits

### Voor Development Teams
- Actuele API documentatie zonder hallucinations
- Best practices voor Docker, Python, Elasticsearch
- Integratie patronen voor enterprise tools

### Voor DevOps Engineers  
- Proxmox high availability setup
- Docker security recommendations
- n8n workflow automation

### Voor Security Teams
- Nessus scan policies voor compliance
- Vulnerability assessment procedures
- Security hardening documentatie

### Voor Enterprise Users
- TopDesk automation workflows
- Confluence API best practices
- Enterprise tool integraties

## Community & Contribution

### Contributing
1. Fork repository
2. Create feature branch
3. Implement changes (follow code style)
4. Add tests
5. Submit pull request

### Development Setup
```bash
git clone https://github.com/hasecon/enterprise-mcp-docs.git
cd enterprise-mcp-docs
pip install -e ".[dev]"
pre-commit install
```

### Testing
- `pytest` - Run all tests
- `pytest --cov=enterprise_mcp_docs` - Met coverage
- `mypy src/` - Type checking
- `black src/ tests/` - Code formatting

## Monitoring & Production

### Health Checks
- `/health` endpoint voor status monitoring
- Metrics voor documentation fetch rates, cache hits, search performance

### Docker Deployment
- Development: `docker-compose -f docker-compose.dev.yml up`
- Production: `docker-compose -f docker-compose.prod.yml up -d`

## Roadmap & Future Plans

### Planned Features
- Context7 Integration voor hybrid approach
- Web UI Dashboard voor visuele documentatie browsing
- Custom Embedding Models voor domain-specific embeddings
- Multi-language Support
- Enterprise SSO integratie
- Cloud deployment opties

### Community Requested Tools
- Grafana (Monitoring) - 45 votes
- Jenkins (CI/CD) - 38 votes  
- MongoDB (Database) - 32 votes
- Nginx (Web Server) - 28 votes
- Redis (Cache/DB) - 25 votes

## Belangrijke Links
- GitHub: https://github.com/hasecon/enterprise-mcp-docs
- Documentation: https://hasecon.github.io/enterprise-mcp-docs
- Issues: https://github.com/hasecon/enterprise-mcp-docs/issues
- Discussions: https://github.com/hasecon/enterprise-mcp-docs/discussions

## License & Support
- MIT License - Volledig open source
- Community support via GitHub
- Commercial support beschikbaar via info@hasecon.nl