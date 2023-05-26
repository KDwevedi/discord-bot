import discord
import os
import dotenv
from discord.ext import commands

class AuthenticationView(discord.ui.View):
    def __init__(self, discord_userdata):
        super().__init__()  # times out after 120 seconds
        button = discord.ui.Button(label='Authenticate Github', style=discord.ButtonStyle.url, url=f'{os.getenv("FLASK_HOST")}/authenticate/{discord_userdata}')
        self.add_item(button)
        self.message = None
    




class UserHandler(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot    


    @commands.command(aliases=['join'])
    async def add_user(self, ctx):
        dmchannel = ctx.author.dm_channel if ctx.author.dm_channel else await ctx.author.create_dm()


        userdata = str(ctx.author.id)+'$'+ctx.author.name

        view = AuthenticationView(userdata)


        await dmchannel.send("Please authenticate your github account to register for Code for GovTech 2023", view=view)
        
        

        



async def setup(bot):
    await bot.add_cog(UserHandler(bot))