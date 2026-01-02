"""
Test module for Executor in summarizer agent.

This module contains unit tests for the Executor class,
verifying plan execution functionality.
"""

import unittest
from unittest.mock import Mock
from typing import Dict, Any

from src.agents.summarizer_agent.executor import Executor


class TestExecutor(unittest.TestCase):
    """
    Test cases for the Executor class.

    This class tests the execution of plans using mocked tools.

    Args:
        unittest.TestCase: The base test case class.
    """

    def setUp(self) -> None:
        """
        Set up test fixtures.

        Creates a mock provider, Executor, and mock tool for testing.
        """
        self.provider: Mock = Mock()
        self.executor: Executor = Executor(self.provider)
        self.mock_tool: Mock = Mock()
        self.executor.tools = {"file_read": self.mock_tool}

    def test_run(self) -> None:
        """
        Test plan execution.

        Verifies that the executor calls the appropriate tool with correct arguments.
        """
        plan: Dict[str, Any] = {
            "steps": [{"tool": "file_read", "input": {"path": "test.txt"}}]
        }
        self.executor.run(plan)
        self.mock_tool.run.assert_called_once_with({"path": "test.txt"}, {})


if __name__ == "__main__":
    unittest.main()
