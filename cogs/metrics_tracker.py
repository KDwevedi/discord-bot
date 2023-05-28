#Track metrics on github and discord and update the database accordingly
#Implement using: https://discordpy.readthedocs.io/en/stable/ext/tasks/index.html?highlight=tasks#
from discord.ext import commands, tasks
from datetime import time, datetime
from models.product import Product
from models.project import Project
from utils.api import GithubAPI
import os

class MetricsTracker(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.measure_times = [
            time(hour = 12, )
        ]
        self.test_task.start()
    
    
    #Command to assign a channel to a product
    @commands.command(aliases=['product','assign', 'assign channel', 'add channel'])
    #@commands.has_any_role([])
    @commands.has_permissions(administrator=True)
    async def assign_channel_to_product(self, ctx, product_name=None):

        #Check if product name was given
        if product_name is None:
            await ctx.channel.send("This command expects the name of the product as an argument like '!assign <product name>'")
            return

        #Check if channel is a valid type
        if str(ctx.channel.type) not in ['text']:
            await ctx.channel.send("Only text channels may be assigned to products")
            return
        

        #Check if given product name 
        if not Product.is_product(product_name):
            await ctx.channel.send("This is not a valid product name. Please try again.")
            return
        
        
        product = Product(name=product_name)
        product.assign_channel(ctx.channel.id)
        await ctx.channel.send(f"Channel successfully assigned to product {product_name}")
        return
    
    #error handling for assigning channel to product
    @assign_channel_to_product.error
    async def handle_assignment_error(self, ctx, error):
        pass

    async def get_discord_metrics(self, ctx):
        products = Product.get_all_products()

        print(products)

        discord_metrics = {
            "measured_at": datetime.now(),
            "metrics": dict()
        }

        for product in products:
            discord_metrics["metrics"][product['name']] = {
                "mentor_messages": 0,
                "contributor_messages": 0
            }
            channel_id = product["channel"]
            channel = await self.bot.fetch_channel(channel_id)

            await ctx.channel.send(channel)
            
            async for message in channel.history(limit=None):
                if any(role.name.lower() == 'mentor' for role in message.author.roles):
                    discord_metrics["metrics"][product['name']]['mentor_messages'] +=1
                
                if any(role.name.lower() == 'contributor' for role in message.author.roles):
                    discord_metrics["metrics"][product['name']]['contributor_messages'] +=1

        # send this to the server instead
        await ctx.channel.send(discord_metrics)
        return
    
    async def get_github_metrics(self, ctx):

        #Get all projects in the db
        projects = Project.get_all_projects()

        github_metrics = {
            "updated_at": datetime.now(),
            "metrics": dict()
        }

        for project in projects:
            url_components = str(project['repository']).split('/')
            url_components = [component for component in url_components if component != '']
            print(url_components)
            [protocol, host, repo_owner, repo_name] = url_components
            api = GithubAPI(owner=repo_owner, repo=repo_name)


            github_metrics["metrics"][project["product"]] = {
                "project": project["name"],
                "repository": project["repository"],
                "total_commits":  api.get_commit_count()
            }
        
        await ctx.channel.send(github_metrics)

        return
    
    @tasks.loop(seconds=5.0)
    async def test_task(self):
        print("Periodic task is running")

    @commands.command(aliases=['metrics'])
    # @tasks.loop(seconds=10.0)
    async def update_metrics_periodically(self, ctx):
        # Discord Metrics
        await self.get_discord_metrics(ctx)
        await self.get_github_metrics(ctx)

        

        # Github Metrics
        #   Get repo url
        #   Fetch metrics
        #   Update metrics
        return
    


async def setup(bot):
    await bot.add_cog(MetricsTracker(bot))
