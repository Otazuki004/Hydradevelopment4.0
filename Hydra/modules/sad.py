from Hydra import tbot as tbot
from Hydra.events import register

PHOTO = "https://te.legra.ph/file/d3b7a83fe1f6e17c17135.mp4"


@register(pattern=("Sad"))
async def awake(event):
    HYDRA = "Don't sad because our life has all emotions sad is one part of emotion don't sad be happy."
    await tbot.send_file(event.chat_id, PHOTO, caption=HYDRA)


PHOTO = "https://te.legra.ph/file/d3b7a83fe1f6e17c17135.mp4"


@register(pattern=("So sad"))
async def awake(event):
    HYDRA = "Don't sad because our life has all emotions sad is one part of emotion don't sad be happy."
    await tbot.send_file(event.chat_id, PHOTO, caption=HYDRA)


PHOTO = "https://te.legra.ph/file/d3b7a83fe1f6e17c17135.mp4"


@register(pattern=("Sed"))
async def awake(event):
    HYDRA = "Don't sad because our life has all emotions sad is one part of emotion don't sad be happy."
    await tbot.send_file(event.chat_id, PHOTO, caption=HYDRA)
