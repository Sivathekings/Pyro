from pyrogram import Client, filters
import os 


API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
TOKEN = os.getenv("TOKEN")

Siva = Client(
    "pyrogrambot",
    api_id = "API_ID",
    api_hash = "API_HASH",
    bot_token = "TOKEN",
    plugins=dict(root="Siva")
)



print("bot is started")
Siva.run()

