from Hydra.events import register
@register(pattern=("Alive?"))
async def awake(event):
    await event.reply("I am alive."),
