from abc import ABC, abstractmethod
from typing import List, Dict, Any

class LanguageProcessor(ABC):
    """Base class for language-specific processing"""
    
    @abstractmethod
    def normalize(self, text: str) -> str:
        """Normalize text for language"""
        pass
    
    @abstractmethod
    def tokenize(self, text: str) -> List[str]:
        """Tokenize text for language"""
        pass
    
    @abstractmethod
    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """Remove stop words for language"""
        pass
    
    def preprocess(self, text: str) -> Dict[str, Any]:
        """Complete preprocessing pipeline"""
        # Normalize
        normalized = self.normalize(text)
        
        # Tokenize
        tokens = self.tokenize(normalized)
        
        # Remove stop words
        filtered = self.remove_stopwords(tokens)
        
        return {
            'original': text,
            'normalized': normalized,
            'tokens': tokens,
            'filtered_tokens': filtered,
            'processed_text': ' '.join(filtered)
        }
