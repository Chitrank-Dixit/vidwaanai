from src.language.hindi_processor import HindiProcessor


class ChhattisgarhiProcessor(HindiProcessor):
    """Chhattisgarhi processor - extends Hindi"""

    def __init__(self) -> None:
        super().__init__()
        # Add Chhattisgarhi-specific stop words
        chhattisgarhi_stops = {
            "havay",
            "he",
            "har",
            "ola",
            "ela",
            "ka",
            "bar",
            "ma",
            "le",
            "se",
            "ke",
            "au",
            "mor",
            "tor",
            "haman",
            "tuman",
        }
        self.stop_words.update(chhattisgarhi_stops)
