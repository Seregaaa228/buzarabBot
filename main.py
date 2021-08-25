import discord


token = "ODY2NzE4NDQ2MTc5ODQ0MTA2.YPWodA.4JholynjVlQuJF46OuVnqqGkYXs"



client = discord.Client()


@client.event
async def on_ready():
    print('БОТ ЗАПУЩЕН')

client.run(token)

