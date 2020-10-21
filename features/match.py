from discord.ext import commands


class Match(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='match')
    async def show_latest_match(self, ctx):
        await ctx.send('To be implemented')


def setup(bot):
    bot.add_cog(Match(bot))
