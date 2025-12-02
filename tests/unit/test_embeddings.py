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
            # Mock dimension
            mock_model.return_value.get_sentence_embedding_dimension.return_value = 384
            
            manager = EmbeddingManager(model_name="all-MiniLM-L6-v2")
            return manager

    def test_initialization(self, embedding_manager):
        assert embedding_manager.model is not None
        assert embedding_manager.embedding_dim == 384

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

    def test_embed_text_list_input(self, embedding_manager):
        """Test embed_text with list input"""
        texts = ["Text 1", "Text 2"]
        with patch.object(embedding_manager.model, 'encode') as mock_encode:
            mock_encode.return_value = np.array([[0.1]*384, [0.2]*384])
            
            embeddings = embedding_manager.embed_text(texts)
            assert isinstance(embeddings, list)
            assert len(embeddings) == 2
            assert len(embeddings[0]) == 384

    def test_similarity(self):
        """Test similarity calculation"""
        vec1 = [1.0, 0.0, 0.0]
        vec2 = [1.0, 0.0, 0.0]
        vec3 = [0.0, 1.0, 0.0]
        
        # Exact match
        sim1 = EmbeddingManager.similarity(vec1, vec2)
        assert abs(sim1 - 1.0) < 0.0001
        
        # Orthogonal
        sim2 = EmbeddingManager.similarity(vec1, vec3)
        assert abs(sim2 - 0.0) < 0.0001
        
        # Zero vector handling
        sim3 = EmbeddingManager.similarity(vec1, [0.0, 0.0, 0.0])
        assert sim3 == 0.0

    def test_embed_text_error(self, embedding_manager):
        """Test error handling in embed_text"""
        with patch.object(embedding_manager.model, 'encode', side_effect=Exception("Model error")):
            with pytest.raises(Exception) as exc:
                embedding_manager.embed_text("text")
            assert "Model error" in str(exc.value)

    def test_embed_batch_error(self, embedding_manager):
        """Test error handling in embed_batch"""
        with patch.object(embedding_manager.model, 'encode', side_effect=Exception("Batch error")):
            with pytest.raises(Exception) as exc:
                embedding_manager.embed_batch(["text"])
            assert "Batch error" in str(exc.value)

    def test_initialization_error(self):
        """Test initialization error"""
        with patch('src.rag.embeddings.SentenceTransformer', side_effect=Exception("Init failed")):
            with pytest.raises(Exception) as exc:
                EmbeddingManager()
            assert "Init failed" in str(exc.value)
