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
from src.graph.hybrid_search import HybridSearch as GraphHybridSearch
from src.retrieval.bm25_search import BM25Search
from src.retrieval.hybrid_search import HybridSearch
from src.graph.entity_extractor import EntityExtractor
from src.core.monitoring import track_query_latency, record_retrieval_quality
from src.utils.confidence import calculate_confidence_score
from src.retrieval.advanced_retrieval_pipeline import AdvancedRetrievalPipeline
from neo4j import GraphDatabase
from src.rag.multilingual_search import MultilingualSearch

from src.cache.query_cache import QueryCache

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
        # Use MultilingualSearch for embeddings and language processing
        self.multilingual_search = MultilingualSearch()
        # Keep EmbeddingManager for legacy support if needed, but MultilingualSearch handles embedding now
        # self.embeddings = EmbeddingManager()
        
        if use_lmstudio:
            self.llm = LMStudioClient(base_url=lmstudio_url or "http://localhost:8000")
        else:
            self.llm = OpenAIClient(api_key=openai_key)
        self.router = QueryRouter()
        self.cache = QueryCache()
        
        # Hybrid Search (BM25 + Vector)
        try:
            verses = self.db.get_all_verses()
            self.bm25_search = BM25Search(verses)
            
            def vector_search_func(query, top_k):
                # Use multilingual embedding
                query_data = self.multilingual_search.process_query(query)
                emb = query_data['embedding']
                results = self.db.retrieve_verses(emb, top_k=top_k)
                for r in results:
                    r['score'] = r.get('similarity', 0.0)
                return results
                
            self.hybrid_retriever = HybridSearch(
                bm25_search=self.bm25_search,
                vector_search_func=vector_search_func
            )
            
            # Initialize Advanced Pipeline
            self.retrieval_pipeline = AdvancedRetrievalPipeline(self.hybrid_retriever)
            logger.info("Advanced Retrieval Pipeline initialized")
            
        except Exception as e:
            logger.error(f"Failed to initialize Retrieval Pipeline: {e}")
            self.retrieval_pipeline = None
            self.hybrid_retriever = None

        # Graph RAG setup
        self.enable_graph_rag = enable_graph_rag
        if enable_graph_rag and neo4j_uri:
            try:
                self.neo4j_driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))
                self.graph_retriever = GraphRetriever(self.neo4j_driver)
                self.entity_extractor = EntityExtractor(self.llm)
                self.graph_search = GraphHybridSearch(
                    self.graph_retriever, self.db, self.multilingual_search.embeddings, self.entity_extractor
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
            # Step 1: Detect language and process query
            query_data = self.multilingual_search.process_query(question)
            detected_lang = query_data['language_code']
            query_embedding = query_data['embedding']
            
            logger.info(f"Query language: {detected_lang}")

            # Check Cache
            cached_result = self.cache.get(question, detected_lang, scripture_filter)
            if cached_result:
                return cached_result

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
                    top_k=5
                )

            graph_context = ""
            if self.enable_graph_rag:
                # We use graph_search to get graph context, but ignore its vector results
                # as we already have better ones from hybrid_retriever
                try:
                    graph_results = self.graph_search.search(question, top_k=5)
                    graph_context = graph_results.get('fused_context', '')
                except Exception as e:
                    logger.error(f"Graph search failed: {e}")

            if verbose:
                logger.info(f"Retrieved {len(retrieved_verses)} verses")
            
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

            result = {
                "answer": final_answer,
                "retrieved_verses": retrieved_verses,
                "language": detected_lang,
                "confidence": confidence_result, # detailed dict
                "timestamp": datetime.now().isoformat()
            }
            
            # Store in cache
            self.cache.set(question, detected_lang, result, scripture_filter)
            
            return result

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
