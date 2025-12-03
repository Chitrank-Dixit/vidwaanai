from typing import List, Dict, Any
from src.rag.multilingual_search import MultilingualSearch
from src.core.logger import get_logger

logger = get_logger(__name__)


class CrosslingualSearch:
    """
    Search across languages
    e.g., query in Hindi, get results in English (or other languages)
    """

    def __init__(self, multilingual_search: MultilingualSearch):
        self.multilingual_search = multilingual_search

    def search_across_languages(
        self,
        query: str,
        target_languages: List[str],
        corpus_embeddings: Any,
        top_k: int = 10,
    ) -> Dict[str, List[Dict]]:
        """
        Search for same concept across multiple languages.

        Args:
            query: The search query (in any language)
            target_languages: List of language codes to filter results by (if corpus supports it)
            corpus_embeddings: The embeddings to search against
            top_k: Number of results per language

        Returns:
            Dictionary mapping language code to list of results
        """
        # Process query once
        query_data = self.multilingual_search.process_query(query)
        # query_embedding = query_data['embedding'] # Not used directly here, search uses it internally

        # Perform search
        # Note: In a real system with language-segmented indices, we would query specific indices.
        # Here, assuming a single shared embedding space (which e5-large provides),
        # we search the whole corpus and then filter/group by language if metadata allows.
        # Since our current DB setup mixes everything, we'll just do a standard search
        # and let the semantic similarity handle the cross-lingual matching.

        results = self.multilingual_search.search(
            query, corpus_embeddings, top_k=top_k * len(target_languages)
        )

        # Group by language (if we had language metadata in results)
        # For now, we just return the raw results as they are already cross-lingual

        return {"mixed": results}
