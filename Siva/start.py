from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import asyncio
import random




START_BUTTON = [[
    InlineKeyboardButton("👨 Owner 👨", url="https://t.me/sivathe_king")
]]


@Client.on_message(filters.command("start"))
async def start_cmd(client, msg):
    PM_TEXT =f"""
Hello {msg.from_user.first_name} ⚡,
I am Shiva robot...
I am at construction. 
"""
    await msg.reply_photo(
        photo="https://telegra.ph/file/8ca45a14bf4a8788ae79b.jpg",
        caption = PM_TEXT,
        reply_markup=InlineKeyboardMarkup(START_BUTTON)
        
    )

