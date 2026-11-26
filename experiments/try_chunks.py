from app.retrieval.vectorstore import get_all_chunks

for c in get_all_chunks():
    print(c["source"])
    print(c["text"])
    print("-" * 40)