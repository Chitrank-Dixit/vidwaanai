from src.language.hindi_processor import HindiProcessor

class HaryanviProcessor(HindiProcessor):
    """Haryanvi processor - extends Hindi"""
    
    def __init__(self):
        super().__init__()
        # Add Haryanvi-specific stop words
        haryanvi_stops = {
            'ib', 'eb', 'kad', 'jad', 'kit', 'jit',
            'ke', 'yo', 'ya', 'wa', 'wo', 'su', 'se', 'sai',
            'na', 'nu', 'nyu', 'ade', 'ode', 'uray', 'paray'
        }
        self.stop_words.update(haryanvi_stops)
