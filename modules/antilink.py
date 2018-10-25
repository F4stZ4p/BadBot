import discord
import re
from discord.ext import commands

class Antilink():
    def __init__(self, bot):
        self.bot = bot
        self._link_regex = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
        
    async def delete_link(self, message):
        if not message.channel:
            return
        if message.author == self.bot.user:
            return
        if re.match(message, self._link_regex):
            try:
                await message.delete()
                await message.channel.send(f':link: | **{message.author.mention}, no links allowed here!**', delete_after=5)
            except:
                pass

    async def on_message(self, message):
        await self.delete_link(message)

def setup(bot):
    bot.add_cog(Antilink(bot))
    print('Antilink loaded')
