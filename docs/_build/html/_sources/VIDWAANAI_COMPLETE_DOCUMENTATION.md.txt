# Vidwaanai - Complete Project Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Goals and Objectives](#project-goals-and-objectives)
3. [Tech Stack](#tech-stack)
4. [Repository Structure](#repository-structure)
5. [Installation Guide](#installation-guide)
6. [Configuration](#configuration)
7. [Docker Setup](#docker-setup)
8. [Usage Instructions](#usage-instructions)
9. [API and MCP Protocol](#api-and-mcp-protocol)
10. [Supported Languages](#supported-languages)
11. [Testing and Quality Assurance](#testing-and-quality-assurance)
12. [Architecture Overview](#architecture-overview)
13. [Development Workflow](#development-workflow)
14. [Troubleshooting](#troubleshooting)
15. [Contributing Guidelines](#contributing-guidelines)

---

## Project Overview

**Vidwaanai** is an innovative **Agentic AI project** designed to preserve and digitize ancient civilization scriptures. The project leverages modern artificial intelligence, specifically agentic AI systems, to extract, process, analyze, and preserve historical texts and scriptures from various ancient civilizations.

### Mission
To preserve humanity's intellectual and cultural heritage by digitizing and analyzing ancient civilization scriptures using cutting-edge AI technology.

### Key Characteristics
- **Agentic AI Architecture:** Uses autonomous agents to perform complex tasks
- **Multi-language Support:** Handles various ancient and modern languages
- **Scalable Infrastructure:** Docker and Kubernetes ready
- **Production-Ready:** Includes CI/CD pipelines and comprehensive testing
- **MCP Protocol Integration:** Modern Model Context Protocol support

---

## Project Goals and Objectives

### Primary Goals
1. **Digitize Ancient Texts:** Convert physical and scanned ancient scriptures into digital formats
2. **Preserve Knowledge:** Ensure long-term preservation of cultural heritage
3. **Enable Analysis:** Provide tools for linguistic and historical analysis
4. **Accessibility:** Make ancient knowledge accessible to researchers and the public
5. **Automation:** Use AI agents to automate complex preservation workflows

### Specific Objectives
- Extract text from various source formats (images, PDFs, manuscripts)
- Process and clean extracted text with OCR and language models
- Store and manage large-scale scripture databases
- Generate comprehensive reports and analysis
- Support multiple ancient and modern languages
- Maintain data integrity and version control
- Provide API access for integration with external systems

---

## Tech Stack

### Core Technologies
- **Language:** Python 3.x
- **AI/ML Framework:** LLM-based agentic systems
- **Containerization:** Docker and Docker Compose
- **Infrastructure:** Ansible for IaC
- **Testing:** pytest with coverage tracking
- **Build System:** Make, uv (fast Python package manager)

### Key Dependencies
- **API Framework:** FastAPI or Flask (likely)
- **Database:** Multiple database support (PostgreSQL, MongoDB, etc.)
- **Message Queue:** Redis or RabbitMQ (likely, for async operations)
- **AI Models:** OpenAI, Claude, or other LLM providers
- **Data Processing:** Pandas, NumPy
- **NLP Tools:** spaCy, NLTK, or similar

### Development Tools
- Git for version control
- GitHub Actions for CI/CD
- Docker for containerization
- Ansible for infrastructure management
- pytest for testing

---

## Repository Structure

```
vidwaanai/
├── .github/workflows/              # GitHub Actions CI/CD pipelines
├── ansible/                        # Infrastructure automation scripts
├── config/                         # Configuration files for different environments
├── data/                           # Input data and datasets
├── database/                       # Database schemas, migrations, and setup scripts
├── docs/                           # Project documentation
├── output/reports/                 # Generated reports and outputs
├── scripts/                        # Utility and helper scripts
├── src/                            # Main source code
│   ├── agents/                     # Agentic AI implementation
│   ├── processors/                 # Text processing and OCR modules
│   ├── models/                     # Data models and schemas
│   ├── database/                   # Database ORM and queries
│   ├── api/                        # API endpoints
│   └── utils/                      # Utility functions
├── tests/                          # Test suite
│   ├── unit/                       # Unit tests
│   ├── integration/                # Integration tests
│   └── fixtures/                   # Test data and fixtures
├── Dockerfile                      # Production Docker image
├── Dockerfile.ci                   # CI/CD Docker image
├── Dockerfile.mcp                  # MCP protocol Docker image
├── docker-compose.yml              # Main Docker Compose configuration
├── docker-compose-full.yml         # Full stack Docker Compose
├── docker-compose-ci.yml           # CI Docker Compose
├── docker-compose-mcp.yml          # MCP Docker Compose
├── docker-compose-test.yml         # Testing Docker Compose
├── pyproject.toml                  # Python project metadata and settings
├── requirements.txt                # Python package dependencies
├── setup.sh                        # Initial setup script
├── QUICKSTART.md                   # Quick start guide
├── DOCKER-QUICKSTART.md            # Docker setup guide
├── SUPPORTED_LANGUAGES.md          # Supported languages documentation
├── HOW-TO-RUN-MCP                  # MCP protocol setup guide
├── Makefile                        # Build and task automation
├── Makefile-docker                 # Docker-specific tasks
├── pytest.ini                      # pytest configuration
├── .coveragerc                     # Code coverage settings
└── uv.lock                         # Locked dependency versions

```

### Directory Details

#### `/src` - Source Code
Contains the main application logic organized by functionality:
- **agents/**: Agentic AI system implementation
- **processors/**: Text extraction, OCR, and cleaning
- **models/**: Data structures and database models
- **database/**: Database connections and queries
- **api/**: RESTful API endpoints
- **utils/**: Helper functions and utilities

#### `/tests` - Test Suite
Comprehensive testing infrastructure:
- **unit/**: Tests for individual components
- **integration/**: End-to-end workflow tests
- **fixtures/**: Mock data and test databases

#### `/database` - Database Layer
- Migration files
- Schema definitions
- Seed data

#### `/config` - Configuration
Environment-specific configurations:
- Development settings
- Production settings
- Test settings

#### `/scripts` - Automation Scripts
- Setup and initialization scripts
- Data preprocessing scripts
- Maintenance scripts

---

## Installation Guide

### Prerequisites
- Python 3.8 or higher
- Docker and Docker Compose (optional but recommended)
- Git
- Virtual environment tool (venv or conda)

### Local Installation

#### Step 1: Clone Repository
```bash
git clone https://github.com/Chitrank-Dixit/vidwaanai.git
cd vidwaanai
```

#### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Run Setup Script
```bash
bash setup.sh
```

#### Step 5: Configure Environment
```bash
cp .env.example .env
# Edit .env with your configuration
nano .env
```

#### Step 6: Initialize Database
```bash
make db-init
```

#### Step 7: Verify Installation
```bash
make test
```

### Docker Installation

#### Quick Start with Docker
```bash
docker-compose up -d
```

#### Full Stack Setup
```bash
docker-compose -f docker-compose-full.yml up -d
```

#### Access the Application
- API: `http://localhost:8000`
- Docs: `http://localhost:8000/docs`

---

## Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Application
APP_NAME=Vidwaanai
APP_ENV=development
DEBUG=true
LOG_LEVEL=INFO

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/vidwaanai
DATABASE_ECHO=false

# API
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=4

# LLM Configuration
LLM_PROVIDER=openai  # or anthropic, local, etc.
LLM_API_KEY=your-api-key-here
LLM_MODEL=gpt-4
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=2048

# Redis/Cache
REDIS_URL=redis://localhost:6379/0

# File Storage
STORAGE_PATH=/data/storage
UPLOAD_LIMIT=100MB

# Security
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# MCP Protocol
MCP_ENABLED=true
MCP_PORT=5678
```

### Configuration Files

#### `pyproject.toml`
Main Python project configuration including:
- Project metadata
- Dependencies
- Build system configuration
- Tool configurations

#### `pytest.ini`
Testing configuration:
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

#### `.coveragerc`
Code coverage configuration for tracking test coverage.

---

## Docker Setup

### Understanding Docker Configurations

#### Main Docker Compose (`docker-compose.yml`)
Basic setup with:
- API service
- Database service
- Redis cache

#### Full Stack (`docker-compose-full.yml`)
Extended setup including:
- API service
- PostgreSQL database
- Redis cache
- Elasticsearch
- Monitoring tools

#### CI Setup (`docker-compose-ci.yml`)
Optimized for continuous integration:
- Minimized resources
- Test database
- Coverage reporting

#### MCP Setup (`docker-compose-mcp.yml`)
Model Context Protocol setup:
- MCP server
- API service
- Database

### Running Docker Containers

#### Start Services
```bash
docker-compose up -d
```

#### View Logs
```bash
docker-compose logs -f app
```

#### Stop Services
```bash
docker-compose down
```

#### Run Migrations
```bash
docker-compose exec app python -m alembic upgrade head
```

#### Access Services
- API: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- Database: `localhost:5432`
- Redis: `localhost:6379`

---

## Usage Instructions

### Running the Application

#### Local Development
```bash
make run
```

#### With Specific Configuration
```bash
APP_ENV=development python -m src.main
```

#### Running Specific Agents
```bash
python -m src.agents.scripture_processor --input data/raw/ --output data/processed/
```

### Common Tasks

#### Process Scriptures
```bash
python scripts/process_scriptures.py --source ancient_texts/ --destination output/
```

#### Generate Reports
```bash
python scripts/generate_report.py --data output/ --format html
```

#### Export Data
```bash
python scripts/export_data.py --format json --output exports/
```

#### Run API Server
```bash
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
```

---

## API and MCP Protocol

### REST API Endpoints

#### Scripture Management
```
POST   /api/scriptures          - Create new scripture entry
GET    /api/scriptures          - List all scriptures
GET    /api/scriptures/{id}     - Get specific scripture
PUT    /api/scriptures/{id}     - Update scripture
DELETE /api/scriptures/{id}     - Delete scripture
```

#### Processing
```
POST   /api/process             - Start processing job
GET    /api/process/{job_id}    - Get job status
GET    /api/process/{job_id}/result - Get results
```

#### Reports
```
GET    /api/reports             - List reports
GET    /api/reports/{id}        - Get specific report
POST   /api/reports/generate    - Generate new report
```

### MCP Protocol Support

The project includes Model Context Protocol support for advanced AI integrations.

#### Running MCP Server
```bash
docker-compose -f docker-compose-mcp.yml up -d
```

#### MCP Configuration
Edit `.env.mcp`:
```env
MCP_ENABLE=true
MCP_PROTOCOL_VERSION=1.0
MCP_MAX_CONNECTIONS=10
```

#### MCP Tools Available
- Scripture analysis
- Text extraction
- Language processing
- Report generation
- Data export

---

## Supported Languages

The project supports processing and analyzing texts in multiple languages:

### Ancient Languages
- Sanskrit
- Pali
- Tamil
- Kannada
- Telugu
- Malayalam
- Ancient Greek
- Latin
- Aramaic
- Hebrew
- Old Persian

### Modern Languages
- English
- Hindi
- Spanish
- French
- German
- Chinese
- Japanese
- Arabic
- Portuguese
- Russian

See `SUPPORTED_LANGUAGES.md` for detailed language support information.

---

## Testing and Quality Assurance

### Running Tests

#### All Tests
```bash
make test
```

#### Specific Test File
```bash
pytest tests/unit/test_processors.py -v
```

#### With Coverage
```bash
pytest --cov=src --cov-report=html
```

#### Integration Tests
```bash
pytest tests/integration/ -v
```

### Test Structure

```
tests/
├── unit/
│   ├── test_agents.py
│   ├── test_processors.py
│   ├── test_models.py
│   └── test_api.py
├── integration/
│   ├── test_workflows.py
│   ├── test_database.py
│   └── test_api_endpoints.py
└── fixtures/
    ├── sample_texts/
    └── test_data.json
```

### Coverage Requirements
- Minimum: 80% code coverage
- Target: 90%+ code coverage

### CI/CD Pipeline

GitHub Actions workflows automatically:
1. Run all tests on push
2. Check code coverage
3. Lint code
4. Build Docker images
5. Deploy to staging

---

## Architecture Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    INPUT LAYER                          │
│  (Ancient Texts, Manuscripts, PDFs, Images)            │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│              DATA PROCESSING LAYER                      │
│  - Text Extraction                                      │
│  - OCR Processing                                       │
│  - Language Detection                                   │
│  - Text Cleaning and Normalization                     │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                 AGENTIC AI LAYER                        │
│  - LLM Integration                                      │
│  - Intelligent Agents                                   │
│  - Semantic Analysis                                    │
│  - Entity Recognition                                   │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│              KNOWLEDGE STORAGE LAYER                    │
│  - Primary Database (PostgreSQL)                        │
│  - Cache Layer (Redis)                                  │
│  - Vector Database (for embeddings)                     │
│  - File Storage (for originals)                         │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│               API & INTERFACE LAYER                     │
│  - REST API                                             │
│  - MCP Protocol                                         │
│  - Web Dashboard                                        │
│  - CLI Tools                                            │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│              OUTPUT & REPORTING LAYER                   │
│  - Digital Archives                                     │
│  - Analysis Reports                                     │
│  - Exported Data (JSON, XML, CSV)                       │
│  - Public Access Portals                                │
└─────────────────────────────────────────────────────────┘
```

### Component Interactions

#### Agent Workflow
1. **Input Processing**: Documents are received and validated
2. **Extraction**: Text is extracted using OCR and parsing
3. **Analysis**: Agentic AI analyzes content linguistically
4. **Storage**: Processed data stored in knowledge base
5. **Retrieval**: API serves data to consumers
6. **Reporting**: Analysis results compiled into reports

#### Data Flow
```
Raw Input → Processing Pipeline → AI Agents → Database → API → Output
```

---

## Development Workflow

### Setting Up Development Environment

#### 1. Initial Setup
```bash
git clone https://github.com/Chitrank-Dixit/vidwaanai.git
cd vidwaanai
bash setup.sh
source venv/bin/activate
```

#### 2. Creating Feature Branch
```bash
git checkout -b feature/my-feature
```

#### 3. Making Changes
```bash
# Make your code changes
# Follow PEP 8 style guide
```

#### 4. Testing
```bash
pytest tests/ -v
pytest --cov=src
```

#### 5. Linting
```bash
make lint
flake8 src/
black src/
isort src/
```

#### 6. Committing
```bash
git add .
git commit -m "feat: description of changes"
git push origin feature/my-feature
```

#### 7. Creating Pull Request
- Go to GitHub repository
- Create PR with clear description
- Ensure CI/CD passes

### Code Style Guidelines
- Follow PEP 8
- Use type hints
- Write docstrings for all functions
- Keep functions small and focused
- Maximum line length: 88 characters (Black)

### Commit Message Convention
```
<type>(<scope>): <subject>

<body>

<footer>
```

Types: feat, fix, docs, style, refactor, test, chore

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000
# Kill the process
kill -9 <PID>
# Or use different port
docker-compose up -e API_PORT=8001
```

#### Issue: Database Connection Error
```bash
# Check database is running
docker-compose ps
# Verify connection string in .env
# Reset database
make db-reset
```

#### Issue: Out of Memory
```bash
# Increase Docker memory
# Edit docker-compose.yml or Docker Desktop settings
docker-compose down
docker system prune -a
```

#### Issue: Module Not Found
```bash
# Reinstall dependencies
pip install --upgrade pip
pip install -r requirements.txt
# Clear Python cache
find . -type d -name __pycache__ -exec rm -r {} +
```

#### Issue: Tests Failing
```bash
# Run with verbose output
pytest -vv
# Check test dependencies
pip install -r requirements-dev.txt
# Run specific test
pytest tests/unit/test_specific.py -v
```

### Debug Mode

#### Enable Debug Logging
```bash
export LOG_LEVEL=DEBUG
export DEBUG=true
python -m src.main
```

#### Using Python Debugger
```python
import pdb; pdb.set_trace()
```

#### Using VS Code Debugger
Add `.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```

---

## Contributing Guidelines

### How to Contribute

1. **Fork the Repository**
   ```bash
   Click "Fork" button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/vidwaanai.git
   cd vidwaanai
   ```

3. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes**
   - Follow code style guidelines
   - Add tests for new features
   - Update documentation

5. **Run Tests**
   ```bash
   make test
   make lint
   ```

6. **Push Changes**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create Pull Request**
   - Provide clear description
   - Reference related issues
   - Ensure all checks pass

### Code Review Process
- At least 2 approvals required
- CI/CD must pass
- Code coverage must not decrease
- Documentation must be updated

### Reporting Issues
- Use GitHub Issues
- Provide clear description
- Include reproduction steps
- Attach relevant logs

---

## Additional Resources

### Documentation Files
- `README.md` - Project overview
- `QUICKSTART.md` - Quick start guide
- `DOCKER-QUICKSTART.md` - Docker setup
- `SUPPORTED_LANGUAGES.md` - Language support
- `HOW-TO-RUN-MCP` - MCP protocol setup

### Build Automation
```bash
make help          # Show all available commands
make run           # Run application
make test          # Run tests
make lint          # Lint code
make docker-build  # Build Docker image
make docker-up     # Start Docker containers
```

### Project Links
- **Repository**: https://github.com/Chitrank-Dixit/vidwaanai
- **Issues**: https://github.com/Chitrank-Dixit/vidwaanai/issues
- **Discussions**: https://github.com/Chitrank-Dixit/vidwaanai/discussions

---

## License

This project is open source. Check the repository for license details.

---

## Contact and Support

For questions, issues, or contributions:
- Create an issue on GitHub
- Check existing documentation
- Review project discussions

---

**Last Updated**: January 2026  
**Version**: 1.0  
**Project**: Vidwaanai - Agentic AI for Civilization Scripture Preservation

