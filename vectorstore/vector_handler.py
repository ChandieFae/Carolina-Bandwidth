## vectorstore/vector_handler.py
import faiss
import numpy as np
import os

index_path = os.getenv("VECTOR_DB_PATH", "./data/vector.index")

if os.path.exists(index_path):
    index = faiss.read_index(index_path)
else:
    index = faiss.IndexFlatL2(512)  # Assume 512-dim embeddings


def embed_text(text: str) -> np.ndarray:
    # Dummy embedder - replace with real model like SentenceTransformer
    np.random.seed(abs(hash(text)) % 2**32)
    return np.random.rand(512).astype('float32')


def add_to_vector_store(text: str):
    vector = embed_text(text)
    index.add(np.array([vector]))
    faiss.write_index(index, index_path)
    return {"status": "added", "dim": vector.shape[0]}


def search_vector_store(query: str, k=3):
    query_vector = embed_text(query)
    D, I = index.search(np.array([query_vector]), k)
    return {"matches": I[0].tolist(), "distances": D[0].tolist()}
