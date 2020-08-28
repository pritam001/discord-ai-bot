import os
from os.path import join, dirname

from discord import Client
from dotenv import load_dotenv
import discord

client: Client = discord.Client()
dotenv_path: str = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

PING_PY_BOT_TOKEN: str = os.environ.get('PING_PY_BOT_TOKEN')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print("message received")
    if message.author == client.user:
        return

    if message.content.lower().find('hello') != -1:
        await message.channel.send('HELLO!')

    if message.content.lower().find('ping') != -1:
        await message.channel.send('PONG!')

print(PING_PY_BOT_TOKEN)
client.run(PING_PY_BOT_TOKEN)
