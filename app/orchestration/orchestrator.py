from app.retrieval.embedder import embed_query
from app.retrieval.search import search
from generation.prompt_builder import build_messages
from generation.generator import generate


def ask(question: str) -> str:
    query_embedding = embed_query(question)
    search_results = search(query_embedding)
    messages = build_messages(question, search_results)
    answer = generate(messages)
    return answer
