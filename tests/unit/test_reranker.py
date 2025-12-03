import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add project root to path
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from src.retrieval.reranker import ContextAwareReranker


class TestContextAwareReranker(unittest.TestCase):
    def setUp(self):
        # Patch CrossEncoder to avoid loading real model
        self.patcher = patch("sentence_transformers.CrossEncoder")
        self.MockCrossEncoder = self.patcher.start()
        self.mock_model = self.MockCrossEncoder.return_value

    def tearDown(self):
        self.patcher.stop()

    def test_initialization_success(self):
        """Test successful initialization"""
        reranker = ContextAwareReranker()
        self.assertIsNotNone(reranker.model)
        self.MockCrossEncoder.assert_called_with("cross-encoder/ms-marco-MiniLM-L-6-v2")

    def test_initialization_failure(self):
        """Test initialization failure handling"""
        self.MockCrossEncoder.side_effect = Exception("Model load failed")
        reranker = ContextAwareReranker()
        self.assertIsNone(reranker.model)

    def test_rerank_empty(self):
        """Test reranking with empty input"""
        reranker = ContextAwareReranker()
        results = reranker.rerank("query", [])
        self.assertEqual(results, [])

    def test_rerank_no_model(self):
        """Test reranking when model failed to load"""
        self.MockCrossEncoder.side_effect = Exception("Model load failed")
        reranker = ContextAwareReranker()
        docs = [{"text": "doc1"}]
        results = reranker.rerank("query", docs)
        self.assertEqual(results, docs)

    def test_rerank_success(self):
        """Test successful reranking"""
        reranker = ContextAwareReranker()

        docs = [
            {"text": "doc1", "id": 1},
            {"text": "doc2", "id": 2},
            {"text": "doc3", "id": 3},
        ]

        # Mock scores: doc2 > doc1 > doc3
        self.mock_model.predict.return_value = [0.5, 0.9, 0.1]

        results = reranker.rerank("query", docs, top_k=2)

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["id"], 2)  # Highest score
        self.assertEqual(results[1]["id"], 1)  # Second highest
        self.assertEqual(results[0]["rerank_score"], 0.9)

    def test_rerank_different_fields(self):
        """Test reranking with different document fields"""
        reranker = ContextAwareReranker()

        docs = [
            {"content": "doc1", "id": 1},
            {"document": "doc2", "id": 2},
            {"other": "doc3", "id": 3},  # Fallback to str(doc)
        ]

        self.mock_model.predict.return_value = [0.1, 0.2, 0.3]

        reranker.rerank("query", docs)

        # Verify calls to predict used correct text
        call_args = self.mock_model.predict.call_args[0][0]
        self.assertEqual(call_args[0], ["query", "doc1"])
        self.assertEqual(call_args[1], ["query", "doc2"])
        self.assertIn("doc3", call_args[2][1])

    def test_rerank_exception(self):
        """Test exception during reranking"""
        reranker = ContextAwareReranker()
        self.mock_model.predict.side_effect = Exception("Predict failed")

        docs = [{"text": "doc1"}]
        results = reranker.rerank("query", docs)

        # Should return original docs on failure
        self.assertEqual(results, docs)


if __name__ == "__main__":
    unittest.main()
