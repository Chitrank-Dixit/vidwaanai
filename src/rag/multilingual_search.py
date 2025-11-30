from typing import List, Dict, Any
import numpy as np
from src.language.language_detector import LanguageDetector
from src.language.hindi_processor import HindiProcessor
from src.language.gujarati_processor import GujaratiProcessor
from src.language.tamil_processor import TamilProcessor
from src.language.telugu_processor import TeluguProcessor
from src.language.kannada_processor import KannadaProcessor
from src.rag.multilingual_embeddings import MultilingualEmbeddings
from src.core.logger import get_logger

logger = get_logger(__name__)

class MultilingualSearch:
    def __init__(self):
        self.detector = LanguageDetector()
        self.embeddings = MultilingualEmbeddings()
        self.processors = {
            'hi': HindiProcessor(),
            'gu': GujaratiProcessor(),
            'ta': TamilProcessor(),
            'te': TeluguProcessor(),
            'kn': KannadaProcessor()
        }
    
    def process_query(self, query: str) -> Dict[str, Any]:
        """Process query for any language"""
        # Detect language
        lang_code, lang_name, confidence = self.detector.detect_language(query)
        logger.info(f"Detected language: {lang_name} ({lang_code}) with confidence {confidence}")
        
        # Get processor for language
        processor = self.processors.get(lang_code)
        
        # Preprocess if processor exists
        if processor:
            processed_data = processor.preprocess(query)
            processed_text = processed_data['processed_text']
        else:
            processed_text = query
        
        # Generate embedding
        embedding = self.embeddings.embed_text(query, lang_code)
        
        return {
            'original_query': query,
            'language': lang_name,
            'language_code': lang_code,
            'confidence': confidence,
            'processed_text': processed_text,
            'embedding': embedding
        }
    
    def search(self, query: str, corpus_embeddings: np.ndarray, top_k: int = 10) -> List[Dict[str, Any]]:
        """
        Search across multilingual corpus.
        Note: This assumes corpus_embeddings is a numpy array of all document embeddings.
        In a real DB scenario, we would pass the query embedding to the DB.
        This method is useful for in-memory search or re-ranking.
        """
        # Process query
        query_data = self.process_query(query)
        query_embedding = np.array(query_data['embedding'])
        
        # Calculate similarities
        similarities = np.dot(corpus_embeddings, query_embedding)
        
        # Get top-k results
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            results.append({
                'index': int(idx),
                'similarity': float(similarities[idx])
            })
        
        return results
