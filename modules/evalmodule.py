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
        return f"""
class MessageAuthor():
    def __init__(self):
        self.id = {ctx.author.id}
        self.name = '{ctx.author.name}'
    def __repr__(self):
        return '{ctx.author.name}#{ctx.author.discriminator}'
    def __setattr__(self, name, value):
        raise RuntimeError("Can't set an attribute")

class Context():
    def __init__(self):
        self.author = MessageAuthor()
    def __repr__(self):
        return 'Context Object'
    def __setattr__(self, name, value):
        raise RuntimeError("Can't set an attribute")

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
