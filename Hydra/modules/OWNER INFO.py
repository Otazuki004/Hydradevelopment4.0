from telethon import Button

from Hydra import tbot as tbot
from Hydra.events import register

PHOTO = "https://te.legra.ph/file/91493c2284a4cbc0c5ba2.jpg"


@register(pattern=("/owninfo"))
async def awake(event):
    Hydra = """
    ╒═══「• OWNER INFO • 」
• ID: 1985665341
• First Name: [O T A Z U K I • 카빌란](https://telegram.dog/Otazuki_004)
• Username: @OTAZUKI_004
• Userlink: [Link](@otazuki_004)
• Github : [Here](https://Github.com/Otazuki004)
• Details : [Here](https://telegram.dog/Otazuki_bio)
• Python Knowledge : 1%
• Telethon Knowledge : 20%
• Pyrogram Knowledge : 5%
• Future City : [Here](https://telegram.dog/FutureCity005)

╘══「 Bot count: 2 」

• SUPPORT : [Here](https://telegram.dog/FutureCity005)
• UPDATES : [Here](https://telegram.dog/Updates004)
"""

    BUTTON = [
        [
            Button.url("۞ 𝙁𝙪𝙩𝙪𝙧𝙚 𝘾𝙞𝙩𝙮 ۞", "https://telegram.dog/FutureCity005"),
            Button.url(" 🔥 MORE INFO 🔥", "https://telegram.dog/otazuki_bio"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=Hydra, buttons=BUTTON)
    __help__ = """
*OWNER INFO:* 
• /owninfo Get Owner's Info (beta)
"""


__mod_name__ = "OWNER INFO"
