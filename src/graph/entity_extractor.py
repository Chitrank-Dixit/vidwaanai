from typing import List, Dict
import logging
import logging
import re
import json

logger = logging.getLogger(__name__)

class EntityExtractor:
    """Extract entities and relationships from scripture verses."""
    
    def __init__(self, llm_client):
        self.llm = llm_client
        
    def extract_entities(self, verse_text: str, translation: str, 
                        scripture_name: str) -> Dict:
        """
        Extract entities using LLM.
        
        Returns:
        {
            "entities": [
                {"type": "Person", "name": "Krishna", "attributes": {...}},
                {"type": "Concept", "name": "dharma", "attributes": {...}}
            ],
            "relationships": [
                {"from": "Krishna", "to": "Arjuna", "type": "TEACHES", 
                 "attributes": {...}}
            ]
        }
        """
        prompt = f"""
Extract entities and relationships from this scripture verse.

Scripture: {scripture_name}
Original: {verse_text}
Translation: {translation}

Extract:
1. PERSONS (deities, sages, warriors, kings)
2. CONCEPTS (dharma, karma, yoga, moksha, etc.)
3. EVENTS (wars, ceremonies, dialogues)
4. LOCATIONS (cities, forests, mountains)

For each entity, identify:
- Type (Person/Concept/Event/Location)
- Name (primary and aliases)
- Attributes (description, role, etc.)

Also extract RELATIONSHIPS between entities:
- Type (TEACHES, RELATES_TO, APPEARS_IN, etc.)
- Direction (from → to)
- Context

Return as JSON.
"""
        
        response = self.llm.generate(prompt, max_tokens=800, temperature=0.3)
        try:
            # Clean response if it contains markdown code blocks
            cleaned_response = response.strip()
            if "```json" in cleaned_response:
                cleaned_response = cleaned_response.split("```json")[1].split("```")[0].strip()
            elif "```" in cleaned_response:
                cleaned_response = cleaned_response.split("```")[1].split("```")[0].strip()
            
            return json.loads(cleaned_response)
        except Exception as e:
            logger.error(f"Failed to parse entity extraction response: {e}")
            logger.debug(f"Raw response: {response}")
            return {"entities": [], "relationships": []}
