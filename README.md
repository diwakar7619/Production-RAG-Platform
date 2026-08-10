# 🚀 Production RAG Platform

> A production-oriented Retrieval-Augmented Generation (RAG) platform built with FastAPI, Sentence Transformers, Qdrant, and Groq.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-green.svg)](https://fastapi.tiangolo.com/)
[![Qdrant](https://img.shields.io/badge/Qdrant-Vector%20DB-red.svg)](https://qdrant.tech/)
[![Tests](https://img.shields.io/badge/Tests-8%20passed-brightgreen.svg)](#testing)
[![Status](https://img.shields.io/badge/Status-Production--Oriented-yellow.svg)](#current-status)

---

## 📖 Overview

The **Production RAG Platform** is a production-oriented document intelligence system that emphasizes engineering excellence over toy examples.

Instead of a simple chatbot, this project implements the entire RAG pipeline as real software: semantic retrieval, vector databases, modular APIs, error handling, logging, testing, and evaluation.

Every component has a defined responsibility. Every critical path is tested. Every decision is documented.

---

## 🎯 Goals

* ✅ Build a production-ready RAG backend
* ✅ Understand every stage of the RAG pipeline
* ✅ Apply software engineering best practices to AI systems
* ✅ Create a resume-worthy AI engineering portfolio project
* ✅ Produce reusable components for future AI applications

---

## 🛠️ Technology Stack

### Backend & API

* Python 3.11+
* FastAPI
* Pydantic (validation)
* uv (package manager)

### AI & Retrieval

* Sentence Transformers (`all-MiniLM-L6-v2`, 384-dim embeddings)
* Qdrant (vector database, cosine similarity)
* RecursiveCharacterTextSplitter (chunking)
* Groq (LLM generation)

### Data Processing

* PyMuPDF (PDF)
* python-docx (DOCX)
* LangChain (where appropriate)

### Quality & Operations

* pytest (testing)
* python-dotenv (environment config)
* Structured logging (built-in)

---

## 🏗️ Architecture

```
User Question
    │
    ▼
FastAPI + Pydantic Validation
    │
    ▼
Orchestrator (coordinates workflow)
    │
    ├─→ Query Embedder
    │
    ├─→ Qdrant Semantic Search
    │
    ├─→ Prompt Builder
    │
    └─→ Groq LLM Generator
    │
    ▼
Grounded Answer
```

### Design Principles

* **Modular:** Each component owns one responsibility
* **Testable:** Clear contracts between layers
* **Observable:** Logging at critical points
* **Resilient:** Error handling at API boundary
* **Replaceable:** Swap implementations without redesign

---

# 📂 Project Structure

```text
Production-RAG-Platform/

├── app/
│   ├── document_processing/
│   │   ├── loader.py          # Load PDF, TXT, DOCX
│   │   └── __init__.py
│   │
│   ├── orchestration/
│   │   ├── orchestrator.py     # Coordinates RAG workflow
│   │   └── __init__.py
│   │
│   ├── retrieval/
│   │   ├── chunker.py          # RecursiveCharacterTextSplitter
│   │   ├── embedder.py         # Sentence Transformers
│   │   ├── search.py           # Semantic search logic
│   │   ├── vector_store.py     # Qdrant wrapper
│   │   ├── qdrant_data/        # Local Qdrant storage
│   │   └── __init__.py
│   │
│   ├── utils/
│   │   ├── helpers.py
│   │   └── __init__.py
│   │
│   ├── config.py               # Configuration
│   ├── main.py                 # FastAPI app
│   └── __init__.py
│
├── generation/
│   ├── generator.py            # LLM calls
│   ├── prompt_builder.py       # Prompt construction
│   ├── rag_pipeline.py         # End-to-end pipeline
│   └── __init__.py
│
├── tests/
│   ├── test_api.py            # API contract tests
│   ├── test_chunker.py        # Chunking tests
│   └── test_prompt_builder.py # Prompt generation tests
│
├── data/
│   └── sample.txt             # Example document
│
├── .env.example
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

---

## 🔄 Request Flow

```
POST /ask { "question": "..." }
    │
    ▼
Pydantic validates input
    │
    ▼
Orchestrator.ask(question)
    │
    ├─ Embedder.embed(question)
    │  └─ Returns: vector (384-dim)
    │
    ├─ Qdrant.search(vector, top_k=3)
    │  └─ Returns: [chunk1, chunk2, chunk3]
    │
    ├─ PromptBuilder.build(question, chunks)
    │  └─ Returns: system_message, user_message
    │
    ├─ Groq.generate(messages)
    │  └─ Returns: answer
    │
    ▼
Return answer JSON
```

---

## 📥 Document Ingestion Pipeline

```
PDF / TXT / DOCX
    │
    ▼
DocumentLoader.load(file_path)
    │
    ▼
RecursiveCharacterTextSplitter.split(text)
    │  └─ chunk_size=500, chunk_overlap=50
    ▼
SentenceTransformer.encode(chunks)
    │  └─ 384-dimensional vectors
    ▼
Qdrant.upsert(vectors, payloads)
    │  └─ Stores chunks + metadata
    ▼
Ready for retrieval
```

---

# ⚙️ Local Setup

## Prerequisites

* Python 3.11+
* uv (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
* Groq API key (free at https://console.groq.com)

## Installation

```bash
# 1. Clone repository
git clone <YOUR_REPO_URL>
cd Production-RAG-Platform

# 2. Install dependencies
uv sync

# 3. Create .env file
cp .env.example .env
# Edit .env and add your GROQ_API_KEY

# 4. Run the API
uv run uvicorn app.main:app --reload
```

API available at: `http://127.0.0.1:8000`
Swagger docs: `http://127.0.0.1:8000/docs`

---

## 🌐 API Endpoints

### GET `/health`

Health check.

```bash
curl http://127.0.0.1:8000/health
```

Response:
```json
{
  "status": "healthy"
}
```

---

### POST `/ask`

Submit a question to the RAG pipeline.

```bash
curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"What is Retrieval-Augmented Generation?"}'
```

Request:
```json
{
  "question": "What is RAG?"
}
```

Response:
```json
{
  "answer": "Retrieval-Augmented Generation (RAG) is..."
}
```

---

# 🧪 Testing

Run all tests:
```bash
uv run pytest -v
```

Run specific test suites:
```bash
uv run pytest tests/test_chunker.py -v
uv run pytest tests/test_prompt_builder.py -v
uv run pytest tests/test_api.py -v
```

**Current Result:** ✅ **8 passed**

## Test Coverage

### Chunker Tests
* ✓ Returns a list
* ✓ Returns non-empty results
* ✓ Returns string chunks
* ✓ Long documents produce multiple chunks

### Prompt Builder Tests
* ✓ Returns expected message structure
* ✓ Contains system and user messages
* ✓ Includes retrieved context and question

### API Tests
* ✓ GET /health returns 200
* ✓ POST /ask returns an answer
* ✓ Pipeline failures produce controlled HTTP 500

---

## 🛡️ Error Handling

Pipeline failures are caught at the API boundary:

```python
try:
    answer = await orchestrator.ask(question)
except Exception as e:
    logger.error(f"Pipeline failed: {e}")
    return HTTPException(status_code=500, detail="Failed to process your question.")
```

Users receive:
```json
{
  "detail": "Failed to process your question."
}
```

Not Python tracebacks. Not internal implementation details.

---

# 📊 Current Status

| Capability | Status |
|-----------|--------|
| Document loading | ✅ |
| PDF support | ✅ |
| TXT support | ✅ |
| DOCX support | ✅ |
| Recursive chunking | ✅ |
| Embeddings (all-MiniLM-L6-v2) | ✅ |
| Qdrant vector storage | ✅ |
| Semantic retrieval | ✅ |
| Prompt construction | ✅ |
| LLM generation (Groq) | ✅ |
| Orchestration | ✅ |
| FastAPI | ✅ |
| Request validation | ✅ |
| Logging | ✅ |
| Error handling | ✅ |
| Automated tests | ✅ |
| Architecture documentation | ✅ |
| Screenshots | ⬜ |
| Public deployment | ⬜ |
| Formal RAG evaluation | ⬜ |
| Advanced observability | ⬜ |

---

# 🧠 Core Engineering Decisions

## 1. Recursive Character Chunking (500 / 50 overlap)

**Why:** Deterministic, preserves text boundaries, easy to test.

**Contract:** `text → list[str]`

**Benefit:** Implementation can change without rewriting retrieval.

---

## 2. Embedding Model: all-MiniLM-L6-v2 (384 dimensions)

**Why:** Lightweight, fast, sufficient quality for semantic search.

**Isolated in:** `app/retrieval/embedder.py`

**Benefit:** Swap model by changing one file.

---

## 3. Qdrant Vector Database

**Why:** Fast semantic search, persistent storage, handles metadata.

**Config:**
* Vector dimension: 384
* Distance metric: Cosine
* Storage: Local (Qdrant data folder)
* Collection: `documents`

---

## 4. Orchestrator Pattern

**Why:** Coordinates workflow without owning components.

**Owns:** Nothing (delegation only)
**Coordinates:** Embedding → Retrieval → Prompt → Generation

**Benefit:** Single place to understand query flow.

---

## 5. FastAPI at Application Boundary

**Why:** Clear separation of HTTP concerns from RAG logic.

**Owns:**
* HTTP requests/responses
* Request validation (Pydantic)
* Error handling
* Response formatting

**Benefit:** RAG components remain testable without HTTP.

---

## 6. Pydantic Request Validation

**Why:** Reject garbage early, clear input contracts.

**Schema:**
```python
class AskRequest(BaseModel):
    question: str
```

---

# 💡 Key Lessons

### 1. RAG is a Pipeline

```
Loading → Chunking → Embedding → Retrieval → Context → Generation
```

Every stage can fail. Every stage matters.

### 2. Retrieval ≠ Generation

Best LLM can't answer from chunks never retrieved.

Retrieval is an independent engineering problem.

### 3. Loose Coupling Wins

Separate components = easy to test, easy to swap, easy to scale.

### 4. Testing ≠ Evaluation

* **Tests:** Does the app work? (software contracts)
* **Evaluation:** Are answers good? (RAG quality)

Need both. Different problems.

### 5. Error Handling at Right Boundary

* Generator = generation
* API = HTTP
* Orchestrator = workflow

Prevents mixing concerns.

---

# 🔮 Roadmap

## Phase 1: Core RAG ✅
* Document ingestion
* Semantic retrieval
* LLM generation
* API endpoints
* Testing

## Phase 2: Production Engineering 🚧
* Docker containerization
* Deployment
* Advanced logging
* Structured observability
* Rate limiting & auth

## Phase 3: Evaluation & Quality
* Retrieval quality benchmark
* Answer relevance evaluation
* Faithfulness measurement
* Latency tracking
* Cost per query

## Phase 4: Advanced Features
* Hybrid BM25 + semantic search
* Reranking
* Metadata filtering
* Streaming responses
* Multi-tenant support

---

# 🎤 Interview Talking Points

### Architecture
* Why orchestrator? *(coordinates workflow, owns nothing)*
* Why separate retrieval from generation? *(loose coupling, testable)*
* What happens during `/ask`? *(full request flow)*

### Retrieval
* Why embeddings? *(semantic similarity vs keyword match)*
* Why 384 dimensions? *(balance quality vs speed)*
* What if wrong chunks retrieved? *(LLM can't fix missing context)*

### Testing
* Testing ≠ AI eval *(different problems)*
* Why mock orchestrator in API test? *(isolate HTTP layer)*

### Production
* How scale? *(managed Qdrant, load balancer, stateless APIs)*
* How add auth? *(middleware, JWT, role checks)*
* How monitor? *(structured logging, tracing, metrics)*

---

# 📈 Resume Bullet

**Production RAG Platform**

> Built production-oriented RAG API: FastAPI + Qdrant + Sentence Transformers + Groq. Implemented document ingestion, semantic retrieval, modular orchestration, error handling, request validation, logging, and automated testing.

---

# 📈 Scaling the Architecture

```
Clients
    │
    ▼
Load Balancer
    ├─→ FastAPI Instance 1
    ├─→ FastAPI Instance 2
    └─→ FastAPI Instance 3
    │
    ├─→ Managed Qdrant
    │
    └─→ Groq API
```

Stateless API instances scale horizontally. Vector DB and LLM are managed services.

---

# 🗂️ Future Enhancements

### Retrieval
* Hybrid BM25 + semantic search
* Reranking
* Metadata filtering
* Configurable top-k

### Generation
* Streaming responses
* Model provider switching
* Structured output

### Production Infrastructure
* Docker & Kubernetes
* CI/CD pipeline
* Managed Qdrant
* Authentication & authorization
* Rate limiting
* Request tracing

### Evaluation
* RAG quality dataset
* Retrieval relevance metrics
* Answer relevance metrics
* Faithfulness measurement
* Hallucination detection
* Latency benchmarking
* Token usage tracking
* Cost measurement

---

# 👨‍💻 Author

**Pratham Diwakar**

AI Engineer | GenAI | AI Application Engineering

Building production systems with:
* Python + FastAPI
* RAG + Vector Databases
* LLM Integration
* AI Agents

---

# ⭐ Philosophy

Not just: *"An LLM can answer a question."*

**But:** *"How do I build this as production software?"*

```
Data Flow
    ↓
Retrieval Architecture
    ↓
Generation Pipeline
    ↓
API Design
    ↓
Error Handling
    ↓
Observability
    ↓
Testing
    ↓
Evaluation
```

Each stage matters. Each stage is engineered. Each stage is production-ready.