"""
llm.py

LLM interface for DeFiLens AI
Uses Ollama + Custom RAG

Author: DeFiLens AI
"""

from __future__ import annotations

import json
import ollama

from rag.retriever import Retriever


class DeFiRiskAnalyzer:

    def __init__(
        self,
        retriever: Retriever,
        model: str = "gemma3:1b"
    ):

        self.retriever = retriever
        self.model = model

    # -------------------------------------------------------------

    def _build_prompt(
        self,
        question: str,
        context: str
    ) -> str:

        return f"""
You are a Senior Blockchain Security Auditor.

Your job is to analyze DeFi protocols ONLY using the retrieved documents.

IMPORTANT RULES

- Never use outside knowledge.
- Never hallucinate.
- If information is unavailable,
  respond with "Not found in retrieved documents."

Analyze carefully.

Retrieved Context

{context}

---------------------------------------------------------

User Question

{question}

---------------------------------------------------------

Return ONLY valid JSON.

Do NOT write markdown.

Do NOT explain anything outside JSON.

JSON Format

{{
    "risk_level": "",
    "summary": "",
    "potential_risks": [
        ""
    ],
    "mitigations": [
        ""
    ]
}}
"""

    # -------------------------------------------------------------

    def ask(
        self,
        question: str,
        top_k: int = 5
    ):

        # Retrieve ranked chunks
        retrieved = self.retriever.retrieve(
            question,
            top_k
        )

        # Build RAG context
        context = self.retriever.build_context(
            question,
            top_k
        )

        # Ask Ollama
        response = ollama.chat(

            model=self.model,

            messages=[

                {

                    "role": "user",

                    "content": self._build_prompt(
                        question,
                        context
                    )

                }

            ]

        )

        content = response["message"]["content"]

        # Parse JSON safely
        try:

            parsed = json.loads(content)

        except Exception:

            parsed = {

                "risk_level": "Unknown",

                "summary": content,

                "potential_risks": [],

                "mitigations": []

            }

        # ---------------------------------------------------------
        # Add REAL citations from Retriever
        # ---------------------------------------------------------

        sources = []

        seen = set()

        for item in retrieved:

            source = f"{item['file']} (Page {item['page']})"

            if source not in seen:

                seen.add(source)

                sources.append(source)

        parsed["sources"] = sources

        # ---------------------------------------------------------

        parsed["retrieved_documents"] = retrieved

        parsed["context"] = context

        return parsed