"""
Test module for memory manager in virtual assistant agent.

This module contains unit tests for the MemoryManager class, verifying
experience loading and adding functionality.
"""

import unittest
from unittest.mock import patch, Mock

from src.agents.virtual_assistant_agent.memory.memory_manager import MemoryManager


class TestMemoryManager(unittest.TestCase):
    """
    Test cases for the MemoryManager class.

    This class tests the memory manager's ability to load and add experiences.

    Args:
        unittest.TestCase: The base test case class.
    """

    @patch("pathlib.Path.mkdir")
    @patch("pathlib.Path.exists")
    @patch("pathlib.Path.write_text")
    def setUp(self, mock_write: Mock, mock_exists: Mock, mock_mkdir: Mock) -> None:
        """
        Set up test environment.

        Args:
            mock_write: Mock for Path.write_text.
            mock_exists: Mock for Path.exists.
            mock_mkdir: Mock for Path.mkdir.
        """
        mock_exists.return_value = True
        self.manager = MemoryManager("test_dir")

    @patch("json.loads")
    @patch("pathlib.Path.read_text")
    def test_load_experience(self, mock_read: Mock, mock_loads: Mock) -> None:
        """
        Test experience loading from file.

        Args:
            mock_read: Mock for Path.read_text.
            mock_loads: Mock for json.loads.
        """
        mock_read.return_value = "[]"
        mock_loads.return_value = []
        result = self.manager.load_experience()
        self.assertEqual(result, [])

    @patch("json.dumps")
    @patch("pathlib.Path.write_text")
    @patch("pathlib.Path.read_text")
    @patch("json.loads")
    def test_add_experience(
        self, mock_loads: Mock, mock_read: Mock, mock_write: Mock, mock_dumps: Mock
    ) -> None:
        """
        Test experience addition to file.

        Args:
            mock_loads: Mock for json.loads.
            mock_read: Mock for Path.read_text.
            mock_write: Mock for Path.write_text.
            mock_dumps: Mock for json.dumps.
        """
        mock_read.return_value = "[]"
        mock_loads.return_value = []
        mock_dumps.return_value = "[]"
        self.manager.add_experience("content", "category")
        mock_write.assert_called()


if __name__ == "__main__":
    unittest.main()
