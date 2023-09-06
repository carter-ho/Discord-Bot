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

@bot.command(pass_context=False)
async def commandhelp(ctx):
    text = """```!hello```  
    Bot says hello to the user that invoked the command

    ```!randomuseless```  

    Bot sends a random fact from https://uselessfacts.jsph.pl/

    ```!dailyuseless```  

    Bot sends the daily fact from https://uselessfacts.jsph.pl/

    ```!randomcat```

    Bot sends a picture of a random cat from The Cat API

    ```!randomdog```

    Bot sends a picture of a random dog from The Dog API

    ```!helpme```  

    Bot sends one of two meme edits of a scene of the character Seihai-Kun from the anime Carnival Phantasm.

    ```!artofwar```  

    Bot sends a random quote from the Art of War. Credit for the quotes.json file used goes to github:mattdesl

    ```!dice [X]```  

    Bot sends a value between 1 and X, inclusive. Truncates non-integers, does not work with negative values.

    ```!copy [Y]```  

    Bot sends the message Y"""
    await ctx.send(text)

# Hello Command
@bot.command(pass_context=True)
async def hello(ctx):
    """Answers a !hello command"""
    msg = 'Hello {0.author.mention}'.format(ctx.message)
    await ctx.send(msg)

# Daily Useless Fact
@bot.command(pass_context=False)
async def dailyuseless(ctx):
    uselessFact = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/today")
    await ctx.send(uselessFact.json()["text"])

# Random Useless Fact
@bot.command(pass_context=False)
async def randomuseless(ctx):
    uselessFact = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    await ctx.send(uselessFact.json()["text"])

@bot.command(pass_context=False)
async def randomcat(ctx):
    randomCat = requests.get("https://api.thecatapi.com/v1/images/search")
    await ctx.send(randomCat.json()[0]["url"])

@bot.command(pass_context=False)
async def randomdog(ctx):
    randomDog = requests.get("https://api.thedogapi.com/v1/images/search")
    await ctx.send(randomDog.json()[0]["url"])


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
    w, h = img.size

    I1.text((w//2, h * 9/10 ), text, anchor = 'md', font=myFont, fill=(255,255,255), stroke_width=10, stroke_fill=(0,0,0))

    location = "images/wishMeme.png"
    img.save(location)
    picture = discord.File(location)
    await ctx.send(file=picture)
    img.close()
    if(os.path.exists(location)):
        os.remove(location)

@bot.command(pass_contex = False)
async def artofwar(ctx):
    f = open("./jsons/artofwar.json")
    data = json.load(f)
    upper = len(data)
    randomNum = random.randint(0, upper-1)
    await ctx.send(data[randomNum])

@bot.command(pass_context = False)
async def magic8ball(ctx):
    f = open("./jsons/8ball.json")
    data = json.load(f)
    numResponseTypes = len(data)
    responseType = random.randint(0, numResponseTypes-1)
    numResponses = len(data[responseType])
    responseNum = random.randint(0, numResponses-1)
    await ctx.send(data[responseType][responseNum])

@bot.command(pass_contex = False)
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