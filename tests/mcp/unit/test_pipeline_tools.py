from src.mcp.tools.pipeline_tools import (
    execute_rag_pipeline,
    get_pipeline_strategies,
    validate_pipeline_config,
)


def test_execute_rag_pipeline() -> None:
    config = {"strategy": "standard"}
    result = execute_rag_pipeline("query", config)
    assert "answer" in result
    assert "steps_executed" in result


def test_get_pipeline_strategies() -> None:
    strategies = get_pipeline_strategies()
    assert "standard" in strategies
    assert len(strategies) > 0


def test_validate_pipeline_config_valid() -> None:
    config = {"strategy": "minimal"}
    result = validate_pipeline_config(config)
    assert result["valid"] is True


def test_validate_pipeline_config_invalid() -> None:
    config: dict[str, str] = {}
    result = validate_pipeline_config(config)
    assert result["valid"] is False
    assert len(result["errors"]) > 0
