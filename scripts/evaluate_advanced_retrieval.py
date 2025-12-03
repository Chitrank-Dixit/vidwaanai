import json
import os
import sys
from dotenv import load_dotenv

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

from src.evaluation.retriever_evaluator import RetrieverEvaluator  # noqa: E402
from src.retrieval.advanced_retrieval_pipeline import AdvancedRetrievalPipeline  # noqa: E402
from src.retrieval.bm25_search import BM25Search  # noqa: E402
from src.retrieval.hybrid_search import HybridSearch  # noqa: E402
from src.db.db_manager import DatabaseManager  # noqa: E402
from src.rag.embeddings import EmbeddingManager  # noqa: E402
from src.core.logger import get_logger  # noqa: E402

logger = get_logger(__name__)


def run_evaluation():
    logger.info("Starting advanced retrieval evaluation...")

    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        logger.error("DATABASE_URL not set")
        return

    db_manager = DatabaseManager(db_url)
    evaluator = RetrieverEvaluator()

    # Initialize pipeline
    verses = db_manager.get_all_verses()
    bm25_search = BM25Search(verses)
    embeddings = EmbeddingManager()

    def vector_search_func(query, top_k):
        emb = embeddings.embed_text(query)
        results = db_manager.retrieve_verses(emb, top_k=top_k)
        for r in results:
            r["score"] = r.get("similarity", 0.0)
        return results

    hybrid_search = HybridSearch(
        bm25_search=bm25_search, vector_search_func=vector_search_func
    )

    pipeline = AdvancedRetrievalPipeline(hybrid_search)

    # Load test queries
    with open("scripts/test_benchmark_queries.json", "r") as f:
        test_data = json.load(f)

    for test_query in test_data["queries"]:
        query_text = test_query["query"]
        relevant_verses = test_query["relevant_verses"]

        # Use advanced pipeline
        retrieved = pipeline.retrieve(query_text, top_k=20)
        retrieved_ids = [
            str(r.get("id")) for r in retrieved
        ]  # Ensure IDs are strings for comparison

        # Normalize relevant verses to strings if needed (assuming they are strings in json)

        result = evaluator.evaluate_query(query_text, retrieved_ids, relevant_verses)
        evaluator.results.append(result)

    report = evaluator.generate_report()

    print(json.dumps(report, indent=2))

    with open("docs/advanced_retrieval_results.json", "w") as f:
        json.dump(report, f, indent=2)

    logger.info("Evaluation complete.")


if __name__ == "__main__":
    run_evaluation()
