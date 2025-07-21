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
```
### Insert GROQAPI key from [here](https://groq.com/) in .env file
```bash
# .env
GROQ=your_groq_api_key_here
```

### 📧 Sample Cold Email (Generated)

```markdown
Subject: Application for Data Engineer Position

Dear Hiring Manager,

I am Gandluru Mohammed Yaseen, and I am excited to apply for the Data Engineer position at your esteemed organization. With a strong foundation in data-related occupations and a passion for working with cutting-edge technologies, I am confident that I would be an excellent fit for this role.

As a highly motivated and detail-oriented individual, I have gained valuable experience in my previous internship at Data Valley, where I implemented a Recommendation System for Movie Recommendations and proposed solutions using Machine Learning and Artificial Intelligence. My technical skills include proficiency in Python, PyTorch, TensorFlow, and experience with tools such as Serper API, BeautifulSoup, and Hugging Face models.

In addition to my technical expertise, I have also worked on several personal projects that demonstrate my capabilities in data engineering. Some of my notable projects include:

* Explicit Content Detection using Attention Mechanisms: I developed cutting-edge deep learning models using Vision Transformer (ViT) and Swin ViT for high-precision feature extraction. (GitHub: https://github.com/yaseeng-md/Explicit-Content-Detection)
* Audio Deepfake Detection: I proposed an advanced audio deepfake detection system using CNN, RNN, and LSTM architecture. (GitHub: https://github.com/yaseeng-md/Audio-DeepFake-Detection)
* Fine Tuning Llama Model for Website Article Summarization: I fine-tuned a LLaMA 2 7B model for automatic summarization of website articles.

I am excited about the opportunity to bring my skills and experience to a role where I can design and build simple, reusable components of larger processes or frameworks to support analytics products. I am confident that my strong work ethic, attention to detail, and ability to work collaboratively with cross-functional teams would make me a valuable asset to your organization.

You can find more information about my projects and experience on my GitHub profile: https://github.com/yaseeng-md. Unfortunately, I do not have a LinkedIn profile or personal website at this time. However, I can be reached at my email address: gandlurumohammedyaseen@gmail.com or my mobile number: 8328377285.

Thank you for considering my application. I look forward to the opportunity to discuss my qualifications further and learn more about your team's work.

Sincerely,
Gandluru Mohammed Yaseen
```



