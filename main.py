from discord.ext import commands

from secrets import PRIVATE_KEY
from settings import EXTENSIONS

client = commands.Bot(command_prefix='.', case_insensitive=True)


@client.event
async def on_ready():
    print('The bot is ready!')


if __name__ == '__main__':
    print('Starting the bot...')
    [client.load_extension(ext) for ext in EXTENSIONS]
    client.run(PRIVATE_KEY)
