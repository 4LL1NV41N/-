import discord, os,  logging, signal
from dotenv import load_dotenv
from mainhandlers import messagehandler, readyhandler

# made with love by natalie!! :3c

versionnum = 2

'''
TODO: edit install.sh so that its instructions make more sense
'''

# logging config
logger = logging.getLogger("logs")
logger.setLevel(logging.INFO)
consolehandler = logging.StreamHandler()
filehandler = logging.FileHandler("./main.log")
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

# Loading cogs
cognames = [
    'slashcommandcog',
    'commandcog',
    'admincog'
]

if __name__ == '__main__':
    for extension in cognames:
        try:
            client.load_extension(f"cogs.{extension}")
            logger.info(f"Loaded extension {extension}")
        except Exception as e:
            logger.error(f"Failed to load {extension}: {e}")

def ext_reloadcogs(signal_number, frame):
    logger.info("Received signal to reload cogs.")
    for extension in cognames:
        try:
            client.reload_extension(extension)
            logger.info(f"Reloaded extension {extension}")
        except Exception as e:
            logger.error(f"Failed to reload extension {extension}: {e}")

# discord events
@client.event
async def on_ready():
    await readyhandler(client, clearingrates, versionnum)
    
@client.event
async def on_message(message):
    await messagehandler(client, message, limit, ratelimiting, __SECRET, YAP)

signal.signal(signal.SIGUSR1, ext_reloadcogs)

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
