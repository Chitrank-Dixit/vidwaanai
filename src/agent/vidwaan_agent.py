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

logger = logging.getLogger(__name__)

class VidwaanAI:
    """Main VidwaanAI Agent class."""

    def __init__(
        self,
        db_url: str,
        openai_key: str,
        krutrim_key: Optional[str] = None,
        use_lmstudio=True, lmstudio_url=None
    ):
        """Initialize VidwaanAI agent."""
        self.db = DatabaseManager(db_url)
        self.embeddings = EmbeddingManager()
        if use_lmstudio:
            self.llm = LMStudioClient(base_url=lmstudio_url or "http://localhost:8000")
        else:
            self.llm = OpenAIClient(api_key=openai_key)
        self.router = QueryRouter()

        logger.info("VidwaanAI agent initialized")

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
            retrieved_verses = self.db.retrieve_verses(
                query_embedding=query_embedding,
                scripture_filter=scripture_filter,
                top_k=5
            )

            if verbose:
                logger.info(f"Retrieved {len(retrieved_verses)} verses")

            # Step 4: Format context for LLM
            context = self._format_context(retrieved_verses, detected_lang)

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

            # Step 6: Log query
            self._log_query(
                question=question,
                response=response_text,
                language=detected_lang,
                retrieved_count=len(retrieved_verses)
            )

            return {
                "answer": response_text,
                "retrieved_verses": retrieved_verses,
                "language": detected_lang,
                "confidence": self._calculate_confidence(retrieved_verses),
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
