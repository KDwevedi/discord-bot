import discord
from discord.ext import commands
import os, sys
import asyncio
import dotenv

#Since there are user defined packages, adding current directory to python path
current_directory = os.getcwd()
sys.path.append(current_directory)

dotenv.load_dotenv(".env")
intents = discord.Intents.all()

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# @client.command()
# async def check(ctx,*, channel):
#     await ctx.send("test:"+ channel)
#     if channel == '':
#         await ctx.send('Hello')
#     else:
#         channel = await client.fetch_channel(1110103698761334846)
#         async for message in channel.history(limit=50):
#             await ctx.send(message.author)

        

# @client.command()
# async def ping(ctx):
#     await ctx.send("Pong")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start(os.getenv("TOKEN"))


asyncio.run(main())

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')
    
#     if message.content.startswith('$test'):
#         channel = await client.fetch_channel(1110103698761334846)
#         await channel.send("Hello")
#         # for channel in client.get_all_channels():

#         #     if isinstance(channel, discord.channel.TextChannel):
#         #         await message.channel.send(await channel.webhooks())


        


