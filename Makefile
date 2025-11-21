# Makefile for VidwaanAI (LM Studio + Vyakyarth + flexible everything)

# Environment
PYTHON ?= python
SRC ?= src
REQ ?= requirements.txt
REQ_FLEX ?= requirements-flexible.txt
EMBED_MODEL ?= krutrim-ai-labs/Vyakyarth

.PHONY: help all flexible-req venv install clean cleanall db docker model embeddings data test

help:
	@echo ""
	@echo "VidwaanAI Project Automation"
	@echo "make all         # Full clean install and setup pipeline"
	@echo "make venv        # Create virtualenv"
	@echo "make install     # Install/upgrade Python requirements"
	@echo "make docker      # Start database in Docker"
	@echo "make db          # Initialize database tables"
	@echo "make model       # Download Vyakyarth embedding model"
	@echo "make data        # Load scripture sample data"
	@echo "make test        # Run basic test query"
	@echo "make clean       # Remove venv"
	@echo "make cleanall    # Remove venv & Docker volume"
	@echo ""

# Copy flexible requirements into requirements.txt
flexible-req:
	cp $(REQ_FLEX) $(REQ)

# Create venv (but do not activate)

# Install/upgrade latest requirements
install:
	$(PYTHON) -m pip install --upgrade pip setuptools wheel
	pip install -r $(REQ)

# Start database (docker)
docker:
	docker-compose up -d
	sleep 10

# DB: initialize tables
db: docker
	$(PYTHON) scripts/setup_db.py

# Download Vyakyarth embedding model
model:
	$(PYTHON) -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('$(EMBED_MODEL)'); print('✓ Ready!')"

# Load sample scriptures
data:
	$(PYTHON) scripts/load_sample_data.py

# Run basic query to test
test: venv
	$(PYTHON) -m src.main query "Who is Krishna?"

# Clean up venv
clean:
	rm -rf $(VENV)

# Remove venv and Docker data
cleanall: clean
	docker-compose down -v

# Full pipeline
all: db model data

# All-in-one: Full install through first query
first-test: all test
