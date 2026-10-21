import discord
import random
import os
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')


@bot.command()
async def ciao(ctx, nome):
    await ctx.send(f'Ciao {nome}!')


@bot.command()
async def meme(ctx):
    scelto = random.choice(os.listdir("meme"))
    with open('meme/'+scelto, 'rb') as f:
        dc_file = discord.File(f)
    await ctx.send(file=dc_file)

@bot.command()
async def animali(ctx):
    scelto = random.choice(os.listdir("animali"))
    with open('animali/'+scelto, 'rb') as f:
        dc_file = discord.File(f)
    await ctx.send(file=dc_file)

@bot.command()
async def montagne(ctx):
    scelto = random.choice(os.listdir("montagne"))
    with open('montagne/'+scelto, 'rb') as f:
        dc_file = discord.File(f)
    await ctx.send(file=dc_file)

bot.run("TOKEN")

