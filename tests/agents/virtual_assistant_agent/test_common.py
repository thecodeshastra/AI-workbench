"""
Test module for common utilities in virtual assistant agent.

This module contains unit tests for utility functions like extract_json.
"""

import unittest

from src.agents.virtual_assistant_agent.common import extract_json


class TestCommon(unittest.TestCase):
    """
    Test cases for common utility functions.

    This class tests helper functions used across the virtual assistant agent.

    Args:
        unittest.TestCase: The base test case class.
    """

    def test_extract_json_valid(self) -> None:
        """
        Test extract_json with valid JSON.

        Verifies extraction of plain JSON string.
        """
        text: str = '{"key": "value"}'
        result: dict = extract_json(text)
        self.assertEqual(result, {"key": "value"})

    def test_extract_json_with_markdown(self) -> None:
        """
        Test extract_json with markdown code fences.

        Ensures JSON is extracted from markdown formatted text.
        """
        text: str = '```json\n{"key": "value"}\n```'
        result: dict = extract_json(text)
        self.assertEqual(result, {"key": "value"})

    def test_extract_json_invalid(self) -> None:
        """
        Test extract_json with invalid input.

        Verifies that ValueError is raised for non-JSON text.
        """
        text: str = "no json"
        with self.assertRaises(ValueError):
            extract_json(text)

    def test_extract_json_empty(self) -> None:
        """
        Test extract_json with empty input.

        Ensures ValueError is raised for empty or whitespace-only strings.
        """
        text: str = ""
        with self.assertRaises(ValueError):
            extract_json(text)


if __name__ == "__main__":
    unittest.main()
