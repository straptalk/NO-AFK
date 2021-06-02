import discord
import json
import colorama
import random
import asyncio
import datetime
import time
import os

from colorama import Fore
from colorama import Fore as C
from discord.ext import commands

os.system("title NO AFK MADE BY TOUSKI")

prefix = "."

client = discord.Client()
client = commands.Bot(command_prefix=prefix, self_bot=True)
client.remove_command('help') 

print(f'''{Fore.GREEN}
 ███▄    █  ▒█████       ▄▄▄        █████ ▀██ ▄█▀
 ██ ▀█   █ ▒██▒  ██▒    ▒████▄    ▓██      ██▄█▒ 
▓██  ▀█ ██▒▒██░  ██▒    ▒██  ▀█▄  ▒████   ▓███▄░ 
▓██▒  ▐▌██▒▒██   ██░    ░██▄▄▄▄██ ░▓█▒    ▓██ █▄ 
▒██░   ▓██░░ ████▓▒░     ▓█   ▓██▒░▒█░    ▒██▒ █▄
░ ▒░   ▒ ▒ ░ ▒░▒░▒░      ▒▒   ▓▒█░ ▒ ░    ▒ ▒▒ ▓▒
░ ░░   ░ ▒░  ░ ▒ ▒░       ░   ▒▒ ░ ░      ░ ░▒ ▒░
   ░   ░ ░ ░ ░ ░ ▒        ░   ▒    ░ ░    ░ ░░ ░ 
         ░     ░ ░            ░  ░        ░  ░   
                 MADE BY Touski
                github : TheyLoveTouski
''')


@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
      time.sleep(1)
      await message.channel.send(random.choice(['wtf', 'son', 'jtd', 'L','nope', 'lol', 'stfu', 'focus','idc','1','.',';','noep','tf','ok','nig','lo','sjc','a','b','?','no','sudusb','??','ewr','j6te','6trhj','4y5h','ehyh yr','ik','ky75','uyt','u7k','sdu' ]))
        
with open('./config.json')as f:
  config = json.load(f)

token = config.get('token')
client.run(token, bot=False)
