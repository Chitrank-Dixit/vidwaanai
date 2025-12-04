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


## Future Work

Excellent choice! **Graph RAG** will significantly enhance VidwaanAI by capturing relationships between concepts, people, events, and teachings across scriptures—something traditional vector RAG cannot do well.

Let me provide you with a comprehensive plan for implementing Graph RAG in VidwaanAI.

***

# 🗺️ Graph RAG Implementation Plan for VidwaanAI

## **Executive Summary**

**Goal:** Enhance VidwaanAI with Graph RAG to capture semantic relationships between entities (characters, concepts, events, locations) across Indian scriptures, enabling deeper contextual understanding and cross-scripture knowledge synthesis.

**Timeline:** 6-8 weeks (phased approach)

**Core Value:** Instead of just finding similar verses, Graph RAG will enable queries like:
- "How is Krishna related to dharma across different scriptures?"
- "What are all the teachings about karma and their interconnections?"
- "Compare Rama's and Krishna's approaches to duty"

***

## **Phase 1: Architecture & Design (Week 1-2)**

### 1.1 Understanding Graph RAG

**Traditional Vector RAG (Current VidwaanAI):**
```
Query → Embedding → Vector Search → Top-K verses → LLM → Answer
```

**Graph RAG (Enhanced VidwaanAI):**
```
Query → Entity Extraction → Graph Traversal + Vector Search → 
  Contextual Subgraph → LLM with Graph Context → Rich Answer
```

**Key Differences:**
- Captures **relationships** between entities (e.g., Krishna → teaches → Arjuna)
- Enables **multi-hop reasoning** (e.g., Krishna → Bhagavad Gita → dharma → other scriptures)
- Provides **structured context** beyond just similar text chunks

***

### 1.2 Technology Stack Selection

| Component | Options | Recommendation | Why |
|-----------|---------|----------------|-----|
| **Graph Database** | Neo4j, AWS Neptune, NebulaGraph, PostgreSQL (with AGE) | **Neo4j Community** | Best query language (Cypher), mature ecosystem, free tier, great Python support |
| **Graph Schema** | Property Graph, RDF | **Property Graph** | More flexible for scripture entities and relationships |
| **Entity Extraction** | spaCy, OpenAI, Llama Index, Custom NER | **LLM-based (GPT-4 or local Llama)** | Better for Indic names and concepts |
| **Graph Construction** | Manual, LLM-based, Hybrid | **Hybrid (LLM + rules)** | Balance accuracy and cost |
| **Integration** | Replace vector RAG, Hybrid (Graph + Vector) | **Hybrid** | Keep vector search strength, add graph reasoning |

**Recommended Stack:**
- **Neo4j Community Edition** (graph database)
- **neo4j Python driver** (graph queries)
- **LlamaIndex PropertyGraphIndex** (graph construction from text)
- **Existing Vyakyarth** (embeddings for hybrid search)
- **PostgreSQL** (keep for verse storage)
- **LM Studio / OpenAI** (entity extraction + final generation)

***

### 1.3 Graph Schema Design

#### **Nodes (Entities)**

```
Person
  - name: string
  - aliases: [string]
  - scripture_origin: string
  - description: string
  - type: enum (deity, sage, warrior, king, etc.)

Concept
  - name: string
  - sanskrit_term: string
  - definition: string
  - category: enum (dharma, karma, yoga, moksha, etc.)

Event
  - name: string
  - description: string
  - location: string
  - timeframe: string

Location
  - name: string
  - modern_name: string
  - description: string

Scripture
  - name: string
  - language: string
  - chapter_count: int

Verse
  - scripture_id: int
  - chapter: int
  - verse_num: int
  - text: string
  - translation: string
  - embedding: vector(768)
```

#### **Relationships (Edges)**

```
(Person)-[:TEACHES]->(Concept)
  - verse_reference: string
  - context: string

(Person)-[:APPEARS_IN]->(Scripture)
  - role: string

(Person)-[:RELATES_TO]->(Person)
  - relationship: enum (teacher, student, friend, enemy, parent, child)
  - context: string

(Concept)-[:MENTIONED_IN]->(Verse)
  - importance: float

(Concept)-[:RELATES_TO]->(Concept)
  - relationship: enum (prerequisite, opposite, component, example)

(Event)-[:INVOLVES]->(Person)
  - role: string

(Verse)-[:SIMILAR_TO]->(Verse)
  - similarity_score: float
  - type: enum (semantic, thematic, conceptual)
```

***

### 1.4 Hybrid Architecture Design

```
┌─────────────────────────────────────────────┐
│          User Query                         │
│    "What does Krishna teach about duty?"    │
└──────────────────┬──────────────────────────┘
                   │
    ┌──────────────┴──────────────┐
    │                             │
    ▼                             ▼
┌─────────────────┐     ┌──────────────────────┐
│  Entity          │     │  Vector Search       │
│  Extraction      │ │  (Vyakyarth)         │
│  (LLM)           │ │                      │
│                  │ │  Top-K verses        │
│  Extract:        │ │  about "duty"        │
│  - Krishna       │ └──────────┬───────────┘
│  - duty/dharma   │                │
└────────┬─────────┘                │
         │                          │
         ▼                          │
┌─────────────────────────┐         │
│  Graph Traversal         │         │
│  (Neo4j Cypher)          │         │
│                          │         │
│  Find:                   │         │
│  - Krishna's teachings   │         │
│  - Related concepts      │         │
│  - Cross-references      │         │
└────────┬─────────────────┘         │
         │                           │
         └──────────┬────────────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │  Context Fusion      │
         │                      │
         │  Combine:            │
         │  - Graph subgraph    │
         │  - Vector results    │
         │  - Relationships     │
         └──────────┬───────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │  LLM Generation      │
         │  (LM Studio)         │
         │                      │
         │  Rich, contextual    │
         │  answer with sources │
         └──────────────────────┐
```

***

## **Phase 2: Infrastructure Setup (Week 2-3)**

### 2.1 Neo4j Installation

**Option A: Docker (Recommended for dev)**
```yaml
# Add to docker-compose.yml
neo4j:
  image: neo4j:5.15-community
  ports:
    - "7474:7474"  # HTTP
    - "7687:7687"  # Bolt
  environment:
    NEO4J_AUTH: neo4j/vidwaan123
    NEO4J_PLUGINS: '["apoc", "graph-data-science"]'
  volumes:
    - neo4j_data:/data
    - neo4j_logs:/logs

volumes:
  neo4j_data:
  neo4j_logs:
```

**Option B: Neo4j Desktop (for GUI exploration)**
- Download from neo4j.com
- Create local database
- Enable APOC plugin

### 2.2 Python Dependencies

Update `requirements.txt`:
```
# Graph RAG additions
neo4j>=5.15.0
llama-index-graph-stores-neo4j>=0.1.0
networkx>=3.2
```

### 2.3 Configuration

Update `.env`:
```env
# Graph Database
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=vidwaan123

# Graph RAG settings
ENABLE_GRAPH_RAG=true
GRAPH_TRAVERSAL_DEPTH=2
HYBRID_ALPHA=0.5  # 0=pure vector, 1=pure graph, 0.5=balanced
```

***

## **Phase 3: Entity Extraction Pipeline (Week 3-4)**

### 3.1 Entity Extraction Module

Create `src/graph/entity_extractor.py`:

```python
from typing import List, Dict
import json

class EntityExtractor:
    """Extract entities and relationships from scripture verses."""
    
    def __init__(selfmll_client):
        self.llm = llm_client
        
    def extract_entities(self, verse_text: str, translation: str, 
                        scripture_name: str) -> Dict:
        """
        Extract entities using LLM.
        
        Returns:
        {
            "entities": [
                {"type": "Person", "name": "Krishna", "attributes": {...}},
                {"type": "Concept", "name": "dharma", "attributes": {...}}
            ],
            "relationships": [
                {"from": "Krishna", "to": "Arjuna", "type": "TEACHES", 
                 "attributes": {...}}
            ]
        }
        """
        prompt = f"""
Extract entities and relationships from this scripture verse.

Scripture: {scripture_name}
Original: {verse_text}
Translation: {translation}

Extract:
1. PERSONS (deities, sages, warriors, kings)
2. CONCEPTS (dharma, karma, yoga, moksha, etc.)
3. EVENTS (wars, ceremonies, dialogues)
4. LOCATIONS (cities, forests, mountains)

For each entity, identify:
- Type (Person/Concept/Event/Location)
- Name (primary and aliases)
- Attributes (description, role, etc.)

Also extract RELATIONSHIPS between entities:
- Type (TEACHES, RELATES_TO, APPEARS_IN, etc.)
- Direction (from → to)
- Context

Return as JSON.
"""
        
        response = self.llm.generate(prompt, max_tokens=800, temperature=0.3)
        try:
            return json.loads(response)
        except:
            return {"entities": [], "relationships": []}
```

### 3.2 Graph Builder

Create `src/graph/graph_builder.py`:

```python
from neo4j import GraphDatabase

class GraphBuilder:
    """Build knowledge graph in Neo4j."""
    
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        
    def create_person(self, name: str, attributes: Dict):
        with self.driver.session() as session:
            session.run("""
                MERGE (p:Person {name: $name})
                SET p += $attributes
            """, name=name, attributes=attributes)
    
    def create_concept(self, name: str, attributes: Dict):
        with self.driver.session() as session:
            session.run("""
                MERGE (c:Concept {name: $name})
                SET c += $attributes
            """, name=name, attributes=attributes)
    
    def create_relationship(self, from_name: str, to_name: str, 
                           rel_type: str, attributes: Dict):
        with self.driver.session() as session:
            session.run(f"""
                MATCH (a {{name: $from_name}})
                MATCH (b {{name: $to_name}})
                MERGE (a)-[r:{rel_type}]->(b)
                SET r += $attributes
            """, from_name=from_name, to_name=to_name, attributes=attributes)
```

***

## **Phase 4: Graph Querying & Retrieval (Week 4-5)**

### 4.1 Graph Retriever

Create `src/graph/graph_retriever.py`:

```python
class GraphRetriever:
    """Retrieve relevant subgraphs for queries."""
    
    def __init__(self, neo4j_driver):
        self.driver = neo4j_driver
    
    def find_teachings(self, person_name: str, concept_name: str, 
                      depth: int = 2) -> List[Dict]:
        """Find all teachings by a person about a concept."""
        with self.driver.session() as session:
            result = session.run("""
                MATCH path = (p:Person {name: $person})-[:TEACHES*1..{depth}]->(c:Concept)
                WHERE c.name CONTAINS $concept OR c.sanskrit_term CONTAINS $concept
                RETURN path, 
                       [node in nodes(path) | properties(node)] as entities,
                       [rel in relationships(path) | properties(rel)] as relations
                LIMIT 20
            """, person=person_name, concept=concept_name, depth=depth)
            
            return [record.data() for record in result]
    
    def find_related_concepts(self, concept_name: str, depth: int = 2):
        """Find concepts related to a given concept."""
        with self.driver.session() as session:
            result = session.run("""
                MATCH path = (c1:Concept {name: $concept})-[:RELATES_TO*1..{depth}]-(c2:Concept)
                RETURN c2.name as related_concept,
                       c2.definition as definition,
                       length(path) as distance
                ORDER BY distance
                LIMIT 10
            """, concept=concept_name, depth=depth)
            
            return [record.data() for record in result]
```

### 4.2 Hybrid Search Strategy

Create `src/graph/hybrid_search.py`:

```python
class HybridSearcher:
    """Combine graph traversal with vector search."""
    
    def __init__(self, graph_retriever, vector_db, embeddings, alpha=0.5):
        self.graph = graph_retriever
        self.vector = vector_db
        self.embeddings = embeddings
        self.alpha = alpha  # balance between graph and vector
    
    def search(self, query: str, top_k: int = 5) -> Dict:
        """
        Hybrid search combining graph and vector results.
        
        Returns:
        {
            "graph_results": [...],  # from graph traversal
            "vector_results": [...], # from vector similarity
            "fused_context": "...",  # combined context for LLM
            "sources": [...]         # all sources cited
        }
        """
        # 1. Extract entities from query
        entities = self._extract_query_entities(query)
        
        # 2. Graph traversal
        graph_results = []
        for entity in entities:
            if entity['type'] == 'Person':
                graph_results.extend(
                    self.graph.find_teachings(entity['name'], query)
                )
        
        # 3. Vector search
        query_embedding = self.embeddings.embed_text(query)
        vector_results = self.vector.search_similar_verses(
            query_embedding, top_k=top_k
        )
        
        # 4. Fusion with weighted ranking
        fused = self._fuse_results(graph_results, vector_results)
        
        return fused
```

***

## **Phase 5: Integration with VidwaanAI (Week 5-6)**

### 5.1 Update VidwaanAI Agent

Modify `src/agent/vidwaan_agent.py`:

```python
class VidwaanAI:
    def __init__(self, db_url, openai_key=None, krutrim_key=None, 
                 enable_graph_rag=False):
        self.db = DatabaseManager(db_url)
        self.embeddings = EmbeddingManager()
        
        # LLM setup
        if settings.llm_backend == "lmstudio":
            self.llm = LMStudioClient(...)
        else:
            self.llm = OpenAIClient(...)
        
        # Graph RAG setup
        self.enable_graph_rag = enable_graph_rag
        if enable_graph_rag:
            self.graph_retriever = GraphRetriever(neo4j_driver)
            self.hybrid_search = HybridSearcher(
                self.graph_retriever, self.db, self.embeddings
            )
    
    def query(self, question: str, language='en', **kwargs):
        if self.enable_graph_rag:
            # Use hybrid search
            results = self.hybrid_search.search(question)
            context = results['fused_context']
            sources = results['sources']
        else:
            # Traditional vector search
            embedding = self.embeddings.embed_text(question)
            verses = self.db.search_similar_verses(embedding)
            context = self._format_context(verses)
            sources = verses
        
        # Generate answer with LLM
        answer = self._generate_answer(question, context)
        
        return {
            "answer": answer,
            "sources": sources,
            "mode": "graph_rag" if self.enable_graph_rag else "vector_rag"
        }
```

***

## **Phase 6: Graph Population (Week 6-7)**

### 6.1 Batch Processing Script

Create `scripts/build_knowledge_graph.py`:

```python
"""
Build knowledge graph from existing scripture data.
Process all verses, extract entities, create graph.
"""

def build_graph():
    db = DatabaseManager(settings.DATABASE_URL)
    graph_builder = GraphBuilder(neo4j_uri, neo4j_user, neo4j_pass)
    entity_extractor = EntityExtractor(llm_client)
    
    # Get all verses
    verses = db.get_all_verses()
    
    for i, verse in enumerate(verses):
        print(f"Processing verse {i+1}/{len(verses)}")
        
        # Extract entities and relationships
        extracted = entity_extractor.extract_entities(
            verse['text'],
            verse['translation'],
            verse['scripture_name']
        )
        
        # Add to graph
        for entity in extracted['entities']:
            if entity['type'] == 'Person':
                graph_builder.create_person(entity['name'], entity['attributes'])
            elif entity['type'] == 'Concept':
                graph_builder.create_concept(entity['name'], entity['attributes'])
        
        for rel in extracted['relationships']:
            graph_builder.create_relationship(
                rel['from'], rel['to'], rel['type'], rel['attributes']
            )
        
        # Rate limiting for LLM API
        time.sleep(1)
    
    print("✓ Knowledge graph built successfully!")
```

Run with:
```bash
python scripts/build_knowledge_graph.py
```

***

## **Phase 7: Testing & Optimization (Week 7-8)**

### 7.1 Test Scenarios

```python
# Test 1: Entity-based query
python -m src.main query "What does Krishna teach about dharma?"

# Test 2: Cross-scripture comparison
python -m src.main query "Compare Rama's and Krishna's views on duty"

# Test 3: Concept exploration
python -m src.main query "Explain the relationship between karma and dharma"

# Test 4: Multi-hop reasoning
python -m src.main query "Who learned from Krishna and what did they teach others?"
```

### 7.2 Performance Optimization

- **Graph indexing**: Create Neo4j indexes on frequently queried properties
- **Caching**: Cache common graph queries
- **Batch processing**: Process entities in batches
- **Query optimization**: Use Cypher query profiling

***

## **Cost & Resource Estimates**

| Component | Development Time | Complexity | Dependencies |
|-----------|-----------------|------------|--------------|
| Neo4j setup | 1-2 days | Low | Docker |
| Entity extraction | 4-5 days | Medium | LLM API |
| Graph schema design | 2-3 days | Medium | Domain knowledge |
| Graph population | 3-4 days | Medium | Batch processing |
| Hybrid search | 5-6 days | High | Graph + Vector fusion |
| Integration | 3-4 days | Medium | Existing codebase |
| Testing & optimization | 5-7 days | Medium-High | Test data |

**Total**: ~6-8 weeks (part-time) or 3-4 weeks (full-time)

***

## **Success Metrics**

1. **Coverage**: % of verses with extracted entities (target: >80%)
2. **Accuracy**: Entity extraction precision (target: >85%)
3. **Performance**: Query latency (target: <5s for hybrid search)
4. **Quality**: User satisfaction with graph-enhanced answers
5. **Complexity**: Support for multi-hop queries (target: 3+ hops)

***

## **Risks & Mitigation**

| Risk | Impact | Mitigation |
|------|--------|------------|
| Entity extraction errors | Medium | Human review + iterative refinement |
| Graph becomes too large | High | Pruning strategies, pagination |
| Performance degradation | Medium | Indexing, caching, query optimization |
| LLM API costs | Medium | Use local LM Studio, batch processing |
| Schema evolution | Low | Version graph schema, migration scripts |

***

## **Next Steps (This Week)**

1. **Review this plan** and prioritize features
2. **Set up Neo4j** locally with Docker
3. **Design initial graph schema** for top 10 entities
4. **Create entity extraction prompt** and test on 5-10 sample verses
5. **Build minimal graph** with sample data to validate approach

***

This plan gives you a comprehensive roadmap. We can start with Phase 1-2 this week and iterate from there. Would you like to begin with setting up Neo4j and designing the initial graph schema?

Sources
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
- `make format`: Format code using `black` and `ruff`.
- `make check`: Run type checks using `mypy`.
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

### Generate & Test
- `make -f Makefile-docker docker-generate`: Generate prompts inside Docker.
- `make -f Makefile-docker docker-test`: Run the full test suite inside Docker.
- `make -f Makefile-docker docker-test-lang L=<lang_code>`: Test a specific language (e.g., `L=hi`).
- `make -f Makefile-docker docker-test-category C=<category_name>`: Test a specific category (e.g., `C=ramayana`).

### Analysis & Report
- `make -f Makefile-docker docker-analyze`: Analyze test results.
- `make -f Makefile-docker docker-report`: Generate comprehensive report.

### Workflows
- `make -f Makefile-docker docker-workflow`: Full workflow: generate → test → report.
- `make -f Makefile-docker docker-workflow-quick`: Quick workflow version.

### Knowledge Graph
- `make -f Makefile-docker docker-graph-build`: Build knowledge graph.

### Testing
- `make -f Makefile-docker docker-test-unit`: Run unit tests.
- `make -f Makefile-docker docker-test-functional`: Run functional tests.
- `make -f Makefile-docker docker-test-integration`: Run integration tests.
- `make -f Makefile-docker docker-test-e2e`: Run E2E tests.
- `make -f Makefile-docker docker-test-all`: Run all tests.
- `make -f Makefile-docker docker-test-cleanup`: Clean up the test environment.

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

### MCP Server
- `make -f Makefile-docker mcp-build`: Build MCP containers.
- `make -f Makefile-docker mcp-up`: Start MCP services.
- `make -f Makefile-docker mcp-down`: Stop MCP services.
- `make -f Makefile-docker mcp-logs`: View logs.
- `make -f Makefile-docker mcp-test`: Run MCP unit tests.
- `make -f Makefile-docker mcp-int`: Run MCP integration tests.