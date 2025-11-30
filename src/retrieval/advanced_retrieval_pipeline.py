from typing import List, Dict, Any
from src.retrieval.hybrid_search import HybridSearch
from src.retrieval.reranker import ContextAwareReranker
from src.retrieval.fuzzy_matcher import FuzzyMatcher
from src.retrieval.synonym_handler import SynonymHandler
from src.core.logger import get_logger

logger = get_logger(__name__)

class AdvancedRetrievalPipeline:
    def __init__(self, hybrid_search: HybridSearch):
        self.hybrid_search = hybrid_search
        self.reranker = ContextAwareReranker()
        self.fuzzy_matcher = FuzzyMatcher()
        self.synonym_handler = SynonymHandler()
        
        # Known terms for typo correction (could be loaded from DB/corpus)
        self.known_terms = list(self.synonym_handler.synonyms.keys())
        # Add more terms from corpus if available
        # self.known_terms.extend(...)
    
    def retrieve(self, query: str, top_k: int = 10) -> List[Dict[str, Any]]:
        """Complete retrieval pipeline"""
        logger.info(f"Processing query: {query}")
        
        # Step 1: Correct typos
        corrected_query = self.fuzzy_matcher.correct_query(query, self.known_terms)
        if corrected_query != query:
            logger.info(f"Corrected query: {corrected_query}")
        
        # Step 2: Expand with synonyms
        expanded_query = self.synonym_handler.expand_query(corrected_query)
        logger.info(f"Expanded query: {expanded_query}")
        
        # Step 3: Hybrid search
        # Fetch more results to allow for reranking
        results = self.hybrid_search.search(expanded_query, top_k=top_k*3)
        logger.info(f"Hybrid search returned {len(results)} results")
        
        # Step 4: Rerank with cross-encoder
        # Use corrected query (not expanded) for reranking as it's more precise
        reranked = self.reranker.rerank(corrected_query, results, top_k=top_k)
        
        return reranked
