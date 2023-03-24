# build dia 3/24

# imports

import discord
from discord.ext import commands
from util.config import TOKEN
from util.builds import buildsshow, items


# main

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')


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
    embed.add_field(name='Build 1', value=buildsshow.slowbro1, inline=True)
    embed.add_field(name='Build 2', value=buildsshow.slowbro2, inline=True)
    embed.add_field(name='Build do Aramaki', value=buildsshow.slowbro_aramaki, inline=True)
    embed.set_footer(text='Battle item: Potion', icon_url=items.potion)

    await ctx.send(embed=embed)


@bot.command()
async def goodra(ctx):
    print('Comando goodra chamado')

    embed = discord.Embed(title='Goodra',
                          description='Guia informativo sobre Goodra',
                          color=0x2ecc71)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Goodra.png')
    embed.add_field(name='Build 1', value=buildsshow.goodra1)
    embed.set_footer(text='Battle item: Potion', icon_url=items.potion)

    await ctx.send(embed=embed)


@bot.command()
async def greedent(ctx):
    print('Comando greedent chamado')

    embed = discord.Embed(title='Greedent',
                          description='Guia informativo sobre o theodor do alvin e os esquilos',
                          color=0x2ecc71)
    
    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Greedent.png')
    embed.add_field(name='Build 1', value=buildsshow.theodor1)
    embed.set_footer(text='Battle item: X Speed', icon_url=items.xspeed)

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
    embed.add_field(name='Build 1', value=buildsshow.sylveon1, inline=True)
    embed.add_field(name='Build 2', value=buildsshow.sylveon2, inline=True)
    embed.add_field(name='Build do Aramaki', value=buildsshow.sylveon_aramaki, inline=True)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


@bot.command()
async def greninja(ctx):
    print('Comando greninja chamado')

    embed = discord.Embed(title='Greninja',
                          description='É o guizas',
                          color=0xe74c3c)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Greninja.png')
    embed.add_field(name='Build 1', value=buildsshow.greninja1)
    embed.set_footer(text='Battle item: Full Heal', icon_url=items.full_heal)

    await ctx.send(embed=embed)


@bot.command()
async def gardevoir(ctx):
    print('Comando gardevoir chamado')

    embed = discord.Embed(title='gardevoir',
                        description='Guia informativo sobre Gardevoir',
                        color=0xe74c3c)
    
    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Gardevoir.png')
    embed.add_field(name='Build 1', value=buildsshow.gardevoir1, inline=True)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


@bot.command()
async def dragonite(ctx):
    print('Comando dragonite chamado')

    embed = discord.Embed(title='Dragonite',
                          description='Guia informativo sobre Dragonite',
                          color=0xe74c3c)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Dragonite.png')
    embed.add_field(name='Build 1', value=buildsshow.dragonite1)
    embed.set_footer(text='Battle item: X Attack', icon_url=items.xattack)

    await ctx.send(embed=embed)


@bot.command()
async def espeon(ctx):
    print('Comando espeon chamado')

    embed = discord.Embed(title='Espeon',
                          description='Guia informativo sobre Espeon',
                          color=0xe74c3c)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Espeon.png')
    embed.add_field(name='Build 1', value=buildsshow.espeon1)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


@bot.command()
async def glaceon(ctx):
    print('Comando glaceon chamado')

    embed = discord.Embed(title='glaceon',
                          description='Guia informativo sobre Glaceon',
                          color=0xe74c3c)
    
    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Glaceon.png')
    embed.add_field(name='Build 1', value=buildsshow.glaceon1)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


@bot.command()
async def dragapult(ctx):
    print('Comando dragapult chamado')

    embed = discord.Embed(title='dragapult', 
                          description='Guia informativo sobre o dragapult', 
                          color=0xe74c3c)
    
    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Dragapult.png')
    embed.add_field(name='Build 1', value=buildsshow.dragapult1)
    embed.set_footer(text='Battle item: X Attack')

    await ctx.send(embed=embed)


@bot.command()
async def poligono(ctx):
    print('Comando Duraludon chamado')

    embed = discord.Embed(title='Duraludon', 
                          description='Guia informativo sobre o duraludon',
                          color=0xe74c3c)
    
    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Duraludon.png')
    embed.add_field(name='Build 1', value=buildsshow.poligono1)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


@bot.command()
async def chomp(ctx):
    print('Comando garchomp chamado')

    embed = discord.Embed(title='Garchomp',
                          description='Guia informativo sobre garchomp',
                          color=0xe74c3c)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Garchomp.png')
    embed.add_field(name='Build 1', value=buildsshow.chomp1)
    embed.set_footer(text='Battle item: Full Heal', icon_url=items.full_heal)

    await ctx.send(embed=embed)


@bot.command()
async def gengar(ctx):
    print('Comando gengar chamado')

    embed = discord.Embed(title='Gengar',
                          description='Guia informativo sobre Gengar',
                          color=0xe74c3c)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Gengar.png')
    embed.add_field(name='Build 1', value=buildsshow.gengar1)
    embed.set_footer(text='Battle item: Full Heal', icon_url=items.full_heal)

    await ctx.send(embed=embed)


# Suportes

@bot.command()
async def mime(ctx):
    print('Comando mime chamado')
    # await ctx.send('comando mime.')

    embed = discord.Embed(title='Mr. mime',
                          description='Guia informativo sobre o coringa37(Mr. mime)', 
                          color=0xf1c40f)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Mr.Mime.png')
    embed.add_field(name='Build 1', value=buildsshow.mime1, inline=True)
    embed.add_field(name='Build 2', value=buildsshow.mime2, inline=True)
    embed.add_field(name='Build do Aramaki', value=buildsshow.mime_aramaki, inline=True)
    embed.set_footer(text='Battle item: X speed', icon_url=items.xspeed)

    await ctx.send(embed=embed)


@bot.command()
async def eldegoss(ctx):
    print('Comando eldegoss chamado')

    embed = discord.Embed(title='eldegoss',
                          description='Guia informativo sobre eldegoss',
                          color=0xf1c40f)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Eldegoss.png')
    embed.add_field(name='build 1', value=buildsshow.eldegoss1, inline=True)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


# Speedsters

@bot.command()
async def dodrio(ctx):
    print('Comando dodrio chamado')

    embed = discord.Embed(title='Dodrio',
                          description='Guia informativo sobre dodrio',
                          color=0x3498db)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Dodrio.png')
    embed.add_field(name='Build 1', value=buildsshow.dodrio1)
    embed.set_footer(text='Battle item: Full Heal', icon_url=items.full_heal)

    await ctx.send(embed=embed)


# Util Commands

@bot.command()
async def ajuda(ctx):
    print('Comando help chamado')

    embed = discord.Embed(title='Ajuda',
                          description='Gamipu -> Guia Altamente Mecanico Informativo de Pokemon Unite',
                          color=0xc27c0e)

    embed.set_thumbnail(url='https://github.com/JoaoBompastor/PokemonDBA/blob/main/PokemonDBAAssets/emoticon-confuso-22051357-removebg-preview.png?raw=true')
    embed.add_field(name='Comandos', value='->')
    embed.add_field(name='Comandos Pokemon: ', value=buildsshow.lista_builds)
    embed.add_field(name='Comandos Util: ', value='Ping, Info')

    await ctx.send(embed=embed)


# Comando inoperante por enquanto

@bot.command()
async def teste(ctx):
    ...


@bot.command()
async def info(ctx):
    print('Comando info chamado')

    embed = discord.Embed(title='Informações: ',
                          description='Bot organizado pelo time dos encabacados',
                          color=0x992d22)

    embed.set_thumbnail(url='https://github.com/JoaoBompastor/PokemonDBA/blob/main/PokemonDBAAssets/bannerserio.jpg?raw=true')

    embed.set_author(name='Coringa37', 
                    url='https://github.com/JoaoBompastor',
                    icon_url='https://github.com/JoaoBompastor/PokemonDBA/blob/main/PokemonDBAAssets/bannerserio.jpg?raw=true')

    embed.set_footer(text='footer')

    await ctx.send(embed=embed)
    await ctx.send('novos: gengar, dodrio, dragonite, chomp, poligono, espeon, greedent, goodra, greninja')


bot.run(TOKEN)
