"""Perplexity provider module for AI agent"""

# open ai module
from openai import OpenAI

# interface module
from interfaces.base_provider import BaseProvider


class PerplexityProvider(BaseProvider):
    """
    Perplexity provider.

    Args:
        BaseProvider (BaseProvider): Base provider class.
    """

    def __init__(self, model_name: str, temperature: float = 0.2):
        """
        Initialize the Perplexity provider.

        Args:
            model_name (str): The model name.
            temperature (float, optional): The temperature. Defaults to 0.2.
        """
        self.client = OpenAI(
            api_key=None,  # picked from env
            base_url="https://api.perplexity.ai",
        )
        self.model = model_name
        self.temperature = temperature

    def generate(self, prompt: str, system_prompt: str) -> str:
        """
        Generate a response using the Perplexity provider.

        Args:
            prompt (str): The input prompt.
            system_prompt (str): The system prompt.

        Returns:
            str: The generated response.
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt},
                {"role": "system", "content": system_prompt},
            ],
            temperature=self.temperature,
        )
        return response.choices[0].message.content
