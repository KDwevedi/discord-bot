import requests
import os, sys
import json


class GithubAPI:
    def __init__(self, owner, repo):
        self.owner = owner
        self.repo = repo
        self.headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': os.getenv("GithubPAT")
        }
    
    def get_repo_commits(self):
        url =  f'https://api.github.com/repos/{self.owner}/{self.repo}/commits'
        return requests.get(url, headers=self.headers).json()
    
    def get_latest_repo_commit(self):
        return self.get_commits()[0]
    
    def get_json(self, dict):
        return json.dumps(dict)
    
    def get_pull_requests(self, status):
        pass 

    def get_contributors(self):
        url = f'https://api.github.com/repos/{self.owner}/{self.repo}/contributors'
        return requests.get(url, headers=self.headers).json()




owner = 'KDwevedi'
repo = 'btp'
url =  f'https://api.github.com/repos/{owner}/{repo}/commits'

# r = requests.get(url, headers=headers)
# # sys.stdout.write(r.text)
# print(r.json()[0]["commit"]["author"]["date"], r.json()[-1]["commit"]["author"]["date"])
tester = GithubAPI(owner=owner,repo=repo)
print(tester.get_json(tester.get_contributors()))
