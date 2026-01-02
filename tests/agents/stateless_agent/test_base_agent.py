"""
Test module for StatelessAgent.

This module contains unit tests for the StatelessAgent class,
verifying its initialization, prompt building, and run functionality.
"""

import unittest

from src.agents.stateless_agent.base_agent import StatelessAgent
from src.core.providers.mock_provider import MockProvider


class TestStatelessAgent(unittest.TestCase):
    """
    Test cases for the StatelessAgent class.

    This class tests the core functionality of the StatelessAgent,
    including provider integration and response generation.

    Args:
        unittest.TestCase: The base test case class.
    """

    def setUp(self) -> None:
        """
        Set up test fixtures.

        Initializes a MockProvider and StatelessAgent instance for testing.
        """
        self.provider: MockProvider = MockProvider()
        self.agent: StatelessAgent = StatelessAgent(self.provider)

    def test_init(self) -> None:
        """
        Test StatelessAgent initialization.

        Verifies that the agent is properly initialized with the provider.
        """
        self.assertIsInstance(self.agent.provider, MockProvider)

    def test_build_prompt(self) -> None:
        """
        Test the _build_prompt method.

        Ensures the prompt is correctly constructed with user input.
        """
        user_input: str = "test input"
        prompt: str = self.agent._build_prompt(user_input)
        self.assertIn(user_input, prompt)
        self.assertIn("USER REQUEST:", prompt)

    def test_run(self) -> None:
        """
        Test the run method.

        Verifies that the agent generates a response containing expected content.
        """
        user_input: str = "test"
        response: str = self.agent.run(user_input)
        self.assertIn("MOCK RESPONSE", response)


if __name__ == "__main__":
    unittest.main()
