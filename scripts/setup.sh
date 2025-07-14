#!/bin/bash

# Enterprise MCP Documentation Server Setup Script
# Quick setup for development and testing

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_header() {
    echo -e "${BLUE}"
    echo "=================================================="
    echo "  Enterprise MCP Documentation Server Setup"
    echo "=================================================="
    echo -e "${NC}"
}

# Main setup function
main() {
    print_header
    print_info "Starting Docker environment setup..."

    # Create necessary directories
    print_info "Creating application directories..."
    mkdir -p /app/data /app/logs /app/cache /app/vector_store
    print_success "Created data directories"

    # Set proper permissions
    if [ "$(id -u)" = "0" ]; then
        chown -R mcpuser:mcp /app/data /app/logs /app/cache /app/vector_store 2>/dev/null || true
        print_info "Set directory permissions"
    fi

    # Check if Redis is available
    print_info "Checking Redis connectivity..."
    if command -v redis-cli &> /dev/null; then
        if redis-cli ping >/dev/null 2>&1; then
            print_success "Redis is available and responding"
        else
            print_warning "Redis not responding, but that's OK for Docker setup"
        fi
    else
        print_info "Redis CLI not available, but that's OK for Docker setup"
    fi

    # Environment check
    print_info "Environment: ${ENVIRONMENT:-development}"
    print_info "Log level: ${LOG_LEVEL:-INFO}"
    print_info "Redis URL: ${REDIS_URL:-not configured}"

    print_success "Docker setup completed successfully!"
    print_info "Ready to start the MCP server"
    print_info ""
    print_info "Next steps:"
    print_info "  - Check logs with: docker compose logs -f mcp-server"
    print_info "  - Stop with: docker compose down"
    print_info "  - Rebuild with: docker compose up -d --build"
}

# Run main function
main "$@"
