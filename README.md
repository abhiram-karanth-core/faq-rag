# PDF-based RAG Chat Application

A minimal Flask application that lets an **admin upload PDFs**, stores their embeddings in **Pinecone**, and allows **users to query the content** using a **Mistral LLM**.

---

## Features

* PDF upload and text extraction
* Chunking with page references
* Vector embeddings using Mistral
* Semantic search with Pinecone
* Context-aware Q&A via Mistral LLM

---

## Tech Stack

* **Backend**: Flask
* **LLM**: Mistral (`mistral-large-latest`)
* **Embeddings**: `mistral-embed`
* **Vector DB**: Pinecone
* **PDF Parsing**: PyPDF2

---

## Setup

### 1. Clone & Install

```bash
pip install flask python-dotenv PyPDF2 pinecone-client langchain-mistralai
```

### 2. Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_mistral_key
PINECONE_API_KEY=your_pinecone_key
```

Ensure the Pinecone index name in code exists:

```python
INDEX_NAME = ""
```

---

## Run

```bash
python app.py
```

App runs on: `http://localhost:5000`

---

## Routes

* `/` – Home page
* `/admin` – Upload PDFs (admin)
* `/user` – Ask questions (user)

---

## How It Works

1. Admin uploads a PDF
2. Text is extracted and chunked with page numbers
3. Chunks are embedded and stored in Pinecone
4. User query → embedding → Pinecone search
5. Retrieved context + query → Mistral LLM response

---

## Notes

* Supports out-of-context questions as well
* Conversation history is not persisted
* Designed for educational / demo use

---

