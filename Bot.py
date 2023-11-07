import disnake
import os
import random
import asyncio
from datetime import datetime
from disnake.ext import commands
import settings

intents = disnake.Intents.all()
intents.typing = False
intents.presences = False
intents.message_content = True

cogs: list = ["Functions.Admin.update"]

bot = commands.Bot(command_prefix=settings.Prefix, help_command=None, intents=intents)

JonHate = 0
JonID = 343261954422341653

#sends random number to designated channel
async def send_random_number():
    channel = bot.get_channel(settings.CHANNEL_ID)
    if channel:
        JonHate = random.randint(0, 100)
        if JonHate == 100:
            await channel.send(f"MAX HATE! JO(H)N METER AT: 100% <@{JonID}><@{JonID}><@{JonID}><@{JonID}><@{JonID}>")
        elif JonHate == 0:
            await channel.send(f"min hate, Jonathan beloved meter at 0% <@{JonID}><@{JonID}><@{JonID}><@{JonID}><@{JonID}>")
        else:
            await channel.send(f"<@{JonID}> Hate Meter At: {JonHate}%")

#checks the time and sends random number at 7am and 7pm pst
async def check_time():
    while True:
        now = datetime.now()
        channel = bot.get_channel(settings.CHANNEL_ID)
        if now.hour == 7 and now.minute == 0 and now.second < 30:
            if channel:
                await channel.send(f"Ehrm... it's 7am pst?? time to update Jon Hate!")
            await send_random_number()
            await asyncio.sleep(61)  # Sleep for 61 seconds to avoid sending multiple messages in the same minute
        elif now.hour == 19 and now.minute == 0 and now.second < 30:
            if channel:
                await channel.send(f"Ehrm... it's 7pm pst?? time to update Jon Hate!")
            await send_random_number()
            await asyncio.sleep(61)  # Sleep for 61 seconds to avoid sending multiple messages in the same minute
        else:
            await asyncio.sleep(1)  # Check every second
    
#initializes bot
class Init(commands.Bot):
    def __init__(self, command_prefix, intents = intents):
        super().__init__(command_prefix, intents = intents)
        
    async def on_ready(self):
        print(f"Logged in as {self.user.name} - {self.user.id}")
        await bot.change_presence(status=disnake.Status.online, activity=disnake.Game(settings.BotStatus))
        
    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)
        
    # for cog in cogs:
    #     try:
    #         print(f"Loading cog {cog}")
    #         client.load_extension(cog)
    #         print(f"Loaded cog {cog}")
    #     except Exception as e:
    #         exc = "{}: {}".format(type(e).__name__, e)
    #         print("Failed to load cog {}\n{}".format(cog, exc))
    
    bot.loop.create_task(check_time())  # Start the time checking loop
    
bot = Init(command_prefix=settings.Prefix, intents=intents)

# #command to manually update jon hate
# @bot.command()
# async def update(ctx: commands.Context):
#     await ctx.send("yes xir")
#     channel = bot.get_channel(settings.CHANNEL_ID)
#     if channel:
#         await channel.send(f"Manual Update:")
#     await send_random_number()
        
# #slash command to manually update jon hate
# @bot.slash_command(description="Manually update Jon hate meter")
# async def update(interaction: disnake.ApplicationCommandInteraction):
#     await interaction.send("yes xir")
#     channel = bot.get_channel(settings.CHANNEL_ID)
#     if channel:
#         await channel.send(f"Manual Update:")
#     await send_random_number()
    
# @bot.slash_command(description="Total Hate")
# async def hate(interaction: disnake.ApplicationCommandInteraction):
#     await interaction.send("yes xir")
#     channel = bot.get_channel(settings.CHANNEL_ID)
#     if channel:
#         await channel.send(f"MAX HATE! JO(H)N METER AT: 100% <@{JonID}><@{JonID}><@{JonID}><@{JonID}><@{JonID}>")
        
# @bot.slash_command(description="Total Love")
# async def love(interaction: disnake.ApplicationCommandInteraction):
#     await interaction.send("yes xir")
#     channel = bot.get_channel(settings.CHANNEL_ID)
#     if channel:
#         await channel.send(f"min hate, Jonathan beloved meter at 0% <@{JonID}><@{JonID}><@{JonID}><@{JonID}><@{JonID}>")
        
bot.run(settings.TOKEN)
