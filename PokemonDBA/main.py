# imports

import discord
from discord.ext import commands
from util.config import TOKEN
import util.Embed_Bonitinho


# main

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')


# @bot.event
# async def on_message(message):
#     print(f'Message from: {message.author}: {message.content}')
#
#     if message.author == bot.user:
#         return
#
#     if message.content.lower() == 'alo':
#         await message.channel.send('alo')
#
#     else:
#         pass


# Pokemon Commands

@bot.command()
async def ping(ctx):
    print('commando ping chamado')
    await ctx.message.reply('pong!')


# Defenders

@bot.command()
async def slowbro(ctx):
    print('Comando slowbro chamado')
    # await ctx.send('comando slowbro.')

    embed = discord.Embed(title='slowbro :D',
                          description='Guia altamente mecanico ultra informativo sobre builds de bonecos legais',
                          color=0x2ecc71)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/portrait/Slowbro.png')
    embed.add_field(name='Build 1', value='Exp Share\nFocus Band\nAeos Cookie\n-----\nSurf/Amnesia', inline=True)
    embed.add_field(name='Build 2', value='Focus Band\nAeos Cookie\nChoice Specs(ou Stack)\n-----\nScald/Telekinesis', inline=True)
    embed.add_field(name='Build do Aramaki', value='Choice Specs\nOculos de Stack\nColher\n-----\nScald/Amnesia', inline=True)
    embed.set_footer(text='Battle item: Potion', icon_url='https://github.com/JoaoBompastor/PokemonDBA/blob/main/PokemonDBAAssets/Potion.png?raw=true')

    await ctx.send(embed=embed)


# Attackers

@bot.command()
async def sylveon(ctx):
    print('Comando sylveon chamado')
    # await ctx.send('comando sylveon.')

    embed = discord.Embed(title='sylveon :)',
                          description='Guia altamente mecanico ultra informativo sobre builds de bonecos legais',
                          color=0xe74c3c)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Sylveon.png')
    embed.add_field(name='Build 1', value='Choice Specs\nWise Glasses\nFocus Band\n-----\nHyper Voice/Calm Mind', inline=True)
    embed.add_field(name='Build 2', value='Muscle Band\nScarf\nFocus Band\n-----\nMystical Fire/Draining Kiss', inline=True)
    embed.add_field(name='Build do Aramaki', value='Muscle\nRazor\nScope\n-----\nMystical Fire/Calm Mind', inline=True)
    embed.set_footer(text='Battle Item: Eject Button', icon_url='https://github.com/JoaoBompastor/PokemonDBA/blob/main/PokemonDBAAssets/Eject+Button.png?raw=true')

    await ctx.send(embed=embed)


# Suportes

@bot.command()
async def mime(ctx):
    print('Comando mime chamado')
    # await ctx.send('comando mime.')

    embed = discord.Embed(title='Mr. mime',
                          description='Guia informativo osbre o coringa37(Mr. mime)', 
                          color=0xf1c40f)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Mr.Mime.png')
    embed.add_field(name='Build 1', value='Aeos cookie\nFocus band\nEnergy amp\n-----\nCordinha/psychic', inline=True)
    embed.add_field(name='Build 2', value='Choice Specs\nColher\nFocus Band\n-----\nConfusion/Barreira', inline=True)
    embed.add_field(name='Build do Aramaki', value='Exp Share\nFocus Band\nBuddy Barrier\n-----\nPsychic/Barreira', inline=True)
    embed.set_footer(text='Battle Item: Xspeed', icon_url='https://github.com/JoaoBompastor/PokemonDBA/blob/main/PokemonDBAAssets/X+Speed.png?raw=true')

    await ctx.message.reply(embed=embed)


# Util Commands

@bot.command()
async def ajuda(ctx):
    print('Comando help chamado')

    embed = discord.Embed(title='Ajuda',
                          description='Gamipu -> Guia Altamente Mecanico Informativo de Pokemon Unite',
                          color=0xc27c0e)

    embed.set_thumbnail(url='https://github.com/JoaoBompastor/PokemonDBA/blob/main/PokemonDBAAssets/emoticon-confuso-22051357-removebg-preview.png?raw=true')
    embed.add_field(name='Comandos', value='->')
    embed.add_field(name='Comandos Pokemon: ', value='Mime, sylveon, slowbro')
    embed.add_field(name='Comandos Util: ', value='Ping, Info')

    await ctx.send(embed=embed)


# Comando inoperante por enquanto

@bot.command()
async def teste(ctx):
    init = util.Embed_Bonitinho.Embed_bonitinho('pokemon', 'titulo', ctx=ctx)

    await ctx.send(embed=init)


@bot.command()
async def info(ctx):
    print('Comando info chamado')

    embed = discord.Embed(title='Informações: ',
                          description='Bot organizado pelo time de unite da 5 Elements',
                          color=0x992d22)

    embed.set_thumbnail(url='https://github.com/JoaoBompastor/PokemonDBA/blob/main/PokemonDBAAssets/five_sem_bg.png?raw=true')

    embed.set_author(name='Coringa37', 
                    url='https://github.com/JoaoBompastor',
                    icon_url='https://github.com/JoaoBompastor/PokemonDBA/blob/main/PokemonDBAAssets/bannerserio.jpg?raw=true')

    embed.set_footer(text='footer')

    await ctx.send(embed=embed)


bot.run(TOKEN)
