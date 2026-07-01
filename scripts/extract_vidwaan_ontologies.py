#!/usr/bin/env python3
import argparse
import glob
import json
import logging
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any

from tqdm import tqdm

# Add project root to python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from scripts.clean_duplicate_names import clean_name
from src.core.config import settings
from src.graph.graph_builder import GraphBuilder
from src.graph.schema import EntityType, RelationType
from src.ingestion.pdf_extractor import PdfExtractor
from src.ingestion.scripture_parsers import get_parser
from src.ingestion.text_processor import TextProcessor
from src.llm.lmstudio_client import LMStudioClient
from src.llm.openai_client import OpenAIClient

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("extract_vidwaan_ontologies.log")],
)
logger = logging.getLogger("extract_vidwaan_ontologies")

DEFAULT_INPUT_DIR = "./raw_scriptures/"
DEFAULT_OUTPUT_DIR = "./data/ontologies/"


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
            logger.warning("OPENAI_API_KEY is not set in environment/settings.")
        return OpenAIClient(api_key=settings.OPENAI_API_KEY, model=settings.LLM_MODEL)


def clean_json_response(raw_text: str) -> dict[str, Any]:
    """Clean markdown code block wrapping from the LLM JSON response."""
    cleaned = raw_text.strip()
    if "```json" in cleaned:
        cleaned = cleaned.split("```json")[1].split("```")[0].strip()
    elif "```" in cleaned:
        cleaned = cleaned.split("```")[1].split("```")[0].strip()
    return json.loads(cleaned)


def extract_batch_ontology(llm, chunk: list[dict[str, Any]], scripture_name: str) -> dict[str, Any]:
    """Query LLM to extract entities and relationships from a batch of verses."""
    entity_types = ", ".join([e.value for e in EntityType])
    relation_types = ", ".join([r.value for r in RelationType])

    # Build segment representation
    verses_text = ""
    for i, v in enumerate(chunk):
        num = v.get("mantra_number", i + 1)
        verses_text += f"\n[Verse {num}]:\n{v['text']}\n"

    prompt = f"""
Extract entities and relationships from the following verses of the scripture: {scripture_name}.
Enforce schema constraints and entity resolution.

VERSES TO ANALYZE:
{verses_text}

VALID ENTITY TYPES:
{entity_types}

VALID RELATION TYPES:
{relation_types}

Return ONLY valid JSON format.
Ensure that:
1. Every entity name is canonicalized (e.g. use "Rama" instead of "ram", "Krishna" instead of "krsna", "Arjuna" instead of "arjun").
2. Standardize case and strip trailing whitespace.
3. Every entity maps to a valid "type" from the list above.
4. Every relationship maps to a valid "type" from the list above.
5. "from" and "to" match extracted entity names exactly.

JSON Schema:
{{
  "entities": [
    {{"name": "EntityName", "type": "ValidType", "attributes": {{"description": "..."}}}}
  ],
  "relationships": [
    {{"from": "SourceEntityName", "to": "TargetEntityName", "type": "ValidRelationType", "attributes": {{"context": "..."}}}}
  ]
}}
"""
    try:
        response_text = llm.generate(prompt, max_tokens=2500, temperature=0.1)
        data = clean_json_response(response_text)
        if "entities" not in data:
            data["entities"] = []
        if "relationships" not in data:
            data["relationships"] = []
        return data
    except Exception as e:
        logger.error(f"Failed to parse LLM extraction response: {e}")
        return {"entities": [], "relationships": []}


def process_pdf(pdf_path: str, scripture_type: str, args, llm) -> dict[str, Any]:
    """Process a single PDF: Extract -> Clean -> Segment -> Batch LLM Extraction."""
    filename = os.path.basename(pdf_path)
    scripture_name = os.path.splitext(filename)[0].replace("-", " ").replace("_", " ").title()

    logger.info(f"Processing PDF: {pdf_path} (Type: {scripture_type})")

    # 1. Extraction & Cleaning
    extractor = PdfExtractor()
    processor = TextProcessor()
    
    pages = extractor.extract_with_metadata(pdf_path, max_pages=args.limit_pages)
    for p in pages:
        p["text"] = processor.clean_text(p["text"])

    # 2. Section Segmentation
    parser = get_parser(scripture_type)
    if hasattr(parser, "parse"):
        verses = parser.parse(pages, scripture_type)
    elif hasattr(parser, "parse_vedas"):
        verses = parser.parse_vedas(pages, scripture_type)
    else:
        raise AttributeError(f"Parser {parser} has no parse or parse_vedas method")

    if not verses:
        logger.warning(f"No verses parsed from {pdf_path}. Attempting fallback simple lines parsing.")
        # Fallback segmentation by chunks of text
        verses = []
        full_text = "\n".join(p["text"] for p in pages)
        paragraphs = [p.strip() for p in full_text.split("\n\n") if len(p.strip()) > 30]
        for idx, para in enumerate(paragraphs):
            verses.append({
                "ved_code": scripture_type,
                "mandala_id": 1,
                "sukta_id": 0,
                "mantra_number": idx + 1,
                "text": para
            })

    if args.limit_verses:
        verses = verses[:args.limit_verses]

    logger.info(f"Segmented {len(verses)} verses. Extracting ontology in batches of {args.group_size}...")

    # Group verses into batches
    chunks = [verses[i:i + args.group_size] for i in range(0, len(verses), args.group_size)]

    # 3. LLM Orchestration with ThreadPool
    extracted_entities = []
    extracted_relationships = []
    seen_entity_names = set()

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(extract_batch_ontology, llm, chunk, scripture_name): idx
            for idx, chunk in enumerate(chunks)
        }

        for future in tqdm(as_completed(futures), total=len(chunks), desc=f"Extracting {scripture_name}"):
            res = future.result()
            
            # Normalize entities & resolve IDs
            for entity in res.get("entities", []):
                orig_name = entity.get("name")
                if not orig_name:
                    continue
                
                # Standardize name using clean_duplicate_names resolution layer
                normalized_name = clean_name(orig_name)
                entity["name"] = normalized_name
                
                norm_key = normalized_name.lower()
                if norm_key not in seen_entity_names:
                    extracted_entities.append(entity)
                    seen_entity_names.add(norm_key)

            # Standardize relationships
            for rel in res.get("relationships", []):
                source = rel.get("from") or rel.get("source")
                target = rel.get("to") or rel.get("target")
                rel_type = rel.get("type")

                if source and target and rel_type:
                    normalized_rel = {
                        "from": clean_name(source),
                        "to": clean_name(target),
                        "type": rel_type,
                        "attributes": rel.get("attributes", {}),
                    }
                    extracted_relationships.append(normalized_rel)

    return {
        "ontology": {
            "entity_types": [e.value for e in EntityType],
            "relationship_types": [r.value for r in RelationType],
        },
        "entities": extracted_entities,
        "relationships": extracted_relationships
    }


def deploy_ontology_to_neo4j(ontology_data: dict[str, Any]):
    """Insert the normalized ontology entities and relationships directly into Neo4j."""
    logger.info("Initializing Neo4j connector for direct deployment...")
    try:
        gb = GraphBuilder(
            uri=settings.NEO4J_URI,
            user=settings.NEO4J_USER,
            password=settings.NEO4J_PASSWORD
        )
    except Exception as e:
        logger.error(f"Failed to connect to Neo4j database: {e}")
        return

    # Ingest entities
    entities = ontology_data.get("entities", [])
    logger.info(f"Deploying {len(entities)} entities to Neo4j...")
    gb.create_entities_batch(entities)

    # Ingest relationships
    rels = ontology_data.get("relationships", [])
    logger.info(f"Deploying {len(rels)} relationships to Neo4j...")
    gb.create_relationships_batch(rels)

    gb.close()
    logger.info("Neo4j database deployment complete.")


def auto_detect_type(filename: str) -> str:
    """Guess scripture type based on PDF name."""
    fn = filename.lower()
    if "gita" in fn or "geeta" in fn:
        return "gita"
    elif "ramayana" in fn or "ramayan" in fn:
        return "ramayana"
    elif "mahabharat" in fn or "mahabharata" in fn:
        return "mahabharat"
    elif "puran" in fn:
        return "purana"
    elif "ved" in fn:
        return "veda"
    return "purana"  # Default fallback


def main():
    parser = argparse.ArgumentParser(description="Scaled vidwaanai PDF scripture ontology extraction pipeline.")
    parser.add_argument(
        "--pdf",
        type=str,
        help="Path to single PDF to process (scans target dir if empty)",
    )
    parser.add_argument(
        "--input-dir",
        type=str,
        default=DEFAULT_INPUT_DIR,
        help=f"Directory to scan for raw scripture PDFs (default: {DEFAULT_INPUT_DIR})",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory to save output JSON ontologies (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--type",
        type=str,
        help="Scripture parser type (gita, ramayana, mahabharat, purana, veda)",
    )
    parser.add_argument(
        "--limit-pages",
        type=int,
        help="Limit page extraction size per PDF (for development/testing)",
    )
    parser.add_argument(
        "--limit-verses",
        type=int,
        help="Limit verses size to run through LLM (for development/testing)",
    )
    parser.add_argument(
        "--group-size",
        type=int,
        default=10,
        help="Number of verses grouped per prompt batch (default: 10)",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=settings.GRAPH_BUILD_WORKERS,
        help=f"Parallel worker threads for LLM calls (default: {settings.GRAPH_BUILD_WORKERS})",
    )
    parser.add_argument(
        "--deploy",
        action="store_true",
        help="Directly deploy the extracted ontology to local Neo4j",
    )
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    os.makedirs(args.input_dir, exist_ok=True)

    llm = get_llm_client()

    pdf_files = []
    if args.pdf:
        if os.path.exists(args.pdf):
            pdf_files.append(args.pdf)
        else:
            logger.error(f"PDF not found: {args.pdf}")
            sys.exit(1)
    else:
        pdf_files = glob.glob(os.path.join(args.input_dir, "*.pdf"))

    if not pdf_files:
        logger.warning(f"No PDFs found to process in '{args.input_dir}'. Put PDFs in this folder or specify one with --pdf.")
        return

    logger.info(f"Found {len(pdf_files)} PDFs to process.")

    for pdf_path in pdf_files:
        scripture_type = args.type or auto_detect_type(os.path.basename(pdf_path))
        
        try:
            ontology_data = process_pdf(pdf_path, scripture_type, args, llm)
            
            # Export to JSON
            filename = os.path.basename(pdf_path)
            output_filename = os.path.splitext(filename)[0] + "_ontology.json"
            output_filepath = os.path.join(args.output_dir, output_filename)
            
            with open(output_filepath, "w", encoding="utf-8") as f:
                json.dump(ontology_data, f, indent=4, ensure_ascii=False)
            logger.info(f"✓ Saved extracted ontology cleanly to: {output_filepath}")

            # Deploy to Neo4j if requested
            if args.deploy:
                deploy_ontology_to_neo4j(ontology_data)

        except Exception as e:
            logger.error(f"Error processing {pdf_path}: {e}", exc_info=True)


if __name__ == "__main__":
    main()
