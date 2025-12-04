import pytest
from src.dialects.bhojpuri import (
    BhojpuriProcessor,
)


class TestBhojpuriDialect:

    @pytest.fixture
    def processor(self):
        return BhojpuriProcessor()

    def test_normalization(self, processor):
        # Test ZWNJ removal
        text = "क\u200cख"
        assert processor.normalize(text) == "कख"

        # Test Avagraha handling (Latin S -> Avagraha)
        text = "कS"
        assert processor.normalize(text) == "क\u093d"

    def test_tokenization(self, processor):
        text = "हमर लइका बा।"
        tokens = processor.tokenize(text)
        assert "लइका" in tokens
        assert "बा" in tokens  # Stopword but tokenizer keeps it

    def test_stopwords(self, processor):
        text = "हमर लइका बा"
        # "हमर", "बा" are stopwords
        processed = processor.process(text)
        filtered = processed["filtered_tokens"]

        assert "लइका" in filtered
        assert "हमर" not in filtered
        assert "बा" not in filtered

    def test_legacy_wrapper(self):
        from src.language.bhojpuri_processor import BhojpuriProcessor as LegacyProcessor

        processor = LegacyProcessor()
        assert isinstance(processor, BhojpuriProcessor)

        text = "हमर बा"
        processed = processor.process(text)
        assert "हमर" not in processed["filtered_tokens"]

    def test_classification(self):
        from src.dialects.bhojpuri import BhojpuriDialectClassifier

        classifier = BhojpuriDialectClassifier()

        # Southern (Standard)
        assert classifier.classify("रउआ बानी") == "Southern (Standard)"

        # Northern
        assert classifier.classify("बाटे") == "Northern"

        # Western
        assert classifier.classify("हौ") == "Western"

    def test_morphology(self, processor):
        # Test stemming
        assert processor.get_stem("जाईबानी") == "जाई"  # "बानी" is suffix

        # Test analysis
        analysis = processor.analyze_morphology("जाईबानी")
        assert analysis["root"] == "जाई"
        assert analysis["suffix"] == "बानी"
        assert analysis["category"] == "be"

    def test_grammar_loading(self, processor):
        assert processor.grammar is not None
        assert "syntax" in processor.grammar
        assert processor.grammar["syntax"]["word_order"] == "SOV"

    def test_stress_analysis(self, processor):
        # Test stress assignment
        # "पानी" (pānī) -> pā-nī (both long). Rule: heaviest of last 3.
        # If equal, rightmost? My code: "Find rightmost heavy syllable".
        # So "nī" (index 1) should be stressed.
        assert processor.analyze_stress("पानी") == 1

        # "कमल" (kamal) -> ka-ma-la (all short).
        # Rule: if no heavy, default to penultimate (index 1).
        # ka (0), ma (1), la (2). Penultimate is 'ma' (1).
        assert processor.analyze_stress("कमल") == 1
