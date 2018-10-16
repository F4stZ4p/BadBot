import aiohttp
import asyncio
import json
import discord
from discord.ext import commands

class EvalModule():
    """The best module ever to evaluate code"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
        
    async def _process_code(self, code: str):
        if code.startswith('```') and code.endswith('```'):
            await self.evaluate_code(self.cleanup_code(code))
        
    def cleanup_code(self, content):
        """Clean up the code"""
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])
        return content.strip('` \n')
        
    async def evaluate_code(self, code):
        async with self.session.post('http://coliru.stacked-crooked.com/compile', data=json.dumps({'cmd': 'python main.cpp', 'src': self.cleanup_code(code)})) as resp:
            if resp.status != 200:
                return "Timed out"

            else:
                output = await resp.text(encoding='utf-8')

                if len(output) < 1500:
                    return f"```python\n{output}\n```"
                 
                else:
                    return "Output too long"
                    
    async def on_message(self, message):
        await self._process_code(message.content)
                    
def setup(bot):
    bot.add_cog(EvalModule(bot))
    print('EvalModule loaded.')
