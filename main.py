from pyrogram import Client, filters

Siva = Client(
    "pyrogrambot",
    api_id = "9978416",
    api_hash = "6dffe39cf4f3f43154619eb99b35b7db",
    bot_token = "7186790371:AAHM60ncHHzF-0ulcOT6TkOt8vKk509conA",
    plugins=dict(root="Siva")
)



print("bot is started")
Siva.run()
