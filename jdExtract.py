from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers.json import JsonOutputParser
from utils.clean import clean_text
from templates.extractPattrens import jobDiscritionFormat


class JobDescriptionExtractor:
    def __init__(self, llm):
        self.llm = llm
        self.jsonParser = JsonOutputParser()

    def scrapeWebsite(self, url):
        loader = WebBaseLoader(web_path=url)
        response = loader.load()
        cleaned_response = clean_text(response[0].page_content)
        return cleaned_response

    def promptTemplate(self):
        return PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in following pattern {jobDiscritionFormat}
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )

    def extractJD(self, url: str):
        cleaned_response = self.scrapeWebsite(url)
        prompt_template = self.promptTemplate()
        json_parser = JsonOutputParser()

        chain = prompt_template | self.llm 
        jd_response = chain.invoke({
            "page_data": cleaned_response,
            "jobDiscritionFormat": jobDiscritionFormat
        })
        jd_response = self.jsonParser.parse(jd_response.content)
        return jd_response


# -----------------------> testing <-------------------------

# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# load_dotenv()
# GROQ_API = os.getenv("GROQ")
# llm = ChatGroq(temperature=0, groq_api_key=GROQ_API, model="llama-3.3-70b-versatile")
# jd = JobDescriptionExtractor(llm)
# jdRes = jd.extractJD("https://careers.nike.com/data-engineer/job/R-61137")
# jdRes
