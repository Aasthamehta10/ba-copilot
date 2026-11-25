from pathlib import Path
from app.ingestion.loader import load_document

pages = load_document(Path("data/old_loan_policy.txt"))
print(pages)
print(len(pages))
print(pages[0]["source"])
print(pages[0]["text"])