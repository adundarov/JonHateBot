import discord
import os
import random
import asyncio
from datetime import datetime
from discord.ext import commands
import settings

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

cogs: list = ["Functions.Fun.games", "Functions.Fun.gameinfos", "Functions.Fun.otherfuncommands", "Functions.Info.info",
        "Functions.Misc.misc", "Functions.NewMember.newmember", "Functions.Admin.admin"]

client = commands.Bot(command_prefix=settings.Prefix, help_command=None, intents=intents)

async def send_random_number():
    # Replace YOUR_CHANNEL_ID with the actual channel ID where you want to send the messages
    channel = client.get_channel(settings.CHANNEL_ID)
    if channel:
        random_num = random.randint(1, 100)
        await channel.send(f"Random number: {random_num}")

async def check_time():
    while True:
        now = datetime.now()
        if now.hour == 8 and now.minute == 0 and now.second == 0:
            await send_random_number()
            await asyncio.sleep(61)  # Sleep for 61 seconds to avoid sending multiple messages in the same minute
        elif now.hour == 20 and now.minute == 0 and now.second == 0:
            await send_random_number()
            await asyncio.sleep(61)  # Sleep for 61 seconds to avoid sending multiple messages in the same minute
        else:
            await asyncio.sleep(1)  # Check every second

## for when we add commands

@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(settings.BotStatus))
    
    # for cog in cogs:
    #     try:
    #         print(f"Loading cog {cog}")
    #         client.load_extension(cog)
    #         print(f"Loaded cog {cog}")
    #     except Exception as e:
    #         exc = "{}: {}".format(type(e).__name__, e)
    #         print("Failed to load cog {}\n{}".format(cog, exc))
    
    client.loop.create_task(check_time())  # Start the time checking loop

client.run(settings.TOKEN)
