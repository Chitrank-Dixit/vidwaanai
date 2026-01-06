
import logging
from typing import List, Dict, Any, Optional
import time

from src.db.db_manager import DatabaseManager
from src.graph.graph_builder import GraphBuilder
from src.graph.entity_extractor import EntityExtractor

logger = logging.getLogger(__name__)

class GraphIngestor:
    """
    Orchestrates the ingestion of mantras into the Knowledge Graph.
    Iterates through mantras in Postgres, extracts entities, and populates Neo4j.
    """

    def __init__(
        self,
        db_manager: DatabaseManager,
        graph_builder: GraphBuilder,
        entity_extractor: EntityExtractor
    ):
        self.db = db_manager
        self.graph = graph_builder
        self.extractor = entity_extractor

    def process_mantra(self, mantra_id: int, text: str, translation: str, source: str) -> Dict[str, int]:
        """
        Process a single mantra: extract entities and push to graph.
        Returns stats about extracted items.
        """
        # 1. Extract Entities & Relations
        # We use the hybrid extraction (SpaCy + LLM)
        extraction_result = self.extractor.extract_entities(
            verse_text=text,
            translation=translation,
            scripture_name=source
        )
        
        entities = extraction_result.get("entities", [])
        relationships = extraction_result.get("relationships", [])
        
        # 2. Add Mantra Node itself
        mantra_node_id = self.graph.create_entity(
            name=f"Mantra {mantra_id}",
            entity_type="Concept", # Or a specific 'Mantra' type if schema supports
            attributes={
                "text": text,
                "translation": translation,
                "source": source,
                "type": "Mantra"
            }
        )
        
        # 3. Create Entity Nodes
        self.graph.create_entities_batch(entities)
        
        # 4. Create Relationships (Entity -> Entity)
        self.graph.create_relationships_batch(relationships)
        
        # 5. Link Mantra to extracted entities (MENTIONS)
        # This is important for "Which mantra mentions Agni?"
        mantra_links = []
        for ent in entities:
            mantra_links.append({
                "from": f"Mantra {mantra_id}",
                "to": ent["name"],
                "type": "RELATED_TO", # or MENTIONS
                "attributes": {"confidence": 1.0}
            })
        self.graph.create_relationships_batch(mantra_links)
        
        return {
            "entities": len(entities),
            "relationships": len(relationships) + len(mantra_links)
        }

    def ingest_all_mantras(self, batch_size: int = 10, limit: Optional[int] = None) -> Dict[str, int]:
        """
        Ingest all mantras from the database.
        """
        start_time = time.time()
        stats = {"processed": 0, "entities": 0, "relationships": 0, "errors": 0}
        
        offset = 0
        while True:
            # Fetch batch from Postgres
            # Assuming db_manager has a way to fetch mantras or we use raw query
            # We need a method fetch_mantras(limit, offset)
            rows = self._fetch_mantras(limit=batch_size, offset=offset)
            
            if not rows:
                break
                
            for row in rows:
                # row: id, text, translation, source_name
                try:
                    res = self.process_mantra(
                        mantra_id=row["id"],
                        text=row["text"],
                        translation=row["translation"] or "",
                        source=row["source"]
                    )
                    stats["processed"] += 1
                    stats["entities"] += res["entities"]
                    stats["relationships"] += res["relationships"]
                    
                    if limit and stats["processed"] >= limit:
                        logger.info(f"Hit limit of {limit} mantras.")
                        return stats
                        
                except Exception as e:
                    logger.error(f"Error processing mantra {row['id']}: {e}")
                    stats["errors"] += 1
            
            offset += batch_size
            logger.info(f"Processed {stats['processed']} mantras...")
            
        duration = time.time() - start_time
        logger.info(f"Ingestion complete in {duration:.2f}s. Stats: {stats}")
        return stats

    def _fetch_mantras(self, limit: int, offset: int) -> List[Dict[str, Any]]:
        """
        Helper to fetch mantras from DB.
        """
        query = """
            SELECT m.id, m.text_sanskrit as text, m.translation_en as translation, v.name as source
            FROM mantras m
            JOIN vedas v ON m.ved_id = v.id
            ORDER BY m.id
            LIMIT %s OFFSET %s
        """
        results = []
        with self.db._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (limit, offset))
                columns = [desc[0] for desc in cursor.description]
                for row in cursor.fetchall():
                    results.append(dict(zip(columns, row)))
        return results
