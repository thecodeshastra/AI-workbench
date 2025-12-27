"""Base provider interface for AI agent"""

# asyncio module
import asyncio

# abc module
from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Abstract base class for all AI providers.

    Args:
        ABC (ABC): Abstract base class.
    """

    @abstractmethod
    def generate(self, prompt: str, system_prompt: str) -> str:
        """
        Generate a text response for the given prompt.

        Args:
            prompt (str): The input prompt.
            system_prompt (str): The system prompt.

        Returns:
            str: The generated response.
        """
        pass

    async def generate_async(self, prompt: str, system_prompt: str) -> str:
        """
        Default async wrapper for sync providers.

        Args:
            prompt (str): The input prompt.
            system_prompt (str): The system prompt.

        Returns:
            str: The generated response.
        """
        return await asyncio.to_thread(self.generate, prompt, system_prompt)
