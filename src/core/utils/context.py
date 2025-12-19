"""Agent context module for AI agent"""

# python module
import asyncio
from typing import Any, Dict


class AgentContext:
    """
    Async-safe shared context for agent execution.

    Attributes:
        _data (Dict[str, Any]): Internal storage for context data.
        _lock (asyncio.Lock): Lock for thread-safe access to _data.
    """

    def __init__(self):
        """
        Initialize the AgentContext.
        """
        self._data: Dict[str, Any] = {}
        self._lock = asyncio.Lock()

    async def set(self, key: str, value: Any):
        """
        Set a value in the context.

        Args:
            key (str): The key for the value.
            value (Any): The value to store.
        """
        async with self._lock:
            self._data[key] = value

    async def get(self, key: str):
        """
        Get a value from the context.

        Args:
            key (str): The key for the value.

        Returns:
            Any: The value associated with the key, or None if not found.
        """
        async with self._lock:
            return self._data.get(key)

    async def snapshot(self) -> Dict[str, Any]:
        """
        Create a snapshot of the current context state.

        Returns:
            Dict[str, Any]: A copy of the context data.
        """
        async with self._lock:
            return dict(self._data)
