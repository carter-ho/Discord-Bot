import os
import json
import random
import discord
import requests
from discord.ext import commands
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import constants



discord_key = constants.discord_key


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Hello Command
@bot.command(pass_context=True)
async def hello(ctx):
    """Answers a !hello command"""
    msg = 'Hello {0.author.mention}'.format(ctx.message)
    await ctx.send(msg)

# Daily Useless Fact
@bot.command(pass_context=True)
async def dailyuseless(ctx):
    uselessFact = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/today")
    await ctx.send(uselessFact.json()["text"])

# Random Useless Fact
@bot.command(pass_context=True)
async def randomuseless(ctx):
    uselessFact = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    await ctx.send(uselessFact.json()["text"])


# Testing function
@bot.command(pass_context = True) #passing context
async def salute(ctx): #context gets passed into the first parameter
    print(str(ctx.message.author))
    print(str(ctx.message.channel))
    print(str(ctx.message.content))

# 
@bot.command(pass_contex = True)
async def helpme(ctx, *, arg):
    text = arg + " Kit!"
    randomNum = random.randint(0, 1)
    img = ""
    if(randomNum):
        img = Image.open('images/wish.png')
    else:
        img = Image.open('images/wish2.png')
    
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype("fonts/trebuc.ttf", 110)
    # 122, 371
    if(randomNum):
        I1.text((180,500), text, font=myFont, fill=(255,255,255), stroke_width=10, stroke_fill=(0,0,0))
    else:
        I1.text((122,371), text, font=myFont, fill=(255,255,255), stroke_width=10, stroke_fill=(0,0,0))
    location = "images/wishMeme.png"
    img.save(location)
    picture = discord.File(location)
    await ctx.send(file=picture)
    img.close()
    if(os.path.exists(location)):
        os.remove(location)

@bot.command(pass_contex = True)
async def artofwar(ctx):
    f = open("jsons/quotes.json")
    data = json.load(f)
    upper = len(data)
    randomNum = random.randint(0, upper-1)
    await ctx.send(data[randomNum])

@bot.command(pass_contex = True)
async def dice(ctx, arg):
    try:
        arg = int(arg)
        rand = random.randint(1, arg)
    except:
        await ctx.send("Not a valid number value")
    else:
        await ctx.send(rand)

@bot.command(pass_contex = True)
async def copy(ctx, *, arg):
    await ctx.send(arg)

            
bot.run(discord_key)