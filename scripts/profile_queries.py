import time
import json
import os
import sys
import time
from typing import Any, Dict, List, Optional, Union

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.logger import get_logger

logger = get_logger(__name__)


class QueryProfiler:
    def __init__(self) -> None:
        self.results: List[Dict[str, Any]] = []
        logger.info("Initializing VidwaanAI agent...")
        try:
            from src.core.config import settings
            from src.agent.vidwaan_agent import VidwaanAI

            self.agent = VidwaanAI(
                db_url=settings.DATABASE_URL,
                openai_key=str(settings.OPENAI_API_KEY),
                lmstudio_url=settings.lmstudio_base_url,
                enable_graph_rag=settings.ENABLE_GRAPH_RAG,
                neo4j_uri=settings.NEO4J_URI,
                neo4j_user=settings.NEO4J_USER,
                neo4j_password=settings.NEO4J_PASSWORD,
            )
        except Exception as e:
            logger.error(f"Failed to initialize agent: {e}")
            raise

    def profile_query(self, query_text: str) -> Optional[Dict[str, Any]]:
        start_time = time.time()

        try:
            # Use the initialized agent directly
            _ = self.agent.query(question=query_text)
            total_time = time.time() - start_time

            profile_data = {
                "query": query_text,
                "total_time": total_time,
                "timestamp": time.time(),
            }

            self.results.append(profile_data)
            return profile_data

        except Exception as e:
            logger.error(f"Error profiling query: {e}")
            return None

    def profile_queries_from_file(self, file_path: str) -> None:
        with open(file_path, "r") as f:
            queries = f.readlines()

        for query in queries:
            if query.strip():
                print(f"Profiling: {query.strip()}")
                self.profile_query(query.strip())

    def generate_report(self) -> Union[str, Dict[str, Any]]:
        if not self.results:
            return "No results to report"

        times = [r["total_time"] for r in self.results]

        report = {
            "total_queries": len(self.results),
            "min_time": min(times),
            "max_time": max(times),
            "avg_time": sum(times) / len(times),
            "p95_time": sorted(times)[int(len(times) * 0.95)],
            "p99_time": sorted(times)[int(len(times) * 0.99)],
            "results": self.results,
        }

        return report


if __name__ == "__main__":
    profiler = QueryProfiler()
    test_queries_path = os.path.join(os.path.dirname(__file__), "test_queries.txt")

    if os.path.exists(test_queries_path):
        profiler.profile_queries_from_file(test_queries_path)
        report = profiler.generate_report()

        print(json.dumps(report, indent=2))

        docs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs")
        os.makedirs(docs_dir, exist_ok=True)

        with open(os.path.join(docs_dir, "profiling_results.json"), "w") as f:
            json.dump(report, f, indent=2)
    else:
        print(f"Test queries file not found at {test_queries_path}")
