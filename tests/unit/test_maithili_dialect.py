import pytest
from src.dialects.maithili import (
    MaithiliProcessor,
)


class TestMaithiliDialect:

    @pytest.fixture
    def processor(self):
        return MaithiliProcessor()

    def test_normalization(self, processor):
        # Test ZWNJ removal
        text = "क\u200cख"
        assert processor.normalize(text) == "कख"

        # Test Nukta normalization (qa -> ka+nukta)
        text = "\u0958"
        assert processor.normalize(text) == "\u0915\u093c"

    def test_tokenization(self, processor):
        text = "हम मिथिला के निवासी छी।"
        tokens = processor.tokenize(text)
        assert "मिथिला" in tokens
        assert "निवासी" in tokens
        # "छी" might be a stopword but tokenize keeps it?
        # Tokenizer just splits words.
        assert "छी" in tokens

    def test_stopwords(self, processor):
        text = "हम मिथिला के निवासी छी"
        # "हम", "के", "छी" are stopwords
        processed = processor.process(text)
        filtered = processed["filtered_tokens"]

        assert "मिथिला" in filtered
        assert "निवासी" in filtered
        assert "हम" not in filtered
        assert "छी" not in filtered

    def test_legacy_wrapper(self):
        from src.language.maithili_processor import MaithiliProcessor as LegacyProcessor

        processor = LegacyProcessor()
        assert isinstance(processor, MaithiliProcessor)

        text = "हम अछि"
        processed = processor.process(text)
        assert "हम" not in processed["filtered_tokens"]

    def test_classification(self):
        from src.dialects.maithili import MaithiliDialectClassifier

        classifier = MaithiliDialectClassifier()

        # Sotipura (Standard)
        assert classifier.classify("हम अछि") == "Sotipura (Standard)"

        # Angika
        assert classifier.classify("हमर छै") == "Angika"

        # Bajjika
        assert classifier.classify("रउआ बा") == "Bajjika"

    def test_morphology(self, processor):
        # Test stemming
        assert processor.get_stem("जाइछि") == "जाइ"  # Assuming 'छि' is suffix
        # Wait, my rule was "छि" (chi). "जाइछि" -> "जाइ" + "छि"

        # Test analysis
        analysis = processor.analyze_morphology("जाइछि")
        assert analysis["root"] == "जाइ"
        assert analysis["suffix"] == "छि"
        assert analysis["category"] == "be"

    def test_grammar_loading(self, processor):
        assert processor.grammar is not None
        assert "syntax" in processor.grammar
        assert processor.grammar["syntax"]["word_order"] == "SOV"
