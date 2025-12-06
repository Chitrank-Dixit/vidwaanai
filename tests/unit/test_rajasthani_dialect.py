import pytest
from src.dialects.rajasthani import (
    RajasthaniProcessor,
)


class TestRajasthaniDialect:

    @pytest.fixture
    def processor(self):
        return RajasthaniProcessor()

    def test_normalization(self, processor):
        # Test ZWNJ removal
        text = "क\u200cख"
        assert processor.normalize(text) == "कख"

        # Test Nukta normalization
        text = "\u0958"
        assert processor.normalize(text) == "\u0915\u093c"

    def test_tokenization(self, processor):
        text = "म्हे जास्यां।"
        tokens = processor.tokenize(text)
        assert "म्हे" in tokens
        assert "जास्यां" in tokens

    def test_stopwords(self, processor):
        text = "म्हे जास्यां कोनी"
        # "म्हे", "कोनी" are stopwords
        processed = processor.process(text)
        filtered = processed["filtered_tokens"]

        assert "जास्यां" in filtered
        assert "म्हे" not in filtered
        assert "कोनी" not in filtered

    def test_legacy_wrapper(self):
        from src.language.rajasthani_processor import (
            RajasthaniProcessor as LegacyProcessor,
        )

        processor = LegacyProcessor()
        assert isinstance(processor, RajasthaniProcessor)

        text = "म्हे कोनी"
        processed = processor.process(text)
        assert "म्हे" not in processed["filtered_tokens"]

    def test_grammar_loading(self, processor):
        assert processor.grammar is not None
        assert "syntax" in processor.grammar
        assert processor.grammar["syntax"]["word_order"] == "SOV"
