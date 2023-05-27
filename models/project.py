import sys, os
sys.path.append('/home/kanavdwevedi/Desktop/discord-bot-for-c4gt/')
print(sys.path)
from utils.db import SupabaseInterface

class Project:
    def __init__(self, data=None, name=None) -> None:
        if name is not None:
            data = SupabaseInterface(table="projects").read(query_key="name",query_value=name)[0]
        self.name = data["name"]
        self.desc = data["description"]
        self.repository = data['repository']
        self.contributor = data['contributor']
        self.mentor = data['mentor']
        self.product = data['product']
        self.issue_page_url = data['issue_page_url']
    
    @classmethod
    def is_project(project_name):
        db_client = SupabaseInterface(table="projects")
        data = db_client.read(query_key="name", query_value=project_name)
        if len(data)==1:
            return True
        if len(data)>1:
            raise Exception("Project name should be unique but recieved multiple items for this name.")
        return False
    

        


# test = Project(name='test')