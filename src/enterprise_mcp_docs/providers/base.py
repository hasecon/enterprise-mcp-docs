"""Base provider class for documentation sources.

This module defines the abstract base class for all documentation providers.
Currently implemented as a placeholder for CI/CD compatibility.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseProvider(ABC):
    """Abstract base class for documentation providers.

    This class defines the interface that all documentation providers
    must implement. Each provider is responsible for crawling and
    processing documentation from a specific tool or service.
    """

    def __init__(self, config: Dict[str, Any]):
        """Initialize the provider with configuration.

        Args:
            config: Configuration dictionary for this provider
        """
        self.config = config
        self.name = config.get("name", "Unknown")
        self.base_url = config.get("base_url", "")
        self.sections = config.get("sections", [])
        self.cache_ttl = config.get("cache_ttl", 3600)
        self.enabled = config.get("enabled", True)

    @abstractmethod
    async def crawl_docs(self) -> List[Dict[str, Any]]:
        """Crawl documentation from the source.

        This method should fetch and process documentation from
        the provider's source (website, API, etc.).

        Returns:
            List of document dictionaries containing title, content, url, etc.
        """
        pass

    @abstractmethod
    async def search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search documentation content.

        Args:
            query: Search query string
            limit: Maximum number of results to return

        Returns:
            List of search result dictionaries
        """
        pass

    async def get_health(self) -> Dict[str, Any]:
        """Check provider health status.

        Returns:
            Dictionary containing health status information
        """
        return {
            "name": self.name,
            "status": "not_implemented",
            "enabled": self.enabled,
            "last_crawl": None,
            "document_count": 0,
        }

    async def validate_config(self) -> bool:
        """Validate provider configuration.

        Returns:
            True if configuration is valid, False otherwise
        """
        required_fields = ["base_url", "sections"]
        for field in required_fields:
            if field not in self.config:
                return False
        return True
