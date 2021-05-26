import random
from string import ascii_letters
import aiohttp

from discord.ext import commands

from utils.constants import HIRAGANA, KATAKANA


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def choose(self, ctx, *, args):
        """Randomly choose user's choices."""
        choices = args.split("/")
        if len(choices) < 1:
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
    async def hiragana(self, ctx, *, args=None):
        if args is None:
            pass
        else:
            hiragana_text = ""
            kana = ""
            args = " ".join(map(str.lower, args.split()))
            for index, char in enumerate(args):
                look_ahead = args[min(index+1, len(args)-1)]
                if char not in ascii_letters + " ":
                    hiragana_text += char
                else:
                    if (char in HIRAGANA and kana == ""
                        and (char == "n"
                             and look_ahead not in "aeiouy")):
                        hiragana_text += HIRAGANA[char]
                        kana = ""
                    else:
                        if (not {char,
                                 look_ahead}.intersection({"a", "e", "i", "u", "o", "y"})
                           and char == look_ahead):
                            hiragana_text += HIRAGANA["sakuon"]
                            continue
                        if char == "n" and look_ahead in {"a", "e", "i", "u", "o", "y"}:
                            kana += char
                            continue
                        if char == " ":
                            continue
                        kana += char
                        if kana in HIRAGANA:
                            hiragana_text += HIRAGANA[kana]
                            kana = ""
            await ctx.send(hiragana_text)

    @convert.command()
    async def katakana(self, ctx, *, args):
        if args is None:
            pass
        else:
            katakana_text = ""
            kana = ""
            args = " ".join(map(str.lower, args.split()))
            for index, char in enumerate(args):
                look_ahead = args[min(index+1, len(args)-1)]
                if char not in ascii_letters + " _":
                    katakana_text += char
                elif char == "_":
                    katakana_text += KATAKANA["pause"]
                else:
                    if (char in KATAKANA and kana == ""
                        and (char == "n"
                             and look_ahead not in "aeiouy")):
                        katakana_text += KATAKANA[char]
                        kana = ""
                    else:
                        if (not {char,
                                 look_ahead}.intersection({"a", "e", "i", "u", "o", "y"})
                           and char == look_ahead):
                            katakana_text += KATAKANA["sakuon"]
                            continue
                        if char == "n" and look_ahead in {"a", "e", "i", "u", "o", "y"}:
                            kana += char
                            continue
                        if char == " ":
                            continue
                        kana += char
                        if kana in KATAKANA:
                            katakana_text += KATAKANA[kana]
                            kana = ""
            await ctx.send(katakana_text)

    @commands.command()
    async def jisho(self, ctx, *args):
        with aiohttp.ClientSession() as cl:
            pass
        await ctx.send("Not yet")
