from Hydra import tbot as tbot
from Hydra.events import register

ImG = "https://te.legra.ph/file/191a2b533e49ddd8f63cc.jpg"


@register(pattern=("Varisu"))
async def awake(event):
  NO = f"""
🎬 Title : Varisu 
🗓 Year : 2023
🔊 Audio : Tamil 
💿 Quality : PreDVD
📥 Upload : @FutureCity005
"""
    await tbot.send_file(event.chat_id, ImG, caption=NO)


from Hydra import tbot as tbot
from Hydra.events import register

Movie = "https://t.me/CSFH005/3"


@register(pattern=("Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, Movie)


from Hydra import tbot as tbot
from Hydra.events import register

Moviek = "https://t.me/CSFH005/4"


@register(pattern=("Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, Moviek)


from Hydra import tbot as tbot
from Hydra.events import register

Moviey = "https://t.me/CSFH005/5"


@register(pattern=("Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, Moviey)


from Hydra import tbot as tbot
from Hydra.events import register

Movieo = "https://t.me/CSFH005/6"


@register(pattern=("Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, Movieo)


from Hydra import tbot as tbot
from Hydra.events import register

Moviee = "https://t.me/CSFH005/7"


@register(pattern=("Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, Moviee)
