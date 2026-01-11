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
from src.graph.ontology import VEDIC_ONTOLOGY
from scripts.seed_ontology import OntologySeeder

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

    # Flatten ontology for lookup if passed (optimization: do this once outside, but passed here or do simplistic check)
    # Ideally passed as argument, but for minimal change let's do a quick lookup strategy or assume it's global
    # Let's use a helper if we could, but let's implement checking against VEDIC_ONTOLOGY directly or via a comprehensive flattening
    
    # 0. Ontology Matching (New Logic)
    # We want to check if any known concept from VEDIC_ONTOLOGY is mentioned in the text
    # A simple flattened map would be best. 
    # Let's assume a global 'ONTOLOGY_LOOKUP' is available or we build it here briefly (inefficient if per verse)
    # Better: Build it once in main and pass it, but changing signature requires updating call site.
    # Let's update call site in main to pass `ontology_lookup`.
    
    # Placeholder for signature update below
    pass
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

def flatten_ontology(ontology):
    """
    Flatten ontology into a lookup map: Lowercase Name -> {id, type, name}
    """
    lookup = {}
    
    def _traverse(obj):
        if isinstance(obj, dict):
            if "id" in obj and "name" in obj:
                entry = {
                    "id": obj["id"],
                    "type": obj.get("type", "Concept"),
                    "name": obj["name"]
                }
                # Add exact name match
                lookup[obj["name"].lower()] = entry
                
                # Add synoynms if any
                for syn in obj.get("synonyms", []):
                    lookup[syn.lower()] = entry
                    
                # Add sanskrit name if any
                if "sanskrit_name" in obj:
                    lookup[obj["sanskrit_name"].lower()] = entry
            
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    _traverse(v)
        elif isinstance(obj, list):
            for item in obj:
                _traverse(item)

    _traverse(ontology)
    return lookup

def extract_from_verse_with_ontology(
    verse,
    extractor: EntityExtractor,
    tax_extractor: TaxonomyExtractor,
    ontology_lookup: dict,
    skip_llm: bool = False,
):
    """
    Extraction with Ontology looking for creating MENTIONS relationships.
    """
    verse_id = verse["id"]
    text = verse.get("text", "") or ""
    translation = verse.get("translation", "") or ""
    scripture = verse.get("scripture_name", "Unknown")

    entities_accum = []
    rels_accum = []
    
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
    
    combined_text = (f"{text} {translation}").lower()

    # 0. Ontology Lookup (Deterministic linking)
    # Check if any ontology concept name is in the text
    found_ontology_concepts = []
    for term, concept_info in ontology_lookup.items():
        # Simple substring match - can be improved with regex word boundaries
        if term in combined_text:
            found_ontology_concepts.append(concept_info)
            
            # Create Relationship: Verse -> MENTIONS -> Concept
            # Note: We assume Concept node exists (seeded) or we create a stub reference.
            # GraphBuilder.create_relationships_batch needs identifiers. 
            # If we used create_entity_batch, we have names. 
            # If concept nodes are created with specific properties (like ID) in Neo4j, 
            # we need to ensure we link to them correctly.
            # GraphBuilder usually links by NAME and TYPE if using `create_relationship(from_node_name, to_node_name...)` approach
            # But `create_relationships_batch` takes raw dicts.
            
            rels_accum.append({
                "from": verse_node_name,
                "to": concept_info["name"],  # Linking by Name
                "type": "MENTIONS",
                "attributes": {
                    "source": "ontology_lookup", 
                    "matched_term": term,
                    "confidence": 1.0
                }
            })

    # 1. Taxonomy (Rule-based)
    found_entities = tax_extractor.extract(f"{text} {translation}")
    
    for entity in found_entities:
        # Check if this rule-based entity matches ontology
        ent_name_lower = entity["name"].lower()
        if ent_name_lower in ontology_lookup:
            # It's a known concept! Use the official name/type
            official = ontology_lookup[ent_name_lower]
            entity["name"] = official["name"]
            entity["type"] = official["type"]
        else:
             entity["type"] = "Concept" # Default

        entities_accum.append(
            {
                "name": entity["name"],
                "type": entity["type"],
                "attributes": {"source": "taxonomy"},
            }
        )

        # Rel: Entity -> MENTIONED_IN -> Verse (Inverted Logic in original code??)
        # Original: Entity -> MENTIONED_IN -> Verse
        # User Request: Text -> MENTIONS -> Concept
        # Let's add BOTH or prefer User Request. 
        # User request said: "Text Nodes ... [MENTIONS] -> Concept Nodes"
        
        rels_accum.append(
            {
                "from": verse_node_name,
                "to": entity["name"],
                "type": "MENTIONS",
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
                # Normalization against ontology
                if ent["name"].lower() in ontology_lookup:
                     official = ontology_lookup[ent["name"].lower()]
                     ent["name"] = official["name"]
                     ent["type"] = official["type"]

                ent["attributes"] = ent.get("attributes", {})
                ent["attributes"]["source_verse_id"] = verse_id
                ent["attributes"]["scripture"] = scripture
                entities_accum.append(ent)
                
                # Ensure we link this entity to the verse if not already explicit
                rels_accum.append({
                    "from": verse_node_name,
                    "to": ent["name"],
                    "type": "MENTIONS",
                    "attributes": {"source": "llm", "confidence": 0.9}
                })

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
        
        # Seed Ontology
        logger.info("Seeding Ontology...")
        seeder = OntologySeeder(graph_builder)
        seeder.seed()

    # Pre-compute flattened ontology for fast lookup
    ontology_lookup = flatten_ontology(VEDIC_ONTOLOGY)
    logger.info(f"Loaded {len(ontology_lookup)} ontology terms for fast lookup.")

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
                    extract_from_verse_with_ontology, v, extractor, tax_extractor, ontology_lookup, args.skip_llm
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
