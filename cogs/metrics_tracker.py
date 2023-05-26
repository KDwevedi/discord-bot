#Track metrics on github and discord and update the database accordingly
#Implement using: https://discordpy.readthedocs.io/en/stable/ext/tasks/index.html?highlight=tasks#
from discord.ext import commands
import os

class MetricsTracker(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

async def setup(bot):
    await bot.add_cog(MetricsTracker(bot))