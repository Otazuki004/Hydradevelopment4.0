from telethon import Button

from Hydra import tbot as tbot
from Hydra.events import register

PHOTO = "https://te.legra.ph/file/447ec551360a04632d5b9.jpg"


@register(pattern=("!credits"))
async def awake(event):
    NEKO = """
    Credits
BOT OWNER : [OTAZUKI](https://telegram.dog/OTAZUKI_004)
REPO OWNER : [NANDHAXD](https://telegram.dog/NandhaxD)
HELPER : [🖤「 𝐌𝐲𝐚𝐚𝐯 𝐁𝐨𝐢™ 」🖤](https://telegram.dog/Awesome_MD)
SUPPORTER : [H M F](https://telegram.dog/HMF_OWNER_1)
ORGINAL REPO LINK : [CLICK](https://gitHub.com/NandhaxD/VegetaRobot.git)


• SUPPORT : [Here](https://telegram.dog/wesupport004)
• UPDATES : [Here](https://telegram.dog/Updates004)

--------------------------------------------------------------------------------
I HOPE YOU ALL
BECAME BEST PROGRAMMERS. THANKS  
"""

    BUTTON = [
        [
            Button.url("۞ 𝙁𝙪𝙩𝙪𝙧𝙚 𝘾𝙞𝙩𝙮 ۞", "https://telegram.dog/FutureCity004"),
            Button.url(" Updates 📢", "https://telegram.dog/Updates004"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
