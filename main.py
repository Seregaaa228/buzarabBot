import discord

client = discord.Client()


@client.event
async def on_ready():
    print('БОТ ЗАПУЩЕН')


client.run("ODY2NzE4NDQ2MTc5ODQ0MTA2.YPWodA.t6gO3HvIQZLxOL_2OFzzNRD9oHk")
