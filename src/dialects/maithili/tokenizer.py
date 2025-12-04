import regex
from typing import List


class MaithiliTokenizer:
    """
    Tokenizer for Maithili text.
    """

    def __init__(self) -> None:
        # Regex for matching words (Devanagari range + common chars)
        # \p{L} matches unicode letters, \p{M} matches marks (matras)
        self.word_pattern = regex.compile(
            r"[\p{L}\p{M}]+|[\p{N}]+|[^\s\p{L}\p{M}\p{N}]+"
        )

        # Sentence splitter pattern (Danda |, Double Danda ||, ?, !, .)
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
