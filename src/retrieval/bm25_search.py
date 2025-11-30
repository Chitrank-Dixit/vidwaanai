from rank_bm25 import BM25Okapi
import numpy as np
from typing import List, Dict, Any
from src.core.logger import get_logger

logger = get_logger(__name__)

class BM25Search:
    def __init__(self, corpus: List[Dict[str, Any]]):
        """
        Initialize BM25 search.
        
        Args:
            corpus: List of dictionaries containing 'text' and 'id' keys.
        """
        self.corpus = corpus
        self.doc_texts = [doc['text'] for doc in corpus]
        self.tokenized_corpus = [self._tokenize(text) for text in self.doc_texts]
        
        logger.info(f"Initializing BM25 with {len(corpus)} documents")
        self.bm25 = BM25Okapi(self.tokenized_corpus)
    
    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization."""
        return text.lower().split()
    
    def search(self, query: str, top_k: int = 10) -> List[Dict[str, Any]]:
        """
        Search using BM25.
        
        Returns:
            List of dicts with 'id', 'score', 'text', and other metadata.
        """
        tokenized_query = self._tokenize(query)
        scores = self.bm25.get_scores(tokenized_query)
        
        # Get top_k indices
        top_indices = np.argsort(scores)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            score = float(scores[idx])
            if score > 0:
                doc = self.corpus[idx].copy()
                doc['score'] = score
                results.append(doc)
        
        return results
