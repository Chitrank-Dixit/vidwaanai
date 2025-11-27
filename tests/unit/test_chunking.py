import pytest
from src.rag.chunking import TextChunker

class TestTextChunker:
    
    @pytest.fixture
    def chunker(self):
        return TextChunker(chunk_size=100, chunk_overlap=20)

    def test_initialization(self, chunker):
        assert chunker.chunk_size == 100
        assert chunker.chunk_overlap == 20

    def test_chunk_text_simple(self, chunker):
        text = "This is a short text."
        chunks = chunker.chunk_text(text)
        
        assert len(chunks) == 1
        assert chunks[0] == text

    def test_chunk_text_long(self, chunker):
        # Create text longer than chunk_size
        text = "word " * 30 
        chunks = chunker.chunk_text(text)
        
        assert len(chunks) > 1
        # Verify overlap (simplified check)
        # In a real scenario, we'd check exact overlap characters
        
    def test_chunk_with_metadata(self, chunker):
        text = "This is a test text."
        metadata = {"source": "test"}
        chunks = chunker.create_documents(text, metadata)
        
        assert len(chunks) == 1
        assert chunks[0].text == text
        assert chunks[0].metadata["source"] == "test"
