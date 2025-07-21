from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from utils.createChroma import ProjectVectorStore
from jdExtract import JobDescriptionExtractor
from candidateInformationExtractor import UserInformationExtractor

class Pipeline:
    def __init__(self, llm):
        self.llm = llm

    # -------------------> Extraction Methods <-------------------

    def extract_candidate_information(self, isPDF: bool, page_content: str = None, path: str = None):
        extractor = UserInformationExtractor(self.llm)

        if isPDF:
            if not path:
                raise ValueError("PDF path is missing.")
            candidateInformation =  extractor.extract_from_pdf(path) 
        else:
            if not page_content:
                raise ValueError("Resume text is missing.")
            candidateInformation =  extractor.extract_from_text(page_content)
        # print(candidateInformation)
        return candidateInformation


    def extract_job_description(self, url: str):
        jd = JobDescriptionExtractor(self.llm)
        jdJson = jd.extractJD(url)
        # print(jdJson)
        return jdJson

    # -------------------> Chroma Vector DB <-------------------

    def createOrGetVDB(self, name, projects, jdSkills, numProjects = 3):
        chroma = ProjectVectorStore(name, projects, jdSkills,numProjects)
        uniqueProjects = chroma.retriveProjects()
        # print(uniqueProjects)
        return uniqueProjects

    # -------------------> Email Generation <-------------------

    def generateEmailPrompt(self):
        prompt = """
        ## Job Discription: {jdJson}
        ## Candidate Information
        Your name is {name} and your job is to write an cold email asking for Job asking. You have a previous experince as {experinece}.
        These are basic details {BasicInfo}, your projects are {projects}, and skills is {skills}.
        Express your projects at same place, and include github links if any.
        Include your qualifications, so that you can get a job. Maintian formal speech tone across mail. And add links to contact like LinkedinLink, GitHub and personal website if any. 
        ## NO PREAMBLE
        """

        return PromptTemplate.from_template(prompt)

    def generateEmail(self,jdJson,jsonCandidate,projects):
        mail_prompt = self.generateEmailPrompt()
        mailLLM = mail_prompt | self.llm
        mailRes = mailLLM.invoke(input={"jdJson":jdJson, "name" : jsonCandidate["BasicInfo"]["name"] ,"experinece" : jsonCandidate["Experience"], 
                     "BasicInfo" : jsonCandidate["BasicInfo"], "projects" : projects, "skills" : jsonCandidate["Skills"] }) 
        return mailRes.content