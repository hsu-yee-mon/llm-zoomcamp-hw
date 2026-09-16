# LLM Zoomcamp — Homework & Learning Portfolio

A collection of my hands-on homework and experiments from **[DataTalksClub LLM Zoomcamp 2026](https://github.com/DataTalksClub/llm-zoomcamp)**.

This repository documents my progression from building a basic **Retrieval-Augmented Generation (RAG)** system to working with **vector search, AI orchestration, retrieval evaluation, and LLM observability**.

The goal was not only to complete the assignments, but to understand the components and engineering practices behind production-oriented LLM applications.

---
## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-000000?style=for-the-badge&logo=opentelemetry&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)


## 🧠 What I Learned

Through the five homework modules, I worked through the following LLM application workflow:

```text
Documents
   ↓
Ingestion & Chunking
   ↓
Retrieval
   ├── Keyword Search
   ├── Vector Search
   └── Hybrid Search
   ↓
RAG
   ↓
Agents & Tool Calling
   ↓
Workflow Orchestration
   ↓
Evaluation
   ↓
Monitoring & Observability
```

This gave me practical experience with the main building blocks of modern RAG and LLM-powered applications.

---

# 📚 Homework Modules

## 01 — Agentic RAG

📁 [`module 1/`](./module%201)

The first module focused on understanding the foundations of **Retrieval-Augmented Generation** and extending a basic RAG pipeline into an agentic workflow.

### What I practiced

* Building a basic RAG pipeline
* Loading and parsing documents
* Document chunking
* Keyword-based retrieval
* Indexing documents with `minsearch`
* Connecting retrieved context to an LLM
* Prompt construction for RAG
* Function/tool calling
* Building an agentic loop
* Letting an LLM decide when to search for additional information
* Tracking LLM token usage and API cost

### Key concepts

**Traditional RAG**

```text
User Question
      ↓
Search
      ↓
Relevant Context
      ↓
LLM
      ↓
Answer
```

**Agentic RAG**

```text
User Question
      ↓
      LLM
       ↓
  Should I search?
     ↙       ↘
   Yes        No
    ↓          ↓
 Search      Answer
    ↓
New Context
    ↓
   LLM
    ↓
 Answer
```

### Skills developed

`RAG` · `Information Retrieval` · `Prompt Engineering` · `Function Calling` · `Agentic Workflows` · `Token/Cost Tracking`

### Main tools

* Python
* OpenAI API
* `minsearch`
* `tiktoken`
* GitHub lesson data

---

## 02 — Vector Search

📁 [`module_2/`](./module_2)

The second module focused on **semantic retrieval using embeddings** and understanding how vector search differs from traditional keyword search.

### What I practiced

* Generating text embeddings
* Converting documents and queries into vectors
* Computing semantic similarity
* Implementing vector search
* Comparing keyword search with vector search
* Working with top-K retrieval
* Combining keyword and semantic retrieval
* Implementing **Reciprocal Rank Fusion (RRF)**
* Working with lightweight local embedding models
* Exploring vector database concepts

### Retrieval approaches

```text
                 Retrieval
                    │
        ┌───────────┴───────────┐
        ↓                       ↓
 Keyword Search          Vector Search
        │                       │
 Exact / lexical          Semantic similarity
        │                       │
        └───────────┬───────────┘
                    ↓
              Hybrid Search
                    │
                   RRF
```

### Skills developed

`Embeddings` · `Semantic Search` · `Vector Search` · `Cosine Similarity` · `Hybrid Search` · `Reciprocal Rank Fusion`

### Main tools

* Python
* `minsearch`
* ONNX Runtime
* `all-MiniLM-L6-v2`
* NumPy
* SQLite/vector-search concepts

---

## 03 — AI Orchestration

📁 [`module_3/`](./module_3)

The third module moved from individual LLM calls toward **orchestrating complete AI workflows**.

I explored how RAG, agents, tools, and multiple LLM calls can be connected into repeatable workflows.

### What I practiced

* Designing multi-step LLM workflows
* Context engineering
* RAG-based workflows
* AI agents
* Tool calling
* Agent decision-making
* Workflow execution
* Multi-agent concepts
* Tracking token usage and cost
* Using external data/tools within AI workflows
* Persisting workflow state and context

### Workflow perspective

Instead of thinking about an LLM application as:

```text
Prompt → LLM → Answer
```

I learned to think in terms of:

```text
Input
  ↓
Context Preparation
  ↓
Retrieval / Tools
  ↓
LLM / Agent
  ↓
Decision
  ↓
Additional Tools
  ↓
Final Response
```

### Skills developed

`AI Orchestration` · `Context Engineering` · `Agents` · `Tool Calling` · `Multi-step Workflows` · `Workflow Automation`

### Main tools

* Python
* Kestra
* LLM APIs
* RAG components
* Docker

---

## 04 — RAG & Retrieval Evaluation

📁 [`module_4/`](./module_4)

This module was particularly important for understanding that **a retrieval system should be measured rather than evaluated only by intuition**.

The homework builds a ground-truth dataset and evaluates keyword, vector, and hybrid search using quantitative retrieval metrics. The official assignment specifically focuses on **Hit Rate and Mean Reciprocal Rank (MRR)**.

### What I practiced

* Generating evaluation questions using an LLM
* Structured LLM outputs
* Creating a ground-truth dataset
* Designing retrieval evaluation experiments
* Evaluating multiple retrieval strategies on the same dataset
* Measuring **Hit Rate**
* Measuring **MRR**
* Comparing keyword, vector, and hybrid retrieval
* Tuning RRF parameters
* Using experimental results to guide retrieval decisions

### Evaluation workflow

```text
Knowledge Base
      ↓
Generate Ground Truth
      ↓
┌──────────────────────────────┐
│       Retrieval Methods      │
│                              │
│  Keyword Search              │
│  Vector Search               │
│  Hybrid Search + RRF         │
└──────────────┬───────────────┘
               ↓
         Retrieved Results
               ↓
       Compare with Ground Truth
               ↓
        Hit Rate / MRR
               ↓
       Retrieval Comparison
```

### Key lesson

Instead of:

> "This retrieval method seems better."

I learned to ask:

> "How does this retrieval method perform according to the same evaluation dataset and metrics?"

### Skills developed

`LLM Evaluation` · `Retrieval Evaluation` · `Ground Truth Creation` · `Hit Rate` · `MRR` · `Experiment Design` · `RRF Tuning`

### Main tools

* Python
* LLM APIs
* Pydantic / structured outputs
* Pandas
* `minsearch`
* Vector search

---

## 05 — LLM Monitoring & Observability

📁 [`module_5/`](./module_5)

The fifth module focused on what happens **after an LLM application has been built and evaluated**: monitoring its behavior during actual usage.

### What I practiced

* Instrumenting LLM applications
* Capturing LLM traces
* Monitoring RAG pipelines
* Tracking input/output tokens
* Estimating LLM cost
* Measuring latency
* Storing telemetry data
* Querying monitoring data with SQL
* Building monitoring dashboards
* Using user feedback as an additional quality signal
* Understanding LLM-as-a-Judge evaluation
* Working with OpenTelemetry traces

### Observability workflow

```text
User Request
     ↓
RAG Application
 ┌───────────────┐
 │ Search        │
 │ Retrieval     │
 │ LLM           │
 └───────┬───────┘
         ↓
    Trace / Metrics
         ↓
 ┌───────────────────────┐
 │ Tokens                │
 │ Cost                  │
 │ Latency               │
 │ Retrieval information │
 │ User feedback         │
 └───────────┬───────────┘
             ↓
      Storage / Database
             ↓
      SQL / Dashboard
```

### Skills developed

`LLM Observability` · `OpenTelemetry` · `Tracing` · `Telemetry` · `Latency Monitoring` · `Cost Monitoring` · `SQL Analytics` · `LLM-as-a-Judge`

### Main tools

* Python
* OpenTelemetry
* SQLite
* SQL
* Streamlit
* Grafana
* LLM APIs

The official homework specifically introduces OpenTelemetry instrumentation, span attributes for token/cost/response-time information, SQLite-based trace storage, and dashboarding.

---

# 🛠️ Technical Skills

Across the homework, I gained hands-on experience with:

### LLM Application Development

* Retrieval-Augmented Generation (RAG)
* Agentic RAG
* LLM APIs
* Prompt engineering
* Context engineering
* Function/tool calling
* AI agents
* Multi-step workflows

### Information Retrieval

* Keyword search
* Semantic search
* Text embeddings
* Vector search
* Cosine similarity
* Hybrid search
* Reciprocal Rank Fusion (RRF)
* Top-K retrieval

### LLM Evaluation

* Ground-truth dataset creation
* Retrieval evaluation
* Hit Rate
* Mean Reciprocal Rank (MRR)
* Retrieval benchmarking
* Parameter tuning
* LLM-as-a-Judge

### LLMOps / Observability

* OpenTelemetry
* Distributed tracing concepts
* Token usage tracking
* Cost monitoring
* Latency monitoring
* SQLite telemetry storage
* SQL-based analysis
* Streamlit dashboards
* Grafana

### Engineering Tools

* Python
* Jupyter Notebooks
* Git & GitHub
* Docker
* Kestra
* ONNX Runtime
* SQLite
* Pandas
* Pydantic

---

# 🔄 My Learning Progression

The five modules helped me build an end-to-end mental model of an LLM application:

| Stage                    | What I Learned                                          |
| ------------------------ | ------------------------------------------------------- |
| **1. Build RAG**         | Retrieve context and generate grounded answers          |
| **2. Improve Retrieval** | Use embeddings and hybrid search                        |
| **3. Orchestrate**       | Connect LLMs, tools, agents, and workflows              |
| **4. Evaluate**          | Measure retrieval quality with quantitative metrics     |
| **5. Monitor**           | Observe cost, latency, traces, and application behavior |

In other words:

```text
              BUILD
                ↓
          RAG Application
                ↓
            RETRIEVE
                ↓
      Keyword + Vector Search
                ↓
           ORCHESTRATE
                ↓
        Agents + Tools + RAG
                ↓
            EVALUATE
                ↓
       Metrics + Ground Truth
                ↓
            MONITOR
                ↓
       Traces + Cost + Latency
```

This progression helped me understand LLM systems not just as **LLM + prompt**, but as software systems with multiple components that need to be **designed, evaluated, and monitored**.

---

# 📂 Repository Structure

```text
llm-zoomcamp-hw/
│
├── module 1/          # Agentic RAG
├── module_2/          # Vector Search
├── module_3/          # AI Orchestration
├── module_4/          # Evaluation
├── module_5/          # Monitoring
│
├── notes/             # Learning notes
│
├── main.py
├── pyproject.toml
├── Pipfile
└── README.md
```

---

# 🎯 Key Takeaways

The most important lessons I took from the course were:

### 1. RAG is a system, not just a prompt

A useful RAG application depends on the quality of its ingestion, chunking, retrieval, context construction, and generation.

### 2. Retrieval quality matters

Different retrieval strategies behave differently. Keyword, vector, and hybrid search should be evaluated on the same dataset rather than selected only based on intuition.

### 3. Agents add decision-making

An agent can decide when it needs additional information or tools instead of following a completely fixed pipeline.

### 4. Evaluation makes iteration measurable

Ground-truth datasets and retrieval metrics provide a way to compare changes systematically.

### 5. Production systems need observability

Even a system that performs well offline can have issues with latency, token consumption, cost, or user experience in real usage.

---

# 📌 About the Course

This repository was created while following **DataTalksClub's LLM Zoomcamp 2026**, a free hands-on course focused on building real-world LLM applications. The 2026 curriculum covers Agentic RAG, Vector Search, AI Orchestration, Evaluation, Monitoring, and a final project.

**Course:** [DataTalksClub LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp)

**My homework repository:** [hsu-yee-mon/llm-zoomcamp-hw](https://github.com/hsu-yee-mon/llm-zoomcamp-hw)
