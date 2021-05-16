import random

from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def choose(self, ctx, *, args):
        """Randomly choose user's choices."""
        choices = args.split("/")
        if len(choices) < 1:  # pragma: no cover
            return None
        await ctx.send(random.choice(choices))
  
    @commands.command()
    async def say(self, ctx, *, args):
        """Repeats user message content and delete original user message"""
        await ctx.message.delete()
        await ctx.send(content=args)

    @commands.group()
    async def convert(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("mzl madert walu")

    @convert.command()
    async def hiragana(self, ctx, *args):
        await ctx.send('おはよ')
