"""
llm.py

LLM interface for DeFiLens AI
Uses Ollama + Hybrid RAG
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
You are an expert Blockchain Security Auditor.

Use ONLY the retrieved context.
Never use outside knowledge.
Never hallucinate.

If information is unavailable, say:
"Not found in retrieved documents."

========================
RETRIEVED CONTEXT
========================

{context}

========================
USER QUESTION
========================

{question}

========================
OUTPUT FORMAT
========================

Return ONLY valid JSON.

{{
  "risk_level": "Low|Medium|High",

  "summary": "A concise 3-5 sentence executive summary.",

  "potential_risks": [
    "Risk 1",
    "Risk 2"
  ],

  "mitigations": [
    {{
      "type": "Testing",
      "priority": "High"
    }},
    {{
      "type": "Simulation",
      "priority": "Medium"
    }}
  ]
}}

Rules:
- If risk_level is Medium or High, include at least 2 potential_risks.
- mitigations MUST be an array of objects.
- Do not output markdown.
- Do not output explanations outside JSON.
"""

    # -------------------------------------------------------------

    def ask(
        self,
        question: str,
        top_k: int = 5
    ):

        retrieved = self.retriever.retrieve(
            question,
            top_k
        )

        context = self.retriever.build_context(
            question,
            top_k
        )

        prompt = self._build_prompt(
            question,
            context
        )

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

        try:
            parsed = json.loads(content)

        except Exception:
            parsed = {
                "risk_level": "Unknown",
                "summary": content,
                "potential_risks": [],
                "mitigations": []
            }

        parsed.setdefault("risk_level", "Unknown")
        parsed.setdefault("summary", "")
        parsed.setdefault("potential_risks", [])
        parsed.setdefault("mitigations", [])

        sources = []
        seen = set()

        for item in retrieved:
            source = f"{item['file']} (Page {item['page']})"

            if source not in seen:
                seen.add(source)
                sources.append(source)

        parsed["sources"] = sources
        parsed["retrieved_documents"] = retrieved
        parsed["context"] = context

        return parsed
