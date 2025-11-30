from src.language.hindi_processor import HindiProcessor

class RajasthaniProcessor(HindiProcessor):
    """Rajasthani processor - extends Hindi"""
    
    def __init__(self):
        super().__init__()
        # Add Rajasthani-specific stop words
        rajasthani_stops = {
            'कोई', 'कुई', 'कूं', 'कै', 'नां', 'ने', 
            'सूं', 'सो', 'स्यो', 'हो', 'हुवो', 'हिओ',
            'पण', 'थे', 'म्हे', 'सा', 'कोनी'
        }
        self.stop_words.update(rajasthani_stops)
