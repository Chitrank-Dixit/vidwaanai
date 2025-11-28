# VidwaanAI Docker Quick Start

## Prerequisites
- **Docker** & **Docker Compose**
- **Make** (optional, but recommended)

## Setup

1. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

2. **First Run** (Builds images, starts services, inits DB, loads data)
   ```bash
   make -f Makefile-docker first-run
   ```

## Daily Usage

**Start Services:**
```bash
make -f Makefile-docker up
```

**Run Query:**
```bash
make -f Makefile-docker query Q="What is dharma?"
```

**Stop Services:**
```bash
make -f Makefile-docker down
```

## Graph RAG (Phase 2)

1. **Build Knowledge Graph:**
   ```bash
   make -f Makefile-docker graph-build
   ```

2. **Enable Graph RAG:**
   Set `ENABLE_GRAPH_RAG=true` in `.env` and restart:
   ```bash
   make -f Makefile-docker up
   ```

3. **Query:**
   ```bash
   make -f Makefile-docker query Q="How is Krishna related to Arjuna?"
   ```

## Troubleshooting

**View Logs:**
```bash
make -f Makefile-docker logs
```

**Open Shell:**
```bash
make -f Makefile-docker shell
```

**Rebuild Containers:**
```bash
make -f Makefile-docker build
```
