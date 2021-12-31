import discord
import random
from datetime import date
from datetime import datetime
import time
from discord import channel
from discord import member
from discord.enums import Status	
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

from discord.role import Role

git = "https://github.com/ian4u/bot-public/tree/main"
bot = commands.Bot(command_prefix="+")
Admin = "IAN#2241"
client = discord.Client()
prefix = '+'
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
inp = "comand was : "
asw = "bot put out : "
bot_status = "Can be used"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))




@client.event #botV2
async def on_message(message):
    
    if message.author == client.user:
        return
   
    if message.content.startswith(prefix):
        print("Bot found a command symbole")
        print(message.content)
        print("The commad was ended successful")
        print()

    if message.content.startswith(prefix + "cmd"):
        print(inp + "cmd")
        await message.channel.send("all cmds start with (+) == 1.rdinfo == 2.cmd (this tool) == 3.rddiscord == 4.rddcgift == 5.chance == 6.online == 7.invite == 8.github ==")
        print(asw + "all cmds start with (+) == 1.rdinfo == 2.cmd (this tool) == 3.rddiscord == 4.rddcgift == 5.chance == 6.online == 7.invite == 8.github ==")
        print() 
    
    if message.content.startswith(prefix + "token"):
        print(inp + "token")
        token_1 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_') for i in range(24)))
        token_2 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for i in range(4)))
        token_3 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for i in range(27)))
        await message.channel.send(token_1 + ".Yb" + token_2 + "." + token_3 )
        print(asw + token_1 + ".Yb" + token_2 + "." + token_3)

    if message.content.startswith(prefix + "rdinfo"):
        print(inp + "rdinfo")
        await message.channel.send("These codes are just for testgin perpus only if u use them against the discord tos you have to think about the following ")
        print(asw + "These codes are just for testgin perpus only if u use them against the discord tos you have to think about the following")


    if message.content.startswith(prefix + "rddiscord"):
        print(inp + "rddiscord")
        num = 0
        while num < 30:
            result_str = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for i in range(8)))
            await message.channel.send("discord.gg/" + result_str )
            print(asw + "discord.gg/" + result_str )
            print()
            time.sleep(2)
            num = num + 1

    if message.content.startswith(prefix + "rddcgift"):
        num_2 = 1
        print(inp + "rddcgift")
        while num_2 < 30:

            result_str2 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for i in range(16)))
            await message.channel.send("discord.gift/" + result_str2 )
            print(asw + "discord.gift/" + result_str2)
            print()
            time.sleep(2)
            num_2 = num_2 + 1 

    if message.content.startswith(prefix + "chance"):
        print(inp + "chance")
        can1 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for i in range(2)))
        can2 = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for i in range(2)))
        await message.channel.send(can1 + "." + can2 + "%")
        print(asw + can1 + "." + can2 + "%")
        print()

    if message.content.startswith(prefix + "online"):
        print(inp + "online")
        await message.channel.send("If the bot is not online pls inform IAN#2241")
        print(asw + "If the bot is not online pls inform IAN#2241")
        print()
    
    if message.content.startswith(prefix + "invite"):
        print(inp + "invite")
        await message.channel.send("The invite link is | https://discord.com/api/oauth2/authorize?client_id=916653706966085663&permissions=8&scope=bot |")
        print(asw + "The invite link is | https://discord.com/api/oauth2/authorize?client_id=916653706966085663&permissions=8&scope=bot |")
        print()

    if message.content.startswith(prefix + "github"):
       await message.channel.send("The public link from my bot is : " + git)

    if message.content.startswith(prefix + "testoutput"):
        if str(message.author) == str(Admin):
            await message.channel.send(str(message.author))
            await message.channel.send("Has send Command: " + message.content)
            await message.channel.send("Bot is login as: " + str(client.user))

    if message.content.startswith(""):
        if message.author == client.user:
            return
        if str(message.author) == str("Ianshub#7786"):
            return
        else:
            channel = client.get_channel(926490522166652969)
            await channel.send(str(message.author) + " did send: " + str(message.content))
