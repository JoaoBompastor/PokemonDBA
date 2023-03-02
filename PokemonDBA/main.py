import discord
from discord.ext import commands
from config import TOKEN

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='-', intents= intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.event
async def on_message(message):
    print(f'Message from: {message.author}: {message.content}')

    if message.author == bot.user:
        return

    if message.content.lower() == 'cu':
        await message.channel.send('cu')

@bot.command(name='bolas')
async def ping(ctx):
    print('commando ping chamado')
    await ctx.channel.message.send('cu')

bot.run(TOKEN)