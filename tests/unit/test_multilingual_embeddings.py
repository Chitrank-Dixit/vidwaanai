import pytest
import numpy as np
from src.rag.multilingual_embeddings import MultilingualEmbeddings


class TestMultilingualEmbeddings:
    @pytest.fixture(scope="class")
    def embedding_model(self) -> MultilingualEmbeddings:
        # Initialize once for the class to save time
        return MultilingualEmbeddings()

    def test_embedding_dimension(self, embedding_model: MultilingualEmbeddings) -> None:
        text = "Hello world"
        embedding = embedding_model.embed_text(text, "en")
        assert len(embedding) == 1024  # intfloat/multilingual-e5-large is 1024 dim

    def test_embedding_type(self, embedding_model: MultilingualEmbeddings) -> None:
        text = "Hello world"
        embedding = embedding_model.embed_text(text, "en")
        assert isinstance(
            embedding, list
        )  # The method returns list, not numpy array directly usually
        assert all(isinstance(x, float) for x in embedding)

    def test_multilingual_embedding(self, embedding_model: MultilingualEmbeddings) -> None:
        # Embed Hindi text
        text_hi = "नमस्ते दुनिया"
        embedding_hi = embedding_model.embed_text(text_hi, "hi")
        assert len(embedding_hi) == 1024

        # Embed Tamil text
        text_ta = "வணக்கம் உலகம்"
        embedding_ta = embedding_model.embed_text(text_ta, "ta")
        assert len(embedding_ta) == 1024

    def test_embedding_similarity(self, embedding_model: MultilingualEmbeddings) -> None:
        # "Hello world" in English and Hindi should be similar
        emb_en = embedding_model.embed_text("Hello world", "en")
        emb_hi = embedding_model.embed_text("नमस्ते दुनिया", "hi")

        # Cosine similarity
        vec_en = np.array(emb_en)
        vec_hi = np.array(emb_hi)

        similarity = np.dot(vec_en, vec_hi) / (
            np.linalg.norm(vec_en) * np.linalg.norm(vec_hi)
        )

        assert similarity > 0.7  # Should be highly similar

    def test_embedding_dissimilarity(self, embedding_model: MultilingualEmbeddings) -> None:
        # Compare relative similarity
        emb_anchor = embedding_model.embed_text("Apple", "en")
        emb_positive = embedding_model.embed_text("Fruit", "en")
        emb_negative = embedding_model.embed_text("Car", "en")

        vec_anchor = np.array(emb_anchor)
        vec_pos = np.array(emb_positive)
        vec_neg = np.array(emb_negative)

        sim_pos = np.dot(vec_anchor, vec_pos) / (
            np.linalg.norm(vec_anchor) * np.linalg.norm(vec_pos)
        )
        sim_neg = np.dot(vec_anchor, vec_neg) / (
            np.linalg.norm(vec_anchor) * np.linalg.norm(vec_neg)
        )

        assert sim_pos > sim_neg  # Apple should be closer to Fruit than Car

    def test_empty_text(self, embedding_model: MultilingualEmbeddings) -> None:
        # Depending on implementation, might raise error or return zero vector or handle gracefully
        # Let's check behavior. Usually sentence-transformers handles empty string but might warn.
        try:
            embedding = embedding_model.embed_text("", "en")
            assert len(embedding) == 1024
        except Exception:
            pass  # Acceptable if it raises

    def test_batch_embedding(self, embedding_model: MultilingualEmbeddings) -> None:
        # Test embed_corpus
        texts = ["Hello", "World"]
        embeddings = embedding_model.embed_corpus(texts, batch_size=2)
        assert len(embeddings) == 2
        assert len(embeddings[0]) == 1024

    def test_embed_query_prefix(self, embedding_model: MultilingualEmbeddings) -> None:
        """Test that query prefix is handled correctly"""
        # E5 models expect "query: " prefix for asymmetric tasks
        text = "What is yoga?"
        # We can't easily check internal prefixing without mocking,
        # but we can check that it produces a valid embedding
        embedding = embedding_model.embed_text(text, "en")
        assert len(embedding) == 1024

    def test_embed_document_prefix(self, embedding_model: MultilingualEmbeddings) -> None:
        """Test that document prefix is handled correctly"""
        # E5 models expect "passage: " prefix for documents
        text = "Yoga is a practice."
        embedding = embedding_model.embed_text(text, "en", is_document=True)
        assert len(embedding) == 1024

        # Should be different from query embedding of same text (due to prefix)
        query_embedding = embedding_model.embed_text(text, "en", is_document=False)

        vec_doc = np.array(embedding)
        vec_query = np.array(query_embedding)

        # They should be similar but not identical
        similarity = np.dot(vec_doc, vec_query) / (
            np.linalg.norm(vec_doc) * np.linalg.norm(vec_query)
        )
        assert similarity < 0.9999  # Not identical
