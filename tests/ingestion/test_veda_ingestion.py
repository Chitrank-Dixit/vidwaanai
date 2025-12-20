from src.ingestion.veda_parser import VedaParser


class TestVedaIngestion:
    """Test Veda ingestion pipeline."""

    def test_veda_structure_parsing(self):
        """Test parsing of Veda structure."""
        parser = VedaParser()
        # Mock 2 pages
        pages = [
            {"text": "मंडल 1 सूक्त 1 mantra_header_ignore\nमंत्र 1\nअग्निमीळे पुरोहितं..."},
            {"text": "मंत्र 2\nअग्निः पूर्वेभिर्ऋषिभिर..."},
        ]

        mantras = parser.parse_vedas(pages, "rig")

        # We might get a header chunk + 2 mantras, or just 2 mantras depending on split
        assert len(mantras) >= 2

        # Find the mantra with number 1 (it might be the first or second depending on if header was valid chunk)
        m1 = next(m for m in mantras if "अग्निमीळे" in m["text"])
        assert m1["mandala_id"] == 1
        assert m1["sukta_id"] == 1
        assert "अग्नि" in m1["text"]

        m2 = next(m for m in mantras if "पूर्वेभिर्ऋषिभिर" in m["text"])
        assert m2["mantra_number"] > m1["mantra_number"]

    def test_tag_extraction(self):
        """Test that tags are extracted correctly."""
        parser = VedaParser()
        text = "यह मंत्र अग्नि और सूर्य की स्तुति करता है"
        tags = parser._extract_tags(text)

        assert "ritual" in tags  # 'अग्नि' -> ritual
        assert "nature" in tags  # 'सूर्य' -> nature
