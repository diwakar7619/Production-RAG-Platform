from .vector_store import CLIENT, COLLECTION_NAME
from typing import TypedDict


class SearchResult(TypedDict):
    text: str
    score: float


def search(query_embedding: list[float], limit: int = 5) -> list[SearchResult]:
    results = CLIENT.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=limit,
    ).points

    search_results: list[SearchResult] = []

    for result in results:
        payload = result.payload

        if payload is None:
            continue

        search_result: SearchResult = {
            "text": payload["text"],
            "score": result.score,
        }

        search_results.append(search_result)

    return search_results
