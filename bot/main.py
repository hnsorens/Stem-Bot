import discord
import os
from discord.ext import commands
from datetime import datetime
import asyncio

client = commands.Bot(command_prefix='!')

#variables
SocrativeAnswer = 'Unknown'
SocrativeTime = 'Unknown'
started = False
dm = 0

@client.event
async def on_ready():
  print('We have logged in as (0.user)'.format(client))

@client.event
async def on_message(message):
  global started
  if (message.content.startswith("!STARTDMSERVER") and started == False):
    global dm
    dm = message.author
    started = True

@client.event
async def on_message_delete(message):
  await dm.send(message.author)
  await dm.send(message.content)
  await dm.send(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
  await dm.send('__ __')

#@client.command()
##async def dm(ctx):
#  await ctx.author.send('k')

#@client.command()
#async def socrative(client,arg):
#  global SocrativeAnswer
#  global SocrativeTime
#  print(arg)
#  [command, answer] = socrative
#  SocrativeAnswer = answer
#  SocrativeTime = datetime.now().strftime("%m/%d")
  #await message.channel.send('the new socrative answers are ' + SocrativeAnswer + ' on ' + SocrativeTime)
  
#@client.event
#async def on_message(message):
#  global SocrativeAnswer
#  global SocrativeTime
#  if message.author == client.user:
#    return

  
#  if message.content.startswith('$socrative'):
#    socrative = message.content.split(" ", 2)
#    print(socrative)
#    [command, answer] = socrative
#    SocrativeAnswer = answer
#    SocrativeTime = datetime.now().strftime("%m/%d")
#    await message.channel.send('the new socrative answers are ' + SocrativeAnswer + ' on #' + SocrativeTime)
#    
#  if message.content.startswith('+socrative'):
#    print(SocrativeAnswer)
#    await message.channel.send('the socrative answers are ' + SocrativeAnswer + ' on ' + #SocrativeTime)
#  if message.content.startswith('+test'):
#    await client.send_message(message.author,"k")
#@client.event
#async def on_message_delete(message):
#  if message.author == client.user:
#    return
#  await message.send_message(message.author,'hi')
  


client.run(os.getenv('TOKEN'))
