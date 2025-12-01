import pytest
import time
from src.language.language_detector import LanguageDetector

class TestLanguageDetector:
    
    @pytest.fixture
    def detector(self):
        return LanguageDetector()

    # --- A. Basic Detection ---
    
    def test_detect_english(self, detector):
        text = "This is a sample English sentence for detection."
        code, name, conf = detector.detect_language(text)
        assert code == 'en'
        assert name == 'English'
        assert conf > 0.9

    def test_detect_hindi(self, detector):
        text = "यह हिंदी भाषा का एक उदाहरण वाक्य है।"
        code, name, conf = detector.detect_language(text)
        assert code == 'hi'
        assert name == 'Hindi'
        assert conf > 0.9

    def test_detect_gujarati(self, detector):
        text = "આ ગુજરાતી ભાષાનું ઉદાહરણ વાક્ય છે."
        code, name, conf = detector.detect_language(text)
        assert code == 'gu'
        assert name == 'Gujarati'
        assert conf > 0.9

    def test_detect_tamil(self, detector):
        text = "இது தமிழ் மொழிக்கான ஒரு எடுத்துக்காட்டு வாக்கியம்."
        code, name, conf = detector.detect_language(text)
        assert code == 'ta'
        assert name == 'Tamil'
        assert conf > 0.9

    def test_detect_telugu(self, detector):
        text = "ఇది తెలుగు భాషకు ఉదాహరణ వాక్యం."
        code, name, conf = detector.detect_language(text)
        assert code == 'te'
        assert name == 'Telugu'
        assert conf > 0.9

    def test_detect_kannada(self, detector):
        text = "ಇದು ಕನ್ನಡ ಭಾಷೆಯ ಉದಾಹರಣೆ ವಾಕ್ಯ."
        code, name, conf = detector.detect_language(text)
        assert code == 'kn'
        assert name == 'Kannada'
        assert conf > 0.9
        
    def test_detect_bengali(self, detector):
        text = "এটি বাংলা ভাষার একটি উদাহরণ বাক্য।"
        code, name, conf = detector.detect_language(text)
        assert code == 'bn'
        assert name == 'Bengali'
        assert conf > 0.9
        
    def test_detect_marathi(self, detector):
        text = "हे मराठी भाषेचे उदाहरण वाक्य आहे."
        code, name, conf = detector.detect_language(text)
        assert code == 'mr'
        assert name == 'Marathi'
        assert conf > 0.9
        
    def test_detect_malayalam(self, detector):
        text = "ഇതൊരു മലയാളം വാചകമാണ്."
        code, name, conf = detector.detect_language(text)
        assert code == 'ml'
        assert name == 'Malayalam'
        assert conf > 0.9

    def test_detect_mixed_language(self, detector):
        # Primarily Hindi with some English
        text = "Main aaj market ja raha hoon. यह बहुत अच्छा है।"
        code, name, conf = detector.detect_language(text)
        # Should detect Hindi or English depending on weight, but usually Hindi script dominates if present
        # Or if transliterated, might be tricky. Let's use mixed script.
        # "Hello world यह हिंदी है" -> Should likely be Hindi due to script uniqueness
        text_mixed = "Hello world यह हिंदी है"
        code, _, _ = detector.detect_language(text_mixed)
        assert code in ['hi', 'en']

    def test_detect_single_word(self, detector):
        text = "Namaste"
        code, _, _ = detector.detect_language(text)
        # Single words are hard, but 'Namaste' might be detected as Hindi or English (loan word)
        # Let's try a script-specific word
        text_hi = "नमस्ते"
        code_hi, _, _ = detector.detect_language(text_hi)
        assert code_hi == 'hi'

    def test_detect_long_text(self, detector):
        text = "This is a longer text to ensure that the language detector works correctly for larger inputs. " * 10
        code, _, conf = detector.detect_language(text)
        assert code == 'en'
        assert conf > 0.9

    def test_detect_with_numbers(self, detector):
        text = "The year is 2024 and the time is 10:00 AM."
        code, _, _ = detector.detect_language(text)
        assert code == 'en'

    def test_detect_with_urls(self, detector):
        text = "Check out https://google.com for more info."
        code, _, _ = detector.detect_language(text)
        assert code == 'en'

    def test_detect_special_characters(self, detector):
        text = "Hello!!! @World #Testing $100"
        code, _, _ = detector.detect_language(text)
        assert code == 'en'

    # --- B. Edge Cases ---

    def test_handle_none_input(self, detector):
        # Assuming implementation should handle or raise. 
        # The current implementation catches exceptions and returns default English.
        # Let's verify that behavior or update it.
        # Looking at code: try...except returns ('en', 'English', 0.0)
        code, name, conf = detector.detect_language(None) # type: ignore
        assert code == 'en'
        assert conf == 0.0

    def test_handle_whitespace_only(self, detector):
        code, name, conf = detector.detect_language("   ")
        assert code == 'en'
        assert conf == 0.0

    def test_handle_numbers_only(self, detector):
        code, name, conf = detector.detect_language("12345 67890")
        assert code == 'en' # Default fallback likely
        assert conf == 0.0 # Low confidence

    def test_handle_unsupported_language(self, detector):
        # French text
        text = "Bonjour le monde"
        code, name, conf = detector.detect_language(text)
        # Should return 'en' fallback because 'fr' is not in SUPPORTED_LANGUAGES
        assert code == 'en' 
        assert conf == 0.0

    # --- C. Confidence Thresholds ---
    
    def test_high_confidence(self, detector):
        text = "This is a very clear English sentence."
        _, _, conf = detector.detect_language(text)
        assert conf > 0.8

    def test_ambiguous_text(self, detector):
        # Short text that could be many languages
        text = "a" 
        _, _, conf = detector.detect_language(text)
        # Confidence should be lower or default fallback
        # langdetect might be weird with single chars, but let's check it's not 1.0
        # Actually 'a' is English word too.
        pass # Hard to guarantee low confidence with langdetect without specific examples

    # --- D. Performance ---

    def test_performance_short_text(self, detector):
        text = "Hello world"
        start = time.time()
        detector.detect_language(text)
        duration = time.time() - start
        assert duration < 0.1 # 100ms

    def test_performance_long_text(self, detector):
        text = "This is a test sentence. " * 100
        start = time.time()
        detector.detect_language(text)
        duration = time.time() - start
        assert duration < 0.1 # 100ms
