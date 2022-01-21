# importing libs
import discord
from discord.ext import commands
import random
import logging
import nekos

logging.basicConfig(level=logging.INFO) # logging stuff

# important stuff
intents = discord.Intents.default()
#bot = discord.Client() <-- dont uncomment lol
bot = commands.Bot(command_prefix="$", help_command=None, intents=intents)

@bot.event # checks if bot is logged in
async def on_ready():
    print(f'We have logged in as {bot.user}') # when the bot is logged in, show it in console
    print(f'Discord version: {discord.__version__}') # print the discord version too
    await bot.change_presence(activity=discord.Game(name="$help1 | Made by verbes4#8839")) # and then set the bots activity

# skidded code to convert a tuple into a string
def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
        str = str + " "
    return str

# load cogs
bot.load_extension('cogs.nsfw')
bot.load_extension('cogs.math')
bot.load_extension('cogs.img')
bot.load_extension('cogs.help')

@bot.command() # will tell the user if they are cool or not
async def cool(ctx):
    randnum = random.randint(1, 2) # picks between 1 or 2
    if randnum == 1: # if it picks 1
        await ctx.send("You are cool!") # say they are cool
    else: # otherwise
        await ctx.send("You are not cool!") # say they arent cool

@bot.command() # will flip a coin (Heads/Tails), basically same code from cool, but changed the output
async def coinflip(ctx):
    randnum = random.randint(1, 2)
    if randnum == 1:
        await ctx.send("Heads!")
    else:
        await ctx.send("Tails!")

@bot.command() # will send a Rick-Roll
async def token(ctx):
    await ctx.send("Here is my Token: <https://www.youtube.com/watch?v=dQw4w9WgXcQ>") # sends link to rickroll with <> to prevent the embed

@bot.command() # make the Bot say stuff
async def say(ctx, *wordsToSay): # puts whatever text the user says into a variable
    str = convertTuple(wordsToSay)
    await ctx.send(str) # sends the text in the variable

@bot.command() # dm people, @ them then put the message, idk what the code does i took it from daniel
#@commands.is_owner() # checks if the person running it is the owner
async def dm(ctx, member: discord.Member, *,  msg=None):
        await ctx.reply(
            f"I have sent that message to: {member.mention}", delete_after=3.0)
        await member.send(
            msg)
        await ctx.message.delete()

@bot.command() # get avatar of user, again idk what the code does i took it from daniel
async def avatar(ctx, member: discord.Member = None):
     if not member:
      member = ctx.author
     await ctx.send(member.avatar_url)

@bot.command() # magic 8-ball command (very optimzied lol)
async def eightball(ctx, eightballquestion):
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

@bot.command() # sends random fact
async def fact(ctx):
    fact = nekos.fact()
    await ctx.send(fact)

@bot.command() # owoify text
async def owoify(ctx, *wantowoed): # stores the users text in the wantowoed variable
    str = convertTuple(wantowoed)
    userowo = nekos.owoify(str)
    await ctx.send(userowo)

@bot.command() # reddit.com/r/showerthoughts type of thing
async def showerthought(ctx):
    shwrthought = nekos.why()
    await ctx.send(shwrthought)

with open('token.txt') as f: # opens token.txt
    token = f.read() # stores whatevers in it into the variable `token`
bot.run(token) # token