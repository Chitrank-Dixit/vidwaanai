# VidwaanAI Quick Start Guide

## Prerequisites
- **Python 3.13+**
- **uv** (Dependency Manager): `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **Docker** & **Docker Compose**

## Installation

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd vidwaan-ai-mvp
   ```

2. **Install dependencies**
   ```bash
   make install-dev
   ```

3. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys (OpenAI, Neo4j, etc.)
   ```

## First Run

Initialize the database and load sample data:
```bash
make first-run
```

## Usage

**Query the agent:**
```bash
make query Q="What is dharma?"
```

**Run tests:**
```bash
make test
```

## Graph RAG (Phase 2)

1. **Start Neo4j:**
   ```bash
   make graph-setup
   ```

2. **Build Knowledge Graph:**
   ```bash
   make graph-build
   ```

3. **Enable Graph RAG:**
   Set `ENABLE_GRAPH_RAG=true` in `.env`.

4. **Query with Graph Context:**
   ```bash
   make query Q="How is Krishna related to Arjuna?"
   ```

## Development

- **Format code:** `make format`
- **Lint code:** `make lint`
- **Type check:** `make check`
- **Clean artifacts:** `make clean`
