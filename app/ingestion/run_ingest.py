from pathlib import Path
from app.ingestion.loader import load_document
from app.ingestion.chunker import chunk_pages

all_chunks = []
for file in Path("data").iterdir():
    if file.is_file():
        all_chunks.extend(chunk_pages(load_document(file), chunk_size=30,chunk_overlap=50))

print(f"Total chunks: {len(all_chunks)}")
for chunk in all_chunks[:3]:
    print("-" * 40)
    print(chunk["chunk_id"])
    print(chunk["text"])