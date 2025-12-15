"""Google Gemini provider module for AI agent"""

# python
import os

# google gemini module
import google.generativeai as genai

# stateless ai agent module
from providers.base_provider import BaseProvider


class GeminiProvider(BaseProvider):
    """
    Google Gemini provider.

    Args:
        BaseProvider (BaseProvider): Base provider class.

    Raises:
        ValueError: If GEMINI_API_KEY is not found in environment.
    """

    def __init__(self, model_name: str = "gemini-1.5-flash", temperature: float = 0.2):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment")

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(model_name)
        self.temperature = temperature

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": self.temperature,
            },
        )

        return response.text.strip()
