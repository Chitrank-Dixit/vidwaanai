from typing import Any, Dict, List

from src.core.profiler import profile_function


class TextChunker:
    """Splits text into chunks with overlap."""

    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    @profile_function
    def chunk_text(self, text: str) -> List[str]:
        """Split text into overlapping chunks."""
        if not text:
            return []

        if len(text) <= self.chunk_size:
            return [text]

        chunks = []
        start = 0

        while start < len(text):
            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk)

            # Move start pointer, accounting for overlap
            start += self.chunk_size - self.chunk_overlap

            # Prevent infinite loop if overlap >= chunk_size (though init should prevent this)
            if self.chunk_overlap >= self.chunk_size:
                start += 1

        return chunks

    def create_documents(self, text: str, metadata: Dict[str, Any]) -> List[Any]:
        """Create document objects with metadata (mock implementation)."""
        # In a real scenario, this would return Document objects
        # For now, we'll return a simple object or dict
        chunks = self.chunk_text(text)
        documents = []

        class Document:
            def __init__(self, text, metadata):
                self.text = text
                self.metadata = metadata

        for chunk in chunks:
            documents.append(Document(chunk, metadata.copy()))

        return documents
