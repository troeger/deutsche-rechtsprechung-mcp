#!/bin/bash
# Wait for OpenSearch to be fully ready is handled in ingest.py, 
# but we can also add a simple sleep or netcat check here if needed.
# ingest.py has a retry loop.

echo "Running Ingestion..."
python src/ingest.py

echo "Starting MCP Server..."
python src/server.py
