from src.language.hindi_processor import HindiProcessor


class BhojpuriProcessor(HindiProcessor):
    """Bhojpuri processor - extends Hindi"""

    def __init__(self):
        super().__init__()
        # Add Bhojpuri-specific stop words
        bhojpuri_stops = {
            "ba",
            "bate",
            "bari",
            "ho",
            "raua",
            "hamar",
            "tohar",
            "ka",
            "ke",
            "ki",
            "se",
            "me",
            "par",
            "ne",
            "bani",
            "bhayil",
            "rah",
            "ja",
            "aa",
            "na",
        }
        self.stop_words.update(bhojpuri_stops)
