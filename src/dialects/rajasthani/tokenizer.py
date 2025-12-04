import regex
from typing import List


class RajasthaniTokenizer:
    """
    Tokenizer for Rajasthani text.
    """

    def __init__(self) -> None:
        # Regex for matching words
        self.word_pattern = regex.compile(
            r"[\p{L}\p{M}]+|[\p{N}]+|[^\s\p{L}\p{M}\p{N}]+"
        )

        # Sentence splitter pattern
        self.sentence_pattern = regex.compile(r"(?<=[।॥?!.])\s+")

    def tokenize_words(self, text: str) -> List[str]:
        """
        Tokenize text into words.

        Args:
            text: Input text

        Returns:
            List of tokens
        """
        if not text:
            return []
        return [str(match) for match in self.word_pattern.findall(text)]

    def tokenize_sentences(self, text: str) -> List[str]:
        """
        Split text into sentences.

        Args:
            text: Input text

        Returns:
            List of sentences
        """
        if not text:
            return []
        return [s.strip() for s in self.sentence_pattern.split(text) if s.strip()]
