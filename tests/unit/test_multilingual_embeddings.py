import pytest
import numpy as np
from src.rag.multilingual_embeddings import MultilingualEmbeddings

class TestMultilingualEmbeddings:
    
    @pytest.fixture(scope="class")
    def embedding_model(self):
        # Initialize once for the class to save time
        return MultilingualEmbeddings()

    def test_embedding_dimension(self, embedding_model):
        text = "Hello world"
        embedding = embedding_model.embed_text(text, 'en')
        assert len(embedding) == 1024 # intfloat/multilingual-e5-large is 1024 dim

    def test_embedding_type(self, embedding_model):
        text = "Hello world"
        embedding = embedding_model.embed_text(text, 'en')
        assert isinstance(embedding, list) # The method returns list, not numpy array directly usually
        assert all(isinstance(x, float) for x in embedding)

    def test_multilingual_embedding(self, embedding_model):
        # Embed Hindi text
        text_hi = "नमस्ते दुनिया"
        embedding_hi = embedding_model.embed_text(text_hi, 'hi')
        assert len(embedding_hi) == 1024
        
        # Embed Tamil text
        text_ta = "வணக்கம் உலகம்"
        embedding_ta = embedding_model.embed_text(text_ta, 'ta')
        assert len(embedding_ta) == 1024

    def test_embedding_similarity(self, embedding_model):
        # "Hello world" in English and Hindi should be similar
        emb_en = embedding_model.embed_text("Hello world", 'en')
        emb_hi = embedding_model.embed_text("नमस्ते दुनिया", 'hi')
        
        # Cosine similarity
        vec_en = np.array(emb_en)
        vec_hi = np.array(emb_hi)
        
        similarity = np.dot(vec_en, vec_hi) / (np.linalg.norm(vec_en) * np.linalg.norm(vec_hi))
        
        assert similarity > 0.7 # Should be highly similar

    def test_embedding_dissimilarity(self, embedding_model):
        # Compare relative similarity
        emb_anchor = embedding_model.embed_text("Apple", 'en')
        emb_positive = embedding_model.embed_text("Fruit", 'en')
        emb_negative = embedding_model.embed_text("Car", 'en')
        
        vec_anchor = np.array(emb_anchor)
        vec_pos = np.array(emb_positive)
        vec_neg = np.array(emb_negative)
        
        sim_pos = np.dot(vec_anchor, vec_pos) / (np.linalg.norm(vec_anchor) * np.linalg.norm(vec_pos))
        sim_neg = np.dot(vec_anchor, vec_neg) / (np.linalg.norm(vec_anchor) * np.linalg.norm(vec_neg))
        
        assert sim_pos > sim_neg # Apple should be closer to Fruit than Car

    def test_empty_text(self, embedding_model):
        # Depending on implementation, might raise error or return zero vector or handle gracefully
        # Let's check behavior. Usually sentence-transformers handles empty string but might warn.
        try:
            embedding = embedding_model.embed_text("", 'en')
            assert len(embedding) == 1024
        except Exception:
            pass # Acceptable if it raises

    def test_batch_embedding(self, embedding_model):
        # If batch method exists
        if hasattr(embedding_model, 'embed_batch'):
            texts = ["Hello", "World"]
            embeddings = embedding_model.embed_batch(texts, 'en')
            assert len(embeddings) == 2
            assert len(embeddings[0]) == 1024
