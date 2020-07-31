
import discord
import readline
import time
import math

client = discord.Client()

@client.event
async def on_ready():
    print('AYYY DA BOT IS THERE AT {0.user}'.format(client))

@client.event
async def on_message(message):
    msgauth = str(message.author)
    if message.author == client.user:
        return

    if message.content.startswith('Copied!'):
        await message.channel.send('Double Copy!')
        print("Handled request")

    if message.content.startswith('Triple Copy!'):
        await message.channel.send('Dominating!!')
        print("Handled request")

    if message.content.startswith('Rampage!!'):
        await message.channel.send('Mega Copy!!')
        print("Handled request")

    if message.content.startswith('bot-get'):
        await message.channel.send('Noticed a get command - attempting to get...')
        print("Handled request")

    if message.content.startswith('bot-help'):
        await message.channel.send('Mainbot commands are: bot-get-hypixnews, bot-get-covstats, and this one. There\'s other hidden ones as well :) As Bodyguard is literally just pulling together lots of opensource projects into one bot, there are other prefixes. The powerful part of the bot uses the prefix :    Enjoy! :) ')

    if message.content.startswith('bot-get-hypixnews'):
        import unicodedata
        from bs4 import BeautifulSoup
        import requests
        import lxml
        sitesource = requests.get("https://hypixel.net/")
        soup = BeautifulSoup(sitesource.text, 'lxml')
        deeper = soup.find("div", class_="block-body block-row").text
        stilldeeper = deeper[0:200] + '...'
        await message.channel.send(stilldeeper)
        await message.channel.send("More at https://hypixel.net")
        print("Handled request")

    if message.content.startswith('bot-get-covstats'):
        import requests
        import json
        r = requests.get('https://covid19-server.chrismichael.now.sh/api/v1/allreports')
        jsonData = open('coronavirus_data','w')
        jsonData.write(r.text)
        jsonData.close
        f = r.text
        a = json.loads(f)
        casecount = 'Total case count: ' + str(a['reports'][0]['cases'])
        deathcount = 'Total death count: ' + str(a['reports'][0]['deaths'])
        recovcount = 'Total recovery count: ' + str(a['reports'][0]['recovered'])
        await message.channel.send(casecount)
        await message.channel.send(deathcount)
        await message.channel.send(recovcount)
        print("Handled request")

    if message.content.startswith('bot-help'):
        await message.channel.send('**If you see ANYTHING wrong with this bot, use :contact to ping me (with a message on the end) I like it when people send me even messages like *the audio failed* and attach the logs. I\'ll put a support server link here.** https://discord.gg/ZZUzRET')
        print("Handled request")

    if message.content.startswith('bot-lfg'):
        msgauth = str(message.author.id)
        msgauth = '<@'+ msgauth +'>'
        mesgtosend = "Hey @here , " + msgauth + " wants to play a game of...".format(client)
        await message.channel.send(mesgtosend)

    if message.content.startswith('bot-lfg-mc'):
        import time
        time.sleep(0.4)
        await message.channel.send('Minecraft!')

    if message.content.startswith('bot-lfg-hypixel'):
        import time
        time.sleep(0.4)
        await message.channel.send('Minecraft on Hypixel! ')

    if message.content.startswith('bot-lfg-ng'):
        import time
        time.sleep(0.4)
        await message.channel.send('Minecraft on Nether Games! ')

    if message.content.startswith('bot-lfg-rr'):
        import time
        time.sleep(0.4)
        await message.channel.send('Realm Royale! ')

    if message.content.startswith('bot-lfg-jsab'):
        import time
        time.sleep(0.4)
        await message.channel.send('Just Shapes and Beats! ')

    if message.content.startswith('bot-lfg-mcb'):
        import time
        time.sleep(0.8)
        await message.channel.send('Bedrock Edition!')

    if message.content.startswith('bot-lfg-hypixel-bedwars'):
        import time
        time.sleep(0.6)
        await message.channel.send('They\'ll be playing Bedwars!')

    if message.content.startswith('bot-lfg-hypixel-skyblock'):
        import time
        time.sleep(0.6)
        await message.channel.send('They\'ll be playing Skyblock')

    if message.content.startswith('bot-lfg-hypixel-duels'):
        import time
        time.sleep(0.6)
        await message.channel.send('They\'ll be playing Duels!')

    if message.content.startswith('bot-lfg-hypixel-pit'):
        import time
        time.sleep(0.6)
        await message.channel.send('They\'ll be playing in the Pit!')

    if message.content.startswith('bot-lfg-hypixel-skywars'):
        import time
        time.sleep(0.6)
        await message.channel.send('They\'ll be playing Skywars')

    if message.content.startswith('bot-lfg-tetris'):
        import time
        time.sleep(0.6)
        await message.channel.send('They\'ll be playing Tetris on https://tetr.io !')

    if message.content.startswith('bot-lfg-ttrs'):
        import time
        time.sleep(0.6)
        await message.channel.send('Tetris on https://tetr.io !')

client.run(TOKEN)
