import json
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.evaluation.retriever_evaluator import RetrieverEvaluator
from src.db.db_manager import DatabaseManager
from src.rag.embeddings import EmbeddingManager
from src.core.logger import get_logger
from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)

from src.retrieval.bm25_search import BM25Search  # noqa: E402
from src.retrieval.hybrid_search import HybridSearch  # noqa: E402


def run_evaluation():
    logger.info("Starting retrieval evaluation...")

    # Initialize components
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        logger.error("DATABASE_URL not set")
        return

    db_manager = DatabaseManager(db_url)
    embedding_manager = EmbeddingManager()
    evaluator = RetrieverEvaluator()

    # Initialize Hybrid Search
    logger.info("Initializing Hybrid Search...")
    verses = db_manager.get_all_verses()
    bm25_search = BM25Search(verses)

    def vector_search_func(query, top_k):
        emb = embedding_manager.embed_text(query)
        results = db_manager.retrieve_verses(emb, top_k=top_k)
        for r in results:
            r["score"] = r.get("similarity", 0.0)
        return results

    hybrid_search = HybridSearch(
        bm25_search=bm25_search,
        vector_search_func=vector_search_func,
        bm25_weight=0.3,
        semantic_weight=0.7,
    )

    # Load benchmark queries
    benchmark_file = os.path.join(
        os.path.dirname(__file__), "test_benchmark_queries.json"
    )
    try:
        with open(benchmark_file, "r") as f:
            test_data = json.load(f)
    except FileNotFoundError:
        logger.error(f"Benchmark file not found: {benchmark_file}")
        return

    logger.info(f"Loaded {len(test_data['queries'])} benchmark queries")

    for test_query in test_data["queries"]:
        query_text = test_query["query"]
        relevant_verses = test_query["relevant_verses"]

        logger.info(f"Evaluating: {query_text}")

        # Retrieve using Hybrid Search
        retrieved_docs = hybrid_search.search(query_text, top_k=10)

        # Extract IDs
        retrieved_ids = [str(doc["id"]) for doc in retrieved_docs]
        relevant_ids = [str(r) for r in relevant_verses]

        # Evaluate
        result = evaluator.evaluate_query(query_text, retrieved_ids, relevant_ids)
        evaluator.results.append(result)

        logger.info(
            f"Precision@10: {result['precision_at_10']:.2f}, Recall@10: {result['recall_at_10']:.2f}"
        )

    # Generate report
    report = evaluator.generate_report()

    print(json.dumps(report, indent=2))

    output_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "docs", "retrieval_baseline.json"
    )
    with open(output_file, "w") as f:
        json.dump(report, f, indent=2)

    logger.info(f"Evaluation complete. Report saved to {output_file}")


if __name__ == "__main__":
    run_evaluation()
