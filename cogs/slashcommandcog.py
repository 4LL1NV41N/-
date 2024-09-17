import discord, jsonhandlers
from discord.ext import commands

class SlashCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # rate limit command group
    ratelimit = discord.SlashCommandGroup("ratelimit", "enable or disable rate limiting")

    @ratelimit.command(name="enable")
    async def ratelimitenable(ctx):
        global ratelimiting
        ratelimiting = True
        await ctx.respond(f"rate limiting toggled to {ratelimiting}", ephemeral=True)


    @ratelimit.command(name="disable")
    async def ratelimitdisable(ctx):
        global ratelimiting
        ratelimiting = False
        await ctx.respond(f"rate limiting toggled to {ratelimiting}", ephemeral=True)


    # clear rate command group
    clearrates = discord.SlashCommandGroup("clearrates", "enable or disable rate clearing")

    @clearrates.command(name="clear")
    async def clear(ctx):
        try:
            data = jsonhandlers.loadjson("./rate.json")
            for key in data:
                data[key] = 0
            jsonhandlers.savejson("./rate.json", data)
            await ctx.respond("rates cleared", ephemeral=True)
        except Exception as e:
            await ctx.respond(f"An error occurred while clearing rates: {e}", ephemeral=True)


    @clearrates.command(name="enable")
    async def enableclearrates(ctx):
        global clearingrates
        clearingrates = True
        await ctx.respond(f"rate clearing toggled to {clearingrates}", ephemeral=True)


    @clearrates.command(name="disable")
    async def disableclearrates(ctx):
        global clearingrates
        clearingrates = False
        await ctx.respond(f"rate clearing toggled to {clearingrates}", ephemeral=True)
        
def setup(bot):
    bot.add_cog(SlashCommandCog(bot))