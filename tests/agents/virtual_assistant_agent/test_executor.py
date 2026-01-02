"""
Test module for Executor in virtual assistant agent.

This module contains unit tests for the Executor class,
verifying tool execution and plan handling functionality.
"""

import unittest
from unittest.mock import Mock, AsyncMock

from src.agents.virtual_assistant_agent.executor import Executor


class TestExecutor(unittest.TestCase):
    """
    Test cases for the Executor class.

    This class tests the executor's ability to execute tools based on plans.

    Args:
        unittest.TestCase: The base test case class.
    """

    def setUp(self) -> None:
        """
        Set up test fixtures.

        Creates a tool registry and Executor instance.
        """
        self.tool_registry: dict = {"tool1": Mock(description="desc1")}
        self.executor: Executor = Executor(self.tool_registry)

    def test_init(self) -> None:
        """
        Test Executor initialization.

        Verifies that the executor is properly initialized with the tool registry.
        """
        self.assertEqual(self.executor.tools, self.tool_registry)

    async def test_arun(self) -> None:
        """
        Test asynchronous execution of a plan.

        Ensures that the executor executes tools based on the plan and returns the result.
        """
        self.tool_registry["tool1"].arun = AsyncMock()
        plan = {"steps": [{"tool": "tool1", "input": {}}]}
        result = await self.executor.arun(plan)
        self.assertEqual(result, {})

    def test_describe_tools(self) -> None:
        """
        Test tool description.

        Ensures that the executor returns a description of the tools in the registry.
        """
        desc: str = self.executor.describe_tools()
        self.assertIn("desc1", desc)


if __name__ == "__main__":
    unittest.main()
