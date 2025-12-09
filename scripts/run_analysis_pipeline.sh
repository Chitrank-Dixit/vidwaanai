#!/bin/bash
set -e

echo "=== STARTING ANALYSIS PIPELINE ==="

echo "[1/4] Resetting Database..."
uv run python scripts/reset_data.py

echo "[2/4] Loading Sample Data..."
uv run python scripts/load_sample_data.py

echo "[3/4] Verifying Data Presence..."
uv run python scripts/debug_verses.py

echo "[4/4] Running Evaluation..."
uv run python scripts/evaluate_retrieval.py

echo "=== PIPELINE COMPLETE ==="
