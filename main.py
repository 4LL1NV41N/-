import discord, os, asyncio, json, logging
from dotenv import load_dotenv

# made with love by natalie!! :3c

# logging config
logger = logging.getLogger("logs")
logger.setLevel(logging.INFO)

consolehandler = logging.StreamHandler()
filehandler = logging.FileHandler("main.log")

consolehandler.setLevel(logging.INFO)
filehandler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - [%(levelname)s]: %(message)s")

consolehandler.setFormatter(formatter)
filehandler.setFormatter(formatter)

# loading token
load_dotenv()
logger.info("loaded dotenv")
logger.info("bot starting... please hold on for a moment...")
__TOKEN = os.getenv("TOKEN")                                                                # dimini discord token

# initializing variables
SECRET = "maestrefi"                                                                        # this is the secret phrase
RESPONSE = "vYfj4iP2yuw"                                                                    # this is the clue that the bot will drop
YAP = f"Good job. Here is your clue for the next step: ```{RESPONSE}``` Good luck."         # thsi si the yap
ratelimiting = True
clearingrates = True

# starting bot
client = discord.Bot(intents=discord.Intents.all(),debug_guilds=[1273798733703675976])


# json handling
def loadjson(filename, defaultval="{\n    \n}"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.warning(f"{filename} either does not exist or is not initialized.")
        logger.info(f"initializing {filename}")
        with open(filename, "w") as file:
            json.dump(defaultval, file, indent=4)
        return json.load(file)
    

def savejson(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
        
        
# async functions
async def handle_secret(message):
    try:
        await message.delete()
    except Exception as e:
        logger.error(f"Error deleting message: {e}")

    winners = loadjson("win.json")
    
    if message.author.id in winners:
        await message.author.send("You already got the clue.")
    else:
        await message.author.send(YAP)
        winners[message.author.id] = 1
        savejson("win.json", winners)


async def clear_rate():
    while True:
        if clearingrates:
            logger.info("Clearing rate limits.")
            data = loadjson("rate.json")
            for key in data:
                data[key] = 0
            savejson("rate.json", data)
            logger.info("Rates cleared.")
        else:
            logger.info("Rate clearing is turned off.")
        await asyncio.sleep(3600)
        

# bot commands
@client.command(name="dimini")
async def dimini(ctx):
    logger.info("sent <:dimini:1273803816357199873> lol")
    await ctx.respond('<:dimini:1273803816357199873>')
    await ctx.respond(file=discord.File('DIMINI.mp4'))


@client.command(name="say")
async def say(ctx, *, message: str):
    await ctx.respond(message)


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
        data = loadjson("rate.json")
        for key in data:
            data[key] = 0
        savejson("rate.json", data)
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


# discord events
@client.event
async def on_ready():
    logger.info(f"Logged in as {client.user}")
    logger.info("Bot is running!! Have fun!! :3")
    client.loop.create_task(clear_rate())
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    data = loadjson("rate.json")
    user_id = str(message.author.id)
    data[user_id] = data.get(user_id, 0) + 1
    savejson("rate.json", data)
    if data[user_id] < 20 and ratelimiting:
        logger.info(f'Message "{message.content}" sent by user {message.author}')
        if message.content.lower().strip() == SECRET:
            await handle_secret(message)
        else:
            logger.info("Incorrect guess.")
    elif data[user_id] >= 20 and ratelimiting:
        await message.author.send("You are sending requests too quickly.")
    elif not ratelimiting:
        logger.info("Rate limiting is off.")


client.add_application_command(ratelimit)
client.add_application_command(clearrates)
client.run(__TOKEN)

# (c) Copyright 2024 Natalie http://github.com/ellipticobj http://ithub.com/mysteriousellipsis
# (c) Copyright 2024 Thern http://github.com/DystopianDood09 http://github.com/4LL1NV4IN

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the “Software”), to deal in the
# Software without restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the
# following conditions:

# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# https://opensource.org/license/mit
