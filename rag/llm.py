"""
llm.py

LLM interface for DeFiLens AI
Uses Ollama + Custom RAG

Features
--------
- Native Ollama JSON mode
- Weighted RAG retrieval
- Robust JSON parsing
- Automatic citation generation
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
        # Recommended:
        # model: str = "qwen2.5:3b"
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
You are an expert Blockchain Security Auditor.

Answer ONLY using the retrieved context.

STRICT RULES

1. Never use outside knowledge.
2. Never hallucinate.
3. If information is unavailable, state:
   "Not found in retrieved documents."

Retrieved Context
-----------------

{context}

----------------------------------------------------

User Question

{question}

----------------------------------------------------

Return a JSON object with exactly these fields:

{{
    "risk_level": "Low | Medium | High",
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

        # -------------------------------
        # Retrieve evidence
        # -------------------------------

        retrieved = self.retriever.retrieve(
            question,
            top_k
        )

        # -------------------------------
        # Build context
        # -------------------------------

        context = self.retriever.build_context(
            question,
            top_k
        )

        prompt = self._build_prompt(
            question,
            context
        )

        # -------------------------------
        # Query Ollama in JSON mode
        # -------------------------------

        response = ollama.chat(

            model=self.model,

            format="json",

            messages=[

                {

                    "role": "user",

                    "content": prompt

                }

            ]

        )

        content = response["message"]["content"].strip()

        # -------------------------------
        # Parse JSON
        # -------------------------------

        try:

            parsed = json.loads(content)

        except Exception as e:

            print("\n========== JSON ERROR ==========")
            print(e)
            print("\nRaw model output:\n")
            print(content)
            print("================================\n")

            parsed = {

                "risk_level": "Unknown",

                "summary": content,

                "potential_risks": [],

                "mitigations": []

            }

        # -------------------------------
        # Ensure required keys exist
        # -------------------------------

        parsed.setdefault("risk_level", "Unknown")
        parsed.setdefault("summary", "")
        parsed.setdefault("potential_risks", [])
        parsed.setdefault("mitigations", [])

        # -------------------------------
        # Build citations
        # -------------------------------

        sources = []
        seen = set()

        for item in retrieved:

            source = f"{item['file']} (Page {item['page']})"

            if source not in seen:

                seen.add(source)
                sources.append(source)

        # -------------------------------
        # Add metadata
        # -------------------------------

        parsed["sources"] = sources
        parsed["retrieved_documents"] = retrieved
        parsed["context"] = context

        return parsed
