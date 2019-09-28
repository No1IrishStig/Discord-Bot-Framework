import os, traceback
import datetime
import discord
import json

from discord.ext import commands
from collections import namedtuple

version = "Beta v0.01"

def get(file):
    try:
        with open(file, encoding="utf8") as data:
            return json.load(data, object_hook=lambda d: namedtuple("X", d.keys())(*d.values()))
    except AttributeError:
        raise AttributeError("Unknown argument")
    except FileNotFoundError:
        raise FileNotFoundError("JSON file wasn't found")

    # Loading Sequence for the CFG File

# Defining the Class
class func(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def EMaker(self, title, description, footer): # Simple Embedded Message Generator
        embed = discord.Embed(
            title = title,
            description = description,
            colour = 0x9bf442, # HEX Colour with 0x at the start
            timestamp=datetime.datetime.utcnow()
            )
        embed.set_footer(text=footer)

        return embed

        #To use: (embed=func.EMaker(title, description, footer))
    

def setup(client):
    client.add_cog(func(client))
# Adding it as a Cog
