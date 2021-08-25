import discord
import os



client = discord.Client()


@client.event
async def on_ready():
    print('БОТ ЗАПУЩЕН')


print("This is my secret key: " + str(os.environ.get("TOKEN")))
