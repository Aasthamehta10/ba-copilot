from pathlib import Path
from pypdf import PdfReader
from docx import Document


def load_document(path: Path) -> list[dict]:
    """Return a list of {text, source, page} dicts for one file."""
    suffix = path.suffix.lower()

    if suffix == ".pdf":
        reader = PdfReader(str(path))
        return [
            {"text": page.extract_text() or "", "source": path.name, "page": i + 1}
            for i, page in enumerate(reader.pages)
        ]

    if suffix == ".docx":
        doc = Document(str(path))
        text = "\n".join(p.text for p in doc.paragraphs)
        return [{"text": text, "source": path.name, "page": 1}]

    if suffix in {".txt", ".md"}:
        return [{"text": path.read_text(encoding="utf-8"), "source": path.name, "page": 1}]

    raise ValueError(f"Unsupported file type: {suffix}")