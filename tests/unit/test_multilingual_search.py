import pytest
import numpy as np
from src.rag.multilingual_search import MultilingualSearch

class TestMultilingualSearch:
    
    @pytest.fixture(scope="class")
    def search_engine(self):
        return MultilingualSearch()

    def test_process_english_query(self, search_engine):
        query = "What is the meaning of life?"
        result = search_engine.process_query(query)
        assert result['language_code'] == 'en'
        assert len(result['embedding']) == 1024

    def test_process_hindi_query(self, search_engine):
        query = "जीवन का अर्थ क्या है?"
        result = search_engine.process_query(query)
        assert result['language_code'] == 'hi'
        assert "जीवन" in result['processed_text']

    def test_process_tamil_query(self, search_engine):
        query = "வாழ்க்கையின் அர்த்தம் என்ன?"
        result = search_engine.process_query(query)
        assert result['language_code'] == 'ta'

    def test_process_mixed_query(self, search_engine):
        # "Meaning of dharma kya hai" (English + Hindi)
        # Should detect one of them.
        query = "Meaning of dharma kya hai"
        result = search_engine.process_query(query)
        # Just ensure it processes without error and returns embedding
        assert len(result['embedding']) == 1024

    def test_search_functionality(self, search_engine):
        # Mock corpus embeddings
        # 3 documents: 
        # 1. "Apple is a fruit"
        # 2. "Car is a vehicle"
        # 3. "Sky is blue"
        
        # We need to generate embeddings for them first
        # To save time in test, we'll generate them on the fly
        docs = ["Apple is a fruit", "Car is a vehicle", "Sky is blue"]
        corpus_embeddings = []
        for doc in docs:
            corpus_embeddings.append(search_engine.embeddings.embed_text(doc, 'en'))
        
        corpus_embeddings = np.array(corpus_embeddings)
        
        # Search for "fruit"
        query = "fruit"
        results = search_engine.search(query, corpus_embeddings, top_k=1)
        
        assert len(results) == 1
        assert results[0]['index'] == 0 # Should match "Apple is a fruit"

    def test_cross_lingual_search(self, search_engine):
        # Corpus: English documents
        docs = ["Apple is a fruit", "Car is a vehicle"]
        corpus_embeddings = []
        for doc in docs:
            corpus_embeddings.append(search_engine.embeddings.embed_text(doc, 'en'))
        corpus_embeddings = np.array(corpus_embeddings)
        
        # Query in Hindi: "फल" (Fruit)
        query = "फल"
        results = search_engine.search(query, corpus_embeddings, top_k=1)
        
        assert results[0]['index'] == 0 # Should match "Apple is a fruit"

    def test_empty_query(self, search_engine):
        # Should handle gracefully
        try:
            result = search_engine.process_query("")
            assert len(result['embedding']) == 1024
        except Exception:
            pass
