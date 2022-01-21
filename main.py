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
    await bot.change_presence(activity=discord.Game(name="$help | Made by verbes4#8839")) # and then set the bots activity

# load cogs
bot.load_extension('cogs.nsfw')
bot.load_extension('cogs.math')
bot.load_extension('cogs.img')
bot.load_extension('cogs.help')
bot.load_extension('cogs.misc')

@bot.command() # get avatar of user, again idk what the code does i took it from daniel
async def avatar(ctx, member: discord.Member = None):
     if not member:
      member = ctx.author
     await ctx.send(member.avatar_url)

with open('token.txt') as f: # opens token.txt
    token = f.read() # stores whatevers in it into the variable `token`
bot.run(token) # token