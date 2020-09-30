import discord
import asyncio
import datetime
from discord.ext import commands
from random import randint
from discord.utils import get




bot = commands.Bot(command_prefix='>>')
token ='el_token'


@bot.event #print que esta listo
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('>help'))
    print('my bot is ready')


@bot.event #da la vienvenida en el canal espcificado
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    embed=discord.Embed(title=f"{member.name} esta en el lobby.",
    description=f"Bienvenido {member.mention} a **{member.guild}** esperemos que no seas un traidor y a reparar!! GG.")

    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    await channel.send(embed=embed)
    print('entro')

volados = ['Cara','Cruz']
volados2 = ['https://rollthedice.online/assets/images/upload/dice/dado-cara-cruz/cara_moneda.png',
'https://rollthedice.online/assets/images/upload/dice/dado-cara-cruz/cruz_moneda.png']
volados3= ['Parece que la suerte\nEsta de tu lado','Parece que hoy\nNo es tu dia','Casi pero no...',
'Hoy no es tu dia\nHe?','F en el chat']

eme = 'http://static.sticker.ly/sticker_pack/3c0fzIkFt7E0YaXYSSXPw/0JZN24/4/1246b776-be23-4581-a37d-4443b31230e1.png'

channelPrueba = ['0']
roleDic = ['0']



@bot.command(pass_context=True)
@commands.has_role("Tecnicos de Nave (Moderador)")
async def castigo(ctx,castigado: discord.Member,*,motivo,):
    autor= ctx.message.author
    rol = discord.utils.get(autor.guild.roles, name="Impostor (Sancionado)")
    channel = bot.get_channel(754074719761858641)

    embed=discord.Embed(title="Un traidor fue encontrado!!",
    description=f"El tripulante {castigado.mention} fue castigado por **{motivo}** \n\n**Moderador:** {autor.mention}")

    embed.set_thumbnail(url=eme)
    embed.set_footer(text=f"{autor.guild}", icon_url=f"{autor.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    await channel.send(embed=embed)
    print('mensaje a prueva2')
    # //////////////////////////////

    embed=discord.Embed(title="Un traidor fue encontrado!!",
    description=f"El tripulante {castigado.mention} fue castigado por **{motivo}** \n\n**Moderador:** {autor.mention}")

    embed.set_thumbnail(url=eme)
    embed.set_footer(text=f"{autor.guild}", icon_url=f"{autor.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed=embed)
    print('mensaje a donde se envio')
    # ////////////////////////////////

    await castigado.send(f'Hola {castigado.mention} fuiste castigado por **{motivo}** por el **Moderador:**{autor.mention} este castigo durara un dia y recuerda que si acumulas 3 castigos se te dara un **ban permanete**.\nSi tienes alguna duda o crees que fue un error contacta con un **admin o piloto de nave**.\n\n**Att:** {autor.guild}')
    print('mensaje personal')
    # ////////////////////////
    await castigado.add_roles(rol)
    print('castigado')
    print('fin')



@bot.command()
async def volado(ctx):
    x = randint(0, 1)
    x1 = randint(0,4)
    embed=discord.Embed(title=volados[x],
    description=volados3[x1])
    embed.set_thumbnail(url=volados2[x])
    await ctx.send(embed=embed)












@bot.command()
async def setChannelPrueba(ctx,channel):
    channelPrueba.clear()
    channelPrueba.append(channel)
    await ctx.send(f'el canal <#{channelPrueba[0]}> fue establecido')



@bot.command()
async def ping(ctx):
    channel = bot.get_channel(int(channelPrueba[0]))
    await channel.send('role')



@bot.command()
async def setRole(ctx,rol):
    roleDic.clear()
    roleDic.append(rol)
    await ctx.send(f'el rol <@&{roleDic[0]}> fue establecido')

@bot.command(pass_context=True)
@commands.has_role("prueva")
async def prue(ctx,user: discord.Member):
    guild = ctx.guild
    role = discord.utils.get(user.guild.roles, name="test")
    #role = get(guild.roles, id=757705860175888524)
    await ctx.send(role)
    await user.add_roles(role)


bot.run(token)
