import discord
from discord.ext import commands


class Insults(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        a = ["nou", "noyou"]
        no_u = ""
        for word in a:
            if word in message.content.lower().replace(" ", ""):
                no_u = "<:ReverseCard:808522739559563285>"
                try:
                    await message.reply(no_u)
                except UnboundLocalError:
                    pass


def setup(bot):
    bot.add_cog(Insults(bot))
