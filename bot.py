import disnake, os, json
from disnake.ext import commands
with open('config.json') as config:
    config = json.load(config)
bot = commands.Bot(command_prefix='b.')

@bot.event
async def on_ready():
    print('запустился ёптить')

@bot.event
async def on_message(ctx):
    words = ctx.content.lower().split(' ')
    if 'буфер' in words:
        image = disnake.File('./nobuffer.png','b.png')
        await ctx.delete()
        await ctx.channel.send(f'<@{ctx.author.id}>', file=image)

@bot.command()
async def ping(ctx):
    await ctx.reply('pong')

bot.run(config['TOKEN'])
