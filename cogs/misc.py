import discord
from discord.ext import commands
import nekos

class miscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() # will tell the user if they are cool or not
    async def cool(self, ctx):
        randnum = random.randint(1, 2) # picks between 1 or 2
        if randnum == 1: # if it picks 1
            await ctx.send("You are cool!") # say they are cool
        else: # otherwise
            await ctx.send("You are not cool!") # say they arent cool

    @commands.command() # will flip a coin (Heads/Tails), basically same code from cool, but changed the output
    async def coinflip(self, ctx):
        randnum = random.randint(1, 2)
        if randnum == 1:
            await ctx.send("Heads!")
        else:
            await ctx.send("Tails!")

    @commands.command() # will send a Rick-Roll
    async def token(self, ctx):
        await ctx.send("Here is my Token: <https://www.youtube.com/watch?v=dQw4w9WgXcQ>") # sends link to rickroll with <> to prevent the embed

    @commands.command() # make the Bot say stuff
    async def say(self, ctx, *, wordsToSay): # puts whatever text the user says into a variable
        await ctx.send(wordsToSay) # sends the text in the variable

    @commands.command() # dm people, @ them then put the message, idk what the code does i took it from daniel
    #@commands.is_owner() # checks if the person running it is the owner
    async def dm(self, ctx, member: discord.Member, *,  msg=None):
            await ctx.reply(
                f"I have sent that message to: {member.mention}", delete_after=3.0)
            await member.send(
                msg)
            await ctx.message.delete()

    @commands.command() # get avatar of user, again idk what the code does i took it from daniel
    async def avatar(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
            await ctx.send(member.avatar_url)

    @commands.command() # magic 8-ball command (very optimzied lol)
    async def eightball(self, ctx, eightballquestion):
        randballnum = random.randint(1, 20) # picks random number between 1 and 20, then sends an answer that is connected to the number through else ifs
        if randballnum == 1:
            await ctx.send("It is certain.")
        elif randballnum == 2:
            await ctx.send("It is decidedly so.")
        elif randballnum == 3:
            await ctx.send("Without a doubt.")
        elif randballnum == 4:
            await ctx.send("Yes – definitely.")
        elif randballnum == 5:
            await ctx.send("You may rely on it.")
        elif randballnum == 6:
            await ctx.send("As I see it, yes.")
        elif randballnum == 7:
            await ctx.send("Most likely.")
        elif randballnum == 8:
            await ctx.send("Outlook good.")
        elif randballnum == 9:
            await ctx.send("Yes.")
        elif randballnum == 10:
            await ctx.send("Signs point to yes.")
        elif randballnum == 11:
            await ctx.send("Reply hazy, try again.")
        elif randballnum == 12:
            await ctx.send("Ask again later.")
        elif randballnum == 13:
            await ctx.send("Better not tell you now.")
        elif randballnum == 14:
            await ctx.send("Cannot predict now.")
        elif randballnum == 15:
            await ctx.send("Concentrate and ask again.")
        elif randballnum == 16:
            await ctx.send("Don't count on it.")
        elif randballnum == 17:
            await ctx.send("My reply is no.")
        elif randballnum == 18:
            await ctx.send("My sources say no.")
        elif randballnum == 19:
            await ctx.send("Outlook not so good.")
        elif randballnum == 20:
            await ctx.send("Very doubtful.")
        else:
            await ctx.send("An error has occurred.") # if there is no number for some reason, send that

    @commands.command() # sends random fact
    async def fact(self, ctx):
        fact = nekos.fact()
        await ctx.send(fact)

    @commands.command() # owoify text
    async def owoify(self, ctx, *wantowoed): # stores the users text in the wantowoed variable
        str = convertTuple(wantowoed)
        userowo = nekos.owoify(str)
        await ctx.send(userowo)

    @commands.command() # reddit.com/r/showerthoughts type of thing
    async def showerthought(self, ctx):
        shwrthought = nekos.why()
        await ctx.send(shwrthought)

def setup(bot: commands.Bot):
    bot.add_cog(miscCog(bot))