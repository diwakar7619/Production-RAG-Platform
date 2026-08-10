from app.retrieval.search import SearchResult
from generation.prompt_builder import build_messages


def test_build_messages_returns_messages():
    search_results: list[SearchResult] = [
        {"text": "RAG combines retrieval with generation.", "score": 0.9}
    ]

    messages = build_messages(
        question="What is RAG?",
        search_results=search_results,
    )

    assert isinstance(messages, list)
    assert len(messages) == 2


def test_build_messages_contains_system_and_user_messages():
    search_results: list[SearchResult] = [
        {"text": "RAG combines retrieval with generation.", "score": 0.9}
    ]

    messages = build_messages(
        question="What is RAG?",
        search_results=search_results,
    )

    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"


def test_build_messages_contains_context_and_question():
    search_results: list[SearchResult] = [
        {"text": "RAG combines retrieval with generation.", "score": 0.9}
    ]

    messages = build_messages(
        question="What is RAG?",
        search_results=search_results,
    )

    assert "RAG combines retrieval with generation." in messages[1]["content"]
    assert "What is RAG?" in messages[1]["content"]
