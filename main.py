'''
This is skeleton code for making discord bot that takes a prefix and has a diction of things you want to send to the channel
'''
import random
import discord #need to install this from https://pypi.org/project/discord.py/
from discord.ext import commands #this will work once it's installed
dictionaryHere={}
cooldDownPhrases=[]

bot=commands.Bot(command_prefix='whatEverYouWant',case_insensitive=True)#case_insensitive=True is default false is up to you

@bot.event
async def on_ready():
    print('What ever you want it to tell you when its ready to do the commands')

@bot.command(name='Phrase you are trying to detect')
@commands.cooldown(1, 60, commands.BucketType.user)#How often a user can call the bot
async def whatEverYouWantThisToBeNamed(ctx):
    if (ctx.author.bot): return #checks to see if the user is a bot so it can't trigger it
    response=dictionaryHere[""]#dictionary entry for whatever
    await ctx.send(response)
#Cooldown error handling
@whatEverYouWantThisToBeNamed.error
async def php_error(ctx, error):
    pharses=random.choice(cooldDownPhrases)#Randomizes phrases from your list
    await ctx.send(pharses)
