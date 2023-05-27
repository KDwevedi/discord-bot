#Track metrics on github and discord and update the database accordingly
#Implement using: https://discordpy.readthedocs.io/en/stable/ext/tasks/index.html?highlight=tasks#
from discord.ext import commands
from models.product import Product
import os

class MetricsTracker(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    
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
    


async def setup(bot):
    await bot.add_cog(MetricsTracker(bot))
