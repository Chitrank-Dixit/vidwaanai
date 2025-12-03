"""OpenAI LLM client."""

from src.core.logger import get_logger
from src.core.profiler import profile_function
import openai

logger = get_logger(__name__)


class OpenAIClient:
    """OpenAI API client for LLM calls."""

    def __init__(self, api_key: str, model: str = "gpt-4-turbo"):
        """Initialize OpenAI client."""
        openai.api_key = api_key
        self.model = model
        logger.info(f"OpenAI client initialized with model: {model}")

    @profile_function
    def generate(
        self, prompt: str, max_tokens: int = 500, temperature: float = 0.3
    ) -> str:
        """Generate response from LLM."""
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a knowledgeable assistant about Indian scriptures.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=max_tokens,
                temperature=temperature,
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            raise
