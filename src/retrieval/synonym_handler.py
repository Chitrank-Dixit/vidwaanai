from typing import List

from src.core.logger import get_logger

logger = get_logger(__name__)


class SynonymHandler:
    def __init__(self) -> None:
        # Domain-specific synonyms for Indian scriptures
        self.synonyms = {
            "dharma": ["duty", "righteousness", "law", "virtue", "ethics"],
            "karma": ["action", "deed", "consequence", "destiny"],
            "moksha": [
                "liberation",
                "enlightenment",
                "nirvana",
                "freedom",
                "salvation",
            ],
            "atman": ["soul", "self", "spirit", "consciousness"],
            "brahman": ["ultimate reality", "absolute", "god", "divine"],
            "vedas": ["scriptures", "holy texts", "knowledge", "sacred texts"],
            "krishna": ["lord krishna", "govinda", "madhava", "vasudeva"],
            "shiva": ["lord shiva", "mahadev", "rudra", "shankar"],
            "vishnu": ["lord vishnu", "narayana", "hari"],
            "arjuna": ["partha", "dhananjaya"],
            "yoga": ["union", "discipline", "practice"],
            "bhakti": ["devotion", "love", "worship"],
            "jnana": ["knowledge", "wisdom"],
            "gita": ["bhagavad gita", "song of god"],
        }

    def get_synonyms(self, term: str) -> List[str]:
        """Get synonyms for a term"""
        term_lower = term.lower()

        if term_lower in self.synonyms:
            return self.synonyms[term_lower]

        # Check if term is a synonym (reverse lookup)
        for key, syn_list in self.synonyms.items():
            if term_lower in [s.lower() for s in syn_list]:
                # Return the key and other synonyms
                others = [s for s in syn_list if s.lower() != term_lower]
                return [key] + others

        return []

    def expand_query(self, query: str) -> str:
        """Expand query with synonyms"""
        words = query.split()
        expanded_terms = []

        for word in words:
            synonyms = self.get_synonyms(word)
            if synonyms:
                # Add original word
                expanded_terms.append(word)
                # Add top 2 synonyms to avoid query drift
                expanded_terms.extend(synonyms[:2])
                logger.info(f"Expanded term '{word}' with: {synonyms[:2]}")
            else:
                expanded_terms.append(word)

        # Remove duplicates while preserving order
        seen = set()
        unique_terms = []
        for x in expanded_terms:
            if x.lower() not in seen:
                seen.add(x.lower())
                unique_terms.append(x)

        return " ".join(unique_terms)
