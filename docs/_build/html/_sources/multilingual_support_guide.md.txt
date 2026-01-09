# Multilingual Support Guide

VidwaanAI now supports 5 major Indian languages alongside English. This guide explains the architecture and how to add new languages.

## Supported Languages

| Language | Code | Script |
|----------|------|--------|
| English  | en   | Latin  |
| Hindi    | hi   | Devanagari |
| Gujarati | gu   | Gujarati |
| Tamil    | ta   | Tamil  |
| Telugu   | te   | Telugu |
| Kannada  | kn   | Kannada |

## Architecture

### 1. Language Detection
- **Module**: `src/language/language_detector.py`
- **Method**: Uses `langdetect` library combined with Unicode script analysis for high accuracy.
- **Usage**: Automatically detects language of every query.

### 2. Language Processing
- **Base Class**: `LanguageProcessor` in `src/language/language_processor.py`
- **Process**:
    1. **Normalization**: Script-specific cleaning (e.g., removing extra spaces).
    2. **Tokenization**: Splitting text into words using `regex`.
    3. **Stopword Removal**: Removing common words (is, the, etc.) using language-specific lists.
- **Implementations**:
    - `HindiProcessor`
    - `GujaratiProcessor`
    - `TamilProcessor`
    - `TeluguProcessor`
    - `KannadaProcessor`

### 3. Multilingual Embeddings
- **Model**: `intfloat/multilingual-e5-large`
- **Dimension**: 1024
- **Capability**: Maps text from all supported languages into a shared semantic space, enabling cross-lingual search (e.g., Hindi query finding relevant English or Sanskrit verses).

### 4. Multilingual Search Orchestrator
- **Module**: `src/rag/multilingual_search.py`
- **Role**: Coordinates detection, processing, and embedding.

## Adding a New Language

1.  **Update Detector**: Add language code and script range to `LanguageDetector.SUPPORTED_LANGUAGES` and `detect_script`.
2.  **Create Processor**: Create `src/language/{lang}_processor.py` inheriting from `LanguageProcessor`.
    - Define stop words.
    - Implement `normalize`, `tokenize`, `remove_stopwords`.
3.  **Register Processor**: Add new processor to `MultilingualSearch.processors` dict.

## Performance
- **Latency**: < 3 seconds per query.
- **Accuracy**: > 95% language detection accuracy.
