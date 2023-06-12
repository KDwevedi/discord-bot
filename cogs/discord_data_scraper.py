from discord.ext import commands, tasks
import os

from utils.db import SupabaseInterface
from utils.api import GithubAPI
import csv


class DiscordDataScaper(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command()
    async def introductions(self, ctx):
        guild = ctx.guild if ctx.guild else await self.bot.fetch_guild(os.getenv("SERVER_ID"))
        intro_channel = await guild.fetch_channel(os.getenv("INTRODUCTIONS_CHANNEL"))
        with open('introduced.csv', 'w') as file:
            writer = csv.writer(file)
            data = []
            async for message in intro_channel.history(limit=None):
                row = [message.author.id]
                if row not in data:
                    count+=1
                    data.append(row)
            writer.writerows(data)
    
    @commands.command()
    async def not_contributors(self, ctx):
        guild = ctx.guild if ctx.guild else await self.bot.fetch_guild(os.getenv("SERVER_ID"))
        orgAndMentors = [role for role in os.getenv("NON_CONTRIBUTOR_ROLES").split(',')]
        with open("not_contributors.csv", "w") as file:
            writer = csv.writer(file)
            data = []
            async for member in guild.fetch_members(limit=None):
                for role in member.roles:
                    if role.id in orgAndMentors:
                        user = [member.name, member.id, member.roles]
                        if user not in data:
                            data.append(user)
            writer.writerows(data)

async def setup(bot):
    await bot.add_cog(DiscordDataScaper(bot))