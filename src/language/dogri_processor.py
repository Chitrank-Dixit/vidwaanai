from src.language.hindi_processor import HindiProcessor


class DogriProcessor(HindiProcessor):
    """Dogri processor - extends Hindi"""

    def __init__(self):
        super().__init__()
        # Add Dogri-specific stop words
        dogri_stops = {
            "sa",
            "si",
            "ha",
            "tha",
            "ne",
            "ki",
            "jo",
            "so",
            "kune",
            "keda",
            "kida",
            "au",
            "tus",
            "as",
            "tus",
        }
        self.stop_words.update(dogri_stops)
