from unittest.mock import patch, mock_open
from src.ingestion.utils import (
    is_processed,
    mark_processed,
    should_process,
    TRACKING_FILE,
)
from src.utils.confidence import calculate_confidence_score

# --- src/ingestion/utils.py Tests ---


def test_is_processed_false_no_file():
    """Test is_processed returns False when tracking file doesn't exist."""
    with patch("os.path.exists", return_value=False):
        assert is_processed("test.pdf") is False


def test_is_processed_true_in_file():
    """Test is_processed returns True when file is in tracking file."""
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data="/abs/path/to/test.pdf\n")):
            with patch("os.path.abspath", return_value="/abs/path/to/test.pdf"):
                assert is_processed("test.pdf") is True


def test_is_processed_false_not_in_file():
    """Test is_processed returns False when file is NOT in tracking file."""
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data="/other/file.pdf\n")):
            with patch("os.path.abspath", return_value="/abs/path/to/test.pdf"):
                assert is_processed("test.pdf") is False


def test_mark_processed_writes_to_file():
    """Test mark_processed appends absolute path to file."""
    m_open = mock_open()
    with patch("builtins.open", m_open):
        with patch("os.path.abspath", return_value="/abs/path/to/new.pdf"):
            with patch("os.makedirs") as mock_makedirs:
                mark_processed("new.pdf")

                mock_makedirs.assert_called_once()
                m_open.assert_called_once_with(TRACKING_FILE, "a")
                m_open().write.assert_called_once_with("/abs/path/to/new.pdf\n")


def test_should_process_force_true():
    """Test should_process returns True if force is True."""
    assert should_process("test.pdf", force=True) is True


def test_should_process_false_already_processed():
    """Test should_process returns False if already processed."""
    with patch("src.ingestion.utils.is_processed", return_value=True):
        assert should_process("test.pdf", force=False) is False


def test_should_process_true_not_processed():
    """Test should_process returns True if not processed."""
    with patch("src.ingestion.utils.is_processed", return_value=False):
        assert should_process("test.pdf", force=False) is True


# --- src/utils/confidence.py Tests ---


def test_calculate_confidence_score_empty_retrieval():
    """Test confidence score is 0/Low when no verses retrieved."""
    result = calculate_confidence_score([0.1], [], "Answer")
    assert result["score"] == 0.0
    assert result["level"] == "Low"
    assert "No verses retrieved" in result["warning"]


def test_calculate_confidence_score_high_match():
    """Test confidence calculation with high similarity and tokens."""
    # Mock embeddings: perfect match [1,0] vs [1,0]
    question_emb = [1.0, 0.0]
    retrieved_verses = [
        {"embedding": [1.0, 0.0], "text": "target text", "translation": "target text"},
        {
            "embedding": [0.9, 0.1],
            "text": "similar text",
            "translation": "similar text",
        },
    ]
    generated_answer = "target text similar text"

    result = calculate_confidence_score(
        question_emb, retrieved_verses, generated_answer
    )

    # Expect high confidence
    # Similarity ~100 -> 40 pts
    # Rank ~87 -> 26 pts
    # Match 100% -> 20 pts
    # Overlap 100% -> 10 pts
    # Total ~96

    assert result["score"] > 90
    assert result["level"] == "High"
    assert result["warning"] is None


def test_calculate_confidence_score_missing_embeddings():
    """Test graceful handling when embeddings are missing."""
    question_emb = [1.0, 0.0]
    retrieved_verses = [
        {"text": "some text", "embedding": None},  # Missing embedding
    ]
    generated_answer = "irrelevant"

    result = calculate_confidence_score(
        question_emb, retrieved_verses, generated_answer
    )

    # Similarity contribution should be 0
    assert result["breakdown"]["similarity"] == 0.0
    # Overall score will be low but valid
    assert result["score"] >= 0


def test_calculate_confidence_score_string_embedding_parsing():
    """Test parsing of stringified embeddings."""
    question_emb = [1.0, 0.0]
    retrieved_verses = [
        {"embedding": "[1.0, 0.0]", "text": "match"},  # String format
    ]
    generated_answer = "match"

    result = calculate_confidence_score(
        question_emb, retrieved_verses, generated_answer
    )

    # Should successfully parse and compute similarity
    assert result["breakdown"]["similarity"] > 99.0


def test_calculate_confidence_score_low_confidence():
    """Test low confidence scenario."""
    question_emb = [1.0, 0.0]
    retrieved_verses = [
        {"embedding": [0.0, 1.0], "text": "unrelated"},  # Orthogonal
    ]
    generated_answer = "completely different"

    result = calculate_confidence_score(
        question_emb, retrieved_verses, generated_answer
    )

    # Similarity 0, Match 0, Overlap 0
    # Only Rank contributes (1.0 * 30% = 30) -> Score around 30 -> Low/Fair
    assert result["score"] < 40
    assert result["level"] == "Low" or "Fair"
    assert result["warning"] is not None
