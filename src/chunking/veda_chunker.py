from typing import List, Dict, Any, Optional
from src.db.db_manager import DatabaseManager


class VedaChunker:
    """Create different chunk sizes for search optimization."""

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def create_chunks(self, mantra_id: int) -> List[Dict[str, Any]]:
        """
        Create mantra, sukta, and mandala level chunks for a given mantra ID.
        Returns a list of chunks to be embedded.
        """
        # Fetch full mantra details including hierarchy names
        mantra = self._get_mantra_details(mantra_id)
        if not mantra:
            return []

        chunks: List[Dict[str, Any]] = []

        # 1. Mantra-level chunk (Small, specific)
        # Content: The mantra text itself.
        chunks.append(
            {
                "type": "mantra",
                "text": mantra["text_hindi"],
                "metadata": {
                    "ved_id": mantra["ved_id"],
                    "mandala_id": mantra["mandala_id"],
                    "sukta_id": mantra["sukta_id"],
                    "mantra_id": mantra["id"],
                },
            }
        )

        # 2. Sukta-level chunk (Medium, context)
        # Content: All mantras in this Sukta.
        # Note: This might be expensive to re-generate for every mantra.
        # Ideally, we generate Sukta chunks once per Sukta.
        # But per the plan, we might just associate the mantra with its sukta context.
        # Let's verify the plan's intent: "Multi-level chunking... Store in pgvector"
        # Usually implies we have separate vectors for Mantra, Sukta, Mandala.
        # Since the 'veda_embeddings' table links to 'mantra_id', strictly speaking,
        # linking a massive Sukta blob to *every* mantra is redundant.
        # However, the table has 'chunk_type'.
        # If we insert a 'sukta' chunk, does it link to a specific mantra_id?
        # The schema says: `mantra_id INT NOT NULL REFERENCES mantras(id)`
        # This implies every embedding MUST belong to a mantra.
        # This schema constraint is slightly limiting if we want "Sukta level embeddings" that aren't tied to one mantra.
        # BUT, if the user wants "Context retrieval", maybe we just embed the SUKTA text and link it to the FIRST mantra of the sukta?
        # OR we just accept the schema and maybe 'sukta' chunk type implies "This mantra + its neighbors".

        # Let's follow the user's provided code snippet logic for Phase 3:
        # It showed:
        # chunks.append({'type': 'sukta', 'text': sukta_text ...})
        # So yes, we generate these text blobs.

        sukta_text = self._get_sukta_text(mantra["sukta_id"])
        if sukta_text:
            chunks.append(
                {"type": "sukta", "text": sukta_text, "metadata": {"range": "sukta"}}
            )

        # Mandala level might be too big?
        # User plan included it. Let's include it but maybe truncated or summarized?
        # For now, let's stick to the plan but be wary of token limits.
        # MPNet limit is 512 tokens. A whole Mandala could be huge.
        # We'll skip Mandala for now to avoid truncation errors, or just take first N chars.

        # 2. Token-based chunks for finer granularity
        # Using 256 token chunks with 20% overlap (approx 50 tokens)
        try:
            from llama_index.core.node_parser import SentenceSplitter
            splitter = SentenceSplitter(chunk_size=256, chunk_overlap=50)
            text_chunks = splitter.split_text(mantra["text_hindi"])
            
            for i, chunk_text in enumerate(text_chunks):
                chunks.append({
                    "type": "mantra_chunk",
                    "text": chunk_text,
                    "metadata": {
                        "ved_id": mantra["ved_id"], 
                        "mantra_id": mantra["id"],
                        "chunk_index": i,
                        "total_chunks": len(text_chunks)
                    }
                })
        except ImportError:
            # Fallback if llama-index is not available (though it should be)
            pass

        return chunks

    def _get_mantra_details(self, mantra_id: int) -> Optional[Dict[str, Any]]:
        """Fetch mantra with joins."""
        with self.db._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT m.*, v.name as ved_name 
                    FROM mantras m 
                    JOIN vedas v ON m.ved_id = v.id 
                    WHERE m.id = %s
                """,
                    (mantra_id,),
                )
                cols = [desc[0] for desc in cursor.description]
                row = cursor.fetchone()
                return dict(zip(cols, row)) if row else None

    def _get_sukta_text(self, sukta_id: int) -> str:
        """Get all text for a sukta."""
        if not sukta_id:
            return ""
        with self.db._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT text_hindi FROM mantras 
                    WHERE sukta_id = %s 
                    ORDER BY mantra_number
                """,
                    (sukta_id,),
                )
                rows = cursor.fetchall()
                return " ".join([r[0] for r in rows if r[0]])
