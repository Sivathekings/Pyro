from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import asyncio
import random


PM_TEXT = f"""
Hello {msg.from_user.first_name} ⚡,
I am Shiva robot...
I am at construction. 
"""

START_BUTTON = [[
    InlineKeyboardButton("👨 Owner 👨", url="https://t.me/sivathe_king")
]]


@Client.on_message(filters.command("start"))
async def start_cmd(client, msg):
    await msg.reply_text(
        text =  PM_TEXT,
        reply_markup=InlineKeyboardMarkup(START_BUTTON)
        
    )

