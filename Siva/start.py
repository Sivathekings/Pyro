from pyrogram import Client, filters 

@Client.on_message(filters.commamd("start"))
async def start_cmd(client, msg):
    await msg.reply_text("hello")
