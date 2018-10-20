import discord
from json import dumps
from discord.ext import commands
from aiohttp import ClientSession

class EvalModule():
    """The best module ever to evaluate code"""

    def __init__(self, bot):
        self.bot = bot
        self.session = ClientSession(loop=self.bot.loop)
        
    async def process_code(self, message: discord.message):
        """Code processor"""
        if message.clean_content.startswith('```') and message.clean_content.endswith('```'):
            await message.channel.send((await self.evaluate_code(self.cleanup_code(message.clean_content), message)))
            await message.add_reaction('Ok:501773759011749898')
        
    def cleanup_code(self, content):
        """Clean up the code"""
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])
        return content.strip('` \n')
    
    def do_code(self, code, ctx):
        """Does Context tricky stuff"""
        return f"""
class DiscordRoleAdaptor():
    def __init__(self, **kwargs):
        self._role = kwargs.pop('role')
        self._position = kwargs.pop('position')
        self._color = kwargs.pop('color')
        
    @property
    def position(self):
        return self._position
        
    @property
    def color(self):
        return self._color
        
    def __repr__(self):
        return self._role

class MessageAuthor():
    def __init__(self):

        self._id = {ctx.author.id}
        self._bot = {ctx.author.bot}
        self._name = '{ctx.author.name}'
        self._display_name = '{ctx.author.display_name}'
        self._avatar_url = '{ctx.author.avatar_url}'
        
        self._roles = []
        
    @property
    def id(self):
        return self._id
        
    @property
    def bot(self):
        return self._bot
        
    @property
    def name(self):
        return self._name
        
    @property
    def display_name(self):
        return self._display_name
        
    @property
    def avatar_url(self):
        return self._avatar_url
        
    @property
    def roles(self):
        return self._roles

    def __repr__(self):
        return '{ctx.author.name}#{ctx.author.discriminator}'

class Context():
    def __init__(self):
        self.author = MessageAuthor()

    def __repr__(self):
        return 'Context Object'

ctx = Context()
{self.cleanup_code(code)}
                """
        
    async def evaluate_code(self, code, ctx):
        """Code evaluator"""
        async with self.session.post('http://coliru.stacked-crooked.com/compile', data=dumps({'cmd': 'python3 main.cpp', 'src': self.do_code(code, ctx)})) as resp:
            if resp.status != 200:
                return f"Unable to process request due to {resp.status} error"

            else:
                output = await resp.text(encoding='utf-8')

                if len(output) < 1500:
                    return f"```python\n{output}\n```"
                 
                else:
                    return "Output too long"
                    
    async def on_message(self, message):
        """Processing our messages"""

        if message.author.bot or message.author == self.bot.user:
            return

        await self.process_code(message)
                    
def setup(bot):
    bot.add_cog(EvalModule(bot))
    print('EvalModule loaded.')
