from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.orchestration.orchestrator import ask
from app.config import logger


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
    logger.info(f"Received question: {request.question}")
    try:
        answer = ask(request.question)

        return {"answer": answer}
    except Exception as e:
        logger.exception("RAG Pipeline failed")

        raise HTTPException(status_code=500, detail="Failed to process your question.")
