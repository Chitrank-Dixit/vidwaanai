import pytest
from unittest.mock import MagicMock, patch
from src.agent.vidwaan_agent import VidwaanAI

class TestWorkflows:
    
    @pytest.fixture
    def mock_deps(self):
        with patch('src.agent.vidwaan_agent.DatabaseManager') as mock_db, \
             patch('src.agent.vidwaan_agent.OpenAIClient') as mock_llm, \
             patch('src.agent.vidwaan_agent.MultilingualSearch') as mock_multi:
            yield mock_db, mock_llm, mock_multi

    @pytest.fixture
    def agent(self, mock_deps):
        mock_db, mock_llm, mock_multi = mock_deps
        mock_db.return_value.get_all_verses.return_value = []
        
        agent = VidwaanAI(
            db_url="postgresql://user:pass@localhost:5432/db",
            openai_key="fake",
            use_lmstudio=False
        )
        return agent

    def test_hindi_workflow(self, agent):
        # Setup
        agent.multilingual_search.process_query.return_value = {
            'language_code': 'hi',
            'embedding': [0.1]*384,
            'processed_text': 'नमस्ते'
        }
        # Mock verse with embedding and text that overlaps with answer
        agent.db.retrieve_verses.return_value = [{
            'text': 'नमस्ते उत्तर', 
            'similarity': 0.9,
            'embedding': [0.1]*384
        }]
        agent.llm.generate.return_value = "नमस्ते उत्तर"
        
        # Execute
        res = agent.query("नमस्ते")
        
        # Verify
        assert res['language'] == 'hi'
        assert res['answer'] == "नमस्ते उत्तर"

    def test_tamil_workflow(self, agent):
        # Setup
        agent.multilingual_search.process_query.return_value = {
            'language_code': 'ta',
            'embedding': [0.1]*384,
            'processed_text': 'வணக்கம்'
        }
        agent.db.retrieve_verses.return_value = [{
            'text': 'வணக்கம் பதில்', 
            'similarity': 0.9,
            'embedding': [0.1]*384
        }]
        agent.llm.generate.return_value = "வணக்கம் பதில்"
        
        # Execute
        res = agent.query("வணக்கம்")
        
        # Verify
        assert res['language'] == 'ta'
        assert res['answer'] == "வணக்கம் பதில்"

    def test_gujarati_workflow(self, agent):
        # Setup
        agent.multilingual_search.process_query.return_value = {
            'language_code': 'gu',
            'embedding': [0.1]*384,
            'processed_text': 'નમસ્તે'
        }
        agent.db.retrieve_verses.return_value = [{
            'text': 'નમસ્તે જવાબ', 
            'similarity': 0.9,
            'embedding': [0.1]*384
        }]
        agent.llm.generate.return_value = "નમસ્તે જવાબ"
        
        # Execute
        res = agent.query("નમસ્તે")
        
        # Verify
        assert res['language'] == 'gu'
        assert res['answer'] == "નમસ્તે જવાબ"
