from dotenv import load_dotenv
import chromadb
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embedder = OpenAIEmbeddings(model="text-embedding-3-small")
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection("ba_docs")


def add_chunks(chunks: list[dict]) -> None:
    texts = [c["text"] for c in chunks]
    vectors = embedder.embed_documents(texts)
    collection.upsert(
        ids=[c["chunk_id"] for c in chunks],
        documents=texts,
        embeddings=vectors,
        metadatas=[{"source": c["source"], "page": c["page"]} for c in chunks],
    )


def search(query: str, k: int = 3) -> list[dict]:
    vector = embedder.embed_query(query)
    result = collection.query(query_embeddings=[vector], n_results=k)
    return [
        {"text": doc, "source": meta["source"], "distance": dist}
        for doc, meta, dist in zip(
            result["documents"][0], result["metadatas"][0], result["distances"][0]
        )
    ]