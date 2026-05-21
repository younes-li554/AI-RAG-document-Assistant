



# 📄 AI Agentic Document Assistant (RAG System)

## 🚀 Overview

This project is an **AI-powered Document Assistant** built using **Retrieval-Augmented Generation (RAG)**.  
It allows users to upload PDF or TXT documents and ask questions based on the document content using **Google Gemini API** and **LangChain**.

The system retrieves relevant document chunks and generates accurate answers grounded in the uploaded data.

---

## 🧠 Features

- 📄 Upload PDF / TXT documents
- 🔍 Automatic text chunking
- 🧬 Embeddings generation
- 📦 Vector database (FAISS)
- 🤖 Gemini AI integration
- 💬 RAG-based question answering
- 🧪 Unit tests with pytest
- 🐳 Docker support (optional deployment)

---

## 🏗️ Architecture

```

User Question
↓
Retriever (FAISS Vector DB)
↓
Relevant Document Chunks
↓
Prompt Builder (LangChain)
↓
Gemini LLM
↓
Final Answer

````

---

## ⚙️ Tech Stack

- Python 3.11+
- Streamlit (UI)
- LangChain
- Google Gemini API
- FAISS (Vector Store)
- Pytest (Testing)
- Docker

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-document-assistant.git
cd ai-document-assistant
````

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app/main.py
```

---

## 🧪 Run Tests

```bash
pytest tests/
```

Expected output:

```text
2 passed
```

---

## 🐳 Run with Docker

### Build image:

```bash
docker build -t rag-assistant .
```

### Run container:

```bash
docker run -p 8501:8501 rag-assistant
```

---

## 📁 Project Structure

```
app/
 ├── main.py
 ├── rag/
 ├── utils/
tests/
 ├── test_loader.py
 ├── test_rag.py
sample.txt
requirements.txt
Dockerfile
README.md
```

---

## 🔐 Security Notes

* Never expose your API key in code
* Use `.env` file for secrets
* Do not push `.env` to GitHub

---

## 🧪 Example Usage

1. Upload a document (PDF or TXT)
2. Ask a question like:

```
What is this document about?
```

3. Get AI-generated answer based on document content

---

## 🧠 Future Improvements

* Chat memory (multi-turn context)
* PDF page citations
* Streaming responses
* FastAPI backend version
* Deployment (Render / Railway / AWS)

---

## 👨‍💻 Author

Built as a learning project for:

* RAG systems
* LangChain pipelines
* Gemini API integration

---

## 📜 License

MIT License

```

