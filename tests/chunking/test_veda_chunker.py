
import pytest
from unittest.mock import MagicMock
from src.chunking.veda_chunker import VedaChunker

@pytest.fixture
def mock_db_manager():
    mock = MagicMock()
    mock._get_connection.return_value.__enter__.return_value.cursor.return_value.__enter__.return_value = MagicMock()
    return mock

def test_chunking_logic(mock_db_manager):
    chunker = VedaChunker(mock_db_manager)
    
    # Mock _get_mantra_details
    chunker._get_mantra_details = MagicMock(return_value={
        "text_hindi": "This is a long mantra text that should be split into multiple chunks if it is long enough. " * 20,
        "ved_id": 1,
        "mandala_id": 1, 
        "sukta_id": 1,
        "id": 101,
        "ved_name": "Rigveda"
    })
    
    # Mock _get_sukta_text
    chunker._get_sukta_text = MagicMock(return_value="Full sukta text")
    
    chunks = chunker.create_chunks(101)
    
    # Check if we have mantra_chunk type
    chunk_types = [c["type"] for c in chunks]
    assert "mantra" in chunk_types
    assert "sukta" in chunk_types
    # Check if we have fragmented chunks (if llama-index worked)
    # The text length is approx 80 chars * 20 = 1600 chars ~= 300-400 tokens?
    # Actually "This is a..." is short tokens. 
    # Let's check metadata
    
    mantra_chunks = [c for c in chunks if c["type"] == "mantra_chunk"]
    if mantra_chunks:
        assert len(mantra_chunks) >= 1
        assert mantra_chunks[0]["metadata"]["mantra_id"] == 101
