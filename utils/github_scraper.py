import csv
from supabase import create_client, Client
from utils.api import GithubAPI

supa: Client = create_client(url, key)

#issues
#prs
#commits
# Status = Merged, Closed, Raised, Draft
# PR Link
# Author
# Comments