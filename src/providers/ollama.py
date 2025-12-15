"""Ollama provider module for AI agent"""

# request module
import requests

# stateless agent module
from providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):
    """
    Ollama local LLM provider.

    Args:
        BaseProvider (BaseProvider): Base provider class.
    """

    def __init__(self, model_name: str, temperature: float = 0.2):
        """
        Initialize the Ollama provider.

        Args:
            model_name (str): The model name.
            temperature (float, optional): The temperature. Defaults to 0.2.
        """
        self.model_name = model_name
        self.temperature = temperature
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt: str) -> str:
        """
        Generate a response using the Ollama provider.

        Args:
            prompt (str): The input prompt.

        Returns:
            str: The generated response.
        """
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": self.temperature,
            },
        }

        response = requests.post(self.url, json=payload)
        response.raise_for_status()

        return response.json()["response"].strip()
