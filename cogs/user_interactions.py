import discord
import os
from discord.ext import commands, tasks
import time, csv
from utils.db import SupabaseInterface
from utils.api import GithubAPI



#This is a Discord View that is a set of UI elements that can be sent together in a message in discord.
#This view send a link to Github Auth through c4gt flask app in the form of a button.
class AuthenticationView(discord.ui.View):
    def __init__(self, discord_userdata):
        super().__init__()
        button = discord.ui.Button(label='Authenticate Github', style=discord.ButtonStyle.url, url=f'{os.getenv("FLASK_HOST")}/authenticate/{discord_userdata}')
        self.add_item(button)
        self.message = None

class UserHandler(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    #Executing this command sends a link to Github OAuth App via a Flask Server in the DM channel of the one executing the command 
    @commands.command(aliases=['join'])
    async def join_as_contributor(self, ctx):
        #create a direct messaging channel with the one who executed the command
        dmchannel = ctx.author.dm_channel if ctx.author.dm_channel else await ctx.author.create_dm()
        userdata = str(ctx.author.id)
        view = AuthenticationView(userdata)
        await dmchannel.send("Please authenticate your github account to register for Code for GovTech 2023", view=view)

     



    

    @commands.command()
    async def announce(self, ctx):
        guild = ctx.guild if ctx.guild else await self.bot.fetch_guild(os.getenv("SERVER_ID"))
        count = 0
        with open('introduced.csv', 'w') as file:
            writer = csv.writer(file)
            data = []
            
        print(count)

        # async for member in guild.fetch_members(limit=None):
        #     print(member.id)
        #     count+=1
        # print(count)
        # members = [476285280811483140]
        # for member_id in members:
            # member = await guild.fetch_member(member_id)
            # dmchannel = member.dm_channel if member.dm_channel else await member.create_dm()
            # await dmchannel.send("Test Announcement")



    @commands.command()
    async def test(self,ctx):
        # print(os.getenv("SERVER_ID"))
        guild = await self.bot.fetch_guild(os.getenv("SERVER_ID"))
        channel = await guild.fetch_channel(973851473131761677)
        async for message in channel.history(limit=20):
            print(message.content, type(message.content))
            if message.content == '':
                print(True)

    @commands.command(aliases=["my_points"])
    async def get_points(self, ctx):
        if ctx.author.id not in [1042682119035568178,476285280811483140]:
            message = f"""Hey, {ctx.author.name}! This command isn't available to unregistered users as of now and will become operational with the rollout of the complete point system!"""
            await ctx.channel.send(message)
        else:
            points_message =f"""Hey {ctx.author.name}

**You have a total of 150 points**🌟 

▶️**Points Basis PRs raised - 20 points**🔥 

▶️ **Points Basis PRs accepted - 70 points**🔥 

Number of tickets solved - 5
Points on tickets with low complexity - 30 points
Points on tickets with medium complexity - 40 points
Points of tickets with high complexity - 0 points

▶️ **Points as per PRs reviewed - 30 points**🙌 

Number of tickets reviewed - 2
Points on tickets with low complexity - 10 points
Points on tickets with medium complexity - 20 points
Points of tickets with high complexity - 0 points


▶️ **Total points for Discord  Engagement- 10 points**🤙 


▶️**Total points for GitHub Engagement- 20 points**😎 


Woah, awesome! Get coding and earn more points to get a spot on the leaderboard📈"""
            await ctx.channel.send(points_message)

    @commands.command(aliases=["point_system_breakdown", "point_system"])
    async def point_breakdown(self, ctx):
        if ctx.author.id not in [1042682119035568178,476285280811483140]:
            message = f"""Hey, {ctx.author.name}! This command isn't available to unregistered users as of now and will become operational with the rollout of the complete point system!"""
            await ctx.channel.send(message)
        else:
            message = f"""Hey **{ctx.author.name}**

Points are allocated on the following basis📊 :

▶️ **Number of PRs raised** 
🚀  **x points per ticket are given** 

▶️ **Number of PRs accepted** 

🚀  **10 points per ticket are given** 
🚀 **Get more points for complex tickets**

- 1x for Low Complexity 
- 2x for Medium Complexity
- 3x for High Complexity

▶️ **Number of PRs reviewed** 

🚀 **10 points per ticket for those who have been made a maintainer to review PRs** 
🚀  **Get more points for complex tickets**

- 1x for Low Complexity 
- 2x for Medium Complexity
- 3x for High Complexity

▶️ **Engagement on Discord & GitHub** 

🚀  **Discord**

- Engage with community via messages across channels to get x points

🚀 **GitHub**

- Engage with the community via x comments & messages on repositories to get x points."""
            await ctx.channel.send(message)
     


        return

dummy_data = {
    "total":190,
    "tickets": {
        "low":2,
        "medium":2,
        "high":2
    },
    "prs":{
        "low":1,
        "medium":1,
        "high":0,
    },
    "discord":{
        "intro":1,
        "other":30,
    },
    "github": {
        "messages":15
    }

}
     
async def setup(bot):
    await bot.add_cog(UserHandler(bot))



