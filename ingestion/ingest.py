"""
ingest.py

Builds the FAISS vector database.

Steps

1. Load documents
2. Chunk documents
3. Generate embeddings
4. Store vectors
5. Save FAISS index
"""

from ingestion.loader import DocumentLoader
from ingestion.chunker import Chunker
from rag.embeddings import EmbeddingEngine
from rag.vector_store import VectorStore


def main():

    print("=" * 60)
    print("Loading documents...")
    print("=" * 60)

    loader = DocumentLoader("data")

    documents = loader.load_documents()

    print(f"Loaded {len(documents)} document pages.")

    print("\nChunking documents...")

    chunker = Chunker(
        max_words=180,
        min_words=40
    )

    chunks = chunker.chunk_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("\nGenerating embeddings...")

    embedding_engine = EmbeddingEngine()

    embeddings = embedding_engine.embed_documents(
        [chunk.text for chunk in chunks]
    )

    print("Embeddings generated.")

    print("\nBuilding FAISS index...")

    store = VectorStore(
        embedding_engine.dimension
    )

    store.add(
        embeddings,
        chunks
    )

    store.save()

    print("\nVector database saved successfully!")

    print(f"\nTotal Chunks Indexed : {store.total_chunks}")

    print("=" * 60)


if __name__ == "__main__":
    main()