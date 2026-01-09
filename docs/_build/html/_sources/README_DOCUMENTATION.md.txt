# Vidwaanai Project Documentation - README

## Overview

This comprehensive documentation package provides complete guidance for the **Vidwaanai** project - an Agentic AI system designed to preserve and digitize ancient civilization scriptures.

**Repository:** https://github.com/Chitrank-Dixit/vidwaanai  
**Project Type:** Python-based Agentic AI Application  
**Status:** Active Development  
**Documentation Version:** 1.0

---

## What is Vidwaanai?

Vidwaanai is an innovative project that combines modern artificial intelligence with cultural preservation. It uses autonomous AI agents to:

- Extract text from ancient manuscripts and documents
- Analyze scriptures linguistically and semantically
- Identify and link historical entities and concepts
- Generate comprehensive analysis reports
- Make ancient knowledge accessible through digital archives
- Support multiple ancient and modern languages

### Key Features

✅ **Agentic AI Architecture** - Specialized agents for different tasks  
✅ **Multi-Layer Processing** - From raw input to structured knowledge  
✅ **Vector Database Integration** - Semantic search capabilities  
✅ **REST API & MCP Protocol** - Multiple access methods  
✅ **Production-Ready** - Docker, CI/CD, monitoring  
✅ **Multi-Language Support** - Ancient and modern languages  
✅ **Scalable Design** - From local dev to enterprise deployment  

---

## Documentation Files Included

### 1. **VIDWAANAI_COMPLETE_DOCUMENTATION.md** ⭐ Main Reference
Comprehensive 15-section documentation covering everything:
- Project overview, goals, and mission
- Complete technology stack
- Installation (Docker and local)
- Configuration and setup
- API documentation
- Architecture and design
- Development workflow
- Troubleshooting and support

**When to Use:** Complete project reference, onboarding, implementation guide

---

### 2. **QUICK_REFERENCE_GUIDE.md** ⚡ Daily Development
Fast-access guide for developers:
- 5-minute setup (2 options)
- Essential commands
- Common tasks with examples
- API quick reference
- Debugging tips
- Performance optimization
- Troubleshooting quick fixes

**When to Use:** Day-to-day development, quick lookups, common operations

---

### 3. **DOCUMENTATION_INDEX.md** 📇 Navigation Guide
Complete index and navigation guide:
- All documentation artifacts listed
- Getting started by role
- Key sections by topic
- File navigation map
- Common use cases
- Feature highlights
- Support and contribution info

**When to Use:** Finding specific information, navigation, understanding structure

---

### 4. **architecture_diagram.txt** 🏗️ System Design
ASCII diagrams and visual representations:
- 7-layer system architecture
- Data flow diagrams
- Agent interaction diagrams
- Technology stack mapping
- Deployment architecture
- Component relationships

**When to Use:** Understanding system design, architecture reviews, presentations

---

### 5. **class_structure_diagram.txt** 💻 Code Architecture
UML-style component diagrams:
- Domain models
- Processing pipeline
- Agentic AI system
- Storage and database layers
- API layer
- Service layer
- Relationships and dependencies
- Enums and constants

**When to Use:** Code development, architecture understanding, design patterns

---

### 6. **repo_analysis.md** 📊 Project Analysis
Repository overview and analysis:
- Project structure summary
- Technology stack list
- Feature summary
- Maturity assessment
- Key findings

**When to Use:** Quick project understanding, capability overview

---

## Quick Start

### Using Docker (Recommended)
```bash
git clone https://github.com/Chitrank-Dixit/vidwaanai.git
cd vidwaanai
docker-compose up -d
# API available at http://localhost:8000
```

### Using Local Python
```bash
git clone https://github.com/Chitrank-Dixit/vidwaanai.git
cd vidwaanai
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
make run
```

See **QUICK_REFERENCE_GUIDE.md** for more details.

---

## Documentation by Role

### 👨‍💻 Developers
1. Start: **QUICK_REFERENCE_GUIDE.md** - Setup
2. Then: **VIDWAANAI_COMPLETE_DOCUMENTATION.md** - Full guide
3. Reference: **class_structure_diagram.txt** - Code structure

### 🔧 DevOps/Infrastructure
1. Start: **architecture_diagram.txt** - Deployment options
2. Then: **VIDWAANAI_COMPLETE_DOCUMENTATION.md** - Docker section
3. Reference: **QUICK_REFERENCE_GUIDE.md** - Docker commands

### 🧠 AI/Data Scientists
1. Start: **architecture_diagram.txt** - System design
2. Then: **class_structure_diagram.txt** - Agent architecture
3. Reference: **VIDWAANAI_COMPLETE_DOCUMENTATION.md** - API section

### 📋 Project Managers
1. Start: **repo_analysis.md** - Overview
2. Then: **VIDWAANAI_COMPLETE_DOCUMENTATION.md** - Goals section
3. Reference: **DOCUMENTATION_INDEX.md** - Feature summary

### 🤝 Contributors
1. Start: **QUICK_REFERENCE_GUIDE.md** - Getting started
2. Then: **VIDWAANAI_COMPLETE_DOCUMENTATION.md** - Contributing
3. Reference: **class_structure_diagram.txt** - Code organization

---

## Key Technologies

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.x |
| **API Framework** | FastAPI / Flask |
| **Databases** | PostgreSQL, Vector DB, Redis |
| **AI/LLM** | OpenAI, Anthropic, local models |
| **Containerization** | Docker, Docker Compose |
| **Testing** | pytest |
| **CI/CD** | GitHub Actions |
| **Infrastructure** | Ansible |
| **NLP** | spaCy, NLTK |
| **API Protocol** | REST, MCP |

---

## Common Tasks

### Run the Application
```bash
docker-compose up -d              # Start services
docker-compose logs -f app        # View logs
curl http://localhost:8000/health # Health check
```

### Development
```bash
make run              # Run app
make test             # Run tests
make lint             # Lint code
make docker-build     # Build Docker image
```

### API Operations
```bash
# Create scripture
curl -X POST http://localhost:8000/api/scriptures \
  -H "Content-Type: application/json" \
  -d '{"title": "Example", "language": "sa"}'

# Get scriptures
curl http://localhost:8000/api/scriptures

# Search
curl "http://localhost:8000/api/scriptures/search?language=sa"
```

See **QUICK_REFERENCE_GUIDE.md** for more examples.

---

## Project Structure

```
vidwaanai/
├── src/                      # Main application code
│   ├── agents/              # AI agents
│   ├── processors/          # Text processing
│   ├── api/                 # API endpoints
│   └── database/            # Database layer
├── tests/                   # Test suite
├── config/                  # Configuration
├── docker-compose.yml       # Services definition
├── Dockerfile               # Container image
├── pyproject.toml          # Project metadata
├── requirements.txt        # Python dependencies
└── Makefile                # Task automation
```

---

## Supported Languages

### Ancient Languages
Sanskrit, Pali, Tamil, Kannada, Telugu, Malayalam, Ancient Greek, Latin, Aramaic, Hebrew, Old Persian, and more.

### Modern Languages
English, Hindi, Spanish, French, German, Chinese, Japanese, Arabic, Portuguese, Russian, and more.

See **SUPPORTED_LANGUAGES.md** in the repository for complete list.

---

## Architecture Highlights

### 7-Layer Architecture
1. **Input Layer** - Ancient texts, PDFs, images
2. **Processing Layer** - Text extraction, normalization, language detection
3. **AI Layer** - LLM models, semantic analysis, agents
4. **Storage Layer** - PostgreSQL, Vector DB, Redis, file storage
5. **API Layer** - REST API, MCP Protocol, CLI tools
6. **Output Layer** - Digital archives, reports, exports
7. **Access Layer** - Public portal, researcher APIs

### Agentic AI System
- **ScriptureAnalyzer** - Content analysis and understanding
- **TextEnricher** - Metadata enrichment and context addition
- **KnowledgeLinker** - Entity linking and relationship creation
- **ReportGenerator** - Automated report generation

---

## Getting Help

### Documentation
1. Check **QUICK_REFERENCE_GUIDE.md** - Troubleshooting section
2. Review **VIDWAANAI_COMPLETE_DOCUMENTATION.md** - Full troubleshooting
3. See **DOCUMENTATION_INDEX.md** - Find specific topics

### Support Resources
- **GitHub Issues:** https://github.com/Chitrank-Dixit/vidwaanai/issues
- **GitHub Discussions:** https://github.com/Chitrank-Dixit/vidwaanai/discussions
- **Repository:** https://github.com/Chitrank-Dixit/vidwaanai

### Common Issues
```bash
# Port conflicts
lsof -i :8000
kill -9 <PID>

# Database issues
docker-compose down
docker-compose up -d

# Test failures
make clean
make test
```

See **QUICK_REFERENCE_GUIDE.md** for more troubleshooting.

---

## Development Workflow

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/vidwaanai.git
   ```

2. **Setup Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Create Feature Branch**
   ```bash
   git checkout -b feature/my-feature
   ```

4. **Make Changes and Test**
   ```bash
   make test
   make lint
   ```

5. **Push and Create PR**
   ```bash
   git push origin feature/my-feature
   ```

See **VIDWAANAI_COMPLETE_DOCUMENTATION.md** for detailed guidelines.

---

## Testing

### Run All Tests
```bash
make test
```

### Run with Coverage
```bash
pytest --cov=src --cov-report=html
```

### Run Specific Tests
```bash
pytest tests/unit/test_processors.py -v
```

### Integration Tests
```bash
pytest tests/integration/ -v
```

---

## Configuration

### Environment Variables
Create a `.env` file with:
```env
APP_ENV=development
DEBUG=true
DATABASE_URL=postgresql://user:pass@localhost:5432/vidwaanai
LLM_PROVIDER=openai
LLM_API_KEY=your-key
```

See **VIDWAANAI_COMPLETE_DOCUMENTATION.md** for complete configuration reference.

---

## Feature Highlights

✨ **Multiple Scripture Sources**
- Ancient manuscripts
- PDF documents  
- Images with OCR
- Digital texts

🤖 **Intelligent Processing**
- Autonomous AI agents
- Semantic understanding
- Entity recognition
- Knowledge linking

📊 **Comprehensive Analysis**
- Linguistic analysis
- Historical context
- Comparative studies
- Automated reports

🌍 **Multi-Language Support**
- Ancient languages (Sanskrit, Latin, Greek, etc.)
- Modern languages (100+ supported)
- Automatic language detection

🔍 **Advanced Search**
- Full-text search
- Semantic similarity search
- Entity-based search
- Faceted filtering

📱 **Multiple Interfaces**
- RESTful API
- MCP Protocol
- CLI tools
- Web dashboard

---

## Project Statistics

- **Repository:** GitHub (Chitrank-Dixit)
- **Language:** Python 3.x
- **Test Coverage:** 80%+ (configurable)
- **Docker Images:** 3 (production, CI, MCP)
- **Database Support:** PostgreSQL + Vector DB
- **API Versions:** RESTful + MCP
- **Supported Languages:** 50+

---

## Next Steps

1. **First Time?** → Read QUICK_REFERENCE_GUIDE.md
2. **Want Details?** → Read VIDWAANAI_COMPLETE_DOCUMENTATION.md
3. **Need Architecture?** → Check architecture_diagram.txt
4. **Code Diving?** → Review class_structure_diagram.txt
5. **Navigation Help?** → Use DOCUMENTATION_INDEX.md

---

## Questions?

- 📖 Check the documentation
- 🔍 Search GitHub Issues
- 💬 Ask in GitHub Discussions
- 🐛 Report bugs with details
- 💡 Suggest improvements

---

## License

Check the repository for license information.

---

## Version Information

- **Documentation Created:** January 2026
- **Last Updated:** January 10, 2026
- **Vidwaanai Version:** 1.0
- **Documentation Status:** Complete

---

**Start with:** [QUICK_REFERENCE_GUIDE.md](QUICK_REFERENCE_GUIDE.md) or [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md)

**Full Reference:** [VIDWAANAI_COMPLETE_DOCUMENTATION.md](VIDWAANAI_COMPLETE_DOCUMENTATION.md)

