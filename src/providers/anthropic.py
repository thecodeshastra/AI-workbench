"""Anthropic provider module for AI agent"""

# anthropic module
import anthropic

# stateless ai agent modules
from providers.base_provider import BaseProvider


class AnthropicProvider(BaseProvider):
    """
    Anthropic provider class.
    """

    def __init__(
        self, model_name: str, temperature: float = 0.2, max_tokens: int = 500
    ):
        """
        Initialize the Anthropic provider.

        Args:
            model_name (str): The model name.
            temperature (float, optional): The temperature. Defaults to 0.2.
            max_tokens (int, optional): The maximum number of tokens. Defaults to 500.
        """
        self.client = anthropic.Anthropic()
        self.model = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate(self, prompt: str) -> str:
        """
        Generate a response using the Anthropic provider.

        Args:
            prompt (str): The input prompt.

        Returns:
            str: The generated response.
        """
        response = self.client.messages.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        return response.content[0].text
