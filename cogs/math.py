# importing libs
import discord
from discord.ext import commands

# initializing cog
class mathCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command() # add some numbers up
    async def add(self, ctx, left: int, right: int): # user inputs 2 numbers
        await ctx.send(left + right) # bot adds them together and sends answer

    @commands.command()# subtraction
    async def subtract(self, ctx, left: int, right: int): # user inputs 2 numbers
        await ctx.send(left - right) # bot subtracts them and sends answer

    @commands.command() # divide
    async def divide(self, ctx, left: int, right: int): # user inputs 2 numbers
        await ctx.send(left / right) # bot divides them and sends answer

    @commands.command() # times tables
    async def multiply(self, ctx, left: int, right: int): # user inputs 2 numbers
        await ctx.send(left * right) # bot multiplies them and sends answer

# makes the cog be recognized by the bot
def setup(bot: commands.Bot):
    bot.add_cog(mathCog(bot))