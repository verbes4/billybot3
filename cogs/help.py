# importing libs
import discord
from discord.ext import commands

# initializing cog
class helpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() # "$help" command
    async def help(self, ctx):
        embed = discord.Embed(title="Help Page 1", color=0xff0000) # setting up embed
        embed.add_field(name="$add num1 num2", value="Billy will add 2 numbers.", inline = False)
        embed.add_field(name="$subtract num1 num2", value="Billy will subtract 2 numbers.", inline=False)
        embed.add_field(name="$divide num1 num2", value="Billy will divide 2 numbers.", inline=False)
        embed.add_field(name="$multiply num1 num2", value="Billy will multiply 2 numbers.", inline=False)
        embed.add_field(name="$coinflip", value="Billy will flip a coin.", inline=False)
        embed.add_field(name="$token", value="Billy will give you his token.", inline=False)
        embed.add_field(name="$say text here", value="Billy will say your text.", inline=False)
        embed.add_field(name="$avatar @user", value="Billy will give you the avatar of whoever you ping.", inline=False)
        embed.add_field(name="$eightball question", value="Ask Billy a question.", inline=False)
        embed.set_footer(text="Bot by verbes4#8839 <3")
        await ctx.send(embed=embed) # bot sends embed

    @commands.command() # help command page 1
    async def help1(self, ctx):
        embed = discord.Embed(title="Help Page 1", color=0xff0000) # setting up embed
        embed.add_field(name="$add num1 num2", value="Billy will add 2 numbers.", inline = False)
        embed.add_field(name="$subtract num1 num2", value="Billy will subtract 2 numbers.", inline=False)
        embed.add_field(name="$divide num1 num2", value="Billy will divide 2 numbers.", inline=False)
        embed.add_field(name="$multiply num1 num2", value="Billy will multiply 2 numbers.", inline=False)
        embed.add_field(name="$coinflip", value="Billy will flip a coin.", inline=False)
        embed.add_field(name="$token", value="Billy will give you his token.", inline=False)
        embed.add_field(name="$say text here", value="Billy will say your text.", inline=False)
        embed.add_field(name="$avatar @user", value="Billy will give you the avatar of whoever you ping.", inline=False)
        embed.add_field(name="$eightball question", value="Ask Billy a question.", inline=False)
        embed.add_field(name="$cat", value="Billy will send a cat.", inline = False)
        embed.set_footer(text="Bot by verbes4#8839 <3")
        await ctx.send(embed=embed) # bot sends embed

    @commands.command() # help command page 2
    async def help2(self, ctx):
        embed = discord.Embed(title="Help Page 2", color=0xff0000) # setting up embed
        embed.add_field(name="$fact", value="Billy will send a random fact.", inline=False)
        embed.add_field(name="$dog", value="Billy will send a dog.", inline=False)
        embed.add_field(name="$goose", value="Billy will send a goose.", inline=False)
        embed.add_field(name="$waifu", value="Billy will send a randomly generated waifu.", inline=False)
        embed.add_field(name="$lizard", value="Billy will send a lizard.", inline=False)
        embed.add_field(name="[NSFW] $feet", value="Billy will send anime feet.", inline=False)
        embed.add_field(name="[NSFW] $yuri", value="Billy will send lesbian anime porn.", inline=False)
        embed.add_field(name="[NSFW] $trap", value="Billy will send a trap.", inline=False)
        embed.add_field(name="[NSFW] $futa", value="Billy will send futa porn.", inline=False)
        embed.add_field(name="[NSFW] $spank", value="Billy will send anime spanking porn.", inline=False)
        embed.set_footer(text="Bot by verbes4#8839 <3")
        await ctx.send(embed=embed) # bot sends embed

    @commands.command() # help command page 3
    async def help3(self, ctx):
        embed = discord.Embed(title="Help Page 3", color=0xff0000) # setting up embed
        embed.add_field(name="[NSFW] $cum", value="Billy will send anime cum porn.", inline=False)
        embed.add_field(name="$tickle", value="Billy will send a tickle.", inline=False)
        embed.add_field(name="[NSFW] $bj", value="Billy will send an anime BJ.", inline=False)
        embed.add_field(name="[NSFW] $gasm", value="Billy will send a gasm.", inline=False)
        embed.add_field(name="[NSFW] $anal", value="Billy will send anime anal.", inline=False)
        embed.add_field(name="$slap", value="Billy will send a slap.", inline=False)
        embed.add_field(name="[NSFW] $hentai", value="Billy will send hentai.", inline=False)
        embed.add_field(name="[NSFW] $pussy", value="Billy will send anime pussy.", inline=False)
        embed.add_field(name="[NSFW] $tits", value="Billy will send anime tits.", inline=False)
        embed.add_field(name="$pat", value="Billy will send a pat.", inline=False)
        embed.set_footer(text="Bot by verbes4#8839 <3")
        await ctx.send(embed=embed) # bot sends embed

    @commands.command() # help command page 4
    async def help4(self, ctx):
        embed = discord.Embed(title="Help Page 4", color=0xff0000) # setting up embed
        embed.add_field(name="[NSFW] $kiss", value="Billy will send a kiss.", inline=False)
        embed.add_field(name="[NSFW] $femdom", value="Billy will send anime femdom porn.", inline=False)
        embed.add_field(name="[NSFW] $spank", value="Billy will send anime spanking porn.", inline=False)
        embed.add_field(name="$neko", value="Billy will send an anime neko.", inline=False)
        embed.add_field(name="$cuddle", value="Billy will send a cuddle.", inline=False)
        embed.add_field(name="$foxgirl", value="Billy will send a foxgirl.", inline=False)
        embed.add_field(name="$owoify text here", value="Billy will owoify your text.", inline=False)
        embed.add_field(name="$showerthought", value="Like the SubReddit.", inline=False)
        embed.set_footer(text="Bot by verbes4#8839 <3")
        await ctx.send(embed=embed) # bot sends embed

# makes the cog be recognized by the bot
def setup(bot: commands.Bot):
    bot.add_cog(helpCog(bot))