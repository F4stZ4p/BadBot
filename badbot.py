import discord
import os
from discord.ext import commands

bot = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('bb.'))

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

if __name__ == "__main__":
    for extension in bot.extensions:
        try:
            bot.load_extension('modules.antilink')
            bot.load_extension('modules.pingmodule')
        except Exception as e:
            print(e)

bot.run(os.getenv('TOKEN'))
