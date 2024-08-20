import discord, os
from dotenv import load_dotenv
import asyncio
import random

# made with love by natalie!! :3c

load_dotenv()
print("loaded dotenv")
print("bot starting... please hold on for a moment...")

SECRET = "maestrefi"                                                                    # this is the secret phrase
RESPONSE = "insert teh end of the youtube link here!!! :33"                             # this is the clue that the bot will drop
YAP = f"Congrats blah blah balh here is the next clue ```{RESPONSE}``` blah blah"       # this is whatever the bot yaps about. you can use '''triple quotes''' if you want
__TOKEN = str(os.getenv("TOKEN"))                                                       # put your token in .env https://guide.pycord.dev/getting-started/creating-your-first-bot#using-dotenv 
# DO NOT PUBLISH YOUR DISCORD TOKEN ONLINE. IT SHOULD NOT BE SHARED

intents = discord.Intents.all()

# init bot
try:
    client = discord.Bot(intents=intents)
except Exception as e:
    print(f"some error occured while trying to load the bot :((\nSTART OF OUTPUT\n{e}\nEND OF OUTPUT\naw man :(")

async def send_random_emoji():
    await client.wait_until_ready()
    channel = client.get_channel(1273798734253133827) 
    while not client.is_closed():
        await asyncio.sleep(random.randint(2916, 8748))
        print("sent <:dimini:1273803816357199873> lol")
        await channel.send('<:dimini:1273803816357199873>')
        await channel.send(file=discord.File('/Users/nat/Downloads/DIMINI.mp4'))
        
        
@client.command(name="dimini")
async def dimini(ctx):
    print("sent <:dimini:1273803816357199873> lol")
    await ctx.send('<:dimini:1273803816357199873>')
    await ctx.send(file=discord.File('/Users/nat/Downloads/DIMINI.mp4'))

@client.command(name='say')
async def say(ctx, *, message: str):
    print(f"say used: {message}")
    try:
        await ctx.message.delete()
    except Exception as e:
        print(f"error while using ^say: {e}")
    await ctx.respond(message)
    
@client.command(name='debug')
async def debug(ctx):
    channel = client.get_channel(1273808376295456868)
    data = {"bot user id": client.user.id}
    await channel.send(data)
    
async def saycmd(ctx, channel):
    message = ctx.content[5::]
    print(f"say used: {message}")
    try:
        await ctx.message.delete()
    except Exception as e:
        print(f"error while using ^say: {e}")
    await channel.send(message)
@client.event
async def on_ready():
    print(f"logged in as {client.user}")
    print("bot is running!! have fun!! :3")
    print("made with love by ellipticobj :3c")
    client.loop.create_task(send_random_emoji())

@client.event
async def on_message(ctx):
    if ctx.author.id != client.user.id:
        print(f"message \"{ctx.content}\" sent by user {ctx.author}")
        s = ctx.content
        print(s)
        print(f"author id: {ctx.author.id}")
        if ctx.content[0:4] == "^say":
            channel = client.get_channel(ctx.channel)
            message = ctx.content[5::]
            print(f"say used: {message}")
            try:
                await ctx.message.delete()
            except Exception as e:
                print(f"error while using ^say: {e}")
            await channel.send(message)
        elif ctx.content.lower().strip() == SECRET:
            try:
                await ctx.message.delete()
            except Exception as e:
                print(f"some error occured while trying to load the bot :((\nSTART OF OUTPUT\n{e}\nEND OF OUTPUT\naw man :(")

            print(f"woah {ctx.author} got it right!!")
            await ctx.author.send(YAP)
            print(f"clue given!! :3")
        else:
            print(f"tehy got it wrong")

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
