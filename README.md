# 🎥 YouTube RAG Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about any YouTube video. The application extracts the video's transcript, retrieves the most relevant context using semantic search, and generates accurate answers using Google's Gemini model.

---

## 🚀 Features

- 🎥 Accepts any public YouTube video URL
- 📝 Retrieves video transcripts
- 🌍 Supports multiple transcript languages
- ✂️ Splits transcripts into semantic chunks
- 🔍 Context retrieval using ChromaDB and MMR
- 🤖 Answer generation using Gemini 2.5 Flash
- ⚡ FastAPI backend
- 🎨 Streamlit frontend
- 🐳 Dockerized application
- 🔄 GitHub Actions CI/CD pipeline
- 📦 Automatic Docker Hub image publishing

---

## 🏗️ Architecture

```
User
   │
   ▼
Streamlit Frontend
   │
   ▼
FastAPI Backend
   │
   ├── YouTube Transcript API
   │
   ├── Text Splitter
   │
   ├── HuggingFace Embeddings
   │
   ├── ChromaDB Vector Store
   │
   ├── MMR Retrieval
   │
   ▼
Gemini 2.5 Flash
   │
   ▼
Answer
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI
- Uvicorn

### RAG Pipeline
- LangChain
- ChromaDB
- HuggingFace Embeddings (`sentence-transformers/all-MiniLM-L6-v2`)
- Recursive Character Text Splitter
- Maximum Marginal Relevance (MMR)

### LLM
- Google Gemini 2.5 Flash

### DevOps
- Docker
- Docker Compose
- GitHub Actions
- Docker Hub

---

## 📂 Project Structure

```
YouTube_RAG_Assistant
│
├── backend/
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run Locally

### Clone the repository

```bash
git clone https://github.com/GauranshChauhan123/YouTube_RAG_Assistant.git
cd YouTube_RAG_Assistant
```

### Create virtual environment

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Run FastAPI

```bash
uvicorn backend.main:app --reload
```

Runs on

```
http://127.0.0.1:8000
```

---

### Run Streamlit

```bash
streamlit run frontend/app.py
```

Runs on

```
http://localhost:8501
```

---

## 🐳 Docker

Build and start the application

```bash
docker compose up --build
```

Run in detached mode

```bash
docker compose up -d --build
```

Stop containers

```bash
docker compose down
```

---

## 🔍 API Endpoints

### Health Check

```
GET /rag/health
```

### Ask Question

```
POST /rag/ask
```

Example Request

```json
{
  "video_url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "question": "What is Retrieval-Augmented Generation?",
  "language": "English"
}
```

---

## 🔄 CI/CD

The project uses **GitHub Actions** for Continuous Integration and Continuous Deployment.

Pipeline includes:

- Install dependencies
- Create `.env` from GitHub Secrets
- Build Docker containers
- Start application using Docker Compose
- Verify FastAPI health endpoint
- Verify Streamlit availability
- Push Docker images to Docker Hub

---

## 🧠 Retrieval Pipeline

1. Extract YouTube transcript
2. Split transcript into chunks
3. Generate embeddings
4. Store vectors in ChromaDB
5. Retrieve relevant chunks using MMR
6. Generate answer with Gemini 2.5 Flash

---


---

## 🔮 Future Improvements

- Conversation memory
- Streaming responses
- Chat history
- Multiple LLM support
- Hybrid search
- Authentication
- Deployment on cloud

---

## 👨‍💻 Author

**Gauransh Chauhan**

GitHub: https://github.com/GauranshChauhan123

---

## ⭐ If you found this project useful, consider giving it a star!