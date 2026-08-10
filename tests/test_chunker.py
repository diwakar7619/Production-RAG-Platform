from app.retrieval.chunker import chunk_document


def test_chunk_document_returns_list():
    text = "AI Engineering is awesome."

    chunks = chunk_document(text)

    assert isinstance(chunks, list)
    assert chunks
    assert all(isinstance(chunk, str) for chunk in chunks)


def test_long_document_produces_multiple_chunks():
    text = "AI Engineering " * 100

    chunks = chunk_document(text)

    assert len(chunks) > 1
