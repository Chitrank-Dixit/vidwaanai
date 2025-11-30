from langdetect import detect, detect_langs, DetectorFactory
import regex
from src.core.logger import get_logger

logger = get_logger(__name__)

# Ensure consistent results
DetectorFactory.seed = 0

class LanguageDetector:
    SUPPORTED_LANGUAGES = {
        'hi': 'Hindi',
        'en': 'English',
        'gu': 'Gujarati',
        'ta': 'Tamil',
        'te': 'Telugu',
        'kn': 'Kannada',
        'ml': 'Malayalam',
        'bn': 'Bengali',
        'mr': 'Marathi'
    }
    
    @staticmethod
    def detect_language(text: str) -> tuple:
        """
        Detect language of text
        Returns: (language_code, language_name, confidence)
        """
        try:
            # Detect with probabilities
            probabilities = detect_langs(text)
            
            if probabilities:
                lang_code = probabilities[0].lang
                confidence = probabilities[0].prob
                
                if lang_code in LanguageDetector.SUPPORTED_LANGUAGES:
                    lang_name = LanguageDetector.SUPPORTED_LANGUAGES[lang_code]
                    return (lang_code, lang_name, confidence)
        
        except Exception as e:
            logger.warning(f"Language detection failed: {e}")
        
        # Default to English
        return ('en', 'English', 0.0)
    
    @staticmethod
    def detect_script(text: str) -> str:
        """Detect Unicode script"""
        for char in text:
            if '\u0939' <= char <= '\u097F': # Devanagari range (approx)
                return 'Devanagari'
            elif '\u0900' <= char <= '\u097F':
                return 'Devanagari'
            elif '\u0A80' <= char <= '\u0AFF':
                return 'Gujarati'
            elif '\u0B80' <= char <= '\u0BFF':
                return 'Tamil'
            elif '\u0C00' <= char <= '\u0C7F':
                return 'Telugu'
            elif '\u0C80' <= char <= '\u0CFF':
                return 'Kannada'
        
        return 'Latin'  # English or other
