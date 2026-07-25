"""
vector_store.py

Custom FAISS Vector Store for DeFiLens AI

Responsibilities:
- Create FAISS index
- Store embeddings
- Save metadata
- Save/load index
- Perform similarity search
"""

from __future__ import annotations

import os
import pickle
from typing import List, Tuple

import faiss
import numpy as np

from ingestion.chunker import Chunk


class VectorStore:

    def __init__(self, dimension: int):

        self.dimension = dimension

        # Since embeddings are normalized,
        # Inner Product = Cosine Similarity
        self.index = faiss.IndexFlatIP(dimension)

        self.metadata: List[Chunk] = []

    # -------------------------------------------------

    def add(
        self,
        embeddings: np.ndarray,
        chunks: List[Chunk]
    ) -> None:

        if len(embeddings) != len(chunks):
            raise ValueError(
                "Embeddings and chunks must have same length."
            )

        embeddings = embeddings.astype("float32")

        self.index.add(embeddings)

        self.metadata.extend(chunks)

    # -------------------------------------------------

    def save(
        self,
        folder: str = "vectorstore"
    ) -> None:

        os.makedirs(folder, exist_ok=True)

        faiss.write_index(
            self.index,
            os.path.join(folder, "index.faiss")
        )

        with open(
            os.path.join(folder, "metadata.pkl"),
            "wb"
        ) as f:

            pickle.dump(
                self.metadata,
                f
            )

    # -------------------------------------------------

    @classmethod
    def load(
        cls,
        folder: str = "vectorstore"
    ) -> "VectorStore":

        index = faiss.read_index(
            os.path.join(folder, "index.faiss")
        )

        with open(
            os.path.join(folder, "metadata.pkl"),
            "rb"
        ) as f:

            metadata = pickle.load(f)

        store = cls(index.d)

        store.index = index

        store.metadata = metadata

        return store

    # -------------------------------------------------

    def search(
        self,
        query_embedding: np.ndarray,
        top_k: int = 5
    ) -> List[Tuple[Chunk, float]]:

        if query_embedding.ndim == 1:
            query_embedding = query_embedding.reshape(1, -1)

        query_embedding = query_embedding.astype("float32")

        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for score, idx in zip(
            scores[0],
            indices[0]
        ):

            if idx == -1:
                continue

            results.append(

                (
                    self.metadata[idx],
                    float(score)
                )

            )

        return results

    # -------------------------------------------------

    @property
    def total_chunks(self):

        return self.index.ntotal