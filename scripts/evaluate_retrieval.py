import json
from typing import Any
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.evaluation.retriever_evaluator import RetrieverEvaluator
from src.db.db_manager import DatabaseManager
from src.core.logger import get_logger
from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)

from src.retrieval.bm25_search import BM25Search  # noqa: E402
from src.retrieval.hybrid_search import HybridSearch  # noqa: E402


def run_evaluation() -> None:
    logger.info("Starting retrieval evaluation...")

    # Initialize components
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        logger.error("DATABASE_URL not set")
        return

    db_manager = DatabaseManager(db_url)
    # Use MultilingualEmbeddings to match DB schema (1024 dim)
    from src.rag.multilingual_embeddings import MultilingualEmbeddings

    embedding_manager = MultilingualEmbeddings()
    evaluator = RetrieverEvaluator()

    # Initialize Hybrid Search
    logger.info("Initializing Hybrid Search...")
    verses = db_manager.get_all_verses()
    bm25_search = BM25Search(verses)

    def vector_search_func(query: str, top_k: int) -> list[dict[str, Any]]:
        # MultilingualEmbeddings.embed_text returns list[float]
        emb = embedding_manager.embed_text(query)
        results = db_manager.retrieve_verses(emb, top_k=top_k)  # type: ignore
        for r in results:
            r["score"] = r.get("similarity", 0.0)
        return results

    hybrid_search = HybridSearch(
        bm25_search=bm25_search,
        vector_search_func=vector_search_func,
        bm25_weight=0.3,
        semantic_weight=0.7,
    )

    # Load test queries and judgments
    try:
        base_dir = os.path.dirname(os.path.dirname(__file__))
        queries_file = os.path.join(base_dir, "tests", "test_queries.json")
        relevance_file = os.path.join(base_dir, "tests", "relevance_judgments.json")

        with open(queries_file, "r") as f:
            test_data = json.load(f)
        with open(relevance_file, "r") as f:
            relevance_data = json.load(f)

        # Build relevance map
        relevance_map = {
            item["query_id"]: item["relevant_docs"]
            for item in relevance_data["judgments"]
        }

        # Build verse signature map for resolution
        # Signature: "ScriptureName Chapter:Verse"
        verse_id_map = {}
        for verse in verses:
            sig = f"{verse['scripture_name']} {verse['chapter_number']}:{verse['verse_number']}"
            verse_id_map[sig] = str(verse["id"])

    except FileNotFoundError as e:
        logger.error(f"Test data file not found: {e}")
        return

    logger.info(f"Loaded {len(test_data['queries'])} test queries")

    # Organize results by category
    category_results: dict[str, list[dict[str, float]]] = {}

    for test_query in test_data["queries"]:
        query_id = test_query["id"]
        query_text = test_query["text"]
        query_type = test_query.get("type", "unknown")

        # Get relevant IDs from judgments
        relevant_signatures = relevance_map.get(query_id, [])
        relevant_ids = []
        for sig in relevant_signatures:
            if sig in verse_id_map:
                relevant_ids.append(verse_id_map[sig])
                logger.info(f"RESOLVED: '{sig}' -> ID {verse_id_map[sig]}")
            else:
                logger.warning(f"Could not resolve verse signature: '{sig}'")
                logger.warning(
                    f"Available signatures (sample): {list(verse_id_map.keys())[:5]}"
                )

        if not relevant_ids:
            logger.warning(f"No relevant verses found for query: {query_id}")
            continue

        logger.info(f"Evaluating ({query_type}): {query_text}")

        # Retrieve using Hybrid Search
        retrieved_docs = hybrid_search.search(query_text, top_k=10)

        # Extract IDs
        retrieved_ids = [str(doc["id"]) for doc in retrieved_docs]

        # Evaluate
        result = evaluator.evaluate_query(query_text, retrieved_ids, relevant_ids)
        evaluator.results.append(result)

        # Add to category buckets
        if query_type not in category_results:
            category_results[query_type] = []
        category_results[query_type].append(result)

        logger.info(
            f"Precision@10: {result['precision_at_10']:.2f}, Recall@10: {result['recall_at_10']:.2f}"
        )

    # Generate global report
    report = evaluator.generate_report()

    # Calculate category metrics
    report["categories"] = {}
    for cat, results in category_results.items():
        if not results:
            continue

        cat_metrics = {
            "num_queries": len(results),
            "avg_precision": sum(r["precision_at_10"] for r in results) / len(results),
            "avg_recall": sum(r["recall_at_10"] for r in results) / len(results),
            "avg_mrr": sum(r["mrr"] for r in results) / len(results),
            "avg_ndcg": sum(r["ndcg_at_10"] for r in results) / len(results),
        }
        report["categories"][cat] = cat_metrics

    print(json.dumps(report, indent=2))

    # Ensure output directory exists
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs")
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "retrieval_baseline.json")
    with open(output_file, "w") as f:
        json.dump(report, f, indent=2)

    logger.info(f"Evaluation complete. Report saved to {output_file}")


if __name__ == "__main__":
    run_evaluation()
