from discord.ext import commands
import discord
import yt_dlp
import os
import validators
from youtubesearchpython import VideosSearch

from time import sleep

client = commands.Bot("-")

YDL_OPTIONS = {"format": "bestaudio", "noplaylist": "False"}
FFMPEG_OPTIONS = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn",
}


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.listen()
async def on_message(message):
    if message.content.startswith("бузураб"):
        await message.channel.send("hello")


@client.command()
async def ping(ctx):
    await ctx.channel.send("pong")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("нема команды такой")


@client.command(pass_context=True, aliases=["p"])
async def play(ctx, *, text):
    voice_channel = ctx.message.author.voice.channel
    vc = await voice_channel.connect()
    searchik = text
    if validators.url(searchik) is not True:
        url = VideosSearch(text, limit=1).result()["result"][0]["link"]
        searchik = url
    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(searchik, download=False)
        url = info.get("url", None)
    vc.play(discord.FFmpegPCMAudio(source=url, **FFMPEG_OPTIONS))
    while vc.is_playing():
            await sleep(1)
    if not vc.is_paused():
            await vc.disconnect()


@client.command(pass_context=True, aliases=["s"])
async def stop(ctx):
    await ctx.voice_client.disconnect()


client.run(os.environ["ACCESS_TOKEN"])


