import json
import uuid
from datetime import datetime
from pathlib import Path


class MemoryManager:
    def __init__(self, memory_dir: str):
        self.dir = Path(memory_dir)
        self.dir.mkdir(parents=True, exist_ok=True)

        self.experience = self.dir / "experience.json"
        self.unknowns = self.dir / "unknowns.json"

        for f in [self.experience, self.unknowns]:
            if not f.exists():
                f.write_text("[]")

    def _load(self, file):
        return json.loads(file.read_text())

    def _append(self, file, entry):
        data = self._load(file)
        data.append(entry)
        file.write_text(json.dumps(data, indent=2))

    def add_experience(self, content: str, category: str):
        self._append(
            self.experience,
            {
                "id": str(uuid.uuid4()),
                "timestamp": datetime.utcnow().isoformat(),
                "category": category,
                "content": content,
            },
        )

    def add_unknown(self, question: str):
        self._append(
            self.unknowns,
            {
                "id": str(uuid.uuid4()),
                "timestamp": datetime.utcnow().isoformat(),
                "question": question,
            },
        )

    def load_experience(self):
        return self._load(self.experience)
