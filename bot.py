import disnake, os, json, re
from disnake.ext import commands
with open('config.json', encoding="utf-8") as config:
    config = json.load(config)

intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or('b.'),intents=intents)

@bot.event
async def on_ready():
    print('запустился ёптить')

@bot.command()
async def ping(ctx):
    await ctx.reply('pong')

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
