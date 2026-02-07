#!/usr/bin/env bash
# Build the test image and run it locally (runs pytest with coverage).
set -e
cd "$(dirname "$0")/.."
docker build --target test -t flask-docker-cicd:test ./app
docker run --rm flask-docker-cicd:test
