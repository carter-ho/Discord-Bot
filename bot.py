import discord
import requests
from discord.ext import commands
import constants


discord_key = constants.discord_key


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(pass_context=True)
async def hello(ctx):
    """Answers a !hello command"""
    msg = 'Hello {0.author.mention}'.format(ctx.message)
    await ctx.send(msg)

@bot.command(pass_context=True)
async def dailyUseless(ctx):
    uselessFact = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/today")
    await ctx.send(uselessFact.json()["text"])

@bot.command(pass_context=True)
async def randomUseless(ctx):
    uselessFact = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    await ctx.send(uselessFact.json()["text"])


@bot.command(pass_context = True) #passing context
async def salute(ctx): #context gets passed into the first parameter
    print(str(ctx.message.author))
    print(str(ctx.message.channel))
    print(str(ctx.message.content))
            
bot.run(discord_key)