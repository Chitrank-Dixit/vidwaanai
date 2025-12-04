from src.language.marathi_processor import MarathiProcessor


class KonkaniProcessor(MarathiProcessor):
    """Konkani processor - extends Marathi due to similarity and Devanagari script"""

    def __init__(self) -> None:
        super().__init__()
        # Add Konkani-specific stop words
        konkani_stops = {
            "asa",
            "zala",
            "kitem",
            "konn",
            "koso",
            "hanv",
            "tum",
            "ami",
            "tumi",
            "te",
            "maka",
            "tuka",
            "amkam",
            "tumkam",
        }
        self.stop_words.update(konkani_stops)
