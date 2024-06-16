from pyrogram import Client, filters

Siva = Client(
    "pyrogrambot",
    api_id = "9978416",
    api_hash = "6dffe39cf4f3f43154619eb99b35b7db",
    bot_token = "7186790371:AAHM60ncHHzF-0ulcOT6TkOt8vKk509conA",
    plugins=dict(root="Siva")
)



print("bot is started")




if __name__ == "__main__":
    with Siva:
        Siva.send_message(
            chat_id = -4283612947,
            text="I am perfectly deployed"
        )

Siva.run()
