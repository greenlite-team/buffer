import disnake, re, env
from disnake.ext import commands
from colorama import init, Style, Fore
from datetime import datetime

init()
intents = disnake.Intents.default()
intents.message_content = True
bot = commands.InteractionBot(intents=intents)

@bot.event
async def on_ready():
    game = disnake.Game("кубы 🧊")
    await bot.change_presence(activity=game)
    print(f'{Fore.LIGHTBLUE_EX}[{datetime.now()}] [LAUNCH] - Loaded as {bot.user}{Style.RESET_ALL}')

@bot.slash_command(description="Проверить пинг бота")
async def ping(inter):
    await inter.response.send_message(f'Pong! Ping: `{round(bot.latency*1000)} ms`')

@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        for word in env.BANWORDS:
            regex = r'\b('+word+r')\b' # прикол
            match = re.search(regex, ctx.content, re.IGNORECASE)
            if match:
                image = disnake.File('./nope.png','nope.png')
                await ctx.delete()
                await ctx.channel.send(f'<@{ctx.author.id}>, я запрещаю вам говорить `{word}`', file=image)
                print(f'{Fore.LIGHTCYAN_EX}[{datetime.now()}] [BLOCKD] - Blocked word "{word}" from {ctx.author}{Style.RESET_ALL}')

bot.run(env.TOKEN)
