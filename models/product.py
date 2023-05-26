class Product:
    def __init__(self, data:dict):
        #Name of the product
        self.name = data["name"]
        #Description of the product
        self.desc = data["desc"]
        #Organisation associated with the product
        self.org = data["org"]
        #The wili page url for the product on C4GT github
        self.wiki_url = data["wiki_url"]
        #Projects under this product
        self.projects = data["projects"]
        #Mentors assigned to projects associated with this product
        self.mentors = data["mentors"] if data["mentors"] else []
        #Contributors assigned to projects under this product
        self.contributers = data["contibutors"] if data["contributers"] else []
        #discord channel id of the dedicated discord channel for this Product
        self.channel = data["channel"]
        



