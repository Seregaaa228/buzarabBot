
from decouple import config
from discord.ext import commands
import discord
import validators
import os

client = commands.Bot('-')


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.listen()
async def on_message(message):
    if message.content.startswith('бузураб'):
        voice = discord.utils.get(client.voice_clients, guild=message.guild)
        voice.play(discord.FFmpegPCMAudio('sounds\\4xIdzwZN6UsN.128.mp3'))

@client.command()
async def ping(ctx):
        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

     
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
       await ctx.send("нету команды такой")      

async def stop(ctx):    
    await ctx.voice_client.disconnect()


client.run(os.environ["ACCESS_TOKEN"])