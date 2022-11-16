from telethon import Button

from Hydra import tbot as tbot
from Hydra.events import register

PHOTO = "https://te.legra.ph/file/5cdc460a2ed69abcbee60.gif"


@register(pattern=("Welcome"))
async def awake(event):
    HYDRA = f" ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴋɪɴɢᴅᴏᴍ! ɪ ʜᴏᴘᴇ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ᴍᴀɴʏ ғʀɪᴇɴᴅs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ"
    BUTTON = [
        [
            Button.url("  UPDATES", "https://telegram.dog/Updates004"),
            Button.url(" SUPPORT", "https://telegram.dog/wesupport004"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=HYDRA, buttons=BUTTON)
