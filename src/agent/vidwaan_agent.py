"""Main VidwaanAI Agent."""

import logging
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from neo4j import GraphDatabase

from src.agent.prompt_templates import SCRIPTURE_PROMPT
from src.agent.query_router import QueryRouter
from src.cache.query_cache import QueryCache
from src.core.monitoring import record_retrieval_quality, track_query_latency
from src.db.db_manager import DatabaseManager
from src.graph.entity_extractor import EntityExtractor
from src.graph.graph_retriever import GraphRetriever
from src.graph.hybrid_search import HybridSearch as GraphHybridSearch
from src.llm.lmstudio_client import LMStudioClient
from src.llm.openai_client import OpenAIClient
from src.rag.embeddings import EmbeddingManager
from src.rag.multilingual_search import MultilingualSearch
from src.retrieval.advanced_retrieval_pipeline import AdvancedRetrievalPipeline
from src.retrieval.bm25_search import BM25Search
from src.retrieval.hybrid_search import HybridSearch
from src.retrieval.veda_retriever import VedaRetriever
from src.utils.confidence import calculate_confidence_score

logger = logging.getLogger(__name__)


class VidwaanAI:
    """Main VidwaanAI Agent class."""

    def __init__(
        self,
        db_url: str,
        openai_key: str,
        krutrim_key: Optional[str] = None,
        use_lmstudio: bool = True,
        lmstudio_url: Optional[str] = None,
        enable_graph_rag: bool = False,
        neo4j_uri: Optional[str] = None,
        neo4j_user: Optional[str] = None,
        neo4j_password: Optional[str] = None,
        llm_timeout: int = 120,
    ):
        """Initialize VidwaanAI agent."""
        self.db = DatabaseManager(db_url)
        self.embeddings = EmbeddingManager()
        # Use MultilingualSearch for embeddings and language processing
        self.multilingual_search = MultilingualSearch()
        # Keep EmbeddingManager for legacy support if needed, but MultilingualSearch handles embedding now
        # self.embeddings = EmbeddingManager()

        self.llm: Union[LMStudioClient, OpenAIClient]
        if use_lmstudio:
            self.llm = LMStudioClient(
                base_url=lmstudio_url or "http://localhost:8000", timeout=llm_timeout
            )
        else:
            self.llm = OpenAIClient(api_key=openai_key)
        self.router = QueryRouter()
        self.cache = QueryCache()
        self.retrieval_pipeline: Optional[AdvancedRetrievalPipeline] = None
        self.hybrid_retriever: Optional[HybridSearch] = None

        # Hybrid Search (BM25 + Vector)
        try:
            verses = self.db.get_all_verses()
            self.bm25_search = BM25Search(verses)

            def vector_search_func(query: str, top_k: int) -> List[Dict[str, Any]]:
                # Use multilingual embedding
                query_data = self.multilingual_search.process_query(query)
                emb = query_data["embedding"]
                results = self.db.retrieve_verses(emb, top_k=top_k)
                for r in results:
                    r["score"] = r.get("similarity", 0.0)
                return results

            self.hybrid_retriever = HybridSearch(
                bm25_search=self.bm25_search, vector_search_func=vector_search_func
            )

            # Initialize Advanced Pipeline
            self.retrieval_pipeline = AdvancedRetrievalPipeline(self.hybrid_retriever)
            logger.info("Advanced Retrieval Pipeline initialized")

        except Exception as e:
            logger.error(f"Failed to initialize Retrieval Pipeline: {e}")
            self.retrieval_pipeline = None
            self.hybrid_retriever = None

        # Veda Retrieval Setup
        self.veda_retriever: Optional[VedaRetriever] = None
        try:
            self.veda_retriever = VedaRetriever(self.db)
            logger.info("Veda Retriever initialized")
        except Exception as e:
            logger.error(f"Failed to initialize Veda Retriever: {e}")

        # Graph RAG setup
        self.enable_graph_rag = enable_graph_rag
        if enable_graph_rag and neo4j_uri and neo4j_user and neo4j_password:
            try:
                self.neo4j_driver = GraphDatabase.driver(
                    neo4j_uri, auth=(neo4j_user, neo4j_password)
                )
                self.graph_retriever = GraphRetriever(self.neo4j_driver)
                self.entity_extractor = EntityExtractor(self.llm)
                self.graph_search = GraphHybridSearch(
                    self.graph_retriever,
                    self.db,
                    self.multilingual_search.embeddings,
                    self.entity_extractor,
                )
                logger.info("Graph RAG enabled and initialized")
            except Exception as e:
                logger.error(f"Failed to initialize Graph RAG: {e}")
                self.enable_graph_rag = False

        logger.info("VidwaanAI agent initialized")

    @track_query_latency
    def query(
        self,
        question: str,
        language: str = "en",
        scripture_filter: Optional[str] = None,
        verbose: bool = False,
    ) -> Dict[str, Any]:
        """Process a user query and return response."""

        try:
            # Step 1: Detect language and process query
            query_data = self.multilingual_search.process_query(question)
            detected_lang = query_data["language_code"]
            query_embedding = query_data["embedding"]

            logger.info(f"Query language: {detected_lang}")

            # Check Cache
            cached_result = self.cache.get(question, detected_lang, scripture_filter)
            if cached_result:
                return cached_result

            # Step 3: Retrieve relevant verses
            # Step 3: Retrieve relevant verses
            if self.retrieval_pipeline:
                # Use Advanced Pipeline
                retrieved_verses = self.retrieval_pipeline.retrieve(question, top_k=5)
            elif self.hybrid_retriever:
                # Fallback to Hybrid
                retrieved_verses = self.hybrid_retriever.search(question, top_k=5)
            else:
                # Fallback to vector only
                retrieved_verses = self.db.retrieve_verses(
                    query_embedding=query_embedding,
                    scripture_filter=scripture_filter,
                    top_k=5,
                )

            # Step 3.5: Retrieve from Vedas (if enabled/available)
            if self.veda_retriever:
                try:
                    veda_results = self.veda_retriever.search(question, top_k=3)
                    # Merge results (simple append for now, or interleave based on score)
                    # Normalize structure to match 'verses' dict
                    formatted_veda = []
                    for v in veda_results:
                        formatted_veda.append(
                            {
                                "scripture": v["source"],  # e.g. "Rig Ved Mandala 1..."
                                "chapter": v.get(
                                    "mantra_num"
                                ),  # Mapping mantra num to chapter for display? Or keep distinct
                                "verse": str(v.get("mantra_num")),
                                "text": v["text"],
                                "translation": v["translation"],
                                "similarity": v["score"],
                            }
                        )
                    retrieved_verses.extend(formatted_veda)
                    # Sort by score
                    retrieved_verses.sort(
                        key=lambda x: x.get("similarity", 0), reverse=True
                    )
                    retrieved_verses = retrieved_verses[:10]  # Keep top 10 total

                except Exception as e:
                    logger.error(f"Veda retrieval failed: {e}")

            graph_context = ""
            if self.enable_graph_rag:
                try:
                    # 1. Extract entities from the user query
                    query_entities = self.entity_extractor.extract_from_query(question)
                    entity_names = [e["name"] for e in query_entities if "name" in e]

                    if entity_names:
                        logger.info(f"Graph RAG: Extracted entities: {entity_names}")

                        # 2. Retrieve subgraph from Neo4j
                        subgraph = self.graph_retriever.get_context_subgraph(
                            entity_names
                        )

                        # 3. Format context string
                        if subgraph:
                            graph_lines = ["**Knowledge Graph Context:**"]
                            for rel in subgraph:
                                # Format: "Krishna (Person) --[TEACHES]--> Arjuna (Person)"
                                line = f"{rel['source']} ({rel.get('source_type',['Entity'])[0]}) --[{rel['relation']}]--> {rel['target']} ({rel.get('target_type',['Entity'])[0]})"
                                graph_lines.append(line)
                            graph_context = "\n".join(graph_lines)
                            logger.info(
                                f"Graph RAG: Retrieved {len(subgraph)} relationships"
                            )
                        else:
                            logger.info(
                                "Graph RAG: No relationships found for entities"
                            )
                    else:
                        logger.info("Graph RAG: No entities found in query")

                except Exception as e:
                    logger.error(f"Graph search failed: {e}")

            if verbose:
                logger.info(f"Retrieved {len(retrieved_verses)} verses")

            # Monitoring: Record retrieval quality
            if retrieved_verses:
                scores = [v.get("similarity", 0.0) for v in retrieved_verses]
                # If reranked, use rerank_score if available, but similarity is what we have from vector DB
                # Rerank score is different scale. Let's stick to vector similarity for now as a proxy for raw retrieval quality
                record_retrieval_quality(scores)

            # Step 4: Format context for LLM
            context = self._format_context(retrieved_verses, detected_lang)
            if self.enable_graph_rag and graph_context:
                context = graph_context + "\n\n" + context

            # Step 5: Generate response
            prompt = SCRIPTURE_PROMPT.format(
                question=question, context=context, language=detected_lang
            )

            response_text = self.llm.generate(
                prompt=prompt, max_tokens=500, temperature=0.3
            )

            # Step 6: Calculate Confidence
            confidence_result = calculate_confidence_score(
                question_embedding=query_embedding,
                retrieved_verses=retrieved_verses,
                generated_answer=response_text,
            )

            # Apply Low Confidence Handling
            final_answer = response_text
            if confidence_result["score"] < 30:
                final_answer = (
                    "⚠️ **Insufficient Information**\n\n"
                    "I cannot confidently answer this question based on the available scriptures. "
                    "The retrieved verses do not appear to be directly relevant.\n\n"
                    "**Suggestion:** Try rephrasing your question or asking about a different topic.\n\n"
                    f"*(Original generated answer for reference: {response_text})*"
                )
            elif confidence_result["warning"]:
                final_answer = (
                    f"⚠️ **{confidence_result['warning']}**\n\n{response_text}"
                )

            # Step 7: Log query
            self._log_query(
                question=question,
                response=final_answer,
                language=detected_lang,
                retrieved_count=len(retrieved_verses),
            )

            result = {
                "answer": final_answer,
                "retrieved_verses": retrieved_verses,
                "language": detected_lang,
                "confidence": confidence_result,  # detailed dict
                "timestamp": datetime.now().isoformat(),
            }

            # Store in cache
            self.cache.set(question, detected_lang, result, scripture_filter)

            return result

        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            raise

    def get_loaded_scriptures(self) -> List[Dict[str, Any]]:
        """Get list of loaded scriptures."""
        return self.db.get_scriptures()

    def _format_context(self, verses: List[Dict[str, Any]], language: str) -> str:
        """Format retrieved verses as context."""
        if not verses:
            return "No relevant verses found."

        context_parts = []
        for verse in verses:
            ref = f"{verse.get('scripture', 'Unknown')} {verse.get('chapter', '')}:{verse.get('verse', '')}"
            text = verse.get("translation", verse.get("text", ""))
            context_parts.append(f"[{ref}] {text}")

        return "\n\n".join(context_parts)

    def _calculate_confidence(self, verses: List[Dict[str, Any]]) -> str:
        """Calculate confidence score."""
        if not verses:
            return "0%"

        avg_similarity = sum(v.get("similarity", 0.8) for v in verses) / len(verses)
        score = int(min(avg_similarity * 100, 100))
        return f"{score}%"

    def _log_query(
        self, question: str, response: str, language: str, retrieved_count: int
    ) -> None:
        """Log user query to database."""
        try:
            self.db.log_query(
                query_text=question,
                response_text=response,
                language=language,
                retrieved_count=retrieved_count,
                timestamp=datetime.now(),
            )
        except Exception as e:
            logger.error(f"Error logging query: {str(e)}")

    def close(self) -> None:
        """Close resources."""
        if hasattr(self, "neo4j_driver") and self.neo4j_driver:
            self.neo4j_driver.close()
            logger.info("Neo4j driver closed")
