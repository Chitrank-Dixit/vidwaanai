import logging
import sys
import os
import argparse
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Add src to python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.core.config import settings
from src.db.db_manager import DatabaseManager
from src.graph.graph_builder import GraphBuilder
from src.graph.entity_extractor import EntityExtractor
from src.graph.taxonomy_extractor import TaxonomyExtractor
from src.llm.lmstudio_client import LMStudioClient
from src.llm.openai_client import OpenAIClient

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("graph_build.log")],
)
logger = logging.getLogger(__name__)


def get_llm_client():
    """Initialize LLM client based on settings."""
    if settings.llm_backend == "lmstudio":
        logger.info(f"Using LM Studio backend: {settings.lmstudio_base_url}")
        return LMStudioClient(
            base_url=settings.lmstudio_base_url, model_name=settings.lmstudio_model
        )
    else:
        logger.info("Using OpenAI backend")
        return OpenAIClient(api_key=settings.OPENAI_API_KEY)


def extract_from_verse(
    verse,
    extractor: EntityExtractor,
    tax_extractor: TaxonomyExtractor,
    skip_llm: bool = False,
):
    """
    Pure extraction function (Read-only).
    Returns dict of entities and relationships to be merged later.
    """
    verse_id = verse["id"]
    text = verse.get("text", "") or ""
    translation = verse.get("translation", "") or ""
    scripture = verse.get("scripture_name", "Unknown")

    entities_accum = []
    rels_accum = []

    # 1. Taxonomy (Rule-based)
    combined_text = f"{text} {translation}"
    found_entities = tax_extractor.extract(combined_text)

    verse_node_name = f"Verse {verse_id}"

    # Verse Node (Implicit entity)
    entities_accum.append(
        {
            "name": verse_node_name,
            "type": "Text",
            "attributes": {
                "text": text,
                "translation": translation,
                "scripture": scripture,
                "verse_id": verse_id,
            },
        }
    )

    for entity in found_entities:
        # Entity from Taxonomy
        entities_accum.append(
            {
                "name": entity["name"],
                "type": "Concept",  # Taxonomy extractor doesn't always give type, assume Concept/Deity based on ontology lookup?
                # For now, let's trust GraphBuilder to default or Taxonomy to improve.
                # Actually TaxonomyExtractor usually returns dict with name/type if configured well.
                # But here 'found_entities' is list of dicts.
                "attributes": {"source": "taxonomy"},
            }
        )

        # Rel: Entity -> MENTIONED_IN -> Verse
        rels_accum.append(
            {
                "from": entity["name"],
                "to": verse_node_name,
                "type": "MENTIONED_IN",
                "attributes": {"context": "Rule-based extraction"},
            }
        )

    # 2. LLM Extraction
    if not skip_llm:
        try:
            data = extractor.extract_entities(text, translation, scripture)
            ext_entities = data.get("entities", [])
            ext_rels = data.get("relationships", [])

            for ent in ext_entities:
                ent["attributes"] = ent.get("attributes", {})
                ent["attributes"]["source_verse_id"] = verse_id
                ent["attributes"]["scripture"] = scripture
                entities_accum.append(ent)

            for rel in ext_rels:
                rel["attributes"] = rel.get("attributes", {})
                rel["attributes"]["source_verse_id"] = verse_id
                rels_accum.append(rel)

        except Exception as e:
            logger.error(f"LLM Extraction failed for verse {verse_id}: {e}")

    return entities_accum, rels_accum


def main():
    parser = argparse.ArgumentParser(
        description="Build Vedic Knowledge Graph Optimized"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Limit number of verses to process (0 for all)",
    )
    parser.add_argument("--offset", type=int, default=0, help="Offset for processing")
    parser.add_argument("--scripture", type=str, help="Filter by scripture name")
    parser.add_argument("--clear", action="store_true", help="Clear graph")
    parser.add_argument("--workers", type=int, default=10, help="Parallel workers")
    parser.add_argument(
        "--batch-size", type=int, default=50, help="DB Write batch size"
    )
    parser.add_argument(
        "--skip-llm", action="store_true", help="Skip LLM extraction (Taxonomy only)"
    )
    args = parser.parse_args()

    # Init Services
    logger.info("Initializing services...")
    db = DatabaseManager(settings.DATABASE_URL)

    # Only init LLM if needed
    llm = None
    extractor = None
    if not args.skip_llm:
        llm = get_llm_client()
        extractor = EntityExtractor(llm)

    tax_extractor = TaxonomyExtractor()

    try:
        graph_builder = GraphBuilder(
            uri=settings.NEO4J_URI,
            user=settings.NEO4J_USER,
            password=settings.NEO4J_PASSWORD,
        )
    except Exception as e:
        logger.error(f"Failed to connect to Neo4j: {e}")
        sys.exit(1)

    if args.clear:
        logger.warning("Clearing existing Knowledge Graph...")
        graph_builder.clear_graph()

    # Fetch Verses
    logger.info("Fetching verses from PostgreSQL...")
    all_verses = db.get_all_verses()

    if args.scripture:
        all_verses = [
            v
            for v in all_verses
            if args.scripture.lower() in v.get("scripture_name", "").lower()
        ]

    start = args.offset
    end = start + args.limit if args.limit > 0 else len(all_verses)
    verses_to_process = all_verses[start:end]

    logger.info(
        f"Processing {len(verses_to_process)} verses with {args.workers} workers. Skip LLM: {args.skip_llm}"
    )

    # Batch Processing Loop
    total_ent = 0
    total_rel = 0

    # Process in chunks of 'batch_size' * 'workers' (e.g. 500 at a time) to manage memory
    chunk_size = args.batch_size * 2  # Process reasonably sized chunks in memory

    start_time = time.time()

    for i in range(0, len(verses_to_process), chunk_size):
        chunk = verses_to_process[i : i + chunk_size]

        batch_entities = []
        batch_rels = []

        # Parallel Extraction
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            # Pass skip_llm
            futures = [
                executor.submit(
                    extract_from_verse, v, extractor, tax_extractor, args.skip_llm
                )
                for v in chunk
            ]

            for future in tqdm(
                as_completed(futures),
                total=len(chunk),
                desc=f"Extracting Batch {i//chunk_size + 1}",
                leave=False,
            ):
                ents, rels = future.result()
                batch_entities.extend(ents)
                batch_rels.extend(rels)

        # Batch Write
        if batch_entities:
            graph_builder.create_entities_batch(batch_entities)
            total_ent += len(batch_entities)

        if batch_rels:
            graph_builder.create_relationships_batch(batch_rels)
            total_rel += len(batch_rels)

        logger.info(
            f"Committed batch {i//chunk_size + 1}: {len(batch_entities)} ents, {len(batch_rels)} rels"
        )

    elapsed = time.time() - start_time
    logger.info(f"Graph Build Complete in {elapsed:.2f}s.")
    logger.info(f"Total Entities: {total_ent}")
    logger.info(f"Total Relationships: {total_rel}")

    graph_builder.close()


if __name__ == "__main__":
    main()
