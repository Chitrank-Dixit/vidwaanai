from src.language.hindi_processor import HindiProcessor

class MaithiliProcessor(HindiProcessor):
    """Maithili processor - extends Hindi"""
    
    def __init__(self):
        super().__init__()
        # Add Maithili-specific stop words
        maithili_stops = {
            'chi', 'achi', 'aich', 'chhai', 'chhal',
            'hum', 'aahan', 'to', 'ki', 'je', 'se',
            'me', 'per', 'le', 'la', 'k', 'r'
        }
        self.stop_words.update(maithili_stops)
