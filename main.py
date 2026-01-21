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
    elif sides < 0:
        await ctx.send(f"{ctx.author.mention} i cant roll a negative sided dice bro, lock tf in")
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

@bot.command()
async def goon(ctx):
    await ctx.send(f"{ctx.author.mention} bro what r u on about lock tf in gang")

@bot.command()
async def looksmax(ctx):
    result = random.randint(1,100)
    if result >= 95:
        await ctx.send(f"{ctx.author.mention} true adam")
    elif result >= 90:
        await ctx.send(f"{ctx.author.mention} chad")
    elif result >= 85:
        await ctx.send(f"{ctx.author.mention} chad lite")
    elif result >= 75:
        await ctx.send(f"{ctx.author.mention} htn")
    elif result >= 65:
        await ctx.send(f"{ctx.author.mention} mtn")
    elif result >= 55:
        await ctx.send(f"{ctx.author.mention} ltn")
    elif result >= 40:
        await ctx.send(f"{ctx.author.mention} sub 5")
    elif result >= 20:
        await ctx.send(f"{ctx.author.mention} sub 3")
    else:   
        await ctx.send(f"{ctx.author.mention} sub human")
   
@bot.command()
async def job(ctx):
    await ctx.send(f"{ctx.author.mention} you can find jobs here: https://www.seek.com.au/ or here: https://www.linkedin.com/jobs/ ")
   
@bot.command()
async def elkin(ctx):
    await ctx.send(f"{ctx.guild.get_member(1053413965637623910).mention} elkin is a legend and a top bloke, so much aura, true adam")

@bot.command()
async def mark(ctx):
    await ctx.send(f"{ctx.guild.get_member(810532743653228654).mention} mark is cool, creator of this amazing bot, mtn")
 
bot.run(token, log_handler=handler, log_level=logging.DEBUG)


