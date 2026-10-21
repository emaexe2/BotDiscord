import discord
import random

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('ciao'):
        await message.channel.send("Ciao!")
    elif message.content.startswith('arrivederci'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('password'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('emoji'):
        await message.channel.send(gen_emodji())
    else:
        await message.channel.send(message.content)
client.run("TOKEN")