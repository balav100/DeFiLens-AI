"""
loader.py

Responsible for loading documents from the knowledge base.

Supported formats:
- PDF
- Markdown
- TXT

Author: DeFiLens AI
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List
import fitz


@dataclass
class Document:
    """
    Represents a single loaded document.
    """

    file_name: str
    page_number: int
    text: str
    source: str


class DocumentLoader:
    """
    Loads documents from the data directory.
    """

    SUPPORTED_EXTENSIONS = {".pdf", ".md", ".txt"}

    def __init__(self, root_directory: str):

        self.root = Path(root_directory)

        if not self.root.exists():
            raise FileNotFoundError(
                f"{self.root} does not exist."
            )

    # ---------------------------------------

    def load_documents(self) -> List[Document]:

        documents: List[Document] = []

        files = list(self.root.rglob("*"))

        for file in files:

            if file.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
                continue

            if file.suffix.lower() == ".pdf":

                documents.extend(
                    self._load_pdf(file)
                )

            elif file.suffix.lower() == ".md":

                documents.append(
                    self._load_markdown(file)
                )

            elif file.suffix.lower() == ".txt":

                documents.append(
                    self._load_text(file)
                )

        return documents

    # ---------------------------------------

    def _load_pdf(
        self,
        path: Path
    ) -> List[Document]:

        pdf = fitz.open(path)

        pages = []

        for page_index in range(len(pdf)):

            page = pdf.load_page(page_index)

            text = page.get_text()

            if text.strip():

                pages.append(

                    Document(

                        file_name=path.name,

                        page_number=page_index + 1,

                        text=text,

                        source=str(path)

                    )

                )

        pdf.close()

        return pages

    # ---------------------------------------

    def _load_markdown(
        self,
        path: Path
    ) -> Document:

        text = path.read_text(
            encoding="utf-8"
        )

        return Document(

            file_name=path.name,

            page_number=1,

            text=text,

            source=str(path)

        )

    # ---------------------------------------

    def _load_text(
        self,
        path: Path
    ) -> Document:

        text = path.read_text(
            encoding="utf-8"
        )

        return Document(

            file_name=path.name,

            page_number=1,

            text=text,

            source=str(path)

        )