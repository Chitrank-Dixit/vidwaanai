import pytest
from src.mcp.tools.generation_tools import generate_answer, summarize_results, translate_answer

def test_generate_answer():
    context = ["Context 1", "Context 2"]
    result = generate_answer(context, "What is this?")
    assert "answer" in result
    assert "citations" in result

def test_summarize_results():
    docs = ["Doc 1", "Doc 2"]
    result = summarize_results(docs, "en")
    assert "summary" in result
    assert "key_points" in result

def test_translate_answer():
    result = translate_answer("Hello", "hi")
    assert "translated" in result
    assert result["target_language"] == "hi"
