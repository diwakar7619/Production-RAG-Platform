from app.document_processing.loader import load_document
from app.retrieval.chunker import chunk_document
from app.retrieval.embedder import embed_chunks
from app.retrieval.vector_store import store_embeddings
from app.retrieval.search import search
from app.retrieval.vector_store import CLIENT

text = load_document("data/sample.txt")

chunks = chunk_document(text)

embeddings = embed_chunks(chunks)

store_embeddings(chunks, embeddings)

print(f"Loaded text length: {len(text)}")

print(f"Chunks created: {len(chunks)}")

print(f"Embeddings created: {len(embeddings)}")

print("Embeddings stored successfully!")

query = "What is this document about?"

query_embedding = embed_chunks([query])[0]

results = search(query_embedding)

print("\nRetrieved Results:\n")

for i, result in enumerate(results, start=1):
    print(f"Result {i}")
    print(f"Score : {result['score']:.4f}")
    print(f"Text  : {result['text']}")
    print("-" * 50)

CLIENT.close()
