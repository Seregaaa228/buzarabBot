import discord
from discord.utils import get
from discord.ext import commands
from youtube_dl import YoutubeDL
from asyncio import sleep
import os

client = commands.Bot(command_prefix='-')


@client.event
async def on_ready():
    print('БОТ ГОТОВ')


YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'False'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
players = {}
queues = {}




@client.command()
async def play(ctx, music):
    discord.opus.load_opus()
    if not discord.opus.is_loaded():
        raise Exception('Opus failed to load')
    global vc
    global info
    try:
        voice_channel = ctx.message.author.voice.channel

        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            vc = await voice.move_to(voice_channel)
        else:
            vc = await voice_channel.connect()
    except AttributeError:
        await ctx.channel.send("ПОЛЬЗОВАТЕЛЬ НЕ В ГОЛОСОВОМ")

    else:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(music, download=False)

        URL = info['formats'][0]['url']

        vc.play(discord.FFmpegPCMAudio(source=URL, **FFMPEG_OPTIONS))
        await ctx.channel.send('МУЗЫКА ИГРАЕТ - ' + info.get('title'))

        while vc.is_playing():
            await sleep(1)
        if not vc.is_paused():
            await vc.disconnect()


@client.command()
async def p(ctx, music):
    discord.opus.load_opus()
    if not discord.opus.is_loaded():
        raise Exception('Opus failed to load')
    global vc
    global info
    try:
        voice_channel = ctx.message.author.voice.channel

        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            vc = await voice.move_to(voice_channel)
        else:
            vc = await voice_channel.connect()
    except AttributeError:
        await ctx.channel.send("ПОЛЬЗОВАТЕЛЬ НЕ В ГОЛОСОВОМ")

    else:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(music, download=False)

        URL = info['formats'][0]['url']

        vc.play(discord.FFmpegPCMAudio(source=URL, **FFMPEG_OPTIONS))
        await ctx.channel.send('МУЗЫКА ИГРАЕТ - ' + info.get('title'))

        while vc.is_playing():
            await sleep(1200)
        if not vc.is_paused():
            await vc.disconnect()


@client.command()
async def stop(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client:
        await ctx.channel.send('ОТКЛЮЧАЮСЬ')
        await sleep(1)
        await voice_client.disconnect()
    else:
        await ctx.channel.send('Я НЕ В КАНАЛЕ')


client.run(os.environ.get("TOKEN"))
