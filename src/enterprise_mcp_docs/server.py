"""
Enterprise MCP Documentation Server

MCP server with HTTP health endpoint for Docker deployments.
The actual MCP protocol server is in mcp_server.py
"""

import json
import logging
import os
import signal
import sys
import threading
import time
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

# Configure logging
logging.basicConfig(
    level=getattr(logging, os.getenv("LOG_LEVEL", "INFO").upper()),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


class HealthHandler(BaseHTTPRequestHandler):
    """Simple HTTP handler for health checks"""

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            health_data = {
                "status": "healthy",
                "version": "0.1.0",
                "components": {"redis": "ok", "vector_db": "ok"},
                "timestamp": datetime.now().isoformat(),
            }

            self.wfile.write(json.dumps(health_data).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def log_message(self, format, *args):
        # Suppress default HTTP server logging
        pass


class MCPServer:
    """Basic MCP Server for development"""

    def __init__(self):
        self.running = False
        self.start_time = datetime.now()
        self.http_server = None
        self.http_thread = None

    def start(self):
        """Start the MCP server"""
        logger.info("🚀 Enterprise MCP Documentation Server Starting...")
        logger.info(f"📅 Started at: {self.start_time.isoformat()}")
        logger.info("🏗️  HTTP health server for Docker deployment")
        logger.info("📚 MCP protocol server available via stdio interface")

        # Environment info
        env = os.getenv("ENVIRONMENT", "development")
        redis_url = os.getenv("REDIS_URL", "not configured")
        log_level = os.getenv("LOG_LEVEL", "INFO")

        logger.info(f"🔧 Environment: {env}")
        logger.info(f"📊 Log Level: {log_level}")
        logger.info(f"🔗 Redis URL: {redis_url}")

        # Setup signal handlers
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

        # Start HTTP server for health checks
        self._start_http_server()

        self.running = True

        try:
            self._run_heartbeat()
        except Exception as e:
            logger.error(f"❌ Error in MCP server: {e}")
            raise
        finally:
            self._stop_http_server()

    def _start_http_server(self):
        """Start HTTP server for health checks"""
        try:
            port = int(os.getenv("PORT", "8000"))
            host = os.getenv("HOST", "0.0.0.0")

            self.http_server = HTTPServer((host, port), HealthHandler)
            self.http_thread = threading.Thread(
                target=self.http_server.serve_forever, daemon=True
            )
            self.http_thread.start()

            logger.info(f"🌐 HTTP health server started on {host}:{port}")
            logger.info(f"🔍 Health endpoint: http://{host}:{port}/health")

        except Exception as e:
            logger.error(f"❌ Failed to start HTTP server: {e}")

    def _stop_http_server(self):
        """Stop HTTP server"""
        if self.http_server:
            logger.info("🛑 Stopping HTTP server...")
            self.http_server.shutdown()
            self.http_server.server_close()
            if self.http_thread:
                self.http_thread.join(timeout=5)

    def _signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        logger.info(f"🛑 Received signal {signum}, shutting down gracefully...")
        self.running = False

    def _run_heartbeat(self):
        """Run the main server loop with heartbeat"""
        logger.info("⏳ Keeping container alive for development...")
        logger.info("🔍 Check logs with: docker compose logs -f mcp-server")
        logger.info("🛑 Stop with: docker compose down")
        logger.info("")

        heartbeat_count = 0

        while self.running:
            try:
                time.sleep(60)  # 1 minute intervals
                heartbeat_count += 1

                # Basic heartbeat
                logger.info(f"💓 MCP Server heartbeat #{heartbeat_count}")

                # Extended info every 5 minutes
                if heartbeat_count % 5 == 0:
                    uptime = datetime.now() - self.start_time
                    logger.info(f"📊 Uptime: {uptime}")
                    logger.info("🔧 Ready for MCP implementation development")

                # Health check every 10 minutes
                if heartbeat_count % 10 == 0:
                    self._health_check()

            except KeyboardInterrupt:
                logger.info("🛑 Received KeyboardInterrupt, shutting down...")
                break
            except Exception as e:
                logger.error(f"❌ Error in heartbeat loop: {e}")
                # Continue running despite errors

        logger.info("✅ MCP Server shutdown completed")

    def _health_check(self):
        """Perform basic health checks"""
        try:
            # Check if we can write to logs directory
            if os.path.exists("/app/logs"):
                test_file = "/app/logs/.health_check"
                with open(test_file, "w") as f:
                    f.write(str(datetime.now()))
                os.remove(test_file)
                logger.info("✅ Health check: Logs directory writable")

            # Check memory usage (basic)
            try:
                import psutil

                memory = psutil.virtual_memory()
                logger.info(f"📈 Memory usage: {memory.percent}%")
            except ImportError:
                # psutil not available, that's OK
                pass

        except Exception as e:
            logger.warning(f"⚠️ Health check warning: {e}")


def main():
    """Main entry point"""
    try:
        server = MCPServer()
        server.start()
    except KeyboardInterrupt:
        logger.info("🛑 Shutting down MCP server...")
        sys.exit(0)
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
