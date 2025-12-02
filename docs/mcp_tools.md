# VidwaanAI MCP Tools Documentation

This document lists the tools available in the VidwaanAI MCP Server.

## Language Tools

### `detect_language`
Detects the language of the given query.
- **Input**: `query` (str)
- **Output**: `{language_code, language_name, confidence}`

### `preprocess_text`
Preprocesses text for a specific language.
- **Input**: `text` (str), `language` (str)
- **Output**: `{normalized_text, tokens}`

### `get_supported_languages`
Returns a list of supported languages.
- **Output**: `[{code, name}]`

## Search Tools

### `search_documents`
Searches for documents using embeddings.
- **Input**: `embedding` (list), `language` (str), `top_k` (int)
- **Output**: `[documents]`

### `hybrid_search`
Performs hybrid search (Semantic + BM25).
- **Input**: `query` (str), `bm25_weight` (float)
- **Output**: `[documents]`

### `generate_embeddings`
Generates embeddings for text.
- **Input**: `text` (str), `language` (str)
- **Output**: `{embedding, model}`

## Reranking Tools

### `rerank_results`
Reranks search results.
- **Input**: `query` (str), `results` (list), `strategy` (str)
- **Output**: `[reranked_results]`

## Knowledge Graph Tools

### `query_knowledge_graph`
Queries the Knowledge Graph.
- **Input**: `query` (str), `language` (str)
- **Output**: `[entities/relations]`

### `find_related_documents`
Finds related documents via KG.
- **Input**: `document_id` (str)
- **Output**: `[documents]`

### `get_entity_context`
Gets context for an entity.
- **Input**: `entity` (str), `entity_type` (str)
- **Output**: `{context}`

## Generation Tools

### `generate_answer`
Generates an answer from context.
- **Input**: `context` (list), `query` (str), `language` (str)
- **Output**: `{answer, citations}`

### `summarize_results`
Summarizes documents.
- **Input**: `documents` (list), `language` (str)
- **Output**: `{summary}`

### `translate_answer`
Translates an answer.
- **Input**: `answer` (str), `target_language` (str)
- **Output**: `{translated_text}`

## Pipeline Tools

### `execute_rag_pipeline`
Executes the full RAG pipeline.
- **Input**: `query` (str), `config` (dict)
- **Output**: `{answer, sources, steps}`
