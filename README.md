# 📧 Cold Email Generator

A smart, LLM-powered tool that generates highly personalized **cold emails** based on a candidate’s resume and a job description link.

Built with **LangChain**, **Streamlit**, **ChromaDB**, and **LLM (Groq + LLaMA-3)**.

---

## 🚀 Features

- ✅ Extracts candidate info from **PDF or raw text**
- ✅ Scrapes job descriptions from **career page URLs**
- ✅ Matches **top projects** based on JD skills using vector similarity (ChromaDB)
- ✅ Embeds **GitHub/LinkedIn/Portfolio links** in the generated email
- ✅ Generates **professional, markdown-formatted cold emails**
- ✅ Streamlit-powered clean UI for easy interaction

---


## 🧠 Tech Stack

| Component          | Technology                |
|--------------------|---------------------------|
| Language Model     | [Groq + LLaMA-3 70B](https://groq.com) |
| Embedding & Vectors| [ChromaDB](https://www.trychroma.com/) |
| LLM Orchestration  | [LangChain](https://www.langchain.com) |
| UI Framework       | [Streamlit](https://streamlit.io/) |
| PDF Parsing        | LangChain PyPDFLoader     |

---


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/cold-email-generator.git
cd cold-email-generator
pip install -r requirements.txt
streamlit run app.py



