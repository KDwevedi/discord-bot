import os
from typing import Any
from supabase import create_client, Client
import dotenv

dotenv.load_dotenv(".env")

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

class SupabaseInterface:
    def __init__(self, url, key) -> None:
        self.supabase_url = url
        self.supabase_key = key
        self.client = create_client(self.supabase_url, self.supabase_key)
    
    def add_user(self, userdata):
        data = self.client.table("users").insert(userdata).execute()
        print(data.data)
        return data

# tester = SupabaseInterface(url,key)
# tester.add_user({
#     "discord_id": 476285280811483140,
#     "github_id": 74085496
# })