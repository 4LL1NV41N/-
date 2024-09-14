import discord, os, asyncio, json
from dotenv import load_dotenv

# made with love by natalie!! :3c

load_dotenv()
print("loaded dotenv")
print("bot starting... please hold on for a moment...")

SECRET = "maestrefi"                                                                        # this is the secret phrase
RESPONSE = "insert teh end of the youtube link here!!! :33"                                 # this is the clue that the bot will drop
YAP = "Congrats blah blah balh here is the next clue ```" + RESPONSE + "``` blah blah"      # optimizing concatenation
__TOKEN = os.getenv("TOKEN")                                                                # use getenv without casting to string, it's already a string in env vars

intents = discord.Intents.all()  # use only required intents to save memory

# init bot
try:
    client = discord.Bot(intents=intents)
except Exception as e:
    print(f"some error occured while trying to load the bot :((\nSTART OF OUTPUT\n{e}\nEND OF OUTPUT\naw man :(")

@client.command(name="dimini")
async def dimini(ctx):
    print("sent <:dimini:1273803816357199873> lol")
    await ctx.respond('<:dimini:1273803816357199873>')
    await ctx.respond(file=discord.File('DIMINI.mp4'))

@client.command(name='say')
async def say(ctx, *, message: str):
    await ctx.respond(message)

@client.event
async def on_ready():
    print(f"logged in as {client.user}")
    print("bot is running!! have fun!! :3")
    print("made with love by ellipticobj :3c")

@client.event
async def on_message(message):
    print(f"message \"{message.content}\" sent by user {message.author}")
    if message.content.lower().strip() == SECRET and message.author.id != client.user.id:
        try:
            await message.delete()
        except Exception as e:
            print(f"some error occured while trying to delete the message :((\nSTART OF OUTPUT\n{e}\nEND OF OUTPUT\naw man :(")
        print(f"woah {message.author} got it right!!")
        await message.author.send(YAP)
        print(f"clue given!! :3")
    else:
        print(f"tehy got it wrong")
        
async def clear_rate():
    with open("rate.json","wr") as file:
        data = json.load(file)

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