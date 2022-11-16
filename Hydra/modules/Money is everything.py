from Hydra import tbot as tbot
from Hydra.events import register

PHOTO = "https://te.legra.ph/file/f395feea438508d9ccdb0.mp4"


@register(pattern=("Money is everything"))
async def awake(event):
    Hydra = "REMEMBER ONE THING MONEY IS EVERYTHING"
    await tbot.send_file(event.chat_id, PHOTO, caption=Hydra)

    # Toon_Lisence
