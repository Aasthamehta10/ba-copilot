from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from app.retrieval.vectorstore import get_all_chunks

load_dotenv()


class Conflict(BaseModel):
    topic: str
    document_a: str
    statement_a: str
    document_b: str
    statement_b: str
    severity: str  # high, medium or low
    suggested_question: str  # what the BA should ask the stakeholder


class ConflictReport(BaseModel):
    conflicts: list[Conflict]


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0).with_structured_output(ConflictReport)

PROMPT = """You are a senior business analyst reviewing documents for contradictions.
Compare the documents below. Find every place where two documents give different
rules, numbers, limits or conditions for the same topic.
Only report real conflicts supported by the text. Do not invent any.
For each conflict, quote the exact statement from each document, rate severity
(high if it affects money, compliance or eligibility), and write one question the
analyst should ask the stakeholder to resolve it.

Documents:
{context}
"""


def find_conflicts() -> ConflictReport:
    chunks = get_all_chunks()
    context = "\n\n".join(f"[{c['source']}]\n{c['text']}" for c in chunks)
    return llm.invoke(PROMPT.format(context=context))