#!/usr/bin/env bash
# Run the full dev stack (web, db, redis, adminer) for local testing.
set -e
cd "$(dirname "$0")/.."

if [[ ! -f .env ]]; then
  echo "No .env found. Copying .env.example to .env"
  cp .env.example .env
fi

echo "Starting full stack (Flask, Postgres, Redis, Adminer)..."
echo "  - Flask:    http://localhost:5001"
echo "  - Health:   http://localhost:5001/health"
echo "  - Adminer:  http://localhost:8080"
echo "Ctrl+C to stop"
echo ""
docker compose up --build
