import discord, logging
from discord.ext import commands

logger = logging.getLogger("logs")

class CommandCog(commands.Cog):
    def __init(self, bot):
        self.bot = bot

    # bot commands
    @commands.command(name="dimini")
    async def dimini(ctx):
        logger.info("sent <:dimini:1273803816357199873> lol")
        await ctx.send('<:dimini:1273803816357199873>')
        await ctx.send(file=discord.File('DIMINI.mp4'))


    @commands.command(name="say")
    async def say(ctx, *, message: str):
        await ctx.send(message)
        

    @commands.command(name="skibidinig")
    async def skibidinig(ctx, *, userid):
        try:
            uid = int(userid)
            user = await commands.fetch_user(uid)
            await user.send("71 sigma skibidinig slicers!")
        except:
            ctx.send("noh sigma")