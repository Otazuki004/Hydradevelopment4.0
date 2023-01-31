from Hydra import tbot as tbot
from Hydra.events import register


@register(pattern=("~Varisu"))
async def awake(event):
  await event.reply("Uploading ⏫")


ImG = "https://t.me/HydraSsto/65"


@register(pattern=("~Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, ImG)


file1 = "https://t.me/HydraSsto/88"


@register(pattern=("~Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, file1)


file2 = "https://t.me/HydraSsto/87"


@register(pattern=("~Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, file2)


file3 = "https://t.me/HydraSsto/86"


@register(pattern=("~Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, file3)


file4 = "https://t.me/HydraSsto/87"


@register(pattern=("~Varisu"))
async def awake(event):
    await tbot.send_file(event.chat_id, file4)


@register(pattern=("~Varisu"))
async def awake(event):
  await event.reply("➠ Uploaded by : @Hydra_100_Bot")
