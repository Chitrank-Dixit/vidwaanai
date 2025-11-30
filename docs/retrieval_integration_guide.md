# Retrieval Integration Guide

This guide explains how to use and configure the advanced retrieval system in VidwaanAI.

## Architecture

The retrieval pipeline consists of 4 stages:
1.  **Preprocessing**:
    - **Typo Correction**: `FuzzyMatcher` fixes spelling mistakes.
    - **Query Expansion**: `SynonymHandler` adds related domain terms.
2.  **Retrieval**:
    - **Hybrid Search**: Combines BM25 and Vector Search scores.
3.  **Post-processing**:
    - **Reranking**: `ContextAwareReranker` uses a cross-encoder to re-score the top results.

## Configuration

### Enabling/Disabling Components
The pipeline is initialized in `VidwaanAI` agent (`src/agent/vidwaan_agent.py`).

```python
# Initialize Advanced Pipeline
self.retrieval_pipeline = AdvancedRetrievalPipeline(self.hybrid_retriever)
```

To disable specific components, modify `src/retrieval/advanced_retrieval_pipeline.py`:

```python
class AdvancedRetrievalPipeline:
    def __init__(self, hybrid_search):
        # Comment out to disable
        self.reranker = ContextAwareReranker() 
        self.fuzzy_matcher = FuzzyMatcher()
        self.synonym_handler = SynonymHandler()
```

### Tuning Parameters

- **Fuzzy Matcher Threshold**: In `src/retrieval/fuzzy_matcher.py`, default is `0.8`. Increase for stricter matching.
- **Hybrid Weights**: In `src/retrieval/hybrid_search.py`, default `bm25_weight=0.3`, `semantic_weight=0.7`.
- **Reranker Model**: In `src/retrieval/reranker.py`, default is `cross-encoder/ms-marco-MiniLM-L-6-v2`.

## Debugging

Enable verbose logging to see pipeline steps:

```python
logger.setLevel(logging.INFO)
```

Logs will show:
- Corrected query
- Expanded query terms
- Hybrid search results count
- Reranking scores
