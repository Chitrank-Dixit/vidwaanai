import json
import os
import sys
from typing import Any
from dotenv import load_dotenv

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

from src.rag.multilingual_search import MultilingualSearch  # noqa: E402
from src.db.db_manager import DatabaseManager  # noqa: E402
from src.core.logger import get_logger  # noqa: E402

logger = get_logger(__name__)


def run_multilingual_eval() -> None:
    logger.info("Starting multilingual evaluation...")

    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        logger.error("DATABASE_URL not set")
        return

    db_manager = DatabaseManager(db_url)
    multilingual_search = MultilingualSearch()

    # Load test queries
    test_file = os.path.join(
        os.path.dirname(__file__), "multilingual_test_queries.json"
    )
    try:
        with open(test_file, "r") as f:
            test_data = json.load(f)
    except FileNotFoundError:
        logger.error(f"Test file not found: {test_file}")
        return

    results_by_language: dict[str, list[dict[str, Any]]] = {}

    for test in test_data["queries"]:
        query = test["query"]
        language = test["language"]

        logger.info(f"Evaluating ({language}): {query}")

        # Process and search
        # Note: In a real eval, we'd need ground truth IDs.
        # Here we are checking if we get results and if the pipeline runs.
        # We can check if the retrieved verses contain relevant keywords if we had them.
        # For now, we'll just log the retrieved count and top result.

        query_data = multilingual_search.process_query(query)
        embedding = query_data["embedding"]

        if isinstance(embedding[0], list):
            embedding = embedding[0]
        retrieved = db_manager.retrieve_verses(embedding, top_k=5)

        logger.info(f"Retrieved {len(retrieved)} verses")
        if retrieved:
            top_verse = retrieved[0]
            logger.info(
                f"Top result: {top_verse.get('text', '')[:100]}... (Score: {top_verse.get('similarity', 0.0):.4f})"
            )

        if language not in results_by_language:
            results_by_language[language] = []

        results_by_language[language].append(
            {
                "query": query,
                "num_retrieved": len(retrieved),
                "top_score": retrieved[0].get("similarity", 0.0) if retrieved else 0.0,
            }
        )

    # Generate report
    report = {}
    for language, results in results_by_language.items():
        avg_score = sum(r["top_score"] for r in results) / len(results)

        report[language] = {
            "num_queries": len(results),
            "avg_top_score": avg_score,
            "results": results,
        }

    print(json.dumps(report, indent=2))

    output_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "docs",
        "multilingual_evaluation.json",
    )
    with open(output_file, "w") as f:
        json.dump(report, f, indent=2)

    logger.info(f"Evaluation complete. Report saved to {output_file}")


if __name__ == "__main__":
    run_multilingual_eval()
