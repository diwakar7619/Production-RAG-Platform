from fastapi import FastAPI
from pydantic import BaseModel

from app.orchestration.orchestrator import ask


class QuestionRequest(BaseModel):
    question: str


app = FastAPI(
    title="Production RAG Platform",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/ask")
def ask_question(request: QuestionRequest):
    answer = ask(request.question)

    return {"answer": answer}
