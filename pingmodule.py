import discord
from discord.ext import commands

class Pingmodule():
    def __init__(self, bot):
        self.bot = bot
        
    async def on_message(self, message):
        if self.bot.user in message.mentions:
            await message.add_reaction(':ping:456793379808870401')

def setup(bot):
    bot.add_cog(Pingmodule(bot))
