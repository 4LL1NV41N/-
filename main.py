import discord, os, asyncio, json
from dotenv import load_dotenv

# made with love by natalie!! :3c

load_dotenv()
print("loaded dotenv")
print("bot starting... please hold on for a moment...")

SECRET = "maestrefi"                                                                        # this is the secret phrase
RESPONSE = "vYfj4iP2yuw"                                 # this is the clue that the bot will drop
YAP = f"Congrats blah blah balh here is the next clue ```{RESPONSE}``` blah blah" # thsi si the yap
__TOKEN = os.getenv("TOKEN")                                                                # dimini discord token
ratelimiting = True
clearingrates = True


intents = discord.Intents.all()  # use only required intents to save memory

# init bot
try:
    client = discord.Bot(intents=intents,debug_guilds=[1273798733703675976])
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

clearrates = discord.SlashCommandGroup("clearrates", "enable or disable rate clearing")

@clearrates.command()
async def clear(ctx):
    try:
        with open("rate.json","r") as file:
            data = json.load(file)
        for key in data:
            data[key] = 0
        with open("rate.json", "w") as file:
            json.dump(data, file, indent=4)
            await ctx.respond("rates cleared", ephemeral=True)
    except Exception as e:
        await ctx.respond(f"an error occured while trying to clear rates: {e}", ephemeral=True)
        await ctx.respond("rates not cleared", ephemeral=True)

@clearrates.command(name="enable")
async def enableclearrates(ctx):
    global clearrates
    clearrates = True
    await ctx.respond(f"rate clearing toggled to {clearrates}", ephemeral=True)

@clearrates.command(name="disable")
async def disableclearrates(ctx):
    global clearrates
    clearrates = False
    await ctx.respond(f"rate clearing toggled to {clearrates}", ephemeral=True)

@client.event
async def on_ready():
    print(f"logged in as {client.user}")
    print("bot is running!! have fun!! :3")
    print("made with love by ellipticobj :3c")
    client.loop.create_task(clear_rate())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # handling rate limiting n stuff
    with open("rate.json", "r") as file:
        data = json.load(file)

    user_id = str(message.author.id)
    data[user_id] = data.get(user_id, 0) + 1

    with open("rate.json", "w") as file:
        json.dump(data, file, indent=4)

    if data[str(message.author.id)] < 20 and ratelimiting:
        print(f"message \"{message.content}\" sent by user {message.author}")
        if message.content.lower().strip() == SECRET:
            try:
                await message.delete()
            except Exception as e:
                print(f"some error occured while trying to delete the message :((\nSTART OF OUTPUT\n{e}\nEND OF OUTPUT\naw man :(")
            print(f"woah {message.author} got it right!!")
            await message.author.send(YAP)
            print(f"clue given!! :3")
        else:
            print(f"tehy got it wrong")
    elif data[str(message.author.id)] >= 20 and ratelimiting:
        await message.author.send("You are sending requests too quickly.")
    elif not ratelimiting:
        print("rate limiting off.")

async def clear_rate():
    while True:
        if clearingrates:
            print("clearing rate")
            try:
                with open("rate.json","r") as file:
                    data = json.load(file)
                for key in data:
                    data[key] = 0
                with open("rate.json", "w") as file:
                    json.dump(data, file, indent=4)
                    print("rates cleared")
            except Exception as e:
                print(f"an error occured while trying to clear rates: {e}")
                print("rates not cleared, rate limiting turned off")
                global ratelimiting
                ratelimiting = False
        else:
            print("clearing rates turned off")
        await asyncio.sleep(3600)

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
