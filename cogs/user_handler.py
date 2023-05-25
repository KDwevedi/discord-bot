import discord
import os
import dotenv
from discord.ext import commands

class AuthenticationView(discord.ui.View):
    def __init__(self, discord_id):
        super().__init__()  # times out after 120 seconds
        button = discord.ui.Button(label='Authenticate Github', style=discord.ButtonStyle.url, url=f'{os.getenv("FLASK_HOST")}/authenticate/{discord_id}')
        self.add_item(button)
        self.message = None
    




class UserHandler(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot    


    @commands.command(aliases=['join'])
    async def add_user(self, ctx):
        dmchannel = ctx.author.dm_channel if ctx.author.dm_channel else await ctx.author.create_dm()

        view = AuthenticationView(ctx.author.id)

        view.set_msg( await dmchannel.send("Please authenticate your github account to register for Code for GovTech 2023", view=view))
        
        

        



async def setup(bot):
    await bot.add_cog(UserHandler(bot))