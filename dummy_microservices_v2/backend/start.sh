#!/bin/bash
set -e

# Start Nginx in the background
nginx

# Start Uvicorn for FastAPI app
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 