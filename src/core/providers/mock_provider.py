"""Mock provider module for AI agent"""

# interface module
from interfaces.base_provider import BaseProvider


class MockProvider(BaseProvider):
    """
    Mock provider for testing agent logic without any LLM.

    Args:
        BaseProvider (BaseProvider): Base provider class.
    """

    def generate(self, prompt: str) -> str:
        """
        Generate a response using the Mock provider.

        Args:
            prompt (str): The input prompt.

        Returns:
            str: The generated response.
        """
        return (
            "### MOCK RESPONSE ###\n\n"
            "This is a mock provider output.\n\n"
            "Prompt received:\n"
            f"{prompt[:300]}..."
        )
