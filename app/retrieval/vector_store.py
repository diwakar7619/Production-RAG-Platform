from qdrant_client import QdrantClient
from qdrant_client.http import models

CLIENT = QdrantClient(path="./qdrant_data")

if not CLIENT.collection_exists("documents"):
    CLIENT.create_collection(
        collection_name="documents",
        vectors_config=models.VectorParams(
            size=384,
            distance=models.Distance.COSINE,
        ),
    )
