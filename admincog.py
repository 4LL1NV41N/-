# cogs/admin.py

import discord, importlib, logging
from discord.ext import commands
from mainhandlers import messagehandler, readyhandler
from main import cognames

logger = logging.getLogger("logs")

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="reload")
    async def reload(self, ctx):
        try:
            importlib.reload(messagehandler)
            importlib.reload(readyhandler)
            await ctx.send("Event handlers reloaded")
            logger.info("reloaded main event handlers")
        except Exception as e:
            await ctx.send(f"Error reloading: {e}")
            logger.error("event handlers could not be reloaded")
            logger.error(e)

    @commands.command(name='reloadcog')
    async def reload_cog(self, ctx, cog: discord.Option(str, choices=cognames)):
        try:
            self.bot.reload_extension(f'cogs.{cog}')
            await ctx.send(f"Reloaded {cog} cog.")
        except Exception as e:
            await ctx.send(f"Failed to reload {cog} cog: {e}")

# Required setup function for cog loading
def setup(bot):
    bot.add_cog(Admin(bot))