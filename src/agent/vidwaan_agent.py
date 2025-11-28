"""Main VidwaanAI Agent."""

from typing import Dict, List, Optional
from datetime import datetime
import logging

from src.rag.embeddings import EmbeddingManager
from src.db.db_manager import DatabaseManager
from src.agent.query_router import QueryRouter
from src.agent.prompt_templates import SCRIPTURE_PROMPT
from src.llm.openai_client import OpenAIClient
from src.llm.lmstudio_client import LMStudioClient
from src.graph.graph_retriever import GraphRetriever
from src.graph.hybrid_search import HybridSearcher
from src.graph.entity_extractor import EntityExtractor
from src.rag.reranker import Reranker
from src.core.monitoring import track_query_latency, record_retrieval_quality
from src.utils.confidence import calculate_confidence_score
from neo4j import GraphDatabase

logger = logging.getLogger(__name__)

class VidwaanAI:
    """Main VidwaanAI Agent class."""

    def __init__(
        self,
        db_url: str,
        openai_key: str,
        krutrim_key: Optional[str] = None,
        use_lmstudio=True, lmstudio_url=None,
        enable_graph_rag=False, neo4j_uri=None, neo4j_user=None, neo4j_password=None
    ):
        """Initialize VidwaanAI agent."""
        self.db = DatabaseManager(db_url)
        self.embeddings = EmbeddingManager()
        if use_lmstudio:
            self.llm = LMStudioClient(base_url=lmstudio_url or "http://localhost:8000")
        else:
            self.llm = OpenAIClient(api_key=openai_key)
        self.router = QueryRouter()
        
        # Optimization: Reranker
        try:
            self.reranker = Reranker()
        except Exception as e:
            logger.warning(f"Failed to initialize reranker: {e}. Proceeding without reranking.")
            self.reranker = None
        
        # Graph RAG setup
        self.enable_graph_rag = enable_graph_rag
        if enable_graph_rag and neo4j_uri:
            try:
                self.neo4j_driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))
                self.graph_retriever = GraphRetriever(self.neo4j_driver)
                self.entity_extractor = EntityExtractor(self.llm)
                self.hybrid_search = HybridSearcher(
                    self.graph_retriever, self.db, self.embeddings, self.entity_extractor
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
        verbose: bool = False
    ) -> Dict:
        """Process a user query and return response."""

        try:
            # Step 1: Detect language
            detected_lang = self.router.detect_language(question) or language
            logger.info(f"Query language: {detected_lang}")

            # Step 2: Generate embedding for query
            query_embedding = self.embeddings.embed_text(question)

            # Step 3: Retrieve relevant verses
            if self.enable_graph_rag:
                search_results = self.hybrid_search.search(question, top_k=5)
                retrieved_verses = search_results['vector_results']
                # We might want to use fused_context directly, but _format_context expects verses
                # Let's adjust _format_context or pass fused_context
                # For now, let's keep retrieved_verses for compatibility and append graph context
                graph_context = search_results.get('fused_context', '')
            else:
                retrieved_verses = self.db.retrieve_verses(
                    query_embedding=query_embedding,
                    scripture_filter=scripture_filter,
                    top_k=5
                )
                graph_context = ""

            if verbose:
                logger.info(f"Retrieved {len(retrieved_verses)} verses")

            # Optimization: Reranking
            if self.reranker and retrieved_verses:
                logger.info("Reranking retrieved verses...")
                retrieved_verses = self.reranker.rerank(question, retrieved_verses, top_k=5)
            
            # Monitoring: Record retrieval quality
            if retrieved_verses:
                scores = [v.get('similarity', 0.0) for v in retrieved_verses]
                # If reranked, use rerank_score if available, but similarity is what we have from vector DB
                # Rerank score is different scale. Let's stick to vector similarity for now as a proxy for raw retrieval quality
                record_retrieval_quality(scores)

            # Step 4: Format context for LLM
            context = self._format_context(retrieved_verses, detected_lang)
            if self.enable_graph_rag and graph_context:
                context = graph_context + "\n\n" + context

            # Step 5: Generate response
            prompt = SCRIPTURE_PROMPT.format(
                question=question,
                context=context,
                language=detected_lang
            )

            response_text = self.llm.generate(
                prompt=prompt,
                max_tokens=500,
                temperature=0.3
            )

            # Step 6: Calculate Confidence
            confidence_result = calculate_confidence_score(
                question_embedding=query_embedding,
                retrieved_verses=retrieved_verses,
                generated_answer=response_text
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
                final_answer = f"⚠️ **{confidence_result['warning']}**\n\n{response_text}"

            # Step 7: Log query
            self._log_query(
                question=question,
                response=final_answer,
                language=detected_lang,
                retrieved_count=len(retrieved_verses)
            )

            return {
                "answer": final_answer,
                "retrieved_verses": retrieved_verses,
                "language": detected_lang,
                "confidence": confidence_result, # detailed dict
                "timestamp": datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            raise

    def get_loaded_scriptures(self) -> List[Dict]:
        """Get list of loaded scriptures."""
        return self.db.get_scriptures()

    def _format_context(self, verses: List[Dict], language: str) -> str:
        """Format retrieved verses as context."""
        if not verses:
            return "No relevant verses found."

        context_parts = []
        for verse in verses:
            ref = f"{verse.get('scripture', 'Unknown')} {verse.get('chapter', '')}:{verse.get('verse', '')}"
            text = verse.get('translation', verse.get('text', ''))
            context_parts.append(f"[{ref}] {text}")

        return "\n\n".join(context_parts)

    def _calculate_confidence(self, verses: List[Dict]) -> str:
        """Calculate confidence score."""
        if not verses:
            return "0%"

        avg_similarity = sum(v.get('similarity', 0.8) for v in verses) / len(verses)
        score = int(min(avg_similarity * 100, 100))
        return f"{score}%"

    def _log_query(
        self,
        question: str,
        response: str,
        language: str,
        retrieved_count: int
    ) -> None:
        """Log user query to database."""
        try:
            self.db.log_query(
                query_text=question,
                response_text=response,
                language=language,
                retrieved_count=retrieved_count,
                timestamp=datetime.now()
            )
        except Exception as e:
            logger.error(f"Error logging query: {str(e)}")

    def close(self):
        """Close resources."""
        if hasattr(self, 'neo4j_driver') and self.neo4j_driver:
            self.neo4j_driver.close()
            logger.info("Neo4j driver closed")
