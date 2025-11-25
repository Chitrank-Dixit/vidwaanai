# Use Python 3.13 slim image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_SYSTEM_PYTHON=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set working directory
WORKDIR /app

# Copy project configuration
COPY pyproject.toml .
# COPY uv.lock .  # Uncomment when lock file exists

# Install dependencies
RUN uv sync --frozen --no-dev || uv sync --no-dev

# Copy source code
COPY src/ src/
COPY scripts/ scripts/
COPY tests/ tests/
COPY .env.example .env

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Entrypoint
ENTRYPOINT ["uv", "run", "vidwaan"]
CMD ["--help"]
