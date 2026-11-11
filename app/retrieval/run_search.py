from pathlib import Path
from app.ingestion.loader import load_document
from app.ingestion.chunker import chunk_pages
from app.retrieval.vectorstore import add_chunks, search

chunks = []
for file in Path("data").iterdir():
    if file.is_file():
        chunks.extend(chunk_pages(load_document(file), chunk_size=300, chunk_overlap=50))

add_chunks(chunks)
print(f"Stored {len(chunks)} chunks\n")

for question in [
    "What is the minimum credit score?",
    "Can self-employed people apply?",
    "How long does processing take?",
]:
    print("Q:", question)
    for hit in search(question):
        print(f"  [{hit['source']}] {hit['text'][:90]!r}")
    print()