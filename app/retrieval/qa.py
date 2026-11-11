from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from app.retrieval.vectorstore import search

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

PROMPT = """You are a business analysis assistant. Answer the question using ONLY the context below.
Cite the source file name in square brackets after each fact, like [new_loan_brd.txt].
If documents disagree, say so explicitly and cite both.
If the answer is not in the context, say "I could not find this in the documents."

Context:
{context}

Question: {question}
"""


def answer(question: str, k: int = 4) -> str:
    hits = search(question, k=k)
    context = "\n\n".join(f"[{h['source']}]\n{h['text']}" for h in hits)
    return llm.invoke(PROMPT.format(context=context, question=question)).content