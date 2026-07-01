# 🤖 SHL AI Assistant

An AI-powered Retrieval-Augmented Generation (RAG) system that recommends the most relevant SHL assessments based on natural language queries.

---

# 🚀 Features

- 🔍 Semantic search over SHL assessment catalog  
- 🧠 AI-powered recommendations using Groq LLM (LLaMA 3)  
- 📦 Vector database using ChromaDB  
- 🤗 HuggingFace sentence-transformer embeddings  
- ⚡ FastAPI backend  
- 🌐 Deployment ready (Render / Railway / Streamlit)

---

# 🧠 Tech Stack

- Python  

- Streamlit (UI)  
- LangChain  
- ChromaDB  
- HuggingFace Transformers  
- Groq API (LLaMA 3)

---

# 📁 Project Structure

```
app/
│── main.py
│── llm.py
│── retriever.py
│── vector_store.py
│── load_catalog.py
│── rag_pipeline.py

data/
│── shl_product_catalog.json
```

---

# ⚙️ Setup Instructions

## 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

## 2️⃣ Create `.env` file
```
GROQ_API_KEY=your_api_key_here
```

## 3️⃣ Run locally (FastAPI version)
```bash
uvicorn app.main:app --reload
```

## 4️⃣ Run Streamlit UI (if enabled)
```bash
streamlit run streamlit_app.py
```

---

# 🌐 API Endpoints (FastAPI version)

- `/` → Home  
- `/health` → Health check  
- `/chat` → AI assistant endpoint  

---

# 🧪 Example Request

```json
POST /chat
{
  "query": "I need a python assessment for entry level candidates"
}
```

---

# 📊 Dataset

`data/shl_product_catalog.json`

---

# 🚀 Deployment (Render)

## Build Command
```bash
pip install -r requirements.txt
```

## Start Command
```bash
bash start.sh
```

## Health Check
```
/health
```

---

# 👨‍💻 Author

**Biswanath Bhyan**
```



