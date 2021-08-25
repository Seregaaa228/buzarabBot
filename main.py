import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="-")


@client.event
async def on_ready():
    print('БОТ ЗАПУЩЕН')


@client.command()
async def play(ctx, url: str):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="General")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if not voice.is_connected():
        await voiceChannel.connect()


@client.command()
async def stop(ctx):
    voice = discord.utils.get(ctx.guild.voice_channels, name="General")
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("БОТ ОФНУЛСЯ")


client.run(str(os.environ.get("TOKEN")))
