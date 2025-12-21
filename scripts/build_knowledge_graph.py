import logging
import sys
import os
import argparse
from tqdm import tqdm

# Add src to python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.core.config import settings
from src.db.db_manager import DatabaseManager
from src.graph.graph_builder import GraphBuilder
from src.graph.entity_extractor import EntityExtractor
from src.llm.lmstudio_client import LMStudioClient
from src.llm.openai_client import OpenAIClient

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("graph_build.log")
    ]
)
logger = logging.getLogger(__name__)

def get_llm_client():
    """Initialize LLM client based on settings."""
    if settings.llm_backend == "lmstudio":
        logger.info(f"Using LM Studio backend: {settings.lmstudio_base_url}")
        return LMStudioClient(
            base_url=settings.lmstudio_base_url,
            model_name=settings.lmstudio_model
        )
    else:
        logger.info("Using OpenAI backend")
        return OpenAIClient(api_key=settings.OPENAI_API_KEY)

def process_verse(verse, extractor: EntityExtractor, builder: GraphBuilder):
    """Process a single verse: Extract -> Build Graph."""
    verse_id = verse['id']
    text = verse.get('text', '') or ''
    # Fallback to translation if text is non-english/complex and we need clearer entities?
    # Actually extraction usually works better on English translation for many models if the model isn't multilingual trained.
    # Let's pass both to extractor as originally designed.
    translation = verse.get('translation', '') or ''
    scripture = verse.get('scripture_name', 'Unknown')
    
    # Combine text context
    # extractor.extract_entities takes (verse_text, translation, scripture_name)
    
    try:
        data = extractor.extract_entities(text, translation, scripture)
    except Exception as e:
        logger.error(f"Extraction failed for verse {verse_id}: {e}")
        return 0, 0

    entities = data.get('entities', [])
    relationships = data.get('relationships', [])
    
    # Build Entities
    for ent in entities:
        try:
            name = ent.get('name')
            etype = ent.get('type')
            attrs = ent.get('attributes', {})
            # Add metadata source
            attrs['source_verse_id'] = verse_id
            attrs['scripture'] = scripture
            
            if name and etype:
                builder.create_entity(name, etype, attrs)
        except Exception as e:
            logger.error(f"Error creating entity {ent}: {e}")

    # Build Relationships
    for rel in relationships:
        try:
            src = rel.get('from')
            tgt = rel.get('to')
            rtype = rel.get('type')
            attrs = rel.get('attributes', {})
            attrs['source_verse_id'] = verse_id
            
            if src and tgt and rtype:
                builder.create_relationship(src, tgt, rtype, attrs)
        except Exception as e:
            logger.error(f"Error creating relationship {rel}: {e}")
            
    return len(entities), len(relationships)

def main():
    parser = argparse.ArgumentParser(description="Build Vedic Knowledge Graph")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of verses to process (0 for all)")
    parser.add_argument("--offset", type=int, default=0, help="Offset for processing")
    parser.add_argument("--scripture", type=str, help="Filter by scripture name")
    parser.add_argument("--clear", action="store_true", help="Clear graph before building")
    args = parser.parse_args()

    # Init Services
    logger.info("Initializing services...")
    db = DatabaseManager(settings.DATABASE_URL)
    llm = get_llm_client()
    extractor = EntityExtractor(llm)
    
    try:
        graph_builder = GraphBuilder(
            uri=settings.NEO4J_URI, 
            user=settings.NEO4J_USER, 
            password=settings.NEO4J_PASSWORD
        )
    except Exception as e:
        logger.error(f"Failed to connect to Neo4j: {e}")
        sys.exit(1)

    if args.clear:
        logger.warning("Clearing existing Knowledge Graph...")
        graph_builder.clear_graph()
        # Re-run setup to ensure constraints exist? 
        # existing setup_graph.py logic creates IS UNIQUE constraints which are persistent usually.
        # But clear_graph DETACH DELETE n removes nodes, constraints remain.
        
    # Fetch Verses
    logger.info("Fetching verses from PostgreSQL...")
    # We might need a more cursor-based approach for 35k verses if memory is tight, 
    # but get_all_verses fetches list dict. 35k * 1KB ~ 35MB. It's fine for Memory.
    all_verses = db.get_all_verses()
    
    if args.scripture:
        all_verses = [v for v in all_verses if args.scripture.lower() in v.get('scripture_name', '').lower()]
        
    # Slice
    start = args.offset
    end = start + args.limit if args.limit > 0 else len(all_verses)
    verses_to_process = all_verses[start:end]
    
    logger.info(f"Processing {len(verses_to_process)} verses (Total available: {len(all_verses)})")

    total_ent = 0
    total_rel = 0
    
    # Process Loop
    for verse in tqdm(verses_to_process, desc="Building Graph"):
        e_count, r_count = process_verse(verse, extractor, graph_builder)
        total_ent += e_count
        total_rel += r_count

    logger.info(f"Graph Build Complete.")
    logger.info(f"Total Entities Created/Merged: {total_ent}")
    logger.info(f"Total Relationships Created/Merged: {total_rel}")
    
    graph_builder.close()

if __name__ == "__main__":
    main()
