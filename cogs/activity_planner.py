from discord.ext import commands

class ActivityPlanner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def planner(self, ctx):
        if ctx.invoked_subcommand is None:
            m = """Usage : !planner {add , remove, list}
                """
            await ctx.send(m)
    
    @planner.command()
    async def add(self, ctx, *, args):
        await ctx.send("I added your activity ;)")
    @planner.command()
    async def remove(self, ctx, *, args):
        await ctx.send("makayn walo -_-")
    @planner.command()
    async def list(self, ctx):
        await ctx.send("wa glna lik makayn walu XD")
