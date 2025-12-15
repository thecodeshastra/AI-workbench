"""Base provider module for AI agent"""

# abc module
from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Abstract base class for all AI providers.

    Args:
        ABC (ABC): Abstract base class.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a text response for the given prompt.

        Args:
            prompt (str): The input prompt.

        Returns:
            str: The generated response.
        """
        pass
