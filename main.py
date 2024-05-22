from pyrogram import Client, filters

Siva = Client(
    "pyrogrambot",
    api_id = "9978416",
    api_hash = "6dffe39cf4f3f43154619eb99b35b7db",
    bot_token = "6829475237:AAGl3867Iv_Hji268Z7ML9-VnfnFN77-Ue0",
    plugins=dict(root="Siva")
)



print("bot is started")
Siva.run()
