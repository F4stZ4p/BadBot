import discord
import os
from discord.ext import commands

class BadBot(commands.AutoShardedBot):
    def __init__(self):
        self.extensions = ('modules.pingmodule', 'modules.antilink')
        super().__init__(command_prefix=commands.when_mentioned_or('bb.'), case_insensitive=True)
        
    def run(self):
        for extension in self.extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                print(f'Something went wrong while loading extension {extension}: {e}')
        super().run(os.getenv('TOKEN'))

if __name__ == "__main__":
    BadBot().run()
