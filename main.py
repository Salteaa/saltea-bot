import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True  # Required for reading messages

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(discord_token)
