import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='!', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("OTA5MDg5NzU1NTAzOTI3MzQ2.YY_Nzw.Io0k-fb_FteTQ4_W7-VoocjKDlM")