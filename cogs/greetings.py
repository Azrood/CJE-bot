import time

import discord
from discord.ext import commands, tasks

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cje_guild = [guild for guild in bot.guilds if guild.name == "CJE"].pop()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="welcome")
        msg = ""
        if member.guild.name == "CJE":
            msg = f"""Hey {member.mention} , welcome to {member.guild.name}!    ようこそ ヽ(・∀・)ﾉ  !
Check out the <#689806717135224874> and tell us your name in <#689846167055368242>
Enjoy your stay and have fun  <:kannahi:826596670996217876>"""
        else:
            msg = f""" Hey {member.mention}, welcome to our public server CJE ようこそ ヽ(・∀・)ﾉ  !. 
Check out the rules in <#771858767876194325>
Enjoy your stay ＼(＾▽＾)／ """
        await channel.send(content=msg)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="welcome")
        msg = f"Sayonara {member.mention} (╥_╥)."
        await channel.send(content=msg)

   
    @tasks.loop(hours=1)
    async def ohayo(self):
        general_chan = discord.utils.get(self.cje_guild.text_channels, name="général")
        if time.localtime().tm_hour == 10:
            await general_chan.send(content="Ohayo onii-chan <kannahi:826596670996217876>")

    @ohayo.before_loop
    async def before_ohayo(self):
        await self.bot.wait_until_ready()
