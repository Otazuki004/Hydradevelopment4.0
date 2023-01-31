from Hydra import tbot as tbot
from Hydra.events import register


@register(pattern=("~Love Today"))
async def awake(event):
  await event.reply("Uploading ⏫")


ImG = "https://t.me/HydraSsto/174"


@register(pattern=("~Love Today"))
async def awake(event):
    await tbot.send_file(event.chat_id, ImG)


file1 = "https://t.me/HydraSsto/175"


@register(pattern=("~Love Today"))
async def awake(event):
    await tbot.send_file(event.chat_id, file1)


file2 = "https://t.me/HydraSsto/176"


@register(pattern=("~Love Today"))
async def awake(event):
    await tbot.send_file(event.chat_id, file2)


file3 = "https://t.me/HydraSsto/177"


@register(pattern=("~Love Today"))
async def awake(event):
    await tbot.send_file(event.chat_id, file3)


file4 = "https://t.me/HydraSsto/178"


@register(pattern=("~Love Today"))
async def awake(event):
    await tbot.send_file(event.chat_id, file4)

@register(pattern=("~Love Today"))
async def awake(event):
  await event.reply("➠ Uploaded by : @Hydra_100_Bot")
