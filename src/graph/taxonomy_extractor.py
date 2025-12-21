import re
import logging
from typing import Dict, Any, List, Set, Tuple
from src.graph.ontology import VEDIC_ONTOLOGY
from src.graph.schema import EntityType

logger = logging.getLogger(__name__)

class TaxonomyExtractor:
    """
    Rule-based extractor that uses VEDIC_ONTOLOGY to identify entities in text.
    """

    def __init__(self) -> None:
        self.lookup_map: Dict[str, Dict[str, Any]] = {}
        self.patterns: List[Tuple[str, str]] = [] # List of (pattern, entity_id)
        self._build_lookup_map()

    def _build_lookup_map(self) -> None:
        """Flatten ontology into a name -> entity lookup map."""
        
        def traverse(obj: Any) -> None:
            if isinstance(obj, dict):
                # Check if it's an entity definition (has 'id' and 'type')
                if "id" in obj and "type" in obj:
                    entity = obj
                    # Add main name
                    name = entity.get("name", "").lower()
                    if name:
                        self.lookup_map[name] = entity
                    
                    # Add sanskrit name
                    sans_name = entity.get("sanskrit_name", "").lower()
                    if sans_name:
                        self.lookup_map[sans_name] = entity
                        
                    # Add synonyms/aliases if any (not in current minimal schema but good for future)
                    if "synonyms" in entity:
                        for syn in entity["synonyms"]:
                            self.lookup_map[syn.lower()] = entity

                # Recurse
                for key, value in obj.items():
                    # Avoid recursing into entity fields like 'attributes' or 'relations'
                    if key not in ["attributes", "relations", "components"]:
                        traverse(value)
            elif isinstance(obj, list):
                for item in obj:
                    traverse(item)

        traverse(VEDIC_ONTOLOGY)
        
        # Build regex patterns for efficient matching
        # Sort by length desc to match longest phrases first ("Bhakti Yoga" before "Bhakti")
        sorted_names = sorted(self.lookup_map.keys(), key=len, reverse=True)
        
        # Simple word boundary matching
        for name in sorted_names:
            # Escape regex characters
            escaped = re.escape(name)
            # Match whole words only
            pattern = r'\b' + escaped + r'\b'
            self.patterns.append((pattern, name))
            
        logger.info(f"TaxonomyExtractor initialized with {len(self.lookup_map)} entities")

    def extract(self, text: str) -> List[Dict[str, Any]]:
        """
        Scan text and return list of found entities.
        """
        found_entities: List[Dict[str, Any]] = []
        found_ids: Set[str] = set()
        
        lower_text = text.lower()
        
        for pattern, name_key in self.patterns:
            if re.search(pattern, lower_text):
                entity = self.lookup_map[name_key]
                if entity['id'] not in found_ids:
                    found_entities.append(entity)
                    found_ids.add(entity['id'])
        
        return found_entities

if __name__ == "__main__":
    # Simple test
    extractor = TaxonomyExtractor()
    text = "Krishna taught Arjuna about Dharma and Karma Yoga on the battlefield of Kurukshetra."
    results = extractor.extract(text)
    print(f"Found {len(results)} entities:")
    for e in results:
        print(f"- {e['name']} ({e['type']})")
