#!/usr/bin/env python3
"""
Extract Ramayan ontology responses from manual batch query prompts (Batches 171-196).
Group responses into 10-batch JSON files: 171-180, 181-190, 191-196.
"""

import os
import sys
import json
import logging
from typing import Dict, Any, List

# Add project root to python path to import settings and clients
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.core.config import settings
from src.llm.openai_client import OpenAIClient
from src.llm.lmstudio_client import LMStudioClient

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("extract_ramayan_ontology")

# Constants
QUERIES_DIR = "ontology_project/queries/Ramayan"
RESPONSES_DIR = "scripts/responses/perplexity"

ONTOLOGY_HEADER = {
    "entity_types": ["Deity", "Concept", "Character", "Place", "Event", "Text"],
    "relationship_types": [
        "MENTIONS",
        "IS_AVATAR_OF",
        "RELATED_TO",
        "LOCATED_AT",
        "PARTICIPATED_IN",
    ],
}


def get_llm_client():
    """Initialize client based on config settings."""
    if settings.llm_backend == "lmstudio":
        logger.info(f"Using LM Studio backend: {settings.lmstudio_base_url}")
        return LMStudioClient(
            base_url=settings.lmstudio_base_url,
            model_name=settings.lmstudio_model,
            timeout=settings.LLM_TIMEOUT,
        )
    else:
        logger.info("Using OpenAI backend")
        if not settings.OPENAI_API_KEY:
            logger.warning(
                "OPENAI_API_KEY is not set in environment/settings. Attempting load anyway..."
            )
        return OpenAIClient(api_key=settings.OPENAI_API_KEY, model=settings.LLM_MODEL)


def clean_json_response(raw_text: str) -> Dict[str, Any]:
    """Clean markdown code block wrapping from the LLM JSON response."""
    cleaned = raw_text.strip()
    if "```json" in cleaned:
        cleaned = cleaned.split("```json")[1].split("```")[0].strip()
    elif "```" in cleaned:
        cleaned = cleaned.split("```")[1].split("```")[0].strip()
    return json.loads(cleaned)


def extract_from_file(client, filepath: str) -> Dict[str, Any]:
    """Read prompt from file and query LLM for entity extraction."""
    logger.info(f"Processing prompt file: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        prompt = f.read()

    # Query LLM (temperature=0.1 for high reproducibility/accuracy)
    response_text = client.generate(prompt, max_tokens=3000, temperature=0.1)

    try:
        data = clean_json_response(response_text)
        # Check basic keys
        if "entities" not in data:
            data["entities"] = []
        if "relationships" not in data:
            data["relationships"] = []
        return data
    except Exception as e:
        logger.error(f"Failed to parse or clean JSON response from {filepath}: {e}")
        logger.debug(f"Raw response: {response_text}")
        # Return empty template
        return {"entities": [], "relationships": []}


def merge_responses(responses: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Merge multiple batch responses together, deduplicating entities by name."""
    merged = {"ontology": ONTOLOGY_HEADER, "entities": [], "relationships": []}

    seen_entities = set()

    for resp in responses:
        # Normalize and merge entities
        for entity in resp.get("entities", []):
            name = entity.get("name")
            if not name:
                continue
            name_lower = name.lower()
            if name_lower not in seen_entities:
                merged["entities"].append(entity)
                seen_entities.add(name_lower)

        # Combine relationships
        for rel in resp.get("relationships", []):
            # Normalization of keys
            source = rel.get("from") or rel.get("source")
            target = rel.get("to") or rel.get("target")
            rel_type = rel.get("type")

            if source and target and rel_type:
                normalized_rel = {
                    "from": source,
                    "to": target,
                    "type": rel_type,
                    "attributes": rel.get("attributes", {}),
                }
                merged["relationships"].append(normalized_rel)

    return merged


def main():
    os.makedirs(RESPONSES_DIR, exist_ok=True)
    client = get_llm_client()

    # Range of batches to process
    start_batch = 171
    end_batch = 196

    # Store results in memory temporarily
    batch_results = {}

    # Process each batch file
    for batch_id in range(start_batch, end_batch + 1):
        filename = f"Ramayan_batch_{batch_id}.md"
        filepath = os.path.join(QUERIES_DIR, filename)

        if not os.path.exists(filepath):
            logger.warning(f"File not found, skipping: {filepath}")
            continue

        try:
            data = extract_from_file(client, filepath)
            batch_results[batch_id] = data
            logger.info(
                f"Successfully processed batch {batch_id}: {len(data['entities'])} entities, {len(data['relationships'])} relationships."
            )
        except Exception as e:
            logger.error(f"Error processing batch {batch_id}: {e}")

    # Define groups: (Start Batch, End Batch, Target Filename)
    groups = [
        (171, 180, "ramayan_171_180.json"),
        (181, 190, "ramayan_181_190.json"),
        (191, 196, "ramayan_191_196.json"),
    ]

    for start, end, target_name in groups:
        group_responses = []
        for b_id in range(start, end + 1):
            if b_id in batch_results:
                group_responses.append(batch_results[b_id])

        if group_responses:
            merged = merge_responses(group_responses)
            target_path = os.path.join(RESPONSES_DIR, target_name)
            with open(target_path, "w", encoding="utf-8") as f:
                json.dump(merged, f, indent=4, ensure_ascii=False)
            logger.info(
                f"Saved merged response to: {target_path} (Contains batches {start} to {end})"
            )
        else:
            logger.warning(
                f"No data available for group {start}-{end}, skipping {target_name}"
            )


if __name__ == "__main__":
    main()
