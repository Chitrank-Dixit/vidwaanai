import pytest
from unittest.mock import MagicMock, patch
import numpy as np
from src.rag.embeddings import EmbeddingManager

class TestEmbeddingManager:
    
    @pytest.fixture
    def embedding_manager(self):
        with patch('src.rag.embeddings.SentenceTransformer') as mock_model:
            # Mock the encode method to return a dummy vector
            mock_model.return_value.encode.return_value = np.array([0.1] * 384)
            manager = EmbeddingManager(model_name="all-MiniLM-L6-v2", use_onnx=False)
            return manager

    def test_initialization(self, embedding_manager):
        assert embedding_manager.model is not None
        assert embedding_manager.embedding_dim == 768

    def test_embed_text(self, embedding_manager):
        text = "This is a test sentence."
        embedding = embedding_manager.embed_text(text)
        
        assert isinstance(embedding, list)
        assert len(embedding) == 384
        assert embedding[0] == 0.1

    def test_embed_batch(self, embedding_manager):
        texts = ["Sentence 1", "Sentence 2"]
        
        # Mock batch encoding
        with patch.object(embedding_manager.model, 'encode') as mock_encode:
            mock_encode.return_value = np.array([[0.1] * 384, [0.2] * 384])
            
            embeddings = embedding_manager.embed_batch(texts)
            
            assert len(embeddings) == 2
            assert len(embeddings[0]) == 384
            assert embeddings[0][0] == 0.1
            assert embeddings[1][0] == 0.2
