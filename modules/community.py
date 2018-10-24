import discord
from discord.ext import commands

class Community():
    """Commands for The Bad Server community"""
    def __init__(self, bot):
        self.bot = bot
        self._source_url = "https://github.com/F4stZ4p/BadBot"
    
    @property
    def source_url(self):
        return self._source_url
        
    @commands.command()
    async def source(self, ctx, *, command: str = None):
        """Displays the Bad Bot's source"""
        if command is None:
            return await ctx.send(source_url)

        object = self.bot.get_command(command.replace('.', ' '))
        if object is None:
            return await ctx.send('Command not found')

        src = object.callback.__code__
        lines, firstlineno = inspect.getsourcelines(src)
        if not obj.callback.__module__.startswith('discord'):
            location = os.path.relpath(src.co_filename).replace('\\', '/')
        else:
            location = obj.callback.__module__.replace('.', '/') + '.py'

        final_url = f'<{self.source_url}/{location}#L{firstlineno}-L{firstlineno + len(lines) - 1}>'
        await ctx.send(final_url)
        
def setup(bot):
    bot.add_cog(Community(bot))
