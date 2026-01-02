"""
Test module for provider factory.

This module contains unit tests for the get_provider function,
verifying provider instantiation based on configuration.
"""

import unittest
from unittest.mock import patch

from src.core.provider_factory import get_provider


class TestProviderFactory(unittest.TestCase):
    """
    Test cases for the provider factory function.

    This class tests the get_provider function with different provider configurations.

    Args:
        unittest.TestCase: The base test case class.
    """

    @patch("src.core.provider_factory.PROVIDER", "mock")
    def test_get_provider_mock(self) -> None:
        """
        Test get_provider with mock provider.

        Verifies that the mock provider is correctly instantiated.
        """
        provider = get_provider()
        self.assertEqual(provider.__class__.__name__, "MockProvider")


if __name__ == "__main__":
    unittest.main()
