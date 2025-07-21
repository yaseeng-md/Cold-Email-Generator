from langchain_community.document_loaders import PyPDFLoader
from templates.extractPattrens import resumeExtractFormat
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers.json import JsonOutputParser

class UserInformationExtractor:
    def __init__(self, llm):
        self.llm = llm
        self.prompt_template = PromptTemplate.from_template(
            """
            The Resume information is {page_content}
            You are a smart assistant, and I have provided you a text.
            Your task is to return me details in format of {resumeExtractFormat} and for discription include the summary of discription of that project with numerical results avilable.
            Return strictly in JSON format, and if anything is unknown placeholder is "None".
            If there are many projects, append them in a list of JSON. 
            NO PREAMBLE
            """
        )
        self.parser = JsonOutputParser()

    def extract_from_pdf(self, path: str) -> dict:
        loader = PyPDFLoader(path)
        pages = loader.load()
        page_content = pages[0].page_content
        return self._extract(page_content)

    def extract_from_text(self, text: str) -> dict:
        return self._extract(text)

    def _extract(self, page_content: str) -> dict:
        chain = self.prompt_template | self.llm
        response = chain.invoke({
            "page_content": page_content,
            "resumeExtractFormat": resumeExtractFormat
        })
        return self.parser.parse(response.content)


# candidateInformationExtractrorPy = UserInformationExtractor(llm)
# candidateInformation = candidateInformationExtractrorPy.extract_from_pdf("E:/Resumes/Specalized Resume.pdf") 
# candidateInformation
