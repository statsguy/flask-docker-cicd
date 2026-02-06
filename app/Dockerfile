FROM python:3.11-slim AS base

WORKDIR /app

# Install dependencies
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
RUN pip install --no-cache-dir pytest
COPY test_app.py .
USER appuser
CMD ["pytest", "-v"]
