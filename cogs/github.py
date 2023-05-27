import discord
import os
import dotenv
from discord.ext import commands

class GithubTracking(commands.Cog):
    def __init__(self, bot):
        self.bot  = bot
        self.guild = None

    @commands.Cog.listener()
    async def on_ready(self):
        # print('ready')
        self.guild = await self.bot.fetch_guild(os.getenv("SERVER_ID"))
        webhooks = await self.guild.webhooks()
        # print(webhooks[0].url)
    
    # async def get_updates(self, project):
    #     #Gets updates regarding a project


    
    # @commands.command()
    # async def create_webhook():


async def setup(bot):
    await bot.add_cog(GithubTracking(bot))