"""Unit tests for package initialization."""

import enterprise_mcp_docs


def test_package_version():
    """Test that package version is defined."""
    assert hasattr(enterprise_mcp_docs, "__version__")
    assert enterprise_mcp_docs.__version__ == "0.1.0"


def test_package_imports():
    """Test that main classes can be imported."""
    from enterprise_mcp_docs import MCPServer

    assert MCPServer is not None


def test_package_metadata():
    """Test package metadata."""
    assert hasattr(enterprise_mcp_docs, "__author__")
    assert hasattr(enterprise_mcp_docs, "__description__")
    assert enterprise_mcp_docs.__author__ == "Hasecon"
