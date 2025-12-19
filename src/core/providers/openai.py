"""OpenAI provider module for AI agent"""

# open ai module
from openai import OpenAI

# interface module
from interfaces.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):
    """
    OpenAI provider.

    Args:
        BaseProvider (BaseProvider): Base provider class.
    """

    def __init__(
        self, model_name: str, temperature: float = 0.2, max_tokens: int = 500
    ):
        """
        Initialize the OpenAI provider.

        Args:
            model_name (str): The model name.
            temperature (float, optional): The temperature. Defaults to 0.2.
            max_tokens (int, optional): The maximum number of tokens. Defaults to 500.
        """
        self.client = OpenAI()
        self.model = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate(self, prompt: str) -> str:
        """
        Generate a response using the OpenAI provider.

        Args:
            prompt (str): The input prompt.

        Returns:
            str: The generated response.
        """
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
            temperature=self.temperature,
            max_output_tokens=self.max_tokens,
        )
        return response.output_text
