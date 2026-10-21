import random
import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send('Ciao!')

@bot.command()
async def emoji(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def ripeti(ctx, *, testo):
    await ctx.send(testo)

@bot.command()
async def indovina(ctx):
    await ctx.send('Indovina un numero tra 1 e 10.')

    def is_correct(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

    answer = random.randint(1, 10)

    try:
        msg = await bot.wait_for('message', check=is_correct, timeout=5.0)
    except asyncio.TimeoutError:
        return await ctx.send(f'Sorry, you took too long it was {answer}.')

    if int(msg.content) == answer:
        await ctx.send('You are right!')
    else:
        await ctx.send(f'Oops. It is actually {answer}.')

bot.run("TOKEN")