import discord
import os
import dotenv

dotenv.load_dotenv(".env")
#What are intents?
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$test'):
        await message.channel.send(client.guilds)


client.run(os.getenv("TOKEN"))