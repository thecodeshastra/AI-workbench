"""Hugging Face provider module for AI agent"""

# hugging face module
from huggingface_hub import InferenceClient

# interface module
from interfaces.base_provider import BaseProvider


class HuggingFaceProvider(BaseProvider):
    """
    Hugging Face Inference API provider.

    Args:
        BaseProvider (BaseProvider): Base provider class.
    """

    def __init__(
        self, model_name: str, temperature: float = 0.2, max_tokens: int = 500
    ):
        """
        Initialize the Hugging Face provider.

        Args:
            model_name (str): The model name.
            temperature (float, optional): The temperature. Defaults to 0.2.
            max_tokens (int, optional): The maximum number of tokens. Defaults to 500.
        """
        self.client = InferenceClient(model=model_name)
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate(self, prompt: str) -> str:
        """
        Generate a response using the Hugging Face provider.

        Args:
            prompt (str): The input prompt.

        Returns:
            str: The generated response.
        """
        response = self.client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )

        return response.choices[0].message["content"].strip()


class HuggingFaceTextGenerationProvider(BaseProvider):
    """
    Hugging Face Text Generation provider.

    Args:
        BaseProvider (BaseProvider): Base provider class.
    """

    def __init__(self, temperature: float = 0.2, max_tokens: int = 500):
        """
        Initialize the Hugging Face Text Generation provider.

        Args:
            temperature (float, optional): The temperature. Defaults to 0.2.
            max_tokens (int, optional): The maximum number of tokens. Defaults to 500.
        """
        self.client = InferenceClient()
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate(self, prompt: str) -> str:
        """
        Generate a response using the Hugging Face Text Generation provider.

        Args:
            prompt (str): The input prompt.

        Returns:
            str: The generated response.
        """
        response = self.client.text_generation(
            prompt=prompt,
            max_new_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        return response.strip()
