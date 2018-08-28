import discord
import os
from discord.ext import commands

bot = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('bb.'))

@bot.command()
async def ping(ctx):
	await ctx.send('Pong!')

bot.run(os.getenv('TOKEN'))