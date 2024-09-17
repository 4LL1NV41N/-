import discord, os, asyncio, json, logging, importlib, jsonhandlers
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from handlers import on_message as messagehandler, on_ready as readyhandler

# made with love by natalie!! :3c

# logging config
logger = logging.getLogger("logs")
logger.setLevel(logging.INFO)

consolehandler = logging.StreamHandler()
filehandler = logging.FileHandler("./-/main.log")

consolehandler.setLevel(logging.INFO)
filehandler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - [%(levelname)s]: %(message)s")

consolehandler.setFormatter(formatter)
filehandler.setFormatter(formatter)

logger.addHandler(consolehandler)
logger.addHandler(filehandler)

# loading token
envpath = '../.env' if os.path.isfile('../.env') else './.env'
load_dotenv(envpath)
logger.info("loaded dotenv")
logger.info("bot starting... please hold on for a moment...")
__TOKEN = os.getenv("TOKEN")                                                                  # dimini discord token
__SECRET = os.getenv("SECRET")                                                                # this is the secret phrase

# initializing variables
RESPONSE = "vYfj4iP2yuw"                                                                    # this is the clue that the bot will drop
YAP = f"Good job. Here is your clue for the next step: ```{RESPONSE}``` Good luck."         # thsi si the yap
ratelimiting = True
clearingrates = True
limit = 40

# starting bot
client = discord.Bot(intents=discord.Intents.all(),debug_guilds=[1273798733703675976])
os.chdir("../")

# Loading cogs
initial_extensions = [
    'cogs.slashcommands',
    'cogs.commands'
]

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
            logger.info(f"Loaded extension {extension}")
        except Exception as e:
            logger.error(f"Failed to load extension {extension}: {e}")
        
        
# async functions
async def handlesecret(message):
    try:
        await message.delete()
    except Exception as e:
        logger.error(f"Error deleting message: {e}")
    
    await message.author.send(YAP)


async def clearrate():
    now = datetime.now(timezone.utc)
    nexthour = now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    nexthoursecs = (nexthour - now).total_seconds()
    while True:
        await asyncio.sleep(nexthoursecs)
        if clearingrates:
            logger.info("Clearing rate limits.")
            data = jsonhandlers.loadjson("./rate.json")
            logger.info(data)
            for key in data:
                data[key] = 0
            jsonhandlers.savejson("./rate.json", data)
            logger.info("Rates cleared.")
        else:
            logger.info("Rate clearing is turned off.")
        
@client.command(name="reload")
@discord.commands.is_owner()
async def reload(ctx):
    try:
        importlib.reload(messagehandler)
        importlib.reload(readyhandler)
        await ctx.send("Event handlers reloaded")
        logger.info("reloaded main event handlers")
    except Exception as e:
        await ctx.send(f"Error reloading: {e}")
        logger.error("event handlers could not be reloaded")
        logger.error(e)


# discord events
@client.event
async def on_ready():
    await readyhandler(client)
    
@client.event
async def on_message(message):
    await messagehandler(client, message, limit, ratelimiting, __SECRET, YAP)


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
