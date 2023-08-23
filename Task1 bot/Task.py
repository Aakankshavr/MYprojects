from discord.ext import commands
import discord
import random
from tinydb import TinyDB,Query
intents=discord.Intents.default()
client=commands.Bot(command_prefix="!",intents=intents)
register_words=["registration","register","commence","class","start"]
reply_info=["Limited seats available!Sign up today","Ready to learn? Register now","Your learning journey begins with registration-Enroll today"]


@client.event()
async def on_message(ctx):
    await ctx.send("Hey! I'm a musical instruments tutor bot")
async def on_message(message):
    if message.content.startswith('~Tutorials'):
        await message.send("We offer tutorials on instruments like Keyboard,Veena,Guitar,Violin,Flute etc")
        msg=message.content
    if any(word in msg for word in register_words):
        await message.send(random.choice(reply_info))

bot.run('token')
