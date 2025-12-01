import pytest
from src.rag.chunking import TextChunker

class TestDocumentIngestion:
    
    @pytest.fixture
    def chunker(self):
        return TextChunker(chunk_size=10, chunk_overlap=2)

    def test_chunk_text_basic(self, chunker):
        text = "1234567890"
        chunks = chunker.chunk_text(text)
        assert len(chunks) == 1
        assert chunks[0] == "1234567890"

    def test_chunk_text_split(self, chunker):
        text = "1234567890ABC"
        # Chunk size 10, overlap 2
        # Chunk 1: "1234567890" (0-10)
        # Next start: 10 - 2 = 8
        # Chunk 2: "90ABC" (8-13)
        chunks = chunker.chunk_text(text)
        assert len(chunks) == 2
        assert chunks[0] == "1234567890"
        assert chunks[1] == "90ABC"

    def test_chunk_text_overlap(self):
        chunker = TextChunker(chunk_size=5, chunk_overlap=2)
        text = "ABCDEFG"
        # Chunk 1: "ABCDE" (0-5)
        # Next start: 5 - 2 = 3
        # Chunk 2: "DEFG" (3-7)
        chunks = chunker.chunk_text(text)
        assert len(chunks) == 3
        assert chunks[0] == "ABCDE"
        assert chunks[1] == "DEFG"
        assert chunks[2] == "G"
        # Check overlap
        assert chunks[0][-2:] == chunks[1][:2] # "DE"

    def test_empty_text(self, chunker):
        chunks = chunker.chunk_text("")
        assert chunks == []

    def test_none_text(self, chunker):
        chunks = chunker.chunk_text(None) # type: ignore
        assert chunks == []

    def test_create_documents(self, chunker):
        text = "1234567890ABC"
        metadata = {"source": "test", "id": 1}
        docs = chunker.create_documents(text, metadata)
        
        assert len(docs) == 2
        assert docs[0].text == "1234567890"
        assert docs[0].metadata == metadata
        assert docs[1].text == "90ABC"
        assert docs[1].metadata == metadata
        
        # Verify metadata copy (modifying one shouldn't affect other if deep copy needed, 
        # but here it's shallow copy of dict, which is fine as long as dict itself is new object)
        docs[0].metadata["id"] = 2
        assert docs[1].metadata["id"] == 1 # Wait, check implementation. 
        # Implementation: documents.append(Document(chunk, metadata.copy()))
        # So it IS a copy.
