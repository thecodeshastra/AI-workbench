"""
Test module for VirtualAssistantAgent.

This module contains unit tests for the VirtualAssistantAgent class,
verifying initialization and execution functionality.
"""

import unittest
from unittest.mock import Mock, AsyncMock
import asyncio

from src.agents.virtual_assistant_agent.agent import VirtualAssistantAgent


class TestVirtualAssistantAgent(unittest.TestCase):
    """
    Test cases for the VirtualAssistantAgent class.

    This class tests the virtual assistant agent's initialization and run methods.

    Args:
        unittest.TestCase: The base test case class.
    """

    def setUp(self) -> None:
        """
        Set up test fixtures.

        Creates mocked dependencies and VirtualAssistantAgent instance.
        """
        self.persona_loader: Mock = Mock()
        self.persona_loader.load.return_value = "test persona"
        self.planner: Mock = Mock()
        self.planner.aplan = AsyncMock(return_value={"steps": []})
        self.executor: Mock = Mock()
        self.provider: Mock = Mock()
        self.provider.generate_async = AsyncMock(return_value="response")
        self.critic: Mock = Mock()
        self.critic.ahandle = AsyncMock()
        self.agent: VirtualAssistantAgent = VirtualAssistantAgent(
            self.persona_loader, self.planner, self.executor, self.provider, self.critic
        )

    def test_init(self) -> None:
        """
        Test VirtualAssistantAgent initialization.

        Verifies that the agent loads the persona context correctly.
        """
        self.assertEqual(self.agent.persona_context, "test persona")

    def test_arun_no_steps(self) -> None:
        """
        Test asynchronous run with no steps.

        Ensures the agent handles direct chat responses correctly.
        """
        result: str = asyncio.run(self.agent.arun("test"))
        self.assertEqual(result, "response")

    def test_run(self) -> None:
        """
        Test synchronous run method.

        Verifies the wrapper method calls the async version properly.
        """
        result: str = self.agent.run("test")
        self.assertEqual(result, "response")


if __name__ == "__main__":
    unittest.main()
