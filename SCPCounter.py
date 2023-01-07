import sys
import asyncio
import discord
from discord.ext import commands
from discord.ext import tasks
import requests
cooldowns = 20



@tasks.loop(seconds=cooldowns)
async def counter_update():
    rURL = 'https://api.scpslgame.com/serverinfo.php?id=XXXXX&key=XXXXXXX&players=true'
    try:
        response = requests.get(rURL)
        jsondict = response.json()
        #print('JsonDict: ' + str(jsondict)) "debug"
    
        if (jsondict['Success'] == True):
            players = jsondict['Servers'][0]['Players']
            global cooldowns
            cooldown = jsondict['Cooldown']
            await bot.change_presence(activity=discord.Game(name=players+' Spieler'), status=discord.Status.online)
            print(f'Momentane Spieler:{players} Cooldown:{cooldowns}')
        else:
            print('Request fehlgeschlagen. Fehlernachricht: ' + jsondict['Error'])

    except Exception as e:
        await bot.change_presence(activity=discord.Game(name="Server Offlien!"), status=discord.Status.do_not_disturb)
        print(f'Server antwortet nicht: {e}')
        
@bot.event
async def on_ready():
    print('Bot gestartet')
    counter_update.start()

bot.run('XXXXXXXXXX')

# Die Grundlage kamm von Thy
