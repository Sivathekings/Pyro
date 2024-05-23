from pyrogram import Client, filters

Siva = Client(
    "pyrogrambot",
    api_id = "9978416",
    api_hash = "6dffe39cf4f3f43154619eb99b35b7db",
    bot_token = "7097262621:AAHuPb2VV-CxVA451in9rjBNA932woZZD2Y",
    plugins=dict(root="Siva")
)



print("bot is started")




async def main():
    async with Siva:
        await Siva.send_message(text="I am perfectly deployed")

Siva.run(main())
