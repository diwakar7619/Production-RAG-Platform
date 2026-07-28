from qdrant_client import QdrantClient
from qdrant_client.http import models

COLLECTION_NAME = "documents"

CLIENT = QdrantClient(path="./qdrant_data")

if not CLIENT.collection_exists(COLLECTION_NAME):
    CLIENT.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=384,
            distance=models.Distance.COSINE,
        ),
    )


def store_embeddings(chunks: list[str], embeddings):
    points = []

    for i in range(len(chunks)):
        point = models.PointStruct(
            id=i, vector=embeddings[i], payload={"text": chunks[i]}
        )
        points.append(point)

    CLIENT.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
    )
