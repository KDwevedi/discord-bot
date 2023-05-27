import os
from typing import Any
from supabase import create_client, Client
import dotenv

dotenv.load_dotenv("../.env")


class SupabaseInterface:
    def __init__(self, table=None) -> None:
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_KEY")
        self.table = table
        self.client: Client = create_client(self.supabase_url, self.supabase_key)
    
    def read(self, query_key, query_value, columns="*"):
        data = self.client.table(self.table).select(columns).eq(query_key, query_value).execute()
        #data.data returns a list of dictionaries with keys being column names and values being row values
        return data.data
        
    def update(self, update, query_key, query_value):
        data = self.client.table(self.table).update(update).eq(query_key, query_value).execute()
        return data.data

    def insert(self):
        pass
    def delete(self):
        pass
    
        
    
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

tester = SupabaseInterface('users').user_exists(476285280811483140)
print(tester)
# tester.add_user({
#     "discord_id": 476285280811483140,
#     "github_id": 74085496
# })