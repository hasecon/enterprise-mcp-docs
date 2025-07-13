"""Enterprise MCP Documentation Server

Multi-tool documentation provider for Claude Code and other MCP clients.
"""

__version__ = "0.1.0"
__author__ = "Hasecon"
__description__ = "Enterprise MCP Documentation Server"
__url__ = "https://github.com/hasecon/enterprise-mcp-docs"

from .server import MultiDocsServer

__all__ = ["MultiDocsServer"]
