import unittest
from unittest.mock import patch

from src.agents.virtual_assistant_agent.persona_loader import PersonaLoader


class TestPersonaLoader(unittest.TestCase):
    def setUp(self):
        self.loader = PersonaLoader("test_dir")

    @patch("pathlib.Path.exists")
    @patch("pathlib.Path.read_text")
    def test_load(self, mock_read, mock_exists):
        mock_exists.return_value = True
        mock_read.return_value = "content"
        result = self.loader.load()
        self.assertEqual(result, "content")


if __name__ == "__main__":
    unittest.main()
