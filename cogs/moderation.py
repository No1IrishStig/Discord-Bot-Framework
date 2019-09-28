import discord

from utils import functions
from utils.functions import func
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, ctx, user : discord.User=None, *args):
        if ctx.ctx.author.guild_permissions.kick_members: # Checks for kick permission
            if user: # If a mentioned user
                reason = ' '.join(args) # Get the reason
                if reason == "": # Check if there was a reason provided
                    await user.send(embed=func.EMaker(self, "You were kicked", f"You were kicked from **{ctx.guild.name}** by **{ctx.author}**", "Moderation"))
                    await ctx.send(embed=func.EMaker(self, "Success", f"User has been kicked by **{ctx.author.name}**", "Moderation"))
                    await ctx.guild.kick(user) # Messages the user and chat of where the command was ran
                else:
                    await user.send(embed=func.EMaker(self, "You were kicked", f"You were kicked from **{ctx.guild.name}** by **{ctx.author}** for **{reason}**", "Moderation"))
                    await ctx.send(embed=func.EMaker(self, "Success", f"User has been kicked by **{ctx.author.name}** for **{reason}**", "Moderation"))
                    await ctx.guild.kick(user)
            else:
                await ctx.send(embed=func.EMaker(self, "Oops!", f"You forgot something!\n\n{ctx.prefix}kick (@user) (reason)\n\nKicks mentioned user from the {ctx.guild.name}, with or without a reason.", "Kick Usage"))
                # Result if no user is mentioned

    @commands.command()
    async def say(self, ctx, *args):
        words = ' '.join(args)
        await ctx.message.delete()
        if words == "":
            await ctx.send("Please provide a message!")
        else:
            await ctx.send(words)


def setup(client):
    client.add_cog(Moderation(client))
