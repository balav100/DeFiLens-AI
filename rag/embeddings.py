"""
embeddings.py

Embedding engine for DeFiLens AI.

Uses SentenceTransformers to generate vector embeddings
for document chunks and user queries.
"""

from __future__ import annotations

from typing import List

import numpy as np
from sentence_transformers import SentenceTransformer


class EmbeddingEngine:
    """
    Wrapper around SentenceTransformer.
    Loads the model only once.
    """

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2"
    ):

        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

    # --------------------------------------------------

    def embed_documents(
        self,
        texts: List[str]
    ) -> np.ndarray:
        """
        Generate embeddings for document chunks.
        """

        embeddings = self.model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embeddings.astype("float32")

    # --------------------------------------------------

    def embed_query(
        self,
        query: str
    ) -> np.ndarray:
        """
        Generate embedding for a user query.
        """

        embedding = self.model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embedding.astype("float32")

    # --------------------------------------------------

    @property
    def dimension(self) -> int:
        """
        Embedding dimension.
        """

        return self.model.get_sentence_embedding_dimension()