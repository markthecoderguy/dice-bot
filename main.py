import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

secret_role = "Gamer"

@bot.command()
async def info(ctx):
    await ctx.send(f"{ctx.author.mention} remember !info to show this panel \n !dice rolls a 6 sided dice \n !dicesides x rolls a x sided dice \n !dicemm x y rolls a dice between x and y \n !coinflip flips a coin")

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.command()
async def dice(ctx):
    result = random.randint(1, 6)
    await ctx.send(f"{ctx.author.mention} mate you rolled a **{result}** nice one")

@bot.command()
async def twodice(ctx):
    result = random.randint(1, 6)
    result2 = random.randint(1,6)
    await ctx.send(f"{ctx.author.mention} rolled 2 dices,  mate you rolled a **{result + result2}** nice one, ei {result} + {result2}")

@bot.command()
async def dicesides(ctx, *, msg):
    sides = int(str(msg).strip())
    if sides == 0:
        await ctx.send(f"{ctx.author.mention} i cant roll a 0 sided dice bro")
    elif sides == 1:
        await ctx.send(f"{ctx.author.mention} i cant roll a 1 sided dice bro")
    elif sides > 1000000:
        await ctx.send(f"{ctx.author.mention} too many sides")
    else:
        result = random.randint(1, sides)
        await ctx.send(f"{ctx.author.mention} rolled a {sides} sided dice, mate you rolled a **{result}** nice one")

@bot.command()
async def dicemm(ctx, *, msg):
    print(msg)
    list = str(msg).strip().split(" ")
    print(list)
    minside = int(list[0])
    maxside = int(list[1])
    if minside >= maxside:
        await ctx.send(f"{ctx.author.mention} min side has to be more than maxside btw")
    elif maxside == 0:
        await ctx.send(f"{ctx.author.mention} i cant roll a 0 sided dice bro")
    elif maxside == 1:
        await ctx.send(f"{ctx.author.mention} i cant roll a 0 sided dice bro")
    elif maxside > 1000000:
        await ctx.send(f"{ctx.author.mention} too many sides")
    else:
        result = random.randint(minside, maxside)
        await ctx.send(f"{ctx.author.mention} rolled a dice between {minside} and {maxside} sided dice, mate you rolled a **{result}** nice one ")

@bot.command()
async def coinflip(ctx):
    result = random.randint(1,2)
    if result == 1:
        await ctx.send(f"{ctx.author.mention} mate you flipped a **head** nice one")
    if result == 2:
        await ctx.send(f"{ctx.author.mention} mate you flipped a **tail** nice one")



bot.run(token, log_handler=handler, log_level=logging.DEBUG)
