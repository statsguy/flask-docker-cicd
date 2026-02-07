#!/usr/bin/env bash
# Build the app image and run it via compose (same port as dev: http://localhost:5001).
set -e
cd "$(dirname "$0")/.."
docker build -t flask-docker-cicd:app ./app
echo "Starting Flask app at http://localhost:5001 (Ctrl+C to stop)"
docker compose -f docker-compose.app-only.yml up
