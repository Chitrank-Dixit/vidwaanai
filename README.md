# VidwaanAI - MVP

A multilingual AI agent for Indian scriptures with CLI interface.

## Quick Start

### 1. Prerequisites
- Docker & Docker Compose
- Python 3.10+
- OpenAI API key

### 2. Setup Environment
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
