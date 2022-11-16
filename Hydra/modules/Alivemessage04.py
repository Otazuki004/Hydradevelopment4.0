from pyrogram import __version__ as pyrover
from telethon import Button
from telethon import __version__ as tlhver

PHOTO = "https://graph.org/file/ee4fc1bb7a1ef86b6fc41.jpg"

START_HYDRA = f"""
────「 Hydra 」────
ʜᴇʟʟᴏ! Users!
ᕼʏᴅʀᴀ Տᴛᴀʀᴛᴇᴅ Տᴜᴄᴄᴇssғᴜʟʟʏ 
➖➖➖➖➖➖➖➖➖➖➖➖➖
❍ 𝗣ʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : {pyrover}
❍ 𝗧ᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : {tlhver}
➖➖➖➖➖➖➖➖➖➖➖➖➖
➛ Try The ʜᴇʟᴘ Button Below To Know My Abilities ××
"""

START_BUTTON = [
    [
        Button.url("Help", "https://t.me/hydra_100_bot?start=help"),
    ]
]
await tbot.send_file(-1001768984791, PHOTO, caption=HYDRA, buttons=BUTTON),
