"""
Test module for Critic in virtual assistant agent.

This module contains unit tests for the Critic class,
verifying evaluation and memory handling functionality.
"""

import unittest
from unittest.mock import Mock, AsyncMock

from src.agents.virtual_assistant_agent.critic import Critic


class TestCritic(unittest.TestCase):
    """
    Test cases for the Critic class.

    This class tests the critic's ability to evaluate agent output and update memory.

    Args:
        unittest.TestCase: The base test case class.
    """

    def setUp(self) -> None:
        """
        Set up test fixtures.

        Creates mock provider and memory, and Critic instance.
        """
        self.provider: Mock = Mock()
        self.memory: Mock = Mock()
        self.critic: Critic = Critic(self.provider, self.memory)

    def test_init(self) -> None:
        """
        Test Critic initialization.

        Verifies that the critic is properly initialized with provider and memory.
        """
        self.assertEqual(self.critic.provider, self.provider)
        self.assertEqual(self.critic.memory, self.memory)

    async def test_aevaluate(self) -> None:
        """
        Test asynchronous evaluation.

        Verifies that aevaluate returns a valid judgment dictionary.
        """
        self.provider.generate_async = AsyncMock(
            return_value='{"failure": false, "unknown": false, "lesson": null, "unknown_question": null}'
        )
        result: dict = await self.critic.aevaluate("user", "output", "system")
        self.assertIn("failure", result)

    async def test_ahandle(self) -> None:
        """
        Test asynchronous handling of output.

        Ensures the critic updates memory based on evaluation results.
        """
        self.provider.generate_async = AsyncMock(
            return_value='{"failure": true, "unknown": false, "lesson": "test lesson", "unknown_question": null}'
        )
        await self.critic.ahandle("user", "output")
        self.memory.add_experience.assert_called_with(
            content="test lesson", category="failure"
        )


if __name__ == "__main__":
    unittest.main()
