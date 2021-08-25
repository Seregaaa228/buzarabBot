import discord
f = open('TOKEN.txt', 'r')

client = discord.Client()


@client.event
async def on_ready():
    print('БОТ ЗАПУЩЕН')


client.run(f.read())
f.close()
