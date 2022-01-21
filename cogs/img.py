# importing libs
import discord
from discord.ext import commands
import nekos

# initializing cog
class imgCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command() # sends random cat image
    async def cat(self, ctx):
        catimg = nekos.cat()
        await ctx.send(catimg)

    @commands.command() # sends random dog image
    async def dog(self, ctx):
        dogimg = nekos.img("woof")
        await ctx.send(dogimg)

    @commands.command() # sends random goose image
    async def goose(self, ctx):
        gooseimg = nekos.img("goose")
        await ctx.send(gooseimg)

    @commands.command() # sends randomly generated anime girl
    async def waifu(self, ctx):
        waifuimg = nekos.img("waifu")
        await ctx.send(waifuimg)

    @commands.command() # sends random lizard image
    async def lizard(self, ctx):
        lizardimg = nekos.img("lizard")
        await ctx.send(lizardimg)

    @commands.command() # sends random anime tickle image
    async def tickle(self, ctx):
        tickleimg = nekos.img("tickle")
        await ctx.send(tickleimg)

    @commands.command() # sends random anime slap image
    async def slap(self, ctx):
        slapimg = nekos.img("slap")
        await ctx.send(slapimg)

    @commands.command() # sends random anime pat image
    async def pat(self, ctx):
        patimg = nekos.img("pat")
        await ctx.send(patimg)

    @commands.command() # sends random anime neko image
    async def neko(self, ctx):
        nekoimg = nekos.img("neko")
        await ctx.send(nekoimg)

    @commands.command() # sends random anime cuddle image
    async def cuddle(self, ctx):
        cuddleimg = nekos.img("cuddle")
        await ctx.send(cuddleimg)

    @commands.command() # sends random anime foxgirl image
    async def foxgirl(self, ctx):
        foximg = nekos.img("fox_girl")
        await ctx.send(foximg)

# makes the cog be recognized by the bot
def setup(bot: commands.Bot):
    bot.add_cog(imgCog(bot))