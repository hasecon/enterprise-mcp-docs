"""Unit tests for the MCP server."""

from unittest.mock import Mock, patch

from enterprise_mcp_docs.server import MCPServer


class TestMCPServer:
    """Test cases for MCPServer class."""

    def test_server_initialization(self):
        """Test that server initializes correctly."""
        server = MCPServer()
        assert server.running is False
        assert server.start_time is not None
        assert server.http_server is None
        assert server.http_thread is None

    @patch("enterprise_mcp_docs.server.HTTPServer")
    @patch("enterprise_mcp_docs.server.threading.Thread")
    def test_start_http_server(self, mock_thread, mock_http_server):
        """Test HTTP server startup."""
        server = MCPServer()

        # Mock the HTTPServer and Thread
        mock_server_instance = Mock()
        mock_http_server.return_value = mock_server_instance
        mock_thread_instance = Mock()
        mock_thread.return_value = mock_thread_instance

        server._start_http_server()

        # Verify HTTPServer was created
        mock_http_server.assert_called_once()

        # Verify thread was created and started
        mock_thread.assert_called_once()
        mock_thread_instance.start.assert_called_once()

        assert server.http_server == mock_server_instance
        assert server.http_thread == mock_thread_instance

    def test_signal_handler(self):
        """Test signal handler sets running to False."""
        server = MCPServer()
        server.running = True

        server._signal_handler(15, None)  # SIGTERM

        assert server.running is False

    def test_health_check_no_logs_dir(self):
        """Test health check when logs directory doesn't exist."""
        server = MCPServer()

        # Should not raise exception
        server._health_check()
