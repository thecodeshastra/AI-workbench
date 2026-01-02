"""
Test module for memory selector in virtual assistant agent.

This module contains unit tests for the select_relevant_experience function,
verifying experience selection based on query relevance.
"""

import unittest

from src.agents.virtual_assistant_agent.memory_selector import (
    select_relevant_experience,
)


class TestMemorySelector(unittest.TestCase):
    """
    Test cases for the memory selector function.

    This class tests the select_relevant_experience function with different scenarios.

    Args:
        unittest.TestCase: The base test case class.
    """

    def test_select_relevant_experience(self) -> None:
        """
        Test experience selection based on query relevance.

        Ensures that the function returns experiences most relevant to the query.
        """
        experience: list = [{"content": "hello world"}, {"content": "foo bar"}]
        result: list = select_relevant_experience(experience, "hello")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["content"], "hello world")

    def test_select_relevant_experience_max_items(self) -> None:
        """
        Test experience selection with max_items limit.

        Ensures that the function returns experiences within the specified limit.
        """
        experience: list = [
            {"content": "hello world"},
            {"content": "hello there"},
            {"content": "foo"},
        ]
        result = select_relevant_experience(experience, "hello", max_items=1)
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
