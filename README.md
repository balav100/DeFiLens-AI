# 🛡️ DeFiLens AI
### AI-Powered DeFi Risk Analyzer using Retrieval-Augmented Generation (RAG)

DeFiLens AI is an intelligent blockchain security assistant that analyzes DeFi protocol risks using Retrieval-Augmented Generation (RAG). Instead of relying solely on a Large Language Model (LLM), the system retrieves relevant information from protocol whitepapers, security audit reports, and exploit analyses before generating a context-aware response.

The project demonstrates how RAG can improve the reliability of AI-generated answers in the blockchain and decentralized finance (DeFi) domain.

---

## 📌 Features

- 📄 Upload and index DeFi security documents
- 🔍 Semantic search using Sentence Transformers
- 📚 FAISS Vector Database for fast retrieval
- ⭐ Weighted Retrieval based on document trust
- 🤖 AI-powered risk analysis using Ollama
- ⚠️ Risk categorization (Low / Medium / High)
- 🛡️ Security mitigation recommendations
- 📖 Explainable AI with retrieved evidence
- 💻 Interactive Streamlit dashboard

---

# System Architecture

```

+-----------------------+
| PDF Documents |
| |
| Whitepapers |
| Audit Reports |
| Exploit Reports |
+----------+------------+
|
v
+-----------------------+
| Document Loader |
+----------+------------+
|
v
+-----------------------+
| Semantic Chunker |
+----------+------------+
|
v
+-----------------------+
| SentenceTransformer |
| Embeddings |
+----------+------------+
|
v
+-----------------------+
| FAISS Vector Store |
+----------+------------+
|
v
+-----------------------+
| Weighted Retriever |
+----------+------------+
|
v
+-----------------------+
| Ollama LLM |
+----------+------------+
|
v
+-----------------------+
| Risk Analysis |
| |
| Risk Level |
| Mitigations |
| Sources |
+-----------------------+
