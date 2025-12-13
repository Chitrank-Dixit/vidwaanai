import torch
from typing import Any, Dict
from transformers import MarianMTModel, MarianTokenizer

from src.core.logger import get_logger

logger = get_logger(__name__)


class ResponseTranslator:
    def __init__(self) -> None:
        # Load translation models lazily or on init
        # For MVP, we'll load on demand or keep a cache
        self.models: Dict[str, Any] = {}
        self.tokenizers: Dict[str, Any] = {}

        # Supported pairs (Source -> Target)
        # Using Helsinki-NLP models from Hugging Face
        self.model_map = {
            "en_to_hi": "Helsinki-NLP/opus-mt-en-hi",
            "hi_to_en": "Helsinki-NLP/opus-mt-hi-en",
            # Note: Direct models for other Indian languages might be limited in Opus-MT
            # We might need to pivot through English or use a multilingual model like NLLB later
            # For now, let's stick to what's reliably available or fallback to English
        }

    def _load_model(self, model_name: str) -> Any:
        if model_name not in self.models:
            logger.info(f"Loading translation model: {model_name}")
            try:
                self.tokenizers[model_name] = MarianTokenizer.from_pretrained(
                    model_name
                )  # nosec B615
                self.models[model_name] = MarianMTModel.from_pretrained(
                    model_name
                )  # nosec B615
            except Exception as e:
                logger.error(f"Failed to load model {model_name}: {e}")
                return None
        return self.models.get(model_name)

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """Translate text from source to target language"""
        if source_lang == target_lang:
            return text

        key = f"{source_lang}_to_{target_lang}"
        model_name = self.model_map.get(key)

        if not model_name:
            logger.warning(f"No translation model found for {key}")
            return text

        model = self._load_model(model_name)
        if not model:
            return text

        tokenizer = self.tokenizers[model_name]

        # Tokenize
        inputs = tokenizer(
            text, return_tensors="pt", padding=True, truncation=True, max_length=512
        )

        # Generate
        with torch.no_grad():
            translated = model.generate(**inputs)

        # Decode
        result = tokenizer.decode(translated[0], skip_special_tokens=True)
        return str(result)
