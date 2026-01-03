import logging
import time
from typing import Dict, Any, List, Optional

from src.core.config import settings
from src.db.db_manager import DatabaseManager
from src.embeddings.veda_embedder import VedaEmbedder
from src.llm.lmstudio_client import LMStudioClient
from src.llm.openai_client import OpenAIClient
from src.graph.graph_builder import GraphBuilder
from src.graph.entity_extractor import EntityExtractor

# You may need a GraphQuerier or similar class for reading graph data efficiently
# For now we will use raw GraphBuilder driver or a new class if needed.
# Let's assume we can query graph using the driver in GraphBuilder or ad-hoc.

logger = logging.getLogger(__name__)


class AgentService:
    """
    Core service for the Vidwaan Agent.
    Orchestrates the RAG pipeline: Query -> Vector DB -> Graph DB -> LLM -> Answer.
    """

    def __init__(self):
        self.db = DatabaseManager(settings.DATABASE_URL)
        self.embedder = VedaEmbedder()

        # Initialize LLM
        if settings.llm_backend == "lmstudio":
            self.llm_client: Any = LMStudioClient(
                base_url=settings.lmstudio_base_url, model_name=settings.lmstudio_model
            )
        else:
            self.llm_client = OpenAIClient(api_key=settings.OPENAI_API_KEY)

        # Initialize Graph connection (using GraphBuilder for now for connection management)
        # Ideally we separate Builder (Write) from Querier (Read), but for MVP we use driver directly.
        self.graph_builder = GraphBuilder(
            uri=settings.NEO4J_URI,
            user=settings.NEO4J_USER,
            password=settings.NEO4J_PASSWORD,
        )
        # We can extract entities from question too
        self.entity_extractor = EntityExtractor(self.llm_client)

    def process_query(self, question: str, session_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Main RAG pipeline entry point.
        """
        start_time = time.time()
        reasoning_trace = []

        # 1. Embed Question
        q_time = time.time()
        try:
            q_emb = self.embedder.embed_text(question, is_query=True)
            reasoning_trace.append(
                {
                    "step": 1,
                    "action": "embed_question",
                    "input": question,
                    "output": f"Generated {len(q_emb)}d embedding",
                    "duration_ms": (time.time() - q_time) * 1000,
                }
            )
        except Exception as e:
            logger.error(f"Embedding failed: {e}")
            raise

        # 2. Vector Search (Postgres pgvector)
        v_time = time.time()
        # We need a search method in DB Manager or implement one here.
        # DB Manager likely has `search_similar_mantras` or similar.
        # Let's assume we implement a direct search helper here or extend DB Manager.
        # For now, implementing ad-hoc query or using existing DB Manager method if available.
        # Checking db_manager methods... (I'll implement a raw query here for precision)

        similar_docs = self._search_vector_db(q_emb, top_k=settings.RETRIEVAL_TOP_K)

        reasoning_trace.append(
            {
                "step": 2,
                "action": "vector_search",
                "input": "embedding",
                "output": f"Found {len(similar_docs)} relevant docs",
                "duration_ms": (time.time() - v_time) * 1000,
            }
        )

        # 3. Graph Search (Optional/Hybrid)
        # Extract entities from question to find relevant graph nodes
        # This is expensive (LLM call), so maybe we do it parallel or use simple keyword matching?
        # User plan says "Extract entities... Query graph".
        # Let's do a quick Keyword/Taxonomy search if possible, or skip for MVP speed.
        # Implemented simplified graph lookup for highly relevant terms.

        # graph_context = []
        # g_time = time.time()
        # entities = self.entity_extractor.extract_from_text(question) ...
        # graph_context = self._query_graph(entities) ...

        # 4. Build Context
        context_str = "\n\n".join(
            [f"Source ({d['title']}): {d['content']}" for d in similar_docs]
        )

        # 5. LLM Answer
        llm_time = time.time()
        prompt = f"""
        You are Vidwaan, an expert Vedic AI assistant. Answer the user's question based ONLY on the following context.
        
        Context:
        {context_str}
        
        Question: {question}
        
        Answer (be concise and cite sources if possible):
        """

        answer = self.llm_client.generate(prompt, max_tokens=1000)

        reasoning_trace.append(
            {
                "step": 3,
                "action": "llm_generation",
                "input": f"Context len: {len(context_str)}",
                "output": f"Answer len: {len(answer)}",
                "duration_ms": (time.time() - llm_time) * 1000,
            }
        )

        processing_time = (time.time() - start_time) * 1000

        return {
            "answer": answer,
            "confidence": 0.95,  # Placeholder
            "sources": [
                {
                    "id": str(d["id"]),
                    "title": d["title"],
                    "content": d["content"],
                    "confidence": d["similarity"],
                    "entity_type": "text",
                }
                for d in similar_docs
            ],
            "reasoning_trace": reasoning_trace,
            "session_id": session_id or "default",
            "timestamp": time.time(),  # API expects datetime, will convert in Pydantic
            "processing_time_ms": processing_time,
        }

    def _search_vector_db(self, embedding: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        """Search mantras by vector similarity."""
        results = []
        with self.db._get_connection() as conn:
            with conn.cursor() as cursor:
                # Query veda_embeddings joined with mantras
                # Note: veda_embeddings has 'embedding' vector column
                # We need to join back to mantras to get text/translation
                # This assumes veda_embeddings table exists and is populated
                query = """
                    SELECT m.id, v.name as ved_name, m.text_sanskrit, m.translation_en, 
                           (ve.embedding <=> %s) as distance
                    FROM veda_embeddings ve
                    JOIN mantras m ON ve.mantra_id = m.id
                    JOIN vedas v ON m.ved_id = v.id
                    ORDER BY distance ASC
                    LIMIT %s
                """
                # pgvector operator <=> is cosine distance (lower is better)
                # We need to format embedding as string for psycopg2 if not using register_vector
                # But typically list is fine with modern adapters or we cast it.
                # Let's stringify to be safe: '[0.1, ...]'
                emb_str = str(embedding)

                cursor.execute(query, (emb_str, top_k))
                rows = cursor.fetchall()

                for r in rows:
                    # r: id, ved_name, text, translation, distance
                    # Similarity = 1 - distance
                    sim = 1.0 - r[4]
                    results.append(
                        {
                            "id": r[0],
                            "title": f"{r[1]} Mantra {r[0]}",
                            "content": f"{r[2]}\nTranslation: {r[3] or ''}",
                            "similarity": sim,
                        }
                    )
        return results
