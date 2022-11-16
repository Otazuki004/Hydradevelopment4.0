from Hydra import tbot as tbot
from Hydra.events import register

PHOTO = "https://te.legra.ph/file/4e959d8f074bef7061463.mp4"


@register(pattern=("Good night"))
async def awake(event):
    HYDRA = f"Good night I hope tomorrow is the best day in your life. {event.sender.first_name}"
    await tbot.send_file(event.chat_id, PHOTO, caption=HYDRA)
