import discord
import os



client = discord.Client()


@client.event
async def on_ready():
    print('БОТ ЗАПУЩЕН')


client.run(str(os.environ.get("TOKEN")))
