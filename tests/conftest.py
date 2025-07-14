"""Pytest configuration and fixtures."""

import os
import tempfile
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def test_config():
    """Test configuration fixture."""
    return {
        "redis_url": "redis://localhost:6379",
        "log_level": "DEBUG",
        "environment": "test",
    }


@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)


@pytest.fixture
def mock_config_file(temp_dir):
    """Create a mock configuration file."""
    config_content = {
        "tools": {
            "test_tool": {
                "provider": "TestProvider",
                "base_url": "https://example.com/docs/",
                "sections": ["getting-started", "api"],
                "cache_ttl": 3600,
                "enabled": True,
            }
        },
        "vector_db": {"enabled": True, "embedding_model": "all-MiniLM-L6-v2"},
        "cache": {"redis_url": "redis://localhost:6379", "ttl": 3600},
    }

    config_file = temp_dir / "test_config.json"
    import json

    with open(config_file, "w") as f:
        json.dump(config_content, f)

    return config_file


@pytest.fixture(autouse=True)
def set_test_env():
    """Set test environment variables."""
    os.environ["ENVIRONMENT"] = "test"
    os.environ["LOG_LEVEL"] = "DEBUG"
    yield
    # Cleanup not strictly necessary as each test runs in isolation
