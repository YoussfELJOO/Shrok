import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","_𝐄𝐋𝐐𝐉𝐎𝐎","السورس", "سورس _𝐄𝐋𝐐𝐉𝐎𝐎"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/04b2f1f1c808dc49db35b.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ  𝘴ꪮꪊ𝘳𝘴 ꪖᠻ𝘳ꪮ𝓽ꪮꪮ(t.me/source_rolexs)
么 [َ ᦔꫀꪜ ꪖᠻ𝘳ꪮ𝓽ꪮꪮ](t.me/E_L_J_OO)
么 [َ ᥉υρρ᥆ᖇƚ ](https://t.me/+FgMShSOx2E9lOGM0)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹  ᦔꫀꪜ ꪖᠻ𝘳ꪮ𝓽ꪮꪮ . 🕷 › ", url=f"https://t.me/E_L_J_OO"),
                ],[
                    InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲ️ꪀꪀᥱᥣ›", url=f"https://t.me/source_rolexs"), 
                    InlineKeyboardButton(
                        "‹ ᥉υρρ᥆ᖇƚ›", url=f"https://t.me/+FgMShSOx2E9lOGM0"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
            ]
        ]
         ),
     )
  
