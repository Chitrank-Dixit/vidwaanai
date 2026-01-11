# System Architecture

The following diagram illustrates the high-level architecture of the VidwaanAI system, referencing the key services and components described in the documentation.

```{mermaid}
graph TD
    %% Nodes
    Client[Client CLI / Web / MCP Client]
    
    subgraph "API Layer"
        FastAPI[FastAPI Server :8000]
        MCPServer[MCP Server :8001]
    end
    
    subgraph "Application Core"
        AgentOrchestrator[Agent Orchestrator]
        RAGPipeline[RAG Pipeline]
        GraphReasoning[Graph Reasoning Engine]
    end
    
    subgraph "Data Layer"
        Postgres[(PostgreSQL + pgvector)]
        Neo4j[(Neo4j Graph DB)]
        Redis[(Redis Cache)]
        FileSystem[File System / Storage]
    end
    
    subgraph "External Services"
        LLMProvider[LLM Provider (OpenAI/Anthropic/Local)]
    end

    %% Edge Connections
    Client -->|REST API| FastAPI
    Client -->|MCP Protocol| MCPServer
    
    FastAPI --> AgentOrchestrator
    MCPServer --> AgentOrchestrator
    
    AgentOrchestrator --> RAGPipeline
    AgentOrchestrator --> GraphReasoning
    
    RAGPipeline -->|Vector Search| Postgres
    RAGPipeline -->|Embeddings| LLMProvider
    RAGPipeline -->|Cache| Redis
    
    GraphReasoning -->|Cypher Queries| Neo4j
    GraphReasoning -->|Reasoning| LLMProvider
    
    AgentOrchestrator -->|Inference| LLMProvider
    
    %% Ingestion Flow
    subgraph "Ingestion Pipeline"
        IngestionWorker[Ingestion Worker]
        OCR[OCR / Text Extraction]
    end
    
    FileSystem --> IngestionWorker
    IngestionWorker --> OCR
    OCR --> RAGPipeline
    OCR --> GraphReasoning
```

## Component Description

### Client Layer
- **CLI**: The primary interface involves a Typer-based command-line tool.
- **MCP Client**: Supports integration with AI assistants like Claude via the Model Context Protocol.

### API Layer
- **FastAPI**: Handles RESTful requests for queries, management, and ingestion.
- **MCP Server**: Exposes tools (search, rag, graph) to MCP-compatible clients.

### Application Core
- **Agent Orchestrator**: Manages the flow of information between the user, the LLM, and tools.
- **RAG Pipeline**: Implements Retrieval-Augmented Generation using vector search.
- **Graph Reasoning Engine**: Performs multi-hop reasoning on the Knowledge Graph.

### Data Layer
- **PostgreSQL**: Stores structured data and vector embeddings (using `pgvector`).
- **Neo4j**: Stores the semantic knowledge graph (entities and relationships).
- **Redis**: Caches LLM responses and frequent queries.
