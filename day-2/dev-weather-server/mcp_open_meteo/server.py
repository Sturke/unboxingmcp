#!/usr/bin/env python3
"""
Open-Meteo Weather MCP Server

A weather server that uses Open-Meteo APIs for weather forecasting using coordinates.
This example demonstrates clean MCP server development.
"""

import sys
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# Support both package imports and direct execution
try:
    from .tools import register_tools
    from .resources import register_resources
except ImportError:
    # When run directly (e.g., uv run mcp dev mcp_open_meteo/server.py)
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from mcp_open_meteo.tools import register_tools
    from mcp_open_meteo.resources import register_resources

# Create the MCP server
mcp = FastMCP("Open-Meteo Weather")

# Register tools and resources
register_tools(mcp)
register_resources(mcp)


def main():
    """Main entry point for the MCP server"""
    mcp.run()


if __name__ == "__main__":
    main()
