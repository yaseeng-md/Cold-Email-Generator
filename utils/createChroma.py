import chromadb
import uuid
from itertools import chain


class ProjectVectorStore:
    def __init__(self, name, projects, jdSkills, numProjects = 3,storage_path="./chroma_storage"):
        self.projects = projects
        self.jdSkills = jdSkills
        self.numProjects = numProjects
        self.user_name = self._format_name(name)
        self.client = chromadb.PersistentClient(path=storage_path)
        self.collection = self.client.get_or_create_collection(name=f"projects_{self.user_name}")

    def _format_name(self, name: str) -> str:
        return name.lower().replace(" ", "_")
    
    def addDocuments(self):
        for project in self.projects:
            self.collection.add(
                documents = list(project["TechstackUsed"]),  
                metadatas = [{
                    "ProjectTitle": project["ProjectTitle"],
                    "description": project["description"],
                    "GitHub_Link": project["GitHub_Link"]
                    }] * len(project["TechstackUsed"]),
                    ids = [str(uuid.uuid4()) for _ in project["TechstackUsed"]])

    def _query(self):
        projectResponse = self.collection.query(query_texts = self.jdSkills)
        return projectResponse

    def retriveProjects(self):
        self.addDocuments()
        projectResponse = self._query()
        allProjects = list(chain.from_iterable(projectResponse["metadatas"]))
        seenProjectTitles = set()
        uniqueProjects = []
        for project in allProjects:
            title = project.get("ProjectTitle", "").strip()
            if title and title not in seenProjectTitles:
                seenProjectTitles.add(title)
                # Add only selected fields
                uniqueProjects.append({
                    "ProjectTitle": title,
                    "description": project.get("description", "").strip(),
                    "GitHub_Link": project.get("GitHub_Link", "").strip()
                })
            if len(uniqueProjects) == self.numProjects:
                break

        return uniqueProjects


