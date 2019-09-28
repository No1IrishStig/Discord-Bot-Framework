import discord

from utils import functions
from utils.functions import func
from discord.ext import commands

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx): # Defining the Command
        await ctx.author.send("**Available Commands**\n\n**ping**\n**help**") # Sending the message to the Author of the Command Message

    @commands.command()
    async def ping(self, ctx): # Self is a requirement in all commands, and ctx is required to access the command context. (Guild, Invoker and more)
        await ctx.send("Pong")

    @commands.command()
    async def roles(self, ctx):
        if ctx.author.guild_permissions.manage_roles: # Checks for User permissions
            roles = [] # Makes a list for roles
            for role in ctx.guild.roles: # Iterating (looping) through every role in the server and appending (adding) them to the list above.
                roles.append(role.name)
            roles.remove("@everyone") # Removes the @everyone Role from the list
            await ctx.send(embed=func.EMaker(self, "Role List", "{}".format("\n ".join(roles)), "Roles")) # Sends the list in an embed message with a new line between each

def setup(client):
    client.add_cog(Core(client))
