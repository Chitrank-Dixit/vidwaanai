import requests
import logging

logger = logging.getLogger(__name__)

class LMStudioClient:
    """OpenAI-compatible client for LM Studio local inference server."""
    
    def __init__(self, base_url="http://localhost:1234", model_name="falcon-h1-7b-instruct"):
        self.base_url = base_url.rstrip('/')
        if self.base_url.endswith('/v1'):
            self.base_url = self.base_url[:-3]
        self.model_name = model_name
        logger.info(f"Initialized LMStudioClient: {self.base_url} with model {self.model_name}")

    def generate(self, prompt: str, max_tokens=512, temperature=0.7) -> str:
        """Generate text using LM Studio's OpenAI-compatible chat completions endpoint."""
        try:
            # LM Studio uses OpenAI-compatible /v1/chat/completions endpoint
            url = f"{self.base_url}/v1/chat/completions"
            
            payload = {
                "model": self.model_name,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": max_tokens,
                "temperature": temperature,
                "stream": False
            }
            
            logger.debug(f"Sending request to {url}")
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract the generated text from OpenAI-compatible response
            if "choices" in data and len(data["choices"]) > 0:
                message = data["choices"][0].get("message", {})
                text = message.get("content", "").strip()
                logger.debug(f"Generated response: {text[:100]}...")
                return text
            else:
                logger.error(f"Unexpected response format: {data}")
                return ""
                
        except requests.exceptions.Timeout:
            logger.error("LM Studio request timed out")
            raise
        except requests.exceptions.ConnectionError:
            logger.error(f"Could not connect to LM Studio at {self.base_url}. Is the server running?")
            raise
        except Exception as e:
            logger.error(f"LM Studio request failed: {e}")
            raise

    def check_connection(self):
        """Test if LM Studio server is accessible."""
        try:
            url = f"{self.base_url}/v1/models"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            models = response.json()
            logger.info(f"Connected to LM Studio. Available models: {models}")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to LM Studio: {e}")
            return False
