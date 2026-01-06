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
from src.graph.graph_retriever import GraphRetriever
from src.retrieval.hybrid_retriever_service import HybridRetrieverService

# You may need a GraphQuerier or similar class for reading graph data efficiently
# For now we will use raw GraphBuilder driver or a new class if needed.
# Let's assume we can query graph using the driver in GraphBuilder or ad-hoc.

logger = logging.getLogger(__name__)


class AgentService:
    """
    Core service for the Vidwaan Agent.
    Orchestrates the RAG pipeline: Query -> Vector DB -> Graph DB -> LLM -> Answer.
    """

    def __init__(self) -> None:
        self.db = DatabaseManager(settings.DATABASE_URL)
        self.embedder = VedaEmbedder()
        
        # Initialize Hybrid Retriever
        self.retriever = HybridRetrieverService(
            db_manager=self.db, 
            embedder=self.embedder,
            enable_bm25=True # Enable for hybrid support
        )

        # Initialize LLM
        if settings.llm_backend == "lmstudio":
            self.llm_client: Any = LMStudioClient(
                base_url=settings.lmstudio_base_url, model_name=settings.lmstudio_model
            )
        else:
            api_key = settings.OPENAI_API_KEY
            if not api_key:
                raise ValueError("OPENAI_API_KEY is not set")
            self.llm_client = OpenAIClient(api_key=api_key)

        # Initialize Graph connection (using GraphBuilder for now for connection management)
        # Ideally we separate Builder (Write) from Querier (Read), but for MVP we use driver directly.
        self.graph_builder = GraphBuilder(
            uri=settings.NEO4J_URI,
            user=settings.NEO4J_USER,
            password=settings.NEO4J_PASSWORD,
        )
        self.graph_retriever = GraphRetriever(self.graph_builder.driver)
        
        # We can extract entities from question too
        self.entity_extractor = EntityExtractor(self.llm_client)

        self.system_prompt = """
        You are Vidwaan, an expert Vedic AI assistant.
        Answer the user's question based ONLY on the following knowledge graph and retrieval context.
        Be concise and cite sources if possible.
        """

    def process_query(
        self, question: str, session_id: Optional[str] = None
    ) -> Dict[str, Any]:
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

        # 2. Hybrid Retrieval (Vector + BM25)
        v_time = time.time()
        
        # Use new Hybrid Retriever
        # We can expose fusion method in settings later
        similar_docs = self.retriever.search(
            query=question, 
            top_k=settings.RETRIEVAL_TOP_K,
            strategy="hybrid",
            fusion_method="weighted" # or 'rrf'
        )

        reasoning_trace.append(
            {
                "step": 2,
                "action": "hybrid_search",
                "input": "query",
                "output": f"Found {len(similar_docs)} relevant docs",
                "duration_ms": (time.time() - v_time) * 1000,
            }
        )

        # 3. Graph Search (Optional/Hybrid)
        # Extract entities from question to find relevant graph nodes
        graph_context_str = ""
        g_time = time.time()
        
        try:
            # Extract entities from query using the hybrid extractor
            query_entities = self.entity_extractor.extract_from_query(question)
            entity_names = [e["name"] for e in query_entities if "name" in e]
            
            if entity_names:
                # Get 1-hop subgraph
                subgraph = self.graph_retriever.get_context_subgraph(entity_names)
                graph_context_str = self.graph_retriever.format_subgraph_context(subgraph)
                
            reasoning_trace.append(
                {
                    "step": 3,
                    "action": "graph_retrieval",
                    "input": f"Entities: {entity_names}",
                    "output": f"Relations: {len(graph_context_str.splitlines())}",
                    "duration_ms": (time.time() - g_time) * 1000,
                }
            )
        except Exception as e:
             logger.error(f"Graph retrieval failed: {e}")
             # Non-blocking

        # 4. Build Context
        context_snippets = []
        for d in similar_docs:
            source = d.get('title', d.get('source', 'Unknown'))
            content = d.get('content')
            if not content:
                # Fallback for HybridRetriever output which uses text/translation
                text = d.get('text', '')
                trans = d.get('translation', '')
                content = f"{text}\nTranslation: {trans}" if trans else text
            
            context_snippets.append(f"Source ({source}): {content}")

        context_str = "\n\n".join(context_snippets)
        
        if graph_context_str:
            context_str += f"\n\nKnowledge Graph Context:\n{graph_context_str}"

        # 5. LLM Answer
        llm_time = time.time()
        answer = self.llm_client.generate(self.system_prompt, context_str, question)
        
        reasoning_trace.append(
            {
                "step": 5,
                "action": "llm_generation",
                "input": "Prompt + Context",
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
                    "id": str(d.get("id")),
                    "title": d.get("source", "Unknown Source"),
                    "content": f"{d.get('text', '')}\n{d.get('translation', '')}",
                    "confidence": d.get("score"),
                    "entity_type": "text",
                    "retrieval_method": d.get("fusion_method", "hybrid")
                }
                for d in similar_docs
            ],
            "reasoning_trace": reasoning_trace,
            "session_id": session_id or "default",
            "timestamp": time.time(),  # API expects datetime, will convert in Pydantic
            "processing_time_ms": processing_time,
        }

    def _search_vector_db(
        self, embedding: List[float], top_k: int = 5
    ) -> List[Dict[str, Any]]:
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
