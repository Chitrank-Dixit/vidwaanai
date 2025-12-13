# Query Types Specification

This document defines the categorization of test queries to ensure diverse and comprehensive evaluation of the VidwaanAI retrieval system.

## 1. Semantic Queries (40%)
**Intent:** Retrieve documents based on meaning, concepts, or themes rather than keywords.
**Example:** "What is the essence of duty?"
**Technique:** Dense retrieval (Embeddings).

## 2. Entity Queries (20%)
**Intent:** Retrieve documents mentioning specific named entities (People, Places, Scriptures).
**Example:** "Verses about Arjuna", "Ayodhya".
**Technique:** Hybrid search (Keyword + Embedding).

## 3. Linguistic Queries (20%)
**Intent:** Test the system's ability to handle specific languages or linguistic features (e.g., untranslated terms).
**Example:** "Dharma satya" (Hindi), "Aram" (Tamil).
**Technique:** Multilingual embeddings.

## 4. Comparative Queries (20%)
**Intent:** Retrieve documents for comparing concepts across different cultures or texts.
**Example:** "Concept of Truth in different Indian languages".
**Technique:** Cross-lingual retrieval.

## Distribution Target (30 Queries)
- **Semantic:** ~12 queries
- **Entity:** ~6 queries
- **Linguistic:** ~6 queries
- **Comparative:** ~6 queries
