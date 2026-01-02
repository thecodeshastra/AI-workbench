"""
Test module for MockProvider.

This module contains unit tests for the MockProvider class,
verifying its response generation functionality.
"""

import unittest

from src.core.providers.mock_provider import MockProvider


class TestMockProvider(unittest.TestCase):
    """
    Test cases for the MockProvider class.

    This class tests the mock provider's generate method.

    Args:
        unittest.TestCase: The base test case class.
    """

    def setUp(self) -> None:
        """
        Set up test fixtures.

        Creates a MockProvider instance.
        """
        self.provider: MockProvider = MockProvider()

    def test_generate(self) -> None:
        """
        Test the generate method.

        Ensures the mock provider returns a response containing expected mock content.
        """
        result: str = self.provider.generate("prompt", "system")
        self.assertIn("MOCK RESPONSE", result)
        self.assertIn("prompt", result)


if __name__ == "__main__":
    unittest.main()
