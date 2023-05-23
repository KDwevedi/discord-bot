import requests
import os, sys


class GithubInterface:
    def __init__(self, owner, repo):
        self.owner = owner
        self.repo = repo
        self.headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': os.getenv("GithubPAT")
        }
    
    def get_commits(self):
        url =  f'https://api.github.com/repos/{self.owner}/{self.repo}/commits'
        return requests.get(url, headers=self.headers).json()
    
    def get_latest_commit(self):
        url =  f'https://api.github.com/repos/{self.owner}/{self.repo}/commits'
        return requests.get(url, headers=self.headers).json()[0]



owner = 'KDwevedi'
repo = 'btp'
url =  f'https://api.github.com/repos/{owner}/{repo}/commits'

# r = requests.get(url, headers=headers)
# # sys.stdout.write(r.text)
# print(r.json()[0]["commit"]["author"]["date"], r.json()[-1]["commit"]["author"]["date"])

print(GithubInterface(owner=owner,repo=repo).get_latest_commit())