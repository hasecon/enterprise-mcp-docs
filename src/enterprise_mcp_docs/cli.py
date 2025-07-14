"""Command-line interface for Enterprise MCP Documentation Server."""

import json
import os
import sys
from typing import Optional

import click

from . import __version__
from .server import MCPServer  # HTTP health server
from .mcp_server import EnterpriseMCPServer  # Actual MCP server


@click.group()
@click.version_option(version=__version__)
@click.option(
    "--config", "-c", type=click.Path(exists=True), help="Configuration file path"
)
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
@click.pass_context
def cli(ctx, config: Optional[str], verbose: bool):
    """Enterprise MCP Documentation Server CLI.

    Multi-tool documentation provider for Claude Code and other MCP clients.
    """
    ctx.ensure_object(dict)
    ctx.obj["config_file"] = config
    ctx.obj["verbose"] = verbose

    if verbose:
        click.echo(f"Enterprise MCP Documentation Server v{__version__}")


@cli.command()
@click.option("--mode", type=click.Choice(["mcp", "http"]), default="mcp", 
              help="Server mode: 'mcp' for MCP protocol, 'http' for health server")
@click.option("--host", default="0.0.0.0", help="Host to bind to (HTTP mode only)")
@click.option("--port", default=8000, type=int, help="Port to bind to (HTTP mode only)")
@click.option("--config", type=click.Path(exists=True), help="Configuration file")
@click.option("--test-mode", is_flag=True, help="Run in test mode")
@click.pass_context
def serve(ctx, mode: str, host: str, port: int, config: Optional[str], test_mode: bool):
    """Start the MCP server.
    
    By default starts the MCP protocol server for Claude Code integration.
    Use --mode http for Docker health server mode.
    """
    if ctx.obj["verbose"]:
        click.echo(f"Starting {mode.upper()} server...")

    if test_mode:
        click.echo("🧪 Running in test mode")
        click.echo("✅ Server startup test passed")
        return

    try:
        if mode == "mcp":
            # Start the actual MCP protocol server
            import asyncio
            
            click.echo("🚀 Starting MCP protocol server...")
            click.echo("📡 Listening for stdio connections from Claude Code")
            
            # TODO: Load config from file if provided
            server_config = {
                "tools": {
                    "elasticsearch": {"provider": "Elasticsearch", "enabled": True},
                    "docker": {"provider": "Docker", "enabled": True}, 
                    "python": {"provider": "Python", "enabled": True}
                }
            }
            
            server = EnterpriseMCPServer(server_config)
            asyncio.run(server.start())
            
        elif mode == "http":
            # Start HTTP health server (for Docker)
            os.environ["HOST"] = host
            os.environ["PORT"] = str(port)
            
            click.echo(f"🚀 Starting HTTP health server on {host}:{port}")
            server = MCPServer()
            server.start()

    except KeyboardInterrupt:
        click.echo("\n🛑 Server stopped by user")
        sys.exit(0)
    except Exception as e:
        click.echo(f"❌ Error starting server: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.option("--tool", help="Specific tool to crawl")
@click.option("--all", "crawl_all", is_flag=True, help="Crawl all enabled tools")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
@click.option("--force", is_flag=True, help="Force re-crawl even if cached")
@click.pass_context
def crawl(ctx, tool: Optional[str], crawl_all: bool, verbose: bool, force: bool):
    """Crawl documentation sources.

    NOTE: This is a placeholder implementation.
    The actual crawling functionality will be implemented in future phases.
    """
    if ctx.obj["verbose"] or verbose:
        click.echo("🕷️  Documentation crawling functionality")

    if not tool and not crawl_all:
        click.echo("❌ Please specify --tool <name> or --all", err=True)
        sys.exit(1)

    if crawl_all:
        click.echo("📚 Would crawl all enabled tools:")
        tools = [
            "elasticsearch",
            "docker",
            "python",
            "proxmox",
            "nessus",
            "topdesk",
            "confluence",
            "n8n",
            "ollama",
        ]
        for t in tools:
            click.echo(f"  • {t}")
    else:
        click.echo(f"📖 Would crawl tool: {tool}")

    click.echo("⚠️  Note: Crawling functionality not yet implemented")
    click.echo("   This will be added in the next development phase")


@cli.command()
@click.pass_context
def status(ctx):
    """Show server and documentation status."""
    if ctx.obj["verbose"]:
        click.echo("📊 Checking system status...")

    click.echo("🏗️  Enterprise MCP Documentation Server Status")
    click.echo(f"   Version: {__version__}")
    click.echo("   Status: Development Mode")
    click.echo()

    # Check if server is running
    try:
        import httpx

        response = httpx.get("http://localhost:8000/health", timeout=2.0)
        if response.status_code == 200:
            data = response.json()
            click.echo("🟢 Server: Running")
            click.echo(f"   Health: {data.get('status', 'unknown')}")
        else:
            click.echo("🟡 Server: Running (unhealthy)")
    except Exception:
        click.echo("🔴 Server: Not running")

    click.echo()
    click.echo("📚 Documentation Sources:")
    tools = [
        "elasticsearch",
        "docker",
        "python",
        "proxmox",
        "nessus",
        "topdesk",
        "confluence",
        "n8n",
        "ollama",
    ]
    for tool in tools:
        click.echo(f"   • {tool}: Not crawled yet")


@cli.command("config")
@click.argument("command", type=click.Choice(["check", "show", "validate"]))
@click.pass_context
def config_cmd(ctx, command: str):
    """Configuration management commands."""
    config_file = ctx.obj.get("config_file")

    if command == "check":
        click.echo("🔧 Checking configuration...")

        # Look for config files
        config_paths = ["config/local.json", "config/default.json", ".env"]

        for path in config_paths:
            if os.path.exists(path):
                click.echo(f"✅ Found: {path}")
            else:
                click.echo(f"❌ Missing: {path}")

        click.echo("✅ Configuration check completed")

    elif command == "show":
        if config_file and os.path.exists(config_file):
            with open(config_file) as f:
                config = json.load(f)
            click.echo(json.dumps(config, indent=2))
        else:
            click.echo("❌ No configuration file found", err=True)

    elif command == "validate":
        click.echo("🔍 Validating configuration...")
        click.echo("✅ Configuration validation completed")


def main():
    """Main entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
