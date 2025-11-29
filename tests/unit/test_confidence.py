from src.utils.confidence import calculate_confidence_score


class TestConfidenceScore:
    def test_calculate_confidence_score_low(self):
        # Mock data for low confidence scenario
        question_embedding = [1.0, 0.0, 0.0]
        retrieved_verses = [
            {"text": "Completely unrelated text", "embedding": [0.0, 1.0, 0.0]},
            {"text": "Another unrelated verse", "embedding": [0.0, 0.0, 1.0]},
        ]
        generated_answer = "This is a generated answer about something else."

        result = calculate_confidence_score(
            question_embedding, retrieved_verses, generated_answer
        )

        assert result["level"] == "Low"
        assert result["score"] < 40
        assert "warning" in result
        assert result["warning"] is not None

    def test_calculate_confidence_score_high(self):
        # Mock data for high confidence scenario
        question_embedding = [0.1, 0.2, 0.3]
        # Verse similar to question
        retrieved_verses = [
            {
                "text": "The answer is clearly stated here.",
                "embedding": [0.1, 0.2, 0.35],
            },
            {
                "text": "Supporting evidence for the answer.",
                "embedding": [0.12, 0.22, 0.32],
            },
        ]
        generated_answer = (
            "The answer is clearly stated here and supported by evidence."
        )

        result = calculate_confidence_score(
            question_embedding, retrieved_verses, generated_answer
        )

        assert result["level"] in ["High", "Good"]
        assert result["score"] > 60
        assert result["warning"] is None

    def test_calculate_confidence_score_empty(self):
        result = calculate_confidence_score([], [], "")
        assert result["score"] == 0.0
        assert result["level"] == "Low"
