import discord
from discord.ext import commands

class Antilink():
    def __init__(self, bot):
        self.bot = bot
        
    async def delete_link(self, message):
        if not message.channel:
            return
        if message.author == self.bot.user:
            return
        if message.content.startswith('https') or message.content.startswith('http') or message.content.startswith('discord.gg') or message.content.startswith('www'):
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
