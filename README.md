<div align="center">

# 🛡️ DeFiLens AI

### AI-Powered DeFi Risk Analyzer using Retrieval-Augmented Generation (RAG)

Analyze DeFi protocol risks using AI, semantic retrieval, and blockchain security documents.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?style=for-the-badge&logo=streamlit)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-green?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-LLM-black?style=for-the-badge)
![Sentence Transformers](https://img.shields.io/badge/SentenceTransformers-Embeddings-orange?style=for-the-badge)

</div>

---

# 📖 Overview

DeFiLens AI is an AI-powered blockchain security assistant that helps users understand the risks associated with Decentralized Finance (DeFi) protocols using Retrieval-Augmented Generation (RAG).

Unlike traditional chatbots that depend only on a Large Language Model (LLM), DeFiLens AI first retrieves relevant information from trusted blockchain documents—including protocol whitepapers, security audit reports, and exploit analyses—and then generates responses grounded in that retrieved evidence.

This approach significantly improves the relevance and explainability of AI-generated security insights.

---

# 🎯 Objectives

The primary objectives of this project are:

- Build a domain-specific RAG pipeline for blockchain security.
- Retrieve information from trusted security documents instead of relying solely on LLM knowledge.
- Improve answer reliability using metadata-aware document ranking.
- Provide explainable AI responses with document citations.
- Demonstrate an end-to-end AI application integrating semantic search and local LLM inference.

---

# ✨ Features

## 🤖 AI-Powered Risk Analysis

- DeFi protocol security assessment
- Smart contract risk explanation
- Security best-practice recommendations
- Executive summaries

---

## 📚 Retrieval-Augmented Generation (RAG)

- Semantic document search
- FAISS vector similarity search
- Context-aware AI responses
- Evidence-backed answers

---

## 🔍 Weighted Retrieval

Unlike traditional RAG systems, DeFiLens AI re-ranks retrieved documents based on their trustworthiness.

Priority order:

1. Security Audit Reports
2. Exploit Analysis Reports
3. Whitepapers
4. Governance Documents
5. General Documentation

This ensures that the AI primarily relies on trusted security sources.

---

## 📄 Supported Knowledge Sources

- DeFi Whitepapers
- Smart Contract Audit Reports
- Blockchain Security Documentation
- Exploit Reports
- Governance Documents
- Protocol Documentation

---

# 🏗️ Complete System Architecture

```text
                                   ┌───────────────────────────┐
                                   │     User Question         │
                                   └────────────┬──────────────┘
                                                │
                                                ▼
                                   ┌───────────────────────────┐
                                   │     Streamlit Frontend    │
                                   └────────────┬──────────────┘
                                                │
                                                ▼
                              ┌────────────────────────────────────┐
                              │      Query Processing Layer        │
                              │                                    │
                              │  • Input Validation                │
                              │  • Prompt Construction             │
                              │  • Query Embedding                 │
                              └────────────────┬───────────────────┘
                                               │
                                               ▼
                    ┌────────────────────────────────────────────────────┐
                    │              FAISS Vector Database                 │
                    │                                                    │
                    │  Embedded Semantic Chunks                          │
                    │                                                    │
                    │  ┌────────────────────────────────────────────┐    │
                    │  │ Chunk 1 │ Chunk 2 │ Chunk 3 │ Chunk N      │    │
                    │  └────────────────────────────────────────────┘    │
                    └───────────────────┬────────────────────────────────┘
                                        │
                                        ▼
                      ┌─────────────────────────────────────────────┐
                      │      Weighted Retriever                     │
                      │                                             │
                      │  • Semantic Similarity Search               │
                      │  • Metadata Ranking                         │
                      │  • Trust Score Adjustment                   │
                      │  • Top-K Selection                          │
                      └──────────────────┬──────────────────────────┘
                                         │
                                         ▼
                     ┌───────────────────────────────────────────────┐
                     │          Context Builder                      │
                     │                                               │
                     │ Merge Retrieved Chunks into One Prompt        │
                     └──────────────────┬────────────────────────────┘
                                        │
                                        ▼
                      ┌─────────────────────────────────────────────┐
                      │          Ollama LLM                         │
                      │                                             │
                      │  • JSON Mode                               │
                      │  • Risk Analysis                           │
                      │  • Summary                                 │
                      │  • Mitigation                              │
                      └──────────────────┬──────────────────────────┘
                                         │
                                         ▼
                    ┌────────────────────────────────────────────────┐
                    │             Streamlit UI                       │
                    │                                                │
                    │ • Risk Level                                  │
                    │ • Executive Summary                           │
                    │ • Potential Risks                             │
                    │ • Mitigation Strategies                       │
                    │ • Retrieved Sources                           │
                    │ • Retrieved Chunks                            │
                    └────────────────────────────────────────────────┘
```

---

# ⚙️ End-to-End RAG Workflow

```text
                PDF Documents
                     │
                     ▼
          Document Loader (PyMuPDF)
                     │
                     ▼
           Semantic Paragraph Chunking
                     │
                     ▼
 Sentence Transformer Embeddings (MiniLM)
                     │
                     ▼
          FAISS Vector Database
                     │
                     ▼
        Metadata-Aware Weighted Retrieval
                     │
                     ▼
          Context Construction
                     │
                     ▼
          Ollama Local Language Model
                     │
                     ▼
      Structured JSON Risk Assessment
                     │
                     ▼
        Streamlit Interactive Dashboard
```

---

# 📂 Project Structure

```text
DeFiLens-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── Dockerfile
├── docker-compose.yml
│
├── data/
│   ├── audits/
│   ├── exploits/
│   ├── governance/
│   ├── protocols/
│   └── whitepapers/
│
├── ingestion/
│   ├── __init__.py
│   ├── loader.py
│   ├── chunker.py
│   └── ingest.py
│
├── rag/
│   ├── __init__.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── llm.py
│
├── vectorstore/
│   ├── index.faiss
│   └── metadata.pkl
│
├── screenshots/
│
├── utils/
│
└── assets/
```

---

# 🧠 Core Technologies

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.11 |
| Frontend | Streamlit |
| LLM | Ollama |
| Embedding Model | Sentence Transformers |
| Vector Database | FAISS |
| PDF Processing | PyMuPDF |
| Retrieval | Weighted Semantic Retrieval |
| AI Technique | Retrieval-Augmented Generation |

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/balav100/DeFiLens-AI.git

cd DeFiLens-AI
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Major libraries used:

```
streamlit
sentence-transformers
faiss-cpu
PyMuPDF
numpy
pandas
ollama
scikit-learn
torch
transformers
```

or simply

```bash
pip install -r requirements.txt
```

---

# 🤖 Install Ollama

Download Ollama

https://ollama.com/download

Verify installation

```bash
ollama --version
```

---

## Pull a Language Model

Recommended:

```bash
ollama pull qwen2.5:3b
```

or

```bash
ollama pull gemma3:1b
```

---

## Start Ollama

```bash
ollama serve
```

Keep this terminal running.

---

# 📚 Preparing the Knowledge Base

Place PDF documents inside the **data** directory.

Example:

```
data/

├── audits/
│     aave_audit.pdf
│     uniswap_audit.pdf
│
├── exploits/
│     euler_hack.pdf
│     cream_finance.pdf
│
├── whitepapers/
│     aave_whitepaper.pdf
│     compound_whitepaper.pdf
│
├── governance/
│     governance.pdf
│
└── protocols/
      protocol_documentation.pdf
```

---

# 🧩 Build the Vector Database

Generate semantic chunks and embeddings.

```bash
python -m ingestion.ingest
```

This process will:

- Read every PDF
- Extract text
- Preserve paragraphs
- Generate semantic chunks
- Compute embeddings
- Store vectors in FAISS
- Save metadata

Expected output

```
Loading documents...

Creating chunks...

Generating embeddings...

Building FAISS index...

Saving vector database...

Completed Successfully
```

---

# ▶️ Running the Application

```bash
streamlit run app.py
```

Open

```
http://localhost:8501
```

---

# 🖥️ Application Overview

The interface contains

### Sidebar

- Number of Retrieved Chunks
- Analyze Button

---

### Main Panel

- Question Input
- Risk Level
- Executive Summary
- Potential Risks
- Mitigation Strategies
- Source Documents
- Retrieved Chunks

---

# 📸 Screenshots

## Home Screen

```
screenshots/home.png
```

---

## Risk Analysis

```
screenshots/result.png
```

---

## Retrieved Documents

```
screenshots/chunks.png
```

---

# 💬 Example Queries

## Example 1

```
Is Uniswap V3 secure?
```

Expected Output

- Risk Level

- Executive Summary

- Risks

- Mitigations

- Sources

---

## Example 2

```
Explain flash loan attacks.
```

---

## Example 3

```
Compare Aave and Compound security.
```

---

## Example 4

```
How can oracle manipulation attacks be prevented?
```

---

## Example 5

```
What vulnerabilities were identified during security audits?
```

---

## Example 6

```
Explain governance attacks in DeFi.
```

---

## Example 7

```
What caused the Euler Finance exploit?
```

---

# 🔎 Retrieval Process

When a user submits a question, the following operations occur.

```
User Question

↓

Sentence Transformer

↓

Query Embedding

↓

FAISS Similarity Search

↓

Top-K Retrieval

↓

Metadata Ranking

↓

Weighted Retrieval

↓

Context Builder

↓

LLM

↓

JSON Response

↓

Streamlit Dashboard
```

---

# 🧠 Why Retrieval-Augmented Generation?

Traditional LLMs

❌ May hallucinate

❌ Cannot cite sources

❌ May use outdated information

---

RAG

✅ Retrieves relevant documents

✅ Grounds responses in evidence

✅ Produces explainable answers

✅ Improves reliability

---

# 📈 Example Pipeline

```
Question

↓

Retriever

↓

Top 5 Chunks

↓

Context Builder

↓

Ollama

↓

Risk Assessment

↓

JSON Output

↓

Streamlit UI
```

---

# ⚙️ Configuration

### Change LLM

Open

```
rag/llm.py
```

Change

```python
model="gemma3:1b"
```

to

```python
model="qwen2.5:3b"
```

or

```python
model="llama3.2:3b"
```

---

### Change Retrieval Depth

Adjust

```python
top_k=5
```

or use the Streamlit slider.

Higher values

- Better context
- More documents
- Slightly slower

Lower values

- Faster
- More focused retrieval

---

# 📁 Generated Files

After ingestion

```
vectorstore/

index.faiss

metadata.pkl
```

These files contain

- Vector embeddings

- Metadata

- Chunk references

- Source information

Do not delete these unless rebuilding the knowledge base.

---

# 🧩 Project Modules

The project is divided into multiple independent modules to maintain scalability, readability, and ease of maintenance.

---

## 📂 Module 1 — Document Loader

**File**

```
ingestion/loader.py
```

### Responsibilities

- Scan the data directory
- Detect PDF files
- Extract text using PyMuPDF
- Preserve metadata
- Create Document objects

### Output

```
Document

├── file_name
├── source
├── page_number
└── text
```

---

## 📂 Module 2 — Semantic Chunker

**File**

```
ingestion/chunker.py
```

### Responsibilities

- Preserve paragraph boundaries
- Generate semantic chunks
- Maintain metadata
- Detect document type

Supported document categories

- Audit Reports
- Whitepapers
- Exploit Reports
- Governance Documents
- Protocol Documentation

---

## 📂 Module 3 — Embedding Generator

**File**

```
rag/embeddings.py
```

Uses

```
SentenceTransformer

all-MiniLM-L6-v2
```

Responsibilities

- Convert chunks into dense vectors
- Generate query embeddings
- Maintain semantic similarity

---

## 📂 Module 4 — Vector Store

**File**

```
rag/vector_store.py
```

Responsibilities

- Build FAISS index
- Save embeddings
- Store metadata
- Perform similarity search

Generated files

```
vectorstore/

index.faiss

metadata.pkl
```

---

## 📂 Module 5 — Weighted Retriever

**File**

```
rag/retriever.py
```

Responsibilities

- Semantic search
- Metadata-aware ranking
- Trust score adjustment
- Top-K retrieval

Unlike standard RAG systems, this retriever ranks security audit reports higher than general documentation.

---

## 📂 Module 6 — LLM Interface

**File**

```
rag/llm.py
```

Responsibilities

- Build prompts
- Query Ollama
- Parse JSON responses
- Generate explainable answers
- Attach citations

---

## 📂 Module 7 — Streamlit Application

**File**

```
app.py
```

Responsibilities

- Interactive UI
- Query input
- Display results
- Display citations
- Show retrieved chunks

---

# 🔍 Weighted Retrieval Strategy

Traditional RAG

```
Question

↓

Semantic Similarity

↓

Top-K Documents
```

DeFiLens AI

```
Question

↓

Semantic Similarity

↓

Metadata Ranking

↓

Trust Score

↓

Weighted Ranking

↓

Top-K Documents
```

Trust hierarchy

| Document Type | Priority |
|---------------|----------|
| Security Audit | ⭐⭐⭐⭐⭐ |
| Exploit Report | ⭐⭐⭐⭐ |
| Whitepaper | ⭐⭐⭐ |
| Governance | ⭐⭐ |
| General | ⭐ |

This approach increases the likelihood that retrieved evidence comes from authoritative security sources.

---

# 📊 Technology Stack

| Layer | Technology |
|---------|------------|
| Programming Language | Python 3.11 |
| User Interface | Streamlit |
| AI Model | Ollama |
| Embedding Model | Sentence Transformers |
| Vector Database | FAISS |
| PDF Parsing | PyMuPDF |
| Numerical Computing | NumPy |
| Data Processing | Pandas |
| Machine Learning | Scikit-Learn |
| Deep Learning Backend | PyTorch |

---

# 🐳 Docker Deployment

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

Run in background

```bash
docker compose up -d
```

Stop

```bash
docker compose down
```

---

# ☁️ Future Cloud Deployment

Possible deployment options

- AWS EC2
- Azure Virtual Machine
- Google Cloud VM
- Docker
- Kubernetes
- Streamlit Cloud (with hosted LLM)

---

# 📈 Future Enhancements

### Blockchain

- Live blockchain monitoring
- Smart contract scanning
- Wallet risk analysis
- Token reputation scoring

---

### Artificial Intelligence

- Graph RAG
- Hybrid Search
- Multi-Agent AI
- Agentic RAG
- Knowledge Graph integration

---

### Security

- Smart contract vulnerability detection
- CVE integration
- Automated exploit monitoring
- Continuous security updates

---

### User Experience

- Dark mode
- Authentication
- Report export (PDF)
- Chat history
- Multi-language support

---

# 📚 Skills Demonstrated

This project demonstrates practical experience in

- Retrieval-Augmented Generation (RAG)
- Large Language Models
- Semantic Search
- Vector Databases
- Information Retrieval
- Natural Language Processing
- Prompt Engineering
- Python Development
- AI Application Development
- Explainable AI
- Blockchain Security
- Streamlit Application Development
- Local LLM Deployment
- Software Engineering

---

# 💼 Resume Highlights

- Built an end-to-end Retrieval-Augmented Generation (RAG) application for DeFi risk analysis using Streamlit, FAISS, Sentence Transformers, and Ollama.
- Indexed blockchain whitepapers, audit reports, and exploit analyses into a semantic vector database for evidence-backed question answering.
- Implemented metadata-aware weighted retrieval to prioritize trusted security documents over general protocol documentation.
- Developed an interactive AI dashboard that generates structured risk assessments with supporting citations and retrieved context.

---

# ❓ Frequently Asked Questions

### Why RAG instead of only an LLM?

RAG grounds AI responses using retrieved documents, reducing hallucinations and improving answer reliability.

---

### Why FAISS?

FAISS enables efficient semantic similarity search across thousands of embedded document chunks.

---

### Why Sentence Transformers?

They convert text into semantic embeddings that capture contextual meaning beyond keyword matching.

---

### Why Ollama?

Ollama allows local execution of open-source language models without relying on external APIs.

---

### Why weighted retrieval?

Not all documents have the same reliability. Prioritizing audit reports and exploit analyses improves the quality of retrieved evidence.

---

# 🛠 Troubleshooting

## ModuleNotFoundError

Run modules from the project root:

```bash
python -m ingestion.ingest
```

---

## Ollama connection failed

Start the server:

```bash
ollama serve
```

---

## Model not found

Download the model:

```bash
ollama pull qwen2.5:3b
```

or

```bash
ollama pull gemma3:1b
```

---

## FAISS index missing

Rebuild the vector database:

```bash
python -m ingestion.ingest
```

---

## Streamlit won't start

Verify dependencies:

```bash
pip install -r requirements.txt
```

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

---

# 📄 License

This project is released under the **MIT License**.

You are free to use, modify, and distribute this project for educational and research purposes.

---

# 👨‍💻 Author

**Balasubramaniam V**

**GitHub**

https://github.com/balav100

**LinkedIn**

https://www.linkedin.com/in/balasubramaniam-v-280675359

---

# 🙏 Acknowledgements

This project builds upon the following open-source technologies:

- Streamlit
- Ollama
- FAISS
- Sentence Transformers
- PyMuPDF
- Hugging Face Transformers
- PyTorch
- NumPy
- Pandas

Special thanks to the open-source AI and blockchain communities for making these tools available.

---

<div align="center">

## ⭐ If you found this project useful, consider giving it a star!

**Made with ❤️ using Python, RAG, FAISS, Streamlit, and Ollama**

</div>
