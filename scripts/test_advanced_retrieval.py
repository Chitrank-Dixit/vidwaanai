import os
import sys
from dotenv import load_dotenv

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

from src.retrieval.advanced_retrieval_pipeline import AdvancedRetrievalPipeline
from src.retrieval.bm25_search import BM25Search
from src.retrieval.hybrid_search import HybridSearch
from src.db.db_manager import DatabaseManager
from src.rag.embeddings import EmbeddingManager
from src.core.logger import get_logger

logger = get_logger(__name__)

def test_pipeline():
    print("\n--- Testing Advanced Retrieval Pipeline ---")
    
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("DATABASE_URL not set")
        return

    db_manager = DatabaseManager(db_url)
    
    # Initialize components
    print("Initializing components...")
    verses = db_manager.get_all_verses()
    bm25_search = BM25Search(verses)
    
    # Use standard embeddings for vector search
    embeddings = EmbeddingManager()
    
    def vector_search_func(query, top_k):
        emb = embeddings.embed_text(query)
        results = db_manager.retrieve_verses(emb, top_k=top_k)
        for r in results:
            r['score'] = r.get('similarity', 0.0)
        return results
        
    hybrid_search = HybridSearch(
        bm25_search=bm25_search,
        vector_search_func=vector_search_func
    )
    
    pipeline = AdvancedRetrievalPipeline(hybrid_search)
    
    # Test cases
    queries = [
        "dharma meaning",          # Simple
        "what is darma?",          # Typo (darma -> dharma)
        "duty of a warrior",       # Synonym (duty -> dharma)
        "krishna arjuna dialogue"  # Complex
    ]
    
    for query in queries:
        print(f"\nQuery: {query}")
        results = pipeline.retrieve(query, top_k=3)
        
        for i, res in enumerate(results):
            print(f"  {i+1}. {res.get('text', '')[:100]}... (Score: {res.get('final_score', res.get('score', 0)):.4f})")

if __name__ == '__main__':
    test_pipeline()
