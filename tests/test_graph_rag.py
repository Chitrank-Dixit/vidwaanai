import unittest
from unittest.mock import MagicMock
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.graph.graph_builder import GraphBuilder
from src.graph.graph_retriever import GraphRetriever
from src.graph.hybrid_search import HybridSearcher

class TestGraphRAG(unittest.TestCase):
    
    def setUp(self):
        self.mock_driver = MagicMock()
        self.session = MagicMock()
        self.mock_driver.session.return_value.__enter__.return_value = self.session

    def test_graph_builder(self):
        builder = GraphBuilder("bolt://localhost:7687", "neo4j", "password")
        builder.driver = self.mock_driver
        
        builder.create_person("Krishna", {"role": "Deity"})
        
        # Verify session.run was called
        self.session.run.assert_called()
        args = self.session.run.call_args
        self.assertIn("MERGE (p:Person {name: $name})", args[0][0])
        self.assertEqual(args[1]['name'], "Krishna")

    def test_graph_retriever(self):
        retriever = GraphRetriever(self.mock_driver)
        
        # Mock result
        record = MagicMock()
        record.data.return_value = {"entities": [{"name": "Krishna"}], "relations": []}
        self.session.run.return_value = [record]
        
        results = retriever.find_teachings("Krishna", "dharma")
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['entities'][0]['name'], "Krishna")

    def test_hybrid_searcher(self):
        mock_graph = MagicMock()
        mock_vector = MagicMock()
        mock_embeddings = MagicMock()
        mock_extractor = MagicMock()
        
        searcher = HybridSearcher(mock_graph, mock_vector, mock_embeddings, mock_extractor)
        
        # Mock extraction
        mock_extractor.llm.generate.return_value = '[{"name": "Krishna", "type": "Person"}]'
        
        # Mock graph search
        mock_graph.find_teachings.return_value = [{"path": "Krishna->dharma"}]
        
        # Mock vector search
        mock_vector.retrieve_verses.return_value = [{"text": "verse text", "scripture": "Gita", "chapter": 1, "verse": 1, "translation": "text"}]
        
        results = searcher.search("What does Krishna teach?")
        
        self.assertEqual(len(results['graph_results']), 1)
        self.assertEqual(len(results['vector_results']), 1)
        self.assertIn("Krishna->dharma", str(results['graph_results'][0]))

if __name__ == "__main__":
    unittest.main()
