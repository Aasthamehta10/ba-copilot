from fastapi import FastAPI
from pydantic import BaseModel
from app.retrieval.qa import answer

app = FastAPI(title="BA Copilot")


class Question(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask(body: Question):
    return {"question": body.question, "answer": answer(body.question)}