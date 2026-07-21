from numpy import ndarray
from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer("all-MiniLM-L6-v2")


def embed_chunks(chunks: list[str]) -> ndarray:
    return MODEL.encode(chunks)
