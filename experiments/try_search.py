from app.retrieval.vectorstore import search

for hit in search("Can self-employed people apply?", k=1):
    print(hit["source"], round(hit["distance"], 3))
    print(hit["text"][:80])
    print()