from typing import Dict, Any, List


def execute_rag_pipeline(query: str, config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes the full RAG pipeline with the given configuration.

    Args:
        query: The user query.
        config: Configuration dictionary (strategies, models, etc.).

    Returns:
        Result dictionary with answer and sources.
    """
    # Mock pipeline execution
    return {
        "query": query,
        "answer": "Pipeline execution result",
        "sources": ["doc1", "doc2"],
        "steps_executed": ["detect", "search", "generate"],
        "config_used": config,
    }


def get_pipeline_strategies() -> List[str]:
    """
    Returns available pipeline strategies.
    """
    return ["minimal", "standard", "advanced", "research"]


def validate_pipeline_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validates a pipeline configuration.

    Args:
        config: The configuration to validate.

    Returns:
        Validation result (valid/invalid, errors).
    """
    # Mock validation
    required_keys = ["strategy"]
    missing = [k for k in required_keys if k not in config]

    if missing:
        return {"valid": False, "errors": [f"Missing keys: {missing}"]}

    return {"valid": True, "errors": []}
