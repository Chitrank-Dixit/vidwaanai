import pytest
from src.language.hindi_processor import HindiProcessor
from src.language.gujarati_processor import GujaratiProcessor
from src.language.tamil_processor import TamilProcessor
from src.language.telugu_processor import TeluguProcessor
from src.language.kannada_processor import KannadaProcessor
from src.language.malayalam_processor import MalayalamProcessor
from src.language.bengali_processor import BengaliProcessor
from src.language.marathi_processor import MarathiProcessor

class TestLanguageProcessors:

    # --- Hindi Processor Tests ---
    @pytest.fixture
    def hindi_processor(self):
        return HindiProcessor()

    def test_hindi_normalize(self, hindi_processor):
        text = "  नमस्ते   दुनिया  "
        normalized = hindi_processor.normalize(text)
        assert normalized == "नमस्ते दुनिया"

    def test_hindi_tokenize(self, hindi_processor):
        text = "नमस्ते दुनिया"
        tokens = hindi_processor.tokenize(text)
        assert tokens == ["नमस्ते", "दुनिया"]

    def test_hindi_remove_stopwords(self, hindi_processor):
        # "hai" (है) is a stopword
        tokens = ["राम", "अच्छा", "लड़का", "है"]
        filtered = hindi_processor.remove_stopwords(tokens)
        assert "है" not in filtered
        assert "राम" in filtered

    def test_hindi_preprocess(self, hindi_processor):
        text = "राम स्कूल जाता है।"
        result = hindi_processor.preprocess(text)
        assert result['original'] == text
        assert "है" not in result['filtered_tokens']
        assert "राम" in result['filtered_tokens']

    # --- Gujarati Processor Tests ---
    @pytest.fixture
    def gujarati_processor(self):
        return GujaratiProcessor()

    def test_gujarati_preprocess(self, gujarati_processor):
        text = "તમે કેમ છો?" # "How are you?"
        result = gujarati_processor.preprocess(text)
        assert result['original'] == text
        # Assuming 'cho' or similar might be stopword, verifying structure
        assert isinstance(result['tokens'], list)
        assert len(result['tokens']) > 0

    # --- Tamil Processor Tests ---
    @pytest.fixture
    def tamil_processor(self):
        return TamilProcessor()

    def test_tamil_preprocess(self, tamil_processor):
        text = "வணக்கம் உலகம்" # Hello World
        result = tamil_processor.preprocess(text)
        assert result['normalized'] == "வணக்கம் உலகம்"
        assert len(result['tokens']) == 2

    # --- Telugu Processor Tests ---
    @pytest.fixture
    def telugu_processor(self):
        return TeluguProcessor()

    def test_telugu_preprocess(self, telugu_processor):
        text = "నమస్కారం"
        result = telugu_processor.preprocess(text)
        assert len(result['tokens']) == 1

    # --- Kannada Processor Tests ---
    @pytest.fixture
    def kannada_processor(self):
        return KannadaProcessor()

    def test_kannada_preprocess(self, kannada_processor):
        text = "ನಮಸ್ಕಾರ"
        result = kannada_processor.preprocess(text)
        assert len(result['tokens']) == 1

    # --- Malayalam Processor Tests ---
    @pytest.fixture
    def malayalam_processor(self):
        return MalayalamProcessor()

    def test_malayalam_preprocess(self, malayalam_processor):
        text = "നമസ്കാരം"
        result = malayalam_processor.preprocess(text)
        assert len(result['tokens']) == 1
        
    # --- Bengali Processor Tests ---
    @pytest.fixture
    def bengali_processor(self):
        return BengaliProcessor()

    def test_bengali_preprocess(self, bengali_processor):
        text = "নমস্কার"
        result = bengali_processor.preprocess(text)
        assert len(result['tokens']) == 1

    # --- Marathi Processor Tests ---
    @pytest.fixture
    def marathi_processor(self):
        return MarathiProcessor()

    def test_marathi_preprocess(self, marathi_processor):
        text = "नमस्कार"
        result = marathi_processor.preprocess(text)
        assert len(result['tokens']) == 1
        
    def test_marathi_stopwords(self, marathi_processor):
        # 'aahe' is a stopword in Marathi
        tokens = ["पुस्तक", "येथे", "आहे"]
        filtered = marathi_processor.remove_stopwords(tokens)
        assert "आहे" not in filtered
        assert "पुस्तक" in filtered
