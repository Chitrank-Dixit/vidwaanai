from src.mcp.tools.language_tools import (
    detect_language,
    preprocess_text,
    get_supported_languages,
)


def test_get_supported_languages() -> None:
    langs = get_supported_languages()
    assert len(langs) > 0
    assert any(hl["code"] == "hi" for hl in langs)
    assert any(el["code"] == "en" for el in langs)


def test_detect_language_hindi() -> None:
    # "Namaste" in Hindi
    result = detect_language("नमस्ते")
    assert result["language_code"] == "hi"
    assert result["is_supported"] is True
    assert result["confidence"] > 0.0


def test_detect_language_english() -> None:
    result = detect_language(
        "Hello world, this is a longer sentence to ensure correct detection."
    )
    assert result["language_code"] == "en"
    assert result["is_supported"] is True


def test_detect_language_unknown() -> None:
    # Some random text that might be detected as something else or low confidence
    # For now just check structure
    result = detect_language("xyz123")
    assert "language_code" in result
    assert "confidence" in result


def test_preprocess_text() -> None:
    text = "  Hello World  "
    result = preprocess_text(text, "en")
    assert result["normalized_text"] == "hello world"
    assert len(result["tokens"]) == 2
    assert result["tokens"][0] == "hello"
    assert result["tokens"][1] == "world"


def test_preprocess_text_hindi() -> None:
    text = "नमस्ते दुनिया"
    result = preprocess_text(text, "hi")
    assert len(result["tokens"]) == 2
