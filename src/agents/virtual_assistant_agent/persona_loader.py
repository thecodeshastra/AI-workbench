"""Persona loader class for the virtual assistant agent."""

# pathlib module
from pathlib import Path

# pdfplumber module
import pdfplumber


class PersonaLoader:
    """Persona loader class for the virtual assistant agent."""

    def __init__(self, persona_dir: str) -> None:
        """Initializes the persona loader.

        Args:
            persona_dir (str): The persona directory.
        """
        self.persona_dir = Path(persona_dir)

    def load(self) -> str:
        """Loads the persona.

        Returns:
            str: The persona.
        """
        parts = []

        summary = self.persona_dir / "summary.txt"
        if summary.exists():
            parts.append(summary.read_text())

        profile = self.persona_dir / "profile.pdf"
        if profile.exists():
            parts.append(self._load_pdf(profile))

        return "\n\n".join(parts)

    def _load_pdf(self, path: Path) -> str:
        """Loads the PDF.

        Args:
            path (Path): The path to the PDF.

        Returns:
            str: The PDF content.
        """
        text = []
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
        return "\n".join(text)
