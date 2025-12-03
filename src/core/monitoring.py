import functools
import time

from prometheus_client import Counter, Gauge, Histogram

# Metrics definitions
QUERY_COUNTER = Counter(
    "vidwaan_queries_total", "Total number of queries processed", ["status"]
)
QUERY_LATENCY = Histogram(
    "vidwaan_query_duration_seconds", "Time spent processing queries"
)
RETRIEVAL_QUALITY = Gauge(
    "vidwaan_retrieval_quality", "Average similarity score of retrieved documents"
)
DB_CONNECTION_POOL = Gauge(
    "vidwaan_db_pool_size", "Current database connection pool usage"
)


def track_query_latency(func):
    """Decorator to track query latency."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            QUERY_COUNTER.labels(status="success").inc()
            return result
        except Exception as e:
            QUERY_COUNTER.labels(status="error").inc()
            raise e
        finally:
            duration = time.time() - start_time
            QUERY_LATENCY.observe(duration)

    return wrapper


def record_retrieval_quality(scores: list[float]):
    """Record average retrieval quality."""
    if scores:
        avg_score = sum(scores) / len(scores)
        RETRIEVAL_QUALITY.set(avg_score)
