from src.language.hindi_processor import HindiProcessor

class MarathiProcessor(HindiProcessor):
    """Marathi processor - extends Hindi due to same script (Devanagari)"""
    
    def __init__(self):
        # Override Hindi stop words with Marathi stop words
        self.stop_words = set([
            'आहे', 'आहेत', 'होते', 'होती', 'होता',
            'हा', 'ही', 'हे', 'या', 'त्या',
            'व', 'किंवा', 'परंतु', 'कारण', 'म्हणून',
            'असून', 'तरी', 'सारे', 'प्रत्येक', 'काही',
            'पण', 'त्याला', 'तिला', 'मी', 'तुम्ही', 'आपण',
            'नाही', 'नाहीत', 'आहेस', 'होतो'
        ])
    
    # Inherits normalize, tokenize, remove_stopwords from HindiProcessor
    # No need to rewrite - same script = same processing logic
