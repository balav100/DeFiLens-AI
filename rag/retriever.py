"""
retriever.py

Retrieves the most relevant chunks from the FAISS vector store
using semantic similarity + document trust weighting.
"""

from __future__ import annotations

from typing import List, Dict

from rag.embeddings import EmbeddingEngine
from rag.vector_store import VectorStore


class Retriever:

    def __init__(
        self,
        vector_store: VectorStore,
        embedding_engine: EmbeddingEngine
    ):

        self.vector_store = vector_store
        self.embedding_engine = embedding_engine

    # -------------------------------------------------------------

    def _get_document_bonus(
        self,
        document_type: str
    ) -> float:
        """
        Assign trust bonus based on document type.
        """

        bonuses = {

            "audit": 0.20,

            "exploit": 0.15,

            "protocol": 0.05,

            "general": 0.00

        }

        return bonuses.get(document_type.lower(), 0.00)

    # -------------------------------------------------------------

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ) -> List[Dict]:

        query_embedding = self.embedding_engine.embed_query(
            query
        )

        results = self.vector_store.search(
            query_embedding,
            top_k=top_k
        )

        retrieved = []

        for chunk, similarity_score in results:

            trust_bonus = self._get_document_bonus(
                chunk.document_type
            )

            final_score = similarity_score + trust_bonus

            retrieved.append(

                {

                    "text": chunk.text,

                    "file": chunk.source_file,

                    "page": chunk.page_number,

                    "source": chunk.source_path,

                    "chunk_id": chunk.chunk_id,

                    "document_type": chunk.document_type,

                    "similarity_score": round(
                        similarity_score,
                        4
                    ),

                    "trust_bonus": round(
                        trust_bonus,
                        4
                    ),

                    "final_score": round(
                        final_score,
                        4
                    )

                }

            )

        retrieved.sort(

            key=lambda x: x["final_score"],

            reverse=True

        )

        for rank, item in enumerate(
            retrieved,
            start=1
        ):

            item["rank"] = rank

        return retrieved

    # -------------------------------------------------------------

    def build_context(
        self,
        query: str,
        top_k: int = 5
    ) -> str:

        retrieved = self.retrieve(
            query,
            top_k
        )

        context = ""

        for item in retrieved:

            context += f"""

[Document Type : {item['document_type']}]

[Source : {item['file']}]

[Page : {item['page']}]

{item['text']}

"""

        return context.strip()