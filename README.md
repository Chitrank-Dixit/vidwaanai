# VidwaanAI - MVP

A multilingual AI agent for Indian scriptures with CLI interface.

## Quick Start

### 1. Prerequisites
- Docker & Docker Compose
- Python 3.10+
- OpenAI API key

### 2. System Dependencies (OCR Support)
To ingest scanned PDFs (like Mahabharat), you need `tesseract` and `poppler`.

**macOS:**
```bash
brew install tesseract poppler
```

**Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr poppler-utils
```

### 3. Setup Environment
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### 3. Start Database
```bash
docker-compose up -d
sleep 10  # Wait for initialization
```

### 4. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 5. Download Embedding Model (first run only)
```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('krutrim-ai-labs/vyakyarth')"
```

### 6. Initialize Database
```bash
python scripts/setup_db.py
```

### 7. Load Sample Data
```bash
python scripts/load_sample_data.py
```

### 8. Run VidwaanAI!
```bash
# English query
python -m src.main query "Who is Krishna?"

# Hindi query
python -m src.main query "कृष्ण कौन हैं?" --language hi

# With verbose output
python -m src.main query "What is karma?" --verbose

# List scriptures
python -m src.main list-scriptures

# Show settings
python -m src.main settings show

# Check system status
python -m src.main system status
```

## CLI Commands

| Command | Description |
|---------|-------------|
| `query "text"` | Query about scriptures |
| `query "text" -l hi` | Query in Hindi |
| `query "text" -s "Bhagavad Gita"` | Query specific scripture |
| `query "text" -v` | Verbose output with retrieved verses |
| `list-scriptures` | Show loaded scriptures |
| `settings show` | Show current settings |
| `system status` | Check system health |

## MCP Server (Agent Integration)

VidwaanAI now supports the **Model Context Protocol (MCP)**, allowing AI agents (like Claude) to autonomously discover and use its tools.

### Features
- **Language Tools**: `detect_language`, `preprocess_text`
- **Search Tools**: `search_documents`, `hybrid_search`
- **RAG Pipeline**: `execute_rag_pipeline`
- **Knowledge Graph**: `query_knowledge_graph`

### Quick Start (Docker)

```bash
# Start MCP Server
make -f Makefile-docker mcp-up

# Check Health
curl http://localhost:3000/health

# Run Tests
make -f Makefile-docker mcp-test
```

For detailed instructions, see [HOW-TO-RUN-MCP](HOW-TO-RUN-MCP).

## Ansible Automation

VidwaanAI includes Ansible playbooks to automate setup, testing, and quality assurance workflows.

### Prerequisites
- Ansible installed (`brew install ansible` on macOS)
- Docker running

### Available Workflows

#### 1. Full Workflow
Runs the complete CI/CD-like pipeline: builds images, starts services, initializes DB, runs all tests, and generates reports.

```bash
bash scripts/run_ansible_workflow.sh full_workflow.yml
```

#### 2. Quick Workflow
Runs tests and generates a report (assumes environment is already running).

```bash
bash scripts/run_ansible_workflow.sh quick_workflow.yml
```

#### 3. Ingestion Options (Incremental vs Force)
By default, the workflow is **incremental**—it skips files listed in `data/processed_files.txt`.
To force re-ingestion of all content, pass `force_ingestion=true` as an extra variable (3rd argument):

```bash
# bash scripts/run_ansible_workflow.sh [playbook] [tags] [extra_vars]
bash scripts/run_ansible_workflow.sh full_workflow.yml "" "force_ingestion=true"
```



#### 4. Granular Workflow Controls
You can run specific steps of the workflow using **tags** (2nd argument). This is useful for large datasets where you want to separate ingestion, vectorization, and graph building.

| Step | Tag | Command |
|------|-----|---------|
| **Ingestion Only** | `ingest_files` | `bash scripts/run_ansible_workflow.sh full_workflow.yml ingest_files` |
| **Vectorization Only** | `vectorize` | `bash scripts/run_ansible_workflow.sh full_workflow.yml vectorize` |
| **Knowledge Graph Only** | `build_graph` | `bash scripts/run_ansible_workflow.sh full_workflow.yml build_graph` |
| **Ingestion + Force** | `ingest_files` | `bash scripts/run_ansible_workflow.sh full_workflow.yml ingest_files "force_ingestion=true"` |

#### 5. Modular Workflows
For better control, you can run the ingestion/vectorization and graph building steps independently using the dedicated playbooks. This uses `uv` to run `ansible-playbook` ensuring all dependencies are met.

**Ingest and Vectorize Only:**
```bash
uv run ansible-playbook ansible/playbooks/ingest_and_vectorize_workflow.yml
```

**Build Knowledge Graph Only:**
```bash
uv run ansible-playbook ansible/playbooks/building_graph_workflow.yml
```

#### 6. Ontology Manual Workflow (Multi-LLM)
This workflow manages the creation of the **Vedic Ontology** using a human-in-the-loop process with multiple LLMs.

**Why Use This?**
-   **Precision**: Automated extraction often misses nuanced Vedic concepts or relationships. Manual verification with powerful LLMs (like GPT-4, Claude 3) ensures high accuracy.
-   **Control**: Allows you to focus on specific scriptures (e.g., *Ramayan*) one at a time.
-   **Integration**: Seamlessly bridges the gap between your raw queries and the Neo4j Knowledge Graph.

**Step 1: Generate Prompts**
Verifies that query batch files are ready and provides instructions for manual execution.
```bash
# Generate prompts from 20 random verses
bash scripts/run_ansible_workflow.sh ontology --step generate

# Generate prompts specifically for "Ramayan" verses
bash scripts/run_ansible_workflow.sh ontology --step generate --scripture "Ramayan"
```

**Step 2: Deploy (After Manual Querying)**
Once you have saved the JSON responses from Perplexity/Gemini/ChatGPT to `scripts/responses/`, run this step to aggregate, convert, and deploy the ontology to Neo4j.
```bash
bash scripts/run_ansible_workflow.sh ontology --step deploy
```

### Directory Structure
- `ansible/playbooks/`: Workflow definitions
- `ansible/roles/`: Individual task roles (docker_setup, docker_testing, etc.)
- `ansible/group_vars/`: Global variables (docker_hosts.yml)

## Supported Languages
- English (en)
- Hindi (hi)
- Tamil (ta)
- Telugu (te)
- Malayalam (ml)
- Kannada (kn)
- Sanskrit (sa)

## Architecture
- **CLI Framework**: Typer
- **RAG Framework**: LlamaIndex
- **Embeddings**: Vyakyarth (98.7-99.9% accuracy)
- **Vector DB**: PostgreSQL + pgvector
- **LLM**: OpenAI gpt-4-turbo

## Troubleshooting

### Database Connection Error
```bash
# Check if running
docker-compose ps

# Restart
docker-compose down
docker-compose up -d
```

### Port Already in Use
Edit `docker-compose.yml` and change `5432:5432` to `5433:5432`

### OpenAI API Error
Verify your API key in `.env` file

## Project Structure

```
.
├── src/                    # Source code
│   ├── main.py            # CLI entry point
│   ├── core/              # Configuration & logging
│   ├── agent/             # VidwaanAI agent logic
│   ├── rag/               # Embeddings & retrieval
│   ├── llm/               # LLM integration
│   └── db/                # Database operations
├── database/              # Database schemas
├── scripts/               # Setup & utility scripts
├── docker-compose.yml     # Database setup
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Next Steps

1. Customize scripture data in `data/scriptures/`
2. Fine-tune retrieval in `src/rag/`
3. Improve prompts in `src/agent/prompt_templates.py`
4. Add web UI in Phase 2
5. Deploy with Docker

## License

MIT License


## Knowledge Graph System (Implemented)

VidwaanAI now features a comprehensive **Semantic Knowledge Graph** that powers advanced reasoning and hybrid RAG.

### 🌟 Features
- **Vedic Ontology**: A structured taxonomy of Deities, Concepts, Characters, and Locations (defined in `src/graph/ontology.py`).
- **Hybrid Extraction**: Combines rule-based taxonomy extraction with LLM-based relation extraction.
- **Graph Reasoning**: Supports multi-hop traversals, shortest path finding, and hierarchy resolution.
- **Graph RAG**: Fuses vector similarity with graph context for richer answers.

### 🚀 Usage

#### 1. Setup Graph Database
```bash
# Start Neo4j Service
make graph-setup

# Seed the Static Ontology (Deities, Concepts)
uv run python scripts/seed_ontology.py
# Output: Seeding Complete. Created entities like Vishnu, Dharma, etc.
```

#### 2. Build the Graph
Ingest verses and extract relationships (links verses to the ontology).
```bash
# Process a sample (recommended for testing)
uv run python scripts/build_knowledge_graph.py --limit 10

# Process all verses (Long running operation)
uv run python scripts/build_knowledge_graph.py
```

**Checkpointing & Resume:**
The build script automatically maintains a checkpoint file (`graph_build.checkpoint`).
-   **Interrupted?** Run the command again to resume from the last processed batch.
-   **Fresh Start?** Use `--clear` to wipe the graph and the checkpoint.


#### 3. Verify Graph
Check the status of nodes and relationships.
```bash
# Basic Verification (Counts of nodes/relationships)
uv run python scripts/verify_graph.py

# Detailed Ontology Verification (Checks isolation, specific relations)
uv run python scripts/verify_ontology.py
```

#### 4. Step-by-Step Ontology Verification Process
To manually verify that the ontology is correctly applied and relationships exist:

1.  **Check Connection**: Ensure Neo4j is running.
2.  **Run Verification Script**:
    ```bash
    uv run python scripts/verify_ontology.py
    ```
    *Expected Output*:
    -   Graphs Totals: Nodes > 0, Relationships > 0.
    -   TEXT -> MENTIONS -> CONCEPT: Should show explicit links (e.g., `Verse ... --[MENTIONS]-> Dharma`).
    -   Isolated Nodes: Should be 0 (or very low).
    -   Internal Relations: Concepts should link to other concepts (e.g., `Rama --[MANIFESTS_AS]-> Vishnu`).

3.  **Manual Cypher Checks**:
    Open Neo4j Browser (http://localhost:7474) and run:

    *Check Text-Concept Links:*
    ```cypher
    MATCH (t:Text)-[r:MENTIONS]->(c:Concept) RETURN t.name, c.name LIMIT 20
    ```

    *Check Concept Hierarchy:*
    ```cypher
    MATCH (c1:Concept)-[r]->(c2:Concept) RETURN c1.name, type(r), c2.name LIMIT 20
    ```

#### 5. API Endpoints
The Graph Reasoning Service is exposed via REST APIs.

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/kg/search/entities?q=Name` | Fuzzy search for entities |
| `GET` | `/api/kg/entity/{id}` | Get entity details & 1-hop subgraph |
| `GET` | `/api/kg/path/{start}/{end}` | Find shortest path between entities |
| `POST` | `/api/kg/reason` | Multi-hop reasoning (e.g., "What does this lead to?") |
| `GET` | `/api/kg/hierarchy/{id}` | Get parent/child hierarchy (IS_A relations) |

**Example Reasoning Request:**
```json
POST /api/kg/reason
{
  "entity_id": "concept:dharma",
  "hops": 2
}
```

### 🧠 Architecture

**Hybrid RAG Pipeline**:
1. **Query**: User asks "How is Krishna related to Dharma?"
2. **Extraction**: Identify entities "Krishna" and "Dharma".
3. **Retrieval**:
    - **Vector**: Fetch semantically similar verses.
    - **Graph**: Fetch direct relationships and paths between Krishna and Dharma.
4. **Reasoning**: The `GraphReasoningService` traverses the graph to find implied connections.
5. **Synthesis**: LLM generates answer using both Verse text and Graph structure.


## Agent API (REST Service)

The Vidwaan Agent is now exposed as a REST API for backend integration.

### Quick Start
Start the API server on port 8001:

```bash
uv run uvicorn src.api.main:app --host 0.0.0.0 --port 8001 --reload
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/agent/query` | Submit natural language query to the agent |
| `GET` | `/api/v1/agent/health` | Check service health |
| `POST` | `/api/v1/agent/session/create` | Create a new conversation session |

### Usage Examples

#### 1. Check Health
```bash
curl http://localhost:8001/api/v1/agent/health
# {"status": "healthy", ...}
```

#### 2. Query the Agent (RAG)
```bash
curl -X POST http://localhost:8001/api/v1/agent/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is the concept of Dharma?",
    "session_id": "test-session-1"
  }'
```

**Response:**
```json
{
  "answer": "Dharma is the cosmic law referencing...",
  "confidence": 0.95,
  "sources": [
    {
      "id": "100",
      "title": "Rig Ved",
      "content": "..."
    }
  ],
  "retrieval_context": ["..."],
  "reasoning_trace": []
}
```

### Evaluation Pipeline (New)
We use **DeepEval** to measure RAG quality (Faithfulness, Relevancy).

```bash
# Run Evaluation
make -f Makefile-docker mcp-run-eval
```

For interactive documentation, visit **[http://localhost:8001/docs](http://localhost:8001/docs)** after starting the server.


## Local Makefile Commands

This project uses a `Makefile` to streamline common development tasks. Below are some key commands for local development:

### Setup
- `make setup`: Install Python dependencies and create necessary directories.
- `make setup-dev`: Install all dependencies, including development tools.

### Testing
- `make test-setup`: Prepares the test environment by starting Docker services (Postgres, Neo4j), initializing the database, and loading sample data. This ensures a clean and consistent state for your tests.
- `make test`: Runs the main test suite. This command automatically calls `make test-setup` first.
- `make test-verbose`: Runs the test suite with verbose output. Also automatically calls `make test-setup`.
- `make test-cleanup`: Stops the Docker services and removes their data volumes, ensuring a clean slate after testing.
- `make test-all`: Executes the complete testing workflow: sets up the environment, runs all tests, and then cleans up the environment. This is the recommended command for a full test cycle.

### Code Quality
- `make lint`: Run code linting using `ruff`.
- `make format`: Format code using `ruff`.
- `make check`: Run type checks using `pyright`.
- `make test-code`: Run unit tests on the framework.

### Workflows
- `make workflow`: Runs the full development workflow: generates prompts, validates them, runs tests, analyzes results, and generates a report.
- `make workflow-quick`: A quicker workflow for development: runs a dry run, analyzes results, and generates a report.
- `make workflow-dev`: A development workflow: generates prompts, validates them, and runs a dry run.

### Information
- `make help`: Display all available commands and their descriptions.
- `make show-languages`: List all supported languages.
- `make show-categories`: List all test categories.
- `make show-config`: Show the current configuration settings.

### Cleanup
- `make clean`: Remove temporary result and log files, but keeps generated prompts.
- `make clean-cache`: Clear Python cache directories.
- `make clean-all`: Remove all generated files, including prompts, and temporary files.
## Docker Makefile Commands

This project also provides a `Makefile-docker` for managing containerized development and testing workflows. This is particularly useful for ensuring a consistent environment and isolating dependencies.

### Quick Start (Docker)
- `make -f Makefile-docker docker-build`: Build all Docker containers.
- `make -f Makefile-docker docker-up`: Start all Docker services in detached mode.
- `make -f Makefile-docker docker-first-run`: Initialize the database and load sample data within the Docker environment.
- `make -f Makefile-docker docker-test`: Run the full test suite within Docker.
- `make -f Makefile-docker docker-analyze` and `make -f Makefile-docker docker-report`: Analyze test results and generate a comprehensive report.

### Lifecycle
- `make -f Makefile-docker docker-build`: Build all Docker containers.
- `make -f Makefile-docker docker-up`: Start all Docker services in detached mode.
- `make -f Makefile-docker docker-down`: Stop all Docker services.
- `make -f Makefile-docker docker-logs`: View logs from all services.
- `make -f Makefile-docker docker-shell`: Open a shell in the 'app' container.

### Setup
- `make -f Makefile-docker docker-first-run`: Initialize DB and load data.
- `make -f Makefile-docker docker-reset-data`: **CAUTION** Clears ALL data from Postgres and Neo4j.

### Generate & Test
- `make -f Makefile-docker docker-generate`: Generate prompts inside Docker.
- `make -f Makefile-docker docker-test-all`: Run the full test suite inside Docker.
- `make -f Makefile-docker docker-test-lang L=<lang_code>`: Test a specific language (e.g., `L=hi`).
- `make -f Makefile-docker docker-test-category C=<category_name>`: Test a specific category (e.g., `C=ramayana`).

### Custom Single Scripture Workflow

To ingest, vectorize, and build graph for a **single** scripture (instead of everything), use the custom workflow:

```bash
# Example: Ingesting a new PDF using the simplified script
bash scripts/run_ansible_workflow.sh custom \
  --name "Garuda Purana" \
  --code "garuda" \
  --type "purana" \
  --pdf "data/puranas/garuda_purana.pdf" \
  --force
```

Arguments:
- `--name`: Full name of the scripture (e.g. "Garuda Purana").
- `--code`: Short code (e.g. "garuda").
- `--type`: one of `veda`, `gita`, `ramayana`, `mahabharat`, `purana`.
- `--pdf`: Path to the PDF file relative to project root.
- `--force`: Optional flag to force re-ingest if already processed.

### Analysis & Report
- `make -f Makefile-docker docker-analyze`: Analyze test results.
- `make -f Makefile-docker docker-report`: Generate comprehensive report.

### Workflows
- `make -f Makefile-docker docker-workflow`: Full workflow: generate → test → report.
- `make -f Makefile-f Makefile-docker docker-workflow-quick`: Quick workflow version.

### Knowledge Graph
- `make -f Makefile-docker docker-graph-build`: Build knowledge graph (incremental).
- `make -f Makefile-docker docker-graph-rebuild`: Rebuild knowledge graph from scratch (Clear DB + Seed Ontology + Build).

### Testing
- `make -f Makefile-docker docker-test-unit`: Run unit tests.
- `make -f Makefile-docker docker-test-functional`: Run functional tests.
- `make -f Makefile-docker docker-test-integration`: Run integration tests.
- `make -f Makefile-docker docker-test-e2e`: Run E2E tests.
- `make -f Makefile-docker docker-test-all`: Run all tests.
- `make -f Makefile-docker docker-test-cleanup`: Clean up the test environment.

### Documentation
- `make -f Makefile-docker docker-docs`: Build HTML documentation using Sphinx.

### Quality Assurance
- `make -f Makefile-docker docker-lint`: Lint code.
- `make -f Makefile-docker docker-format`: Format code.
- `make -f Makefile-docker docker-check`: Type check.
- `make -f Makefile-docker docker-security`: Security checks.
- `make -f Makefile-docker docker-lint-all`: Run all QA checks.

### Caching
- `make -f Makefile-docker docker-cache-status`: Show cache status.
- `make -f Makefile-docker docker-cache-clear`: Clear caches.
- `make -f Makefile-docker docker-cache-prune`: Prune Docker volumes.
- `make -f Makefile-docker docker-clean-all`: Full cleanup.

### Data Backup
To backup specific components of your data:

**1. Ingestion Only (Text & Metadata):**
```bash
bash scripts/backup_ingestion.sh
```

**2. Vectorization Only (Embeddings):**
```bash
bash scripts/backup_vectorization.sh
```

**3. Knowledge Graph Only (Neo4j):**
```bash
bash scripts/backup_graph.sh
```
*Note: The graph backup script momentarily stops the Neo4j service.*

### MCP Server
- `make -f Makefile-docker mcp-build`: Build MCP containers.
- `make -f Makefile-docker mcp-up`: Start MCP services.
- `make -f Makefile-docker mcp-down`: Stop MCP services.
- `make -f Makefile-docker mcp-logs`: View logs.
- `make -f Makefile-docker mcp-test`: Run MCP unit tests.
- `make -f Makefile-docker mcp-int`: Run MCP integration tests.
- `make -f Makefile-docker mcp-run-eval`: Run RAG evaluation pipeline.

### Agent API
- `make -f Makefile-docker agent-build`: Build Agent API container.
- `make -f Makefile-docker agent-up`: Start Agent API service.
- `make -f Makefile-docker agent-down`: Stop Agent API service.
- `make -f Makefile-docker agent-logs`: View Agent API logs.