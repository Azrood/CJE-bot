import discord
from discord.ext import commands

import cogs
from secret import TOKEN

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", description=None, help_command=None, intents=intents, case_insensitive=True)

cogs_list = [cogs.Greetings,
             cogs.Misc,
             cogs.ActivityPlanner
             ]

@bot.event
async def on_ready():
    """Log in to discord"""
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("--------")
    print("Connected to :")
    print(" | ".join(guild.name for guild in bot.guilds))
    for cog in cogs_list:
        bot.add_cog(cog(bot))

bot.run(TOKEN)
