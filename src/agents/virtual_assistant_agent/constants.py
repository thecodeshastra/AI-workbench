"""Constants for the virtual assistant agent."""

# pathlib module
from pathlib import Path

# Current file path
CURRENT_FILE_PATH = Path(__file__).parent.resolve()

# Memory and persona paths
MEMORY_PATH = CURRENT_FILE_PATH / "memory"
PERSONA_PATH = CURRENT_FILE_PATH / "persona"
