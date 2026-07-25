"""
chunker.py

Custom document chunker for DeFiLens AI.

Instead of splitting every N characters,
we preserve paragraph boundaries and metadata.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from typing import List

from ingestion.loader import Document


@dataclass
class Chunk:
    """
    Represents one semantic chunk.
    """

    chunk_id: str
    text: str
    source_file: str
    source_path: str
    page_number: int
    word_count: int
    character_count: int
    document_type: str


class Chunker:

    def __init__(
        self,
        max_words: int = 180,
        min_words: int = 40
    ):

        self.max_words = max_words
        self.min_words = min_words

    # ------------------------------------------------

    def chunk_documents(
        self,
        documents: List[Document]
    ) -> List[Chunk]:

        chunks: List[Chunk] = []

        for document in documents:

            chunks.extend(
                self._chunk_document(document)
            )

        return chunks

    # ------------------------------------------------

    def _chunk_document(
        self,
        document: Document
    ) -> List[Chunk]:

        paragraphs = self._split_paragraphs(
            document.text
        )

        chunks = []

        current_text = ""

        current_words = 0

        for paragraph in paragraphs:

            words = paragraph.split()

            if not words:
                continue

            paragraph_words = len(words)

            if current_words + paragraph_words <= self.max_words:

                current_text += "\n\n" + paragraph

                current_words += paragraph_words

            else:

                if current_words >= self.min_words:

                    chunks.append(

                        self._create_chunk(
                            current_text.strip(),
                            document
                        )

                    )

                    current_text = paragraph

                    current_words = paragraph_words

                else:

                    current_text += "\n\n" + paragraph

                    current_words += paragraph_words

        if current_text.strip():

            chunks.append(

                self._create_chunk(
                    current_text.strip(),
                    document
                )

            )

        return chunks

    # ------------------------------------------------

    def _split_paragraphs(
        self,
        text: str
    ) -> List[str]:

        paragraphs = []

        for p in text.split("\n\n"):

            p = p.strip()

            if p:

                paragraphs.append(p)

        return paragraphs

    # ------------------------------------------------

    def _detect_document_type(
        self,
        path: str
    ) -> str:

        path = path.lower()

        if "audit" in path:
            return "audit"

        if "exploit" in path:
            return "exploit"

        if "whitepaper" in path:
            return "whitepaper"

        if "governance" in path:
            return "governance"

        if "protocol" in path:
            return "protocol"

        return "general"

    def _create_chunk(
        self,
        text: str,
        document: Document
    ) -> Chunk:

        return Chunk(

            chunk_id=str(uuid.uuid4()),

            text=text,

            source_file=document.file_name,

            source_path=document.source,

            page_number=document.page_number,

            word_count=len(text.split()),

            character_count=len(text),

            document_type=self._detect_document_type(document.source)

        )