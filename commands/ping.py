import discord
from discord.ext.cogs import Cog
from discord import Client

class Ping(Cog):
    def __init__(self, bot: Client):
        self.bot = bot
    
    @Cog.slash_command()
    async def ping(self, inter: discord.Interaction):
        await inter.respond(f"pong! {round(self.bot.latency * 1000)}")

def setup(bot: Client):
    bot.add_cog(Ping(bot))