from pathlib import Path
import pdfplumber


class PersonaLoader:
    def __init__(self, persona_dir: str):
        self.persona_dir = Path(persona_dir)

    def load(self) -> str:
        parts = []

        summary = self.persona_dir / "summary.txt"
        if summary.exists():
            parts.append(summary.read_text())

        profile = self.persona_dir / "profile.pdf"
        if profile.exists():
            parts.append(self._load_pdf(profile))

        return "\n\n".join(parts)

    def _load_pdf(self, path: Path) -> str:
        text = []
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
        return "\n".join(text)
