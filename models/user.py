class User:
    def __init__(self,userData):
        #self.name = userData["name"]
        self.discordId = userData["discordId"]
        self.discordUserName = userData("discordUserName")
        self.githubId = userData["githubId"]


class Contributor(User):
    def __init__(self, userData):
        super().__init__(userData)
        

class Mentor(User):
    def __init__(self, userData):
        super().__init__(userData)

class OrgMember(User):
    def __init__(self, userData):
        super().__init__(userData)
