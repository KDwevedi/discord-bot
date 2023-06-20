import os
from supabase import create_client, Client


class SupabaseInterface:
    def __init__(self, table, url=None, key=None) -> None:

        self.supabase_url = url if url else os.getenv("SUPABASE_URL")
        self.supabase_key = key if key else os.getenv("SUPABASE_KEY")
        self.table = table
        self.client: Client = create_client(self.supabase_url, self.supabase_key)
    
    def read(self, query_key, query_value, columns="*"):
        data = self.client.table(self.table).select(columns).eq(query_key, query_value).execute()
        #data.data returns a list of dictionaries with keys being column names and values being row values
        return data.data
    
    def read_all(self):
        data = self.client.table(self.table).select("*").execute()
        return data.data
        
    def update(self, update, query_key, query_value):
        data = self.client.table(self.table).update(update).eq(query_key, query_value).execute()
        return data.data

    def insert(self, data):
        data = self.client.table(self.table).insert(data).execute()
        return data.data
    def delete(self):
        pass
    

    def test(self):
        contributor = self.client.table("contributor_engagement").select("*").execute()
        print(contributor)
        comment_count = contributor.data[0]["github_comments"]
        data = self.client.table("contributor_engagement").update({"github_comments":comment_count+1}).eq("contributor_github",74085496).execute()
        return data
        
    
    def add_user(self, userdata):
        data = self.client.table("users").insert(userdata).execute()
        print(data.data)
        return data.data
    
    def user_exists(self, discord_id):
        data = self.client.table("users").select("*").eq("discord_id", discord_id).execute()
        if len(data.data)>0:
            return True
        else:
            return False
        



# tester = SupabaseInterface('users', url="https://kcavhjwafgtoqkqbbqrd.supabase.co",key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtjYXZoandhZmd0b3FrcWJicXJkIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODQ5NTQxMzIsImV4cCI6MjAwMDUzMDEzMn0.8PKGvntMY7kw5-wmvG2FBOCxf-OrA2yV5fnudeA6SVQ" )
# tester.test()
# print(tester)
# tester.add_user({
#     "discord_id": 476285280811483140,
#     "github_id": 74085496
# })