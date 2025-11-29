from typing import Dict
import logging
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

Return ONLY valid JSON. For each relationship, provide:
- "from": source entity name (e.g., "Krishna", "dharma")
- "to": target entity name (e.g., "Arjuna", "karma")
- "type": relationship type (TEACHES, RELATES_TO, APPEARS_IN, PERFORMS, etc.)

Example:
{{
  "entities": [
    {{"name": "Krishna", "type": "Person", "attributes": {{"description": "..."}}}},
    {{"name": "dharma", "type": "Concept", "attributes": {{"description": "..."}}}}
  ],
  "relationships": [
    {{"from": "Krishna", "to": "dharma", "type": "TEACHES", "attributes": {{"context": "..."}}}}
  ]
}}

Ensure "from" and "to" are actual entity names, NOT descriptions or sentences.
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
