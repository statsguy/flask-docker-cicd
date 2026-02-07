FROM python:3.11-slim AS base

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app.py .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]

# Test stage (for CI)
FROM base AS test
USER root
RUN pip install --no-cache-dir pytest pytest-cov flake8
COPY test_app.py .
USER appuser
CMD ["pytest", "-v", "--cov=app", "--cov-report=term-missing", "--cov-report=xml:/app/coverage.xml", "--cov-report=html:/app/htmlcov"]
