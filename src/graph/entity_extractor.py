import json
import logging
from typing import Any, Dict, cast

from src.graph.schema import EntityType, RelationType

logger = logging.getLogger(__name__)


class EntityExtractor:
    """Extract entities and relationships from scripture verses."""

    def __init__(self, llm_client: Any) -> None:
        self.llm = llm_client

    def extract_entities(
        self, verse_text: str, translation: str, scripture_name: str
    ) -> Dict[str, Any]:
        """
        Extract entities and relationships using LLM with Schema enforcement.
        """
        # Create lists of valid types for the prompt
        entity_types = ", ".join([e.value for e in EntityType])
        relation_types = ", ".join([r.value for r in RelationType])

        prompt = f"""
Extract entities and relationships from this scripture verse based on the following Ontology.

Scripture: {scripture_name}
Original: {verse_text}
Translation: {translation}

VALID ENTITY TYPES: {entity_types}
VALID RELATION TYPES: {relation_types}

Return ONLY valid JSON. 
For each entity, use a valid "type" from the list above.
For each relationship, use a valid "type" from the list above.

Format:
{{
  "entities": [
    {{"name": "EntityName", "type": "ValidType", "attributes": {{"description": "..."}}}}
  ],
  "relationships": [
    {{"from": "SourceEntityName", "to": "TargetEntityName", "type": "ValidRelationType", "attributes": {{"context": "..."}}}}
  ]
}}

Ensure "from" and "to" match extracted entity names exactly.
"""

        response = self.llm.generate(prompt, max_tokens=1000, temperature=0.1)
        try:
            # Clean response if it contains markdown code blocks
            cleaned_response = response.strip()
            if "```json" in cleaned_response:
                cleaned_response = (
                    cleaned_response.split("```json")[1].split("```")[0].strip()
                )
            elif "```" in cleaned_response:
                cleaned_response = (
                    cleaned_response.split("```")[1].split("```")[0].strip()
                )

            return dict(json.loads(cleaned_response))
        except Exception as e:
            logger.error(f"Failed to parse entity extraction response: {e}")
            logger.debug(f"Raw response: {response}")
            return {"entities": [], "relationships": []}

    def extract_from_query(self, query: str) -> list[dict[str, Any]]:
        """
        Extract entities from a user query.

        Returns:
        [
            {"name": "Krishna", "type": "Person"},
            {"name": "dharma", "type": "Concept"}
        ]
        """
        prompt = f"""
        Extract key entities from this user query for a knowledge graph search.
        Identify Persons, Concepts, Places, or Events.
        
        Query: {query}
        
        Return ONLY valid JSON list of objects.
        Example:
        [
          {{"name": "Krishna", "type": "Person"}},
          {{"name": "karma", "type": "Concept"}}
        ]
        """

        response = self.llm.generate(prompt, max_tokens=300, temperature=0.1)
        try:
            cleaned_response = response.strip()
            if "```json" in cleaned_response:
                cleaned_response = (
                    cleaned_response.split("```json")[1].split("```")[0].strip()
                )
            elif "```" in cleaned_response:
                cleaned_response = (
                    cleaned_response.split("```")[1].split("```")[0].strip()
                )

            result = json.loads(cleaned_response)
            if isinstance(result, list):
                return cast(list[dict[str, Any]], result)
            if isinstance(result, dict) and "entities" in result:
                return cast(list[dict[str, Any]], result["entities"])
            return []
        except Exception as e:
            logger.error(f"Failed to extract entities from query: {e}")
            return []
