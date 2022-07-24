import disnake, os, json, re
from disnake.ext import commands
with open('config.json', encoding="utf-8") as config:
    config = json.load(config)

intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print('запустился ёптить')

@bot.slash_command(description="check if the bot is running")
async def ping(inter):
    await inter.response.send_message(f'Pong! Running on `{os.system("uname -sr")}`')

@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        for word in config["BANWORDS"]:
            regex = r'\b(' + word + r')\b'
            match = re.search(regex, ctx.content, re.IGNORECASE)
            if match:
                image = disnake.File('./nope.png','nope.png')
                await ctx.delete()
                await ctx.channel.send(f'<@{ctx.author.id}>, я запрещаю вам говорить `{word}`', file=image)
        await bot.process_commands(ctx)

bot.run(config['TOKEN'])
