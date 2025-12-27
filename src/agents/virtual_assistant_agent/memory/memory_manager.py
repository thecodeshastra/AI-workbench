"""Memory manager class for the virtual assistant agent."""

# python module
import json
import uuid
from datetime import datetime
from pathlib import Path


class MemoryManager:
    """Memory manager class for the virtual assistant agent."""

    def __init__(self, memory_dir: str) -> None:
        """Initializes the memory manager.

        Args:
            memory_dir (str): The memory directory.
        """
        self.dir = Path(memory_dir)
        self.dir.mkdir(parents=True, exist_ok=True)

        self.experience = self.dir / "experience.json"
        self.unknowns = self.dir / "unknowns.json"

        for f in [self.experience, self.unknowns]:
            if not f.exists():
                f.write_text("[]")

    def _load(self, file: Path) -> list:
        """Loads the memory.

        Args:
            file (Path): The file to load.

        Returns:
            list: The memory.
        """
        return json.loads(file.read_text())

    def _append(self, file: Path, entry: dict) -> None:
        """Appends to the memory.

        Args:
            file (Path): The file to append to.
            entry (dict): The entry to append.
        """
        data = self._load(file)
        data.append(entry)
        file.write_text(json.dumps(data, indent=2))

    def add_experience(self, content: str, category: str) -> None:
        """Adds experience to the memory.

        Args:
            content (str): The content of the experience.
            category (str): The category of the experience.
        """
        self._append(
            self.experience,
            {
                "id": str(uuid.uuid4()),
                "timestamp": datetime.utcnow().isoformat(),
                "category": category,
                "content": content,
            },
        )

    def add_unknown(self, question: str) -> None:
        """Adds unknown to the memory.

        Args:
            question (str): The question.
        """
        self._append(
            self.unknowns,
            {
                "id": str(uuid.uuid4()),
                "timestamp": datetime.utcnow().isoformat(),
                "question": question,
            },
        )

    def load_experience(self) -> list:
        """Loads the experience.

        Returns:
            list: The experience.
        """
        return self._load(self.experience)
