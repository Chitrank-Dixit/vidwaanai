import time
import threading
import random
import sys
import os
from dotenv import load_dotenv
from typing import List

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

from src.main import get_agent
from src.core.logger import get_logger

logger = get_logger(__name__)


class LoadTester:
    def __init__(
        self, queries: List[str], concurrency: int = 10, duration_sec: int = 30
    ):
        self.queries = queries
        self.concurrency = concurrency
        self.duration_sec = duration_sec
        self.stats = {
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "latencies": [],
        }
        self.lock = threading.Lock()
        self.running = False

    def _worker(self, agent):
        while self.running:
            query = random.choice(self.queries)
            start_time = time.time()
            try:
                agent.query(query, verbose=False)
                latency = time.time() - start_time

                with self.lock:
                    self.stats["total_requests"] += 1
                    self.stats["successful_requests"] += 1
                    self.stats["latencies"].append(latency)
            except Exception as e:
                logger.error(f"Request failed: {e}")
                with self.lock:
                    self.stats["total_requests"] += 1
                    self.stats["failed_requests"] += 1

    def run(self):
        print("Initializing agent...")
        agent = get_agent()
        print(
            f"Starting load test with {self.concurrency} threads for {self.duration_sec} seconds..."
        )
        self.running = True
        threads = []

        for _ in range(self.concurrency):
            t = threading.Thread(target=self._worker, args=(agent,))
            t.start()
            threads.append(t)

        time.sleep(self.duration_sec)
        self.running = False

        for t in threads:
            t.join()

        self._print_report()

    def _print_report(self):
        latencies = self.stats["latencies"]
        if not latencies:
            print("No successful requests.")
            return

        avg_latency = sum(latencies) / len(latencies)
        p95_latency = sorted(latencies)[int(len(latencies) * 0.95)]
        p99_latency = sorted(latencies)[int(len(latencies) * 0.99)]
        rps = self.stats["successful_requests"] / self.duration_sec

        print("\n--- Load Test Results ---")
        print(f"Total Requests: {self.stats['total_requests']}")
        print(f"Successful: {self.stats['successful_requests']}")
        print(f"Failed: {self.stats['failed_requests']}")
        print(f"RPS: {rps:.2f}")
        print(f"Avg Latency: {avg_latency:.3f}s")
        print(f"P95 Latency: {p95_latency:.3f}s")
        print(f"P99 Latency: {p99_latency:.3f}s")


if __name__ == "__main__":
    # Sample queries
    queries = [
        "What is dharma?",
        "Who is Krishna?",
        "Explain karma yoga",
        "Meaning of life",
        "Arjuna's dilemma",
        "Yoga types",
        "Meditation in Gita",
        "Duty of a warrior",
        "Soul immortality",
        "Divine nature",
    ]

    tester = LoadTester(queries, concurrency=5, duration_sec=10)
    tester.run()
