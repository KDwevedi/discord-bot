class Project:
    def __init__(self, data):
        self.name = data.name
        self.desc = data.description
        self.repo = data.repo
        self.mentors = data.mentors if data.mentors else []
        self.contributers = data.contributers if data.contributers else []
        self.channel = data.channels
        



