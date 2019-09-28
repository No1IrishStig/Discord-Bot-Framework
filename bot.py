import os, traceback
import discord
import json

from utils import functions
from utils.functions import func
from discord.ext import commands

config = functions.get("utils/cfg.json")

bot = commands.Bot(command_prefix = config.prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'\nSuccessfully logged in as: {bot.user.name}\nVersion: {discord.__version__}\nBuild: {functions.version}')
    await bot.change_presence(activity=discord.Game(name="Discord Bot Framework", type=1, url='https://github.com/No1IrishStig/'))

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        try:
            bot.load_extension(f"cogs.{name}")
        except Exception as error:
            traceback.print_exc()

bot.load_extension("utils.errorhandler")
bot.run(config.token, reconnect=True)
