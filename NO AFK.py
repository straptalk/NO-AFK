import discord
import json
import colorama
from colorama import Fore
from colorama import Fore as C
from discord.ext import commands
import random
import asyncio
import datetime
import time


client = discord.Client()
prefix = "."
client = commands.Bot(
    command_prefix=prefix,
    self_bot=True
)
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
                 MADE BY Tacey''')


@client.event
async def on_message_delete(message):
  if message.author != client.user:
    print(f'''
Message in {C.BLUE}{message.guild}  {C.RED}deleted{C.RESET}
Author: {C.YELLOW}{message.author}{C.RESET}
Content:\n {message.content}
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
