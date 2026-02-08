# Source Material Chunking Strategy

## 1. Data Sources
The project will process scripture data from the following directories in `data/`:
- `data/vedas/`
- `data/puranas/`
- `data/ramayan/`
- `data/mahabharat/`
- `data/bhagwat_geeta/`

## 2. Chunking Methodologies

### 2.1. Structured Data (JSON)
*Target: `bhagavat_gita.json` and similar pre-processed files.*
- **Method**: Logical grouping by Chapter or Canto.
- **Size**: 1 Chapter per chunk (or groups of 20 verses if chapters are long).
- **Context**: Include metadata (Book Name, Chapter Number) in each chunk prompt.

### 2.2. Unstructured Text (TXT)
*Target: Raw text files.*
- **Method**: Sliding window or paragraph-based chunking.
- **Size**: ~1500-2000 tokens per chunk.
- **Overlap**: 200 tokens to maintain context across boundaries.

### 2.3. PDF Documents
*Target: Scanned or digital PDFs.*
- **Method**: Page-level extraction (using OCR if needed).
- **Size**: 1-3 pages per query, depending on density.
- **Preprocessing**: Remove headers/footers before processing.

## 3. Execution Plan
1. **Catalog**: Script will list all files in target directories.
2. **Pre-process**: Convert non-text formats to text (if necessary) or extract text.
3. **Partition**: Split text into `ontology_project/source_materials/chunks/` with naming convention `[scripture_code]_[chunk_id].txt`.
