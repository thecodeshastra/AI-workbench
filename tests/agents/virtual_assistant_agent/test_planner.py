"""
Test module for planner in virtual assistant agent.

This module contains unit tests for the Planner class, verifying
planning functionality.
"""

import unittest
from unittest.mock import Mock, AsyncMock

from src.agents.virtual_assistant_agent.planner import Planner


class TestPlanner(unittest.TestCase):
    """
    Test cases for the Planner class.

    This class tests the planner's ability to generate plans.

    Args:
        unittest.TestCase: The base test case class.
    """

    def setUp(self) -> None:
        """
        Set up test environment.

        This method creates a mock provider, memory, and planner for testing.

        Returns:
            None
        """
        self.provider = Mock()
        self.memory = Mock()
        self.memory.load_experience.return_value = []
        self.tools_description = "tools"
        self.planner = Planner(self.provider, self.memory, self.tools_description)

    async def test_aplan(self) -> None:
        """
        Test plan generation.

        This method tests the planner's ability to generate plans.

        Returns:
            None
        """
        self.provider.generate_async = AsyncMock(return_value='{"steps": []}')
        result = await self.planner.aplan("user", "persona")
        self.assertIn("steps", result)


if __name__ == "__main__":
    unittest.main()
