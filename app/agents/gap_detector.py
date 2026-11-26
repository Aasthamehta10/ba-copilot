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
rules, numbers, limits, eligibility conditions or permissions for the same topic.
Check each requirement in the newer document against the older one, including
yes/no rules such as who is allowed or not allowed.
Only report real conflicts supported by the text.Report each conflict as a separate entry, covering exactly one rule or number.
Never combine two different rules into one entry. Do not invent any.
For each conflict, quote the exact statement from each document, rate severity using these definitions:
- high: changes who qualifies or how much money is involved (eligibility limits, credit rules, approval limits, compliance)
- medium: changes the process or the customer's effort (processing time, required documents, workflow steps)
- low: wording or naming differences that do not change any decision, and write one question the
analyst should ask the stakeholder to resolve it. The question must name both
values and both documents, for example: "Should the minimum credit score be 700
(old policy) or 650 (new BRD)?"
Documents:
{context}
"""


def find_conflicts() -> ConflictReport:
    chunks = get_all_chunks()
    context = "\n\n".join(f"[{c['source']}]\n{c['text']}" for c in chunks)
    return llm.invoke(PROMPT.format(context=context))