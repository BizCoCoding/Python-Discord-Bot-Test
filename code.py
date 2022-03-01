import discord
import os
import time
with open('BadWords.txt', 'r') as f:
    words = f.read()
    badwords = words.splitlines()

client = discord.Client()
@client.event
async def on_message(message):
    if message.content == "a":
        await message.channel.send('a')
  await client.fetch_channel(channelId)
  channel.guild
  await ctx.reply('Hello!')

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.channel.DMChannel) and message.author != bot.user:
        await message.channel.send('This is a DM')

secret = os.environ['token']
client.run(secret)
