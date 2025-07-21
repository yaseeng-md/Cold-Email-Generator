import streamlit as st
import os
from dotenv import load_dotenv
from main import Pipeline
from langchain_groq import ChatGroq

# -----------------------------> Load Environment & Model <-----------------------------
load_dotenv()
GROQ_API = os.getenv("GROQ")
llm = ChatGroq(temperature=0, groq_api_key=GROQ_API, model="llama-3.3-70b-versatile")
pipeline = Pipeline(llm)

# -----------------------------> Streamlit Config <-----------------------------
st.set_page_config(page_title="Cold Email Generator", layout="centered")
st.title("📧 Cold Email Generator")
st.write("Generate a personalized cold email based on a resume and job description.")


# -----------------------------> Resume Input Section <-----------------------------
st.header("1. Candidate Information")
input_mode = st.radio("Select input method for resume:", ["Upload PDF", "Enter Text"], horizontal=True)
candidateInformation = None

if input_mode == "Upload PDF":
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    if uploaded_file is not None:
        os.makedirs("uploads", exist_ok=True)
        save_path = os.path.join("uploads", uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Saved file to {save_path}")
        try:
            candidateInformation = pipeline.extract_candidate_information(isPDF=True, path=save_path)
        except Exception as e:
            st.error(f"Error parsing resume: {e}")
else:
    resume_text = st.text_area("Paste your resume text here")
    if resume_text.strip():
        try:
            candidateInformation = pipeline.extract_candidate_information(isPDF=False, page_content=resume_text)
        except Exception as e:
            st.error(f"Error parsing resume: {e}")

# -----------------------------> Job Description Section <-----------------------------
st.header("2. Job Description")
jd_url = st.text_input("Paste Job Description URL here")
jd = None

if jd_url.strip():
    try:
        jdJson = pipeline.extract_job_description(jd_url)
    except Exception as e:
        st.error(f"Error extracting job description: {e}")

# -----------------------------> Generate Email Section <-----------------------------
st.header("3. Generate Cold Email")

if st.button("Generate Email"):
    if not candidateInformation:
        st.warning("Please provide your resume information first.")
    elif not jdJson:
        st.warning("Please enter a valid job description URL.")
    else:
        try:
            uniqueProjects = pipeline.createOrGetVDB(candidateInformation["BasicInfo"]["name"], candidateInformation["Projects"],jdJson["skills"])
            cold_email = pipeline.generateEmail(jdJson,candidateInformation,uniqueProjects)
            st.text_area("Cold Email", value=cold_email.strip(), height=250)
            st.code(cold_email.strip(), language="markdown")
            # st.success("✅ Cold email generated! Use the copy button on the code block above.")
        except Exception as e:
            st.error(f"Error generating cold email: {e}")
