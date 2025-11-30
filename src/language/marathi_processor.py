from src.language.hindi_processor import HindiProcessor

class MarathiProcessor(HindiProcessor):
    """Marathi processor - extends Hindi due to same script (Devanagari)"""
    
    def __init__(self):
        # Override Hindi stop words with Marathi stop words
        self.stop_words = set([
            'ahe', 'aahet', 'hote', 'hoti', 'hota',
            'ha', 'hi', 'he', 'ya', 'tyaa',
            'v', 'kinva', 'parantu', 'kaaran', 'mhanun',
            'aasanya', 'tari', 'saare', 'pratyek', 'kahi',
            'pan', 'tyala', 'tila', 'mi', 'tumhi', 'apan',
            'aahe', 'nahit', 'nahi', 'aahes', 'hoto'
        ])
    
    # Inherits normalize, tokenize, remove_stopwords from HindiProcessor
    # No need to rewrite - same script = same processing logic
