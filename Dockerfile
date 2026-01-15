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
    tesseract-ocr \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m appuser

# Create cache directories and set permissions
RUN mkdir -p /home/appuser/.cache/huggingface \
    && mkdir -p /home/appuser/.cache/torch \
    && mkdir -p /home/appuser/.cache/uv \
    && mkdir -p /app/models \
    && chown -R appuser:appuser /home/appuser/.cache \
    && chown -R appuser:appuser /app

# Set environment variables for model caching
ENV HF_HOME=/home/appuser/.cache/huggingface
ENV TORCH_HOME=/home/appuser/.cache/torch
ENV SENTENCE_TRANSFORMERS_HOME=/home/appuser/.cache/huggingface/sentence-transformers
ENV PYTHONWARNINGS="ignore:Using `TRANSFORMERS_CACHE` is deprecated"

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
COPY database/ database/
COPY .env.example .env

# Create non-root user
# Fix permissions for app directory (including venv created by uv sync)
RUN chown -R appuser:appuser /app

USER appuser

# Entrypoint
ENTRYPOINT ["uv", "run", "vidwaan"]
CMD ["--help"]
