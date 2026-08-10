from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_ask_returns_answer(monkeypatch):
    def fake_ask(question: str) -> str:
        return "Test answer"

    monkeypatch.setattr("app.main.ask", fake_ask)

    response = client.post(
        "/ask",
        json={"question": "What is RAG?"},
    )

    assert response.status_code == 200
    assert response.json() == {"answer": "Test answer"}


def test_ask_handles_pipeline_failure(monkeypatch):
    def fake_ask(question: str) -> str:
        raise RuntimeError("Simulated pipeline failure")

    monkeypatch.setattr("app.main.ask", fake_ask)

    response = client.post(
        "/ask",
        json={"question": "What is RAG?"},
    )

    assert response.status_code == 500
    assert response.json() == {
        "detail": "Failed to process your question."
    }
