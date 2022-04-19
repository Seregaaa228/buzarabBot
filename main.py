from discord.ext import commands
import discord
import yt_dlp 
import os

from time import sleep
client = commands.Bot("-")

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'False'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.listen()
async def on_message(message):
    if message.content.startswith('бузураб'):
       await message.send('я')

@client.command()
async def ping(ctx):
	await ctx.channel.send("pong")
     
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send("нема команды такой")      

@client.command(pass_context = True, aliases=["p"])
async def play(ctx, args):
    voice_channel = ctx.message.author.voice.channel
    vc = await voice_channel.connect()
    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(args, download = False)
            url = info.get("url", None)       
    vc.play(discord.FFmpegPCMAudio(source = url, **FFMPEG_OPTIONS))
    while vc.is_playing():
        await sleep(1)
    await vc.disconnect()

@client.command(pass_context = True , aliases=['s'])
async def stop(ctx):    
    await ctx.voice_client.disconnect()

client.run(os.environ["ACCESS_TOKEN"])

