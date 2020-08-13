import discord
import time
import math
from discord.ext import commands
from discord.utils import get
import requests
import json

bot = commands.Bot(command_prefix="bot-")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord and is ready to rock and roll!')

@bot.event
async def on_member_join(member):
    await member.add_roles(734990191776759888)

@bot.command(name='rrole')
async def admit(ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    print ("thing 1")
    await ctx.send(f"hey {ctx.author.name}, {user.name} no longer has the role: {role.name}")
    print ("thing 2")

@bot.command(name='get-mcplayer')
async def getmcplayer(message, arg):
    import requests
    r = requests.get("https://playerdb.co/api/player/minecraft/" + arg)
    f = r.text
    a = json.loads(f)
    usrname = 'Username: ' + str(a['data']['player']['username'])
    uuid = str(a['data']['player']['raw_id'])
    pic = "https://crafatar.com/renders/body/" + uuid
    skindl = "https://crafatar.com/skins/" + uuid
    await message.channel.send(usrname + " Skin render: " + pic)
    await message.channel.send("Skin download: " + skindl)


bot.run('TOKEN')