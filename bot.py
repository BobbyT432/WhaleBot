import os
import discord
import random
import time
from discord.ext import commands
from discord import FFmpegPCMAudio

# NOTE: DOTENV IS NOT WORKING
#from dotenv import load_dotenv # this is used to read the environment variable from the .env file

#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN') # reads the discord token var from the .env file



#client = discord.Client() # connection to discord

#@client.event
#async def on_ready(): # when the client has connected to discord, this function runs
#    print(f'{client.user} has connected to Discord!')

#@client.event
#async def on_message(message):
#    if message.author == client.user: # prevents the bot responding to itself and creating a recursive function
#        return
#    
#    if message.content == 'whale' or message.content == 'Whale':
#        response = "*Whale Noise*"
#        await message.channel.send(response)
#    elif message.content == 'raise-exception': # since this is an event, it could raise an exception
#        raise discord.DiscordException

bot = commands.Bot(command_prefix='!') # discord has a library for commands

# bot makes it easier to run commands 
@bot.command(name='whale', help='Blesses you with a majestic whale sound')
async def whale(ctx):
    response = "*Whale Noise*"
    await ctx.send(response)
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio('sound/whale.mp3'))
    time.sleep(7)
    await ctx.voice_client.disconnect()


@bot.command(name='add', help='Adds two numbers.')
async def add(msg, num1 : int, num2: int):
    await msg.send(num1 + num2)

@bot.event
async def on_voice_state_update(member, before, after):
    channel = before.channel or after.channel
    test = bot.get_channel(897345529627938898)
    if channel.id == 645074016872169495: 
        await test.send("Test")
        voice_channel = member.voice.channel
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio('sound/whale.mp3'))
        time.sleep(7)
        await vc.disconnect()

# need to learn exception handling with bot



bot.run("ODk4MzQ4MjczNjI1MDcxNjM2.YWi6Bg.lkMkmb-JPayYKDYike8gqQy71zo")
#https://stackoverflow.com/questions/51234778/what-are-the-differences-between-bot-and-client
#client.run("ODk4MzQ4MjczNjI1MDcxNjM2.YWi6Bg.lkMkmb-JPayYKDYike8gqQy71zo") # this is the bots special token, it must be kept secure as its important, I stored the token in the .env file (that way it can just be read from there)
# Instead of calling TOKEN, I just pasted the token in as it was not working