# Contributing to Enterprise MCP Documentation Server

First off, thank you for considering contributing to Enterprise MCP Documentation Server! It's people like you that make this project great.

## 🤝 How to Contribute

### Reporting Issues

Before creating an issue, please check if a similar issue already exists. When creating an issue, please include:

- **Clear description** of the problem or feature request
- **Steps to reproduce** (for bugs)
- **Expected vs actual behavior** (for bugs)
- **Environment details** (OS, Python version, etc.)
- **Relevant logs** or error messages

### Suggesting Features

We welcome feature suggestions! Please:

1. Check existing issues and discussions first
2. Create a detailed issue describing:
   - The use case for the feature
   - How it would work
   - Why it would be valuable
3. Be open to discussion and feedback

### Contributing Code

#### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/hasecon/enterprise-mcp-docs.git
   cd enterprise-mcp-docs
   ```

2. **Set up development environment**
   ```bash
   # Use the setup script with dev dependencies
   chmod +x scripts/setup.sh
   ./scripts/setup.sh --dev
   
   # Or manually:
   pip install -e ".[dev]"
   pre-commit install
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Development Guidelines

**Code Style**
- We use [Black](https://github.com/psf/black) for code formatting
- [isort](https://github.com/PyCQA/isort) for import sorting
- [flake8](https://flake8.pycqa.org/) for linting
- [mypy](http://mypy-lang.org/) for type checking

**Run code quality checks:**
```bash
black src/ tests/
isort src/ tests/
flake8 src/ tests/
mypy src/
```

**Testing**
- Write tests for new features and bug fixes
- Run the test suite: `pytest`
- Ensure good test coverage: `pytest --cov=enterprise_mcp_docs`
- Test types:
  - **Unit tests**: Fast, isolated component tests
  - **Integration tests**: Test component interactions
  - **End-to-end tests**: Test complete workflows

#### Adding New Documentation Providers

1. **Create provider class** in `src/enterprise_mcp_docs/providers/`:

```python
from .base import BaseProvider

class YourToolProvider(BaseProvider):
    async def crawl_docs(self):
        """Implement documentation crawling logic"""
        docs = []
        # ... fetch and process documentation
        await self.add_to_vector_db(docs)
        return docs
    
    def get_sections(self):
        """Return list of documentation sections"""
        return ["section1", "section2"]
```

2. **Add configuration** to `config/default.json`:

```json
{
  "tools": {
    "yourtool": {
      "provider": "YourTool",
      "base_url": "https://yourtool.com/docs/",
      "sections": ["section1", "section2"],
      "cache_ttl": 3600,
      "enabled": true
    }
  }
}
```

3. **Write tests** in `tests/test_providers.py`:

```python
class TestYourToolProvider:
    async def test_crawl_docs(self):
        # Test your provider
        pass
```

4. **Update documentation** in `README.md` and `docs/providers.md`

#### Commit Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` new features
- `fix:` bug fixes
- `docs:` documentation changes
- `style:` formatting, missing semicolons, etc.
- `refactor:` code refactoring
- `test:` adding tests
- `chore:` maintenance tasks

Examples:
```
feat: add Terraform documentation provider
fix: resolve Redis connection timeout issue
docs: update installation instructions
```

#### Pull Request Process

1. **Ensure your code passes all checks**:
   ```bash
   # Run the full test suite
   pytest
   
   # Check code quality
   black --check src/ tests/
   isort --check-only src/ tests/
   flake8 src/ tests/
   mypy src/
   ```

2. **Update documentation** if needed
3. **Create pull request** with:
   - Clear title and description
   - Reference to related issues
   - Screenshots/examples if applicable

4. **Address review feedback** promptly
5. **Ensure CI passes** before requesting final review

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test types
pytest -m unit
pytest -m integration

# Run with coverage
pytest --cov=enterprise_mcp_docs --cov-report=html

# Run specific test file
pytest tests/test_providers.py
```

### Test Structure

```
tests/
├── unit/          # Fast, isolated tests
├── integration/   # Component interaction tests
├── fixtures/      # Test data and fixtures
└── conftest.py    # Shared test configuration
```

### Writing Tests

- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)
- Mock external dependencies
- Test both success and failure cases

Example:
```python
import pytest
from unittest.mock import AsyncMock

class TestElasticsearchProvider:
    @pytest.fixture
    def provider(self):
        config = {"base_url": "https://example.com", "sections": ["test"]}
        return ElasticsearchProvider(config)
    
    async def test_crawl_docs_success(self, provider):
        # Arrange
        provider.fetch_page = AsyncMock(return_value="<html>test</html>")
        
        # Act
        docs = await provider.crawl_docs()
        
        # Assert
        assert len(docs) > 0
        assert docs[0]["content"] is not None
```

## 📚 Documentation

- Keep documentation up-to-date with code changes
- Use clear, concise language
- Include code examples where helpful
- Follow the existing documentation style

### Documentation Structure

```
docs/
├── index.md           # Main documentation
├── installation.md    # Installation guide
├── configuration.md   # Configuration reference
├── providers.md       # Provider documentation
└── contributing.md    # This file
```

## 🔒 Security

- Never commit sensitive information (API keys, passwords)
- Follow security best practices
- Report security vulnerabilities privately

## 📞 Getting Help

- 💬 [GitHub Discussions](https://github.com/hasecon/enterprise-mcp-docs/discussions)
- 🐛 [GitHub Issues](https://github.com/hasecon/enterprise-mcp-docs/issues)
- 📧 Email: contact@hasecon.nl

## 🏆 Recognition

Contributors will be:
- Listed in the README.md
- Mentioned in release notes for significant contributions
- Invited to become maintainers for consistent contributors

## 📜 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you are expected to uphold this code.

## 🙏 Thank You

Every contribution matters, whether it's:
- Reporting a bug
- Suggesting a feature
- Improving documentation
- Writing code
- Helping other users

Thank you for making Enterprise MCP Documentation Server better! 🚀