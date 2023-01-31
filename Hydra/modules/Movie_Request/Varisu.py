from Hydra.events import register

@register(pattern=("~Varisu"))
async def awake(event):
  await event.reply("Uploading ⏫")

from Hydra import tbot as tbot
from Hydra.events import register

ImG = "https://te.legra.ph/file/191a2b533e49ddd8f63cc.jpg"


@register(pattern=("~Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, ImG)


from Hydra import tbot as tbot
from Hydra.events import register

Movie = "https://t.me/HydraSsto/88"


@register(pattern=("~Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, Movie)


from Hydra import tbot as tbot
from Hydra.events import register

Moviek = "https://t.me/HydraSsto/87"


@register(pattern=("~Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, Moviek)


from Hydra import tbot as tbot
from Hydra.events import register

Moviey = "https://t.me/HydraSsto/86"


@register(pattern=("~Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, Moviey)


from Hydra import tbot as tbot
from Hydra.events import register

Movieo = "https://t.me/HydraSsto/85"


@register(pattern=("~Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, Movieo)
