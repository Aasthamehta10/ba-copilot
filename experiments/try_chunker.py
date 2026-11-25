from pathlib import Path
from app.ingestion.loader import load_document
from app.ingestion.chunker import chunk_pages

pages = load_document(Path("data/old_loan_policy.txt"))

for size in [100, 300, 1000]:
    chunks = chunk_pages(pages, chunk_size=size, chunk_overlap=20)
    print(f"chunk_size={size}: {len(chunks)} chunks")
    print("  first chunk id:", chunks[0]["chunk_id"])