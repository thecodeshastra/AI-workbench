"""
Test module for AsyncExecutor in summarizer agent.

This module contains unit tests for the AsyncExecutor class,
verifying asynchronous plan execution functionality.
"""

import unittest
from unittest.mock import Mock, AsyncMock
import asyncio
from typing import Dict, Any

from src.agents.summarizer_agent.async_executor import AsyncExecutor


class TestAsyncExecutor(unittest.TestCase):
    """
    Test cases for the AsyncExecutor class.

    This class tests asynchronous execution of plans using mocked async tools.

    Args:
        unittest.TestCase: The base test case class.
    """

    def setUp(self) -> None:
        """
        Set up test fixtures.

        Creates a mock provider, AsyncExecutor, and mock async tool.
        """
        self.provider: Mock = Mock()
        self.executor: AsyncExecutor = AsyncExecutor(self.provider)
        self.mock_tool: Mock = Mock()
        self.mock_tool.arun = AsyncMock()
        self.executor.tools = {"file_read": self.mock_tool}

    def test_run(self) -> None:
        """
        Test asynchronous plan execution.

        Verifies that the async executor runs the plan and calls the async tool.
        """
        plan: Dict[str, Any] = {
            "steps": [{"tool": "file_read", "input": {"path": "test.txt"}}]
        }
        asyncio.run(self.executor.run(plan))
        self.mock_tool.arun.assert_called_once()


if __name__ == "__main__":
    unittest.main()
