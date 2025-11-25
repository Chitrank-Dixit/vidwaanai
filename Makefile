# VidwaanAI Makefile
# Powered by uv for fast dependency management

.PHONY: help install install-dev dev test test-verbose format lint check clean db-up db-down db-reset graph-setup graph-build query

# Colors
BOLD := \033[1m
GREEN := \033[32m
YELLOW := \033[33m
CYAN := \033[36m
RED := \033[31m
RESET := \033[0m

# Python
PYTHON := uv run python
PYTEST := uv run pytest
RUFF := uv run ruff
BLACK := uv run black
MYPY := uv run mypy

help:
	@echo "$(BOLD)VidwaanAI Development Commands$(RESET)"
	@echo
	@echo "$(CYAN)Setup:$(RESET)"
	@echo "  $(GREEN)make install$(RESET)       Install dependencies"
	@echo "  $(GREEN)make install-dev$(RESET)   Install dependencies (including dev)"
	@echo "  $(GREEN)make first-run$(RESET)     Complete first-time setup"
	@echo
	@echo "$(CYAN)Development:$(RESET)"
	@echo "  $(GREEN)make dev$(RESET)           Run development server (not implemented yet)"
	@echo "  $(GREEN)make format$(RESET)        Format code with black and ruff"
	@echo "  $(GREEN)make lint$(RESET)          Lint code with ruff"
	@echo "  $(GREEN)make check$(RESET)         Run type checks with mypy"
	@echo
	@echo "$(CYAN)Testing:$(RESET)"
	@echo "  $(GREEN)make test$(RESET)          Run tests"
	@echo "  $(GREEN)make test-verbose$(RESET)  Run tests with verbose output"
	@echo
	@echo "$(CYAN)Infrastructure:$(RESET)"
	@echo "  $(GREEN)make docker$(RESET)        Start Docker services (Postgres + Neo4j)"
	@echo "  $(GREEN)make docker-down$(RESET)   Stop Docker services"
	@echo "  $(GREEN)make db$(RESET)            Initialize database schema"
	@echo "  $(GREEN)make model$(RESET)         Download/setup embedding model (if local)"
	@echo "  $(GREEN)make data$(RESET)          Load sample data"
	@echo
	@echo "$(CYAN)Graph RAG (Phase 2):$(RESET)"
	@echo "  $(GREEN)make graph-setup$(RESET)   Start Neo4j service"
	@echo "  $(GREEN)make graph-build$(RESET)   Build knowledge graph from verses"
	@echo
	@echo "$(CYAN)Usage:$(RESET)"
	@echo "  $(GREEN)make query Q=\"...\"$(RESET) Run a query"

# --- Setup ---

install:
	@echo "$(YELLOW)Installing dependencies with uv...$(RESET)"
	@uv sync --no-dev

install-dev:
	@echo "$(YELLOW)Installing dev dependencies with uv...$(RESET)"
	@uv sync

first-run: install-dev docker db model data
	@echo "$(GREEN)✓ Setup complete! Try: make query Q=\"What is dharma?\"$(RESET)"

# --- Development ---

format:
	@echo "$(YELLOW)Formatting code...$(RESET)"
	@$(BLACK) src tests scripts
	@$(RUFF) check --fix src tests scripts

lint:
	@echo "$(YELLOW)Linting code...$(RESET)"
	@$(RUFF) check src tests scripts

check:
	@echo "$(YELLOW)Running type checks...$(RESET)"
	@$(MYPY) src

# --- Testing ---

test:
	@echo "$(YELLOW)Running tests...$(RESET)"
	@$(PYTEST)

test-verbose:
	@echo "$(YELLOW)Running tests (verbose)...$(RESET)"
	@$(PYTEST) -v -s

# --- Infrastructure ---

docker:
	@echo "$(YELLOW)Starting Docker services...$(RESET)"
	@docker-compose up -d

docker-down:
	@echo "$(YELLOW)Stopping Docker services...$(RESET)"
	@docker-compose down

db:
	@echo "$(YELLOW)Initializing database...$(RESET)"
	@$(PYTHON) scripts/init_db.py

model:
	@echo "$(YELLOW)Setting up models...$(RESET)"
	# Add model download script if needed
	@echo "Model setup skipped (using API or pre-downloaded)"

data:
	@echo "$(YELLOW)Loading sample data...$(RESET)"
	@$(PYTHON) scripts/load_sample_data.py

# --- Graph RAG ---

graph-setup:
	@echo "$(YELLOW)Starting Neo4j...$(RESET)"
	@docker-compose up -d neo4j
	@echo "$(GREEN)Neo4j started on http://localhost:7474$(RESET)"

graph-build:
	@echo "$(YELLOW)Building knowledge graph...$(RESET)"
	@$(PYTHON) scripts/build_knowledge_graph.py

# --- Usage ---

query:
	@if [ -z "$(Q)" ]; then \
		echo "$(RED)Error: Please provide a question using Q=\"...\"$(RESET)"; \
	else \
		$(PYTHON) src/main.py query "$(Q)" --verbose; \
	fi
