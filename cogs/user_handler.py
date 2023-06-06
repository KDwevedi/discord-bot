import discord
import os
import dotenv
from discord.ext import commands, tasks
from utils.db import SupabaseInterface

#This is a Discord View that is a set of UI elements that can be sent together in a message in discord.
#This view send a link to Github Auth through flask app in the form of a button.
class AuthenticationView(discord.ui.View):
    def __init__(self, discord_userdata):
        super().__init__()
        button = discord.ui.Button(label='Authenticate Github', style=discord.ButtonStyle.url, url=f'{os.getenv("FLASK_HOST")}/authenticate/{discord_userdata}')
        self.add_item(button)
        self.message = None

class UserHandler(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.supabase = SupabaseInterface()


    @commands.command(aliases=['join'])
    async def add_user(self, ctx, arg):
        dmchannel = ctx.author.dm_channel if ctx.author.dm_channel else await ctx.author.create_dm()
        Roles = ['contributor', 'mentor', 'org']
        if arg.lower() not in Roles:
            await ctx.channel.send("Invalid Role")
            return 
        if arg.lower() =='org':
            await ctx.channel.send('''Adding org roles isn't figured out yet''')
        if arg.lower() =='mentor':
            await ctx.channel.send('''Joining as mentor needs to be defined''')
            #Verify mentor
            return

        userdata = str(ctx.author.id)+'$'+ctx.author.name+'$'+arg.lower()
        view = AuthenticationView(userdata)
        await dmchannel.send("Please authenticate your github account to register for Code for GovTech 2023", view=view)
    
    @tasks.loop(seconds=5.0, count=18)
    async def user_is_registered(self, ctx, discord_id):
        if self.supabase.user_exists(discord_id=discord_id):
            self.user_is_registered.cancel()
    
    # @user_is_registered.before_loop
    # async

        
        

        



async def setup(bot):
    await bot.add_cog(UserHandler(bot))