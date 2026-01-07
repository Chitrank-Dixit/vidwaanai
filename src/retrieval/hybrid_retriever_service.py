import logging
from typing import List, Dict, Any, Optional

from src.db.db_manager import DatabaseManager
from src.retrieval.bm25_search import BM25Search
from src.retrieval.veda_retriever import VedaRetriever
from src.retrieval.hybrid_search import HybridSearch
from src.embeddings.veda_embedder import VedaEmbedder

logger = logging.getLogger(__name__)


class HybridRetrieverService:
    """
    High-level service for Hybrid Search (BM25 + Vector).
    Manages the lifecycle of BM25 index and Vector retriever.
    """

    def __init__(
        self,
        db_manager: DatabaseManager,
        enable_bm25: bool = True,
        embedder: Optional[VedaEmbedder] = None,
    ):
        self.db_manager = db_manager

        # Initialize Vector Retriever
        self.veda_retriever = VedaRetriever(db_manager, embedder=embedder)

        # Initialize BM25 (lazy load or eager load?)
        # Eager load for MVP: fetch all text from DB
        self.bm25_search: Optional[BM25Search] = None
        if enable_bm25:
            self._initialize_bm25()

        # Initialize Hybrid Search Logic
        # Note: hybrid_search expects a callable for vector_search
        self.hybrid_logic = HybridSearch(
            bm25_search=self.bm25_search,
            vector_search_func=self.veda_retriever.search,
            bm25_weight=0.3,
            semantic_weight=0.7,
        )

    def _initialize_bm25(self) -> None:
        """Fetch all documents and build BM25 index in-memory."""
        logger.info("Initializing BM25 index from Database...")
        try:
            with self.db_manager._get_connection() as conn:
                with conn.cursor() as cursor:
                    # Fetch basic text data
                    cursor.execute(
                        """
                        SELECT id, text_hindi, translation_en, mantra_number 
                        FROM mantras
                    """
                    )
                    rows = cursor.fetchall()

                    corpus = []
                    for row in rows:
                        # Combine text and translation for broader keyword match
                        text_content = f"{row[1]} {row[2]}" if row[2] else row[1]
                        corpus.append(
                            {
                                "id": row[0],
                                "text": text_content,
                                "metadata": {"mantra_num": row[3]},
                            }
                        )

                    if corpus:
                        self.bm25_search = BM25Search(corpus)
                        logger.info(f"BM25 index built with {len(corpus)} documents.")
                    else:
                        logger.warning("No documents found for BM25 index.")
        except Exception as e:
            logger.error(f"Failed to initialize BM25: {e}")

    def search(
        self,
        query: str,
        top_k: int = 10,
        strategy: str = "hybrid",
        fusion_method: str = "weighted",
    ) -> List[Dict[str, Any]]:
        """
        Unified search method.
        strategy: 'hybrid', 'vector', 'keyword'
        """
        if strategy == "vector":
            return self.veda_retriever.search(query, top_k=top_k)

        if strategy == "keyword":
            if self.bm25_search:
                return self.bm25_search.search(query, top_k=top_k)
            else:
                logger.warning("BM25 not initialized, falling back to empty list")
                return []

        # Default to hybrid
        if self.bm25_search:
            return self.hybrid_logic.search(
                query, top_k=top_k, fusion_method=fusion_method
            )
        else:
            logger.warning(
                "BM25 not initialized for hybrid search, falling back to vector"
            )
            return self.veda_retriever.search(query, top_k=top_k)
