class User:
    def __init__(self,userData):
        #self.name = userData["name"]
        self.discordID = userData["discordID"]
        self.githubID = userData["githubID"]


class Contributor(User):
    def __init__(self, userData):
        super().__init__(userData)
        

class Mentor(User):
    def __init__(self, userData):
        super().__init__(userData)

class OrgMember(User):
    def __init__(self, userData):
        super().__init__(userData)

