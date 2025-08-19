# 🚀 AskLearn — Chat with Your PDFs (RAG)

AskLearn lets you upload a PDF and ask questions in a sleek Streamlit UI.  
Under the hood, it uses **LlamaIndex** with **Google Gemini Embeddings** to build a local vector index, then routes your question to your configured LLM to generate grounded answers.

---

## 🔗 Run the App 
  👉 **Live Demo:** https://arpitasingh1199-asklearn.streamlit.app

---

## ✨ Features
- 📄 PDF upload → automatic ingestion & embedding
- 🔎 Retrieval-Augmented Generation (RAG) over your docs
- 🧠 Gemini Embeddings 
- 💾 Local persistent index (`./local_db`)
- 🎬 Futuristic UI (particles + UFOs), **Vladimir** as the AI avatar
- 🧩 Sidebar toggle for immersive chat

---

## 🧰 Tech Stack 
- **UI**: Streamlit
- **RAG Orchestration**: LlamaIndex 
- **Embeddings**: Google Gemini 
- **LLM**
- **Persistence**: LlamaIndex local storage 
