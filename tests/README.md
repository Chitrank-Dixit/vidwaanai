# Vidwaan AI Language Test Suite

Comprehensive framework for benchmarking Vidwaan AI across 17 languages.

## Overview

This suite tests:
- **Languages**: 17 (Core, Regional, Dialects)
- **Categories**: Ramayana, Bhagavad Gita, Mahabharata, Hinduism
- **Metrics**: Keyword precision/recall, F1 score, Language detection accuracy

## Directory Structure

- `prompt_suite/`: JSON files containing prompts for each language.
- `results/`: Output JSON files with test results and summary statistics.
- `metrics/`: CSVs and other metric data.
- `logs/`: Execution logs.

## Quick Start

### 1. Generate Prompts
If the prompt files are missing or need updating:
```bash
python scripts/generate_prompts.py
```

### 2. Run Tests
Run the full suite (mock mode by default):
```bash
python tests/test_runner.py
```

Run specific languages:
```bash
python tests/test_runner.py --languages en hi
```

Run specific categories:
```bash
python tests/test_runner.py --categories ramayana
```

### 3. View Results
Check `tests/results/results_summary.json` for aggregated metrics.
Detailed logs are in `logs/test_execution.log`.

## Configuration
Edit `config/test_config.json` to adjust batch size, timeouts, and other settings.
