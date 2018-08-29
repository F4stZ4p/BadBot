import discord
from discord.ext import commands

class Antilink():
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if self.bot.user in message.mentions:
            await message.add_reaction(':ping:456793379808870401')

        if message.content.startswith('https') or message.content.startswith('http') or message.content.startswith('discord.gg') or message.content.startswith('www'):
            await message.delete()


def setup(bot):
    bot.add_cog(Antilink(bot))