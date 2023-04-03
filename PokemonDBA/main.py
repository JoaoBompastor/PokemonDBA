# patch dia 4/2

# imports

import discord
from discord.ext import commands
from util.config import TOKEN
from util.builds import buildsshow, items, cores

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
                          color=cores.Defenders)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/portrait/Slowbro.png')
    embed.add_field(name='Build 1', value=buildsshow.slowbro1, inline=True)
    embed.add_field(name='Build 2', value=buildsshow.slowbro2, inline=True)
    embed.add_field(name='Build do Aramaki', value=buildsshow.slowbro_aramaki, inline=True)
    embed.set_footer(text='Battle item: Potion', icon_url=items.potion)

    await ctx.send(embed=embed)


@bot.command()
async def mamute(ctx):
    print('Comando mamute chamado.')

    embed = discord.Embed(title='Mamoswine',
                          description='Guia informativo sobre Mamoswine',
                          color=cores.Defenders)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Mamoswine.png')
    embed.add_field(name='Build 1', value=buildsshow.mamute1, inline=True)
    embed.set_footer(text='Battle item: X Attack', icon_url=items.xattack)

    await ctx.send(embed=embed)


@bot.command()
async def snorlax(ctx):
    print('Comando snorlax chamado.')

    embed = discord.Embed(title='Snorlax',
                          description='Guia informativo sobre Snorlax',
                          color=cores.Defenders)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Snorlax.png')
    embed.add_field(name='Build 1', value=buildsshow.snorlax1)
    embed.set_footer(text='Battle Item: X Speed', icon_url=items.xspeed)

    await ctx.send(embed=embed)


@bot.command()
async def goodra(ctx):
    print('Comando goodra chamado')

    embed = discord.Embed(title='Goodra',
                          description='Guia informativo sobre Goodra',
                          color=cores.Defenders)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Goodra.png')
    embed.add_field(name='Build 1', value=buildsshow.goodra1)
    embed.set_footer(text='Battle item: Potion', icon_url=items.potion)

    await ctx.send(embed=embed)


@bot.command()
async def greedent(ctx):
    print('Comando greedent chamado')

    embed = discord.Embed(title='Greedent',
                          description='Guia informativo sobre o theodor do alvin e os esquilos',
                          color=cores.Defenders)

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
                          color=cores.Attackers)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Sylveon.png')
    embed.add_field(name='Build 1', value=buildsshow.sylveon1, inline=True)
    embed.add_field(name='Build 2', value=buildsshow.sylveon2, inline=True)
    embed.add_field(name='Build do Aramaki', value=buildsshow.sylveon_aramaki, inline=True)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


@bot.command()
async def mew(ctx):
    print('Comando mew chamado')

    embed = discord.Embed(title='Mew',
                          description='Guia informativo sobre Mew',
                          color=cores.Attackers)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Mew.png')
    embed.add_field(name='Build 1', value=buildsshow.mew1)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


@bot.command()
async def pikachu(ctx):
    print('Comando pikachu chamado.')

    embed = discord.Embed(title='Pikachu',
                          description='Guia informativo sobre Pikachu',
                          color=cores.Attackers)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Pikachu.png')
    embed.add_field(name='Build 1', value=buildsshow.pikachu1)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


@bot.command()
async def greninja(ctx):
    print('Comando greninja chamado')

    embed = discord.Embed(title='Greninja',
                          description='É o guizas',
                          color=cores.Attackers)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Greninja.png')
    embed.add_field(name='Build 1', value=buildsshow.greninja1)
    embed.set_footer(text='Battle item: X Attack', icon_url=items.xattack)

    await ctx.send(embed=embed)


@bot.command()
async def gardevoir(ctx):
    print('Comando gardevoir chamado')

    embed = discord.Embed(title='gardevoir',
                          description='Guia informativo sobre Gardevoir',
                          color=cores.Attackers)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Gardevoir.png')
    embed.add_field(name='Build 1', value=buildsshow.gardevoir1, inline=True)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


@bot.command()
async def espeon(ctx):
    print('Comando espeon chamado')

    embed = discord.Embed(title='Espeon',
                          description='Guia informativo sobre Espeon',
                          color=cores.Attackers)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Espeon.png')
    embed.add_field(name='Build 1', value=buildsshow.espeon1)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


@bot.command()
async def glaceon(ctx):
    print('Comando glaceon chamado')

    embed = discord.Embed(title='glaceon',
                          description='Guia informativo sobre Glaceon',
                          color=cores.Attackers)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Glaceon.png')
    embed.add_field(name='Build 1', value=buildsshow.glaceon1)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


@bot.command()
async def dragapult(ctx):
    print('Comando dragapult chamado')

    embed = discord.Embed(title='dragapult',
                          description='Guia informativo sobre o dragapult',
                          color=cores.Attackers)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Dragapult.png')
    embed.add_field(name='Build 1', value=buildsshow.dragapult1)
    embed.set_footer(text='Battle item: X Attack')

    await ctx.send(embed=embed)


@bot.command()
async def poligono(ctx):
    print('Comando Duraludon chamado')

    embed = discord.Embed(title='Duraludon',
                          description='Guia informativo sobre o duraludon',
                          color=cores.Attackers)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Duraludon.png')
    embed.add_field(name='Build 1', value=buildsshow.poligono1)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


# Suportes

@bot.command()
async def mime(ctx):
    print('Comando mime chamado')
    # await ctx.send('comando mime.')

    embed = discord.Embed(title='Mr. mime',
                          description='Guia informativo sobre o coringa37(Mr. mime)',
                          color=cores.Supports)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Mr.Mime.png')
    embed.add_field(name='Build 1', value=buildsshow.mime1, inline=True)
    embed.add_field(name='Build 2', value=buildsshow.mime2, inline=True)
    embed.add_field(name='Build do Aramaki', value=buildsshow.mime_aramaki, inline=True)
    embed.set_footer(text='Battle item: X speed', icon_url=items.xspeed)

    await ctx.send(embed=embed)


@bot.command()
async def sableye(ctx):
    print('Comando sableye chamado.')

    embed = discord.Embed(title='Sableye',
                          description='Guia informativo sobre Sableye',
                          color=cores.Supports)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Sableye.png')
    embed.add_field(name='Build 1', value=buildsshow.sableye1)
    embed.set_footer(text='Battle item: Goal Getter', icon_url=items.Goal_Getter)

    await ctx.send(embed=embed)


@bot.command()
async def hoopa(ctx):
    print('Comando hoopa chamado')

    embed = discord.Embed(title='Hoopa',
                          description='Guia informativo sobre Hoopa',
                          color=cores.Supports)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Hoopa.png')
    embed.add_field(name='Build 1', value=buildsshow.hoopa1, inline=True)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


@bot.command()
async def eldegoss(ctx):
    print('Comando eldegoss chamado')

    embed = discord.Embed(title='eldegoss',
                          description='Guia informativo sobre eldegoss',
                          color=cores.Supports)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Eldegoss.png')
    embed.add_field(name='build 1', value=buildsshow.eldegoss1, inline=True)
    embed.set_footer(text='Battle item: Eject Button', icon_url=items.eject)

    await ctx.send(embed=embed)


# Speedsters

@bot.command()
async def gengar(ctx):
    print('Comando gengar chamado')

    embed = discord.Embed(title='Gengar',
                          description='Guia informativo sobre Gengar',
                          color=cores.Speedsters)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Gengar.png')
    embed.add_field(name='Build 1', value=buildsshow.gengar1)
    embed.set_footer(text='Battle item: Full Heal', icon_url=items.full_heal)

    await ctx.send(embed=embed)


@bot.command()
async def dodrio(ctx):
    print('Comando dodrio chamado')

    embed = discord.Embed(title='Dodrio',
                          description='Guia informativo sobre dodrio',
                          color=cores.Speedsters)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Dodrio.png')
    embed.add_field(name='Build 1', value=buildsshow.dodrio1)
    embed.set_footer(text='Battle item: Full Heal', icon_url=items.full_heal)

    await ctx.send(embed=embed)


# All Rounders

@bot.command()
async def dragonite(ctx):
    print('Comando dragonite chamado')

    embed = discord.Embed(title='Dragonite',
                          description='Guia informativo sobre Dragonite',
                          color=cores.AllRounders)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Dragonite.png')
    embed.add_field(name='Build 1', value=buildsshow.dragonite1)
    embed.set_footer(text='Battle item: X Attack', icon_url=items.xattack)

    await ctx.send(embed=embed)


@bot.command()
async def machamp(ctx):
    print('Comando machamp chamado')

    embed = discord.Embed(title='Machamp',
                          description='Guia informativo sobre Machamp',
                          color=cores.AllRounders)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Machamp.png')
    embed.add_field(name='Build 1', value=buildsshow.machamp1)
    embed.set_footer(text='Battle item: X Attack', icon_url=items.xattack)

    await ctx.send(embed=embed)


@bot.command()
async def chomp(ctx):
    print('Comando garchomp chamado')

    embed = discord.Embed(title='Garchomp',
                          description='Guia informativo sobre garchomp',
                          color=cores.AllRounders)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Garchomp.png')
    embed.add_field(name='Build 1', value=buildsshow.chomp1)
    embed.set_footer(text='Battle item: Full Heal', icon_url=items.full_heal)

    await ctx.send(embed=embed)


@bot.command()
async def scizor(ctx):
    print('Comando scizor chamado.')

    embed = discord.Embed(title='Scizor',
                          description='Guia informativo sobre Scizor',
                          color=cores.AllRounders)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Scizor.png')
    embed.add_field(name='Build 1', value=buildsshow.scizor1)
    embed.set_footer(text='Battle item: Full Heal', icon_url=items.full_heal)

    await ctx.send(embed=embed)


@bot.command()
async def scyther(ctx):
    print('Comando scyther chamado.')

    embed = discord.Embed(title='Scyther',
                          description='Guia informativo sobre Scyther',
                          color=cores.AllRounders)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Scyther.png')
    embed.add_field(name='Build 1', value=buildsshow.scyther1)
    embed.set_footer(text='Battle item: Full Heal', icon_url=items.full_heal)

    await ctx.send(embed=embed)


@bot.command()
async def lucario(ctx):
    print('Comando lucario chamado')

    embed = discord.Embed(title='Lucario',
                          description='Guia informativo sobre Lucario',
                          color=cores.AllRounders)

    embed.set_thumbnail(url='https://d275t8dp8rxb42.cloudfront.net/pokemon/thumbnail/Lucario.png')
    embed.add_field(name='Build 1', value=buildsshow.lucario1)
    embed.set_footer(text='Battle item: Full Heal', icon_url=items.full_heal)

    await ctx.send(embed=embed)


# Util Commands

@bot.command()
async def ajuda(ctx):
    print('Comando help chamado')

    embed = discord.Embed(title='Ajuda',
                          description='Gamipu -> Guia Altamente Mecanico Informativo de Pokemon Unite',
                          color=0xc27c0e)

    embed.set_thumbnail(
        url='https://github.com/JoaoBompastor/PokemonDBA/blob/main/PokemonDBAAssets/emoticon-confuso-22051357'
            '-removebg-preview.png?raw=true')
    embed.add_field(name='Comandos', value='->')
    embed.add_field(name='Comandos Pokemon: ', value=buildsshow.lista_builds)
    embed.add_field(name='Comandos Util: ', value='Ping, Info')

    await ctx.send(embed=embed)


@bot.command()
async def info(ctx):
    print('Comando info chamado')

    embed = discord.Embed(title='Informações: ',
                          description='Bot organizado pelo time dos encabacados',
                          color=0x992d22)

    embed.set_thumbnail(
        url='https://github.com/JoaoBompastor/PokemonDBA/blob/main/PokemonDBAAssets/bannerserio.jpg?raw=true')

    embed.set_author(name='Coringa37',
                     url='https://github.com/JoaoBompastor',
                     icon_url='https://github.com/JoaoBompastor/PokemonDBA/blob/main/PokemonDBAAssets/bannerserio.jpg'
                              '?raw=true')

    embed.set_footer(text='footer')

    await ctx.send(embed=embed)
    await ctx.send('novos: mamute, mew, scyther, scizor, pikachu, snorlax, sableye\najustes: acesso ao sistema de cores melhorado')


if __name__ == '__main__':
    bot.run(TOKEN)
