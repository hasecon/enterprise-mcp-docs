"""Integration tests for health endpoint."""

import time

import httpx
import pytest

from enterprise_mcp_docs.server import MCPServer


class TestHealthEndpoint:
    """Integration tests for the health endpoint."""

    @pytest.fixture
    def server(self):
        """Create a test server instance."""
        server = MCPServer()
        return server

    def test_health_endpoint_response(self, server):
        """Test that health endpoint returns correct response."""
        # Start HTTP server in background
        server._start_http_server()

        # Give server time to start
        time.sleep(0.5)

        try:
            # Make request to health endpoint
            response = httpx.get("http://localhost:8000/health", timeout=5.0)

            assert response.status_code == 200
            assert response.headers["content-type"] == "application/json"

            data = response.json()
            assert data["status"] == "healthy"
            assert data["version"] == "0.1.0"
            assert "components" in data
            assert "timestamp" in data

        finally:
            # Cleanup
            server._stop_http_server()

    def test_health_endpoint_not_found(self, server):
        """Test that non-existent endpoints return 404."""
        server._start_http_server()
        time.sleep(0.5)

        try:
            response = httpx.get("http://localhost:8000/nonexistent", timeout=5.0)
            assert response.status_code == 404

        finally:
            server._stop_http_server()
