import json
import logging
from typing import Any, Dict, cast, List

import spacy
from src.graph.schema import EntityType, RelationType

logger = logging.getLogger(__name__)


class EntityExtractor:
    """Extract entities and relationships from scripture verses."""

    def __init__(self, llm_client: Any) -> None:
        self.llm = llm_client
        try:
            self.nlp = spacy.load("en_core_web_sm")
            logger.info("SpaCy model 'en_core_web_sm' loaded successfully.")
        except OSError:
            logger.warning("SpaCy model 'en_core_web_sm' not found. Creating blank model.")
            self.nlp = spacy.blank("en")

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

        except Exception as e:
            logger.error(f"Failed to parse entity extraction response: {e}")
            logger.debug(f"Raw response: {response}")
            return {"entities": [], "relationships": []}

    def extract_with_spacy(self, text: str) -> List[Dict[str, Any]]:
        """
        Extract standard entities using SpaCy.
        Returns mapped entities: PERSON, ORG, GPE, LOC, EVENT
        """
        doc = self.nlp(text)
        entities = []
        
        # Mapping SpaCy labels to our Ontology types
        label_map = {
            "PERSON": "Person",
            "ORG": "Concept",  # Rough mapping
            "GPE": "Place",
            "LOC": "Place",
            "EVENT": "Event",
            "FAC": "Place"
        }
        
        for ent in doc.ents:
            if ent.label_ in label_map:
                entities.append({
                    "name": ent.text,
                    "type": label_map[ent.label_],
                    "source": "spacy"
                })
                
        return entities

    def extract_from_query(self, query: str) -> List[Dict[str, Any]]:
        """
        Extract entities from a user query using Hybrid approach (SpaCy + LLM).
        """
        # 1. Try SpaCy first for speed
        spacy_entities = self.extract_with_spacy(query)
        
        # If we found relevant entities, we might skip LLM or combine.
        # For MVP, if we find Persons or Concepts, we trust them, but Vedic entities 
        # (like 'Dharma', 'Agni') might not be caught by standard metrics unless capitalized.
        
        # Let's always call LLM for now to ensure high recall for Vedic terms, 
        # but in production we can optimize.
        
        # For the purpose of this task (Quick Win), let's just use LLM as primary 
        # but mention SpaCy usage for standard things.
        
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

        try:
            response = self.llm.generate(prompt, max_tokens=300, temperature=0.1)
            cleaned_response = response.strip()
            if "```json" in cleaned_response:
                cleaned_response = (
                    cleaned_response.split("```json")[1].split("```")[0].strip()
                )
            elif "```" in cleaned_response:
                cleaned_response = (
                    cleaned_response.split("```")[1].split("```")[0].strip()
                )

            llm_results = json.loads(cleaned_response)
            if not isinstance(llm_results, list):
                if isinstance(llm_results, dict) and "entities" in llm_results:
                    llm_results = llm_results["entities"]
                else:
                    llm_results = []
            
            # Merge results (deduplicate by name)
            seen_names = set()
            final_entities = []
            
            # Prioritize LLM results (likely better for Vedic context)
            for ent in llm_results:
                name = ent.get("name")
                if name:
                    final_entities.append(ent)
                    seen_names.add(name.lower())
            
            # Add SpaCy results if new
            for ent in spacy_entities:
                name = ent.get("name")
                if name and name.lower() not in seen_names:
                    final_entities.append(ent)
                    seen_names.add(name.lower())
                    
            return final_entities

        except Exception as e:
            logger.error(f"Failed to extract entities from query: {e}")
            # Fallback to just SpaCy if LLM failed
            return spacy_entities
