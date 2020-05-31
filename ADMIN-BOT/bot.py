import discord
import rog
＃自作のやつをインポートしました
from discord.ext import commands


client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='稼働中'))


	


@client.event
async def on_message(message):    
    for word in rog.list:
      if message.author.bot:
        return
      if word in message.content:
        await message.delete()
        embed=discord.Embed(title="現在のコメントは削除されました",description=message.author.mention, color=0xdc0909)
        embed.add_field(name="削除されたコメント:", value= word, inline=True)
        embed.add_field(name="理由：", value="現在のコメントは暴言にあたります", inline=True

        await message.channel.send(message.author.mention)
        await message.channel.send(embed=embed) 
     







           
client.run("トークン")

