import discord
import random
from datetime import date
from datetime import datetime
import time
from discord.enums import Status	
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

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
    print("Prefix is set to == " + prefix + " ==")
    print("Status is set to : " + bot_status + ".")
    print()


@client.event #botV2
async def on_message(message):
    
    if message.author == client.user:
        return
   
    if message.content.startswith(prefix):
        print("Bot found a command symbole")
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

    if message.content.startswith(prefix + "cmd"):
        print(inp + "cmd")
        await message.channel.send("all cmds start with (+) == 1.start == 2.hackerbot == 3.rddiscord == 4.cmd == 5.admin == 7.online == 8.invite == 9.rddcgift == 10.rdinfo ==")
        print(asw + "all cmds start with (+) == 1.start == 2.rddiscord == 3.cmd == 4.admin == 5.online == 6.invite == 7.rddcgift == 8.rdinfo ==")
        print()

    if message.content.startswith(prefix + 'start'):
        print(inp + "start")
        await message.channel.send('ONLINE NOW ' + now.strftime("%d/%m/%Y %H:%M:%S"))
        print(asw + "ONLINE NOW + time")
        print()

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
