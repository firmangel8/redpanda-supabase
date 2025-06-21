"""Simple run simulation supabase"""


import os
from supabase import create_client, Client
import dotenv

dotenv.load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


# procedure to insert data
message_data = {
    "topic": "trpl-room",
    "message": "Hello",
    "sender": "pagedev-mac"
}
data = supabase.table("message_store").insert(message_data).execute()
len(data.data)
