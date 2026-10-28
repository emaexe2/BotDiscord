import random
import asyncio
import discord
import os
from discord.ext import commands

siti_inquinamento = [
    "https://www.legambiente.it/",
    "https://www.wwf.it/",
    "https://www.greenpeace.org/italy/",
    "https://www.isprambiente.gov.it/it",
    "https://www.eea.europa.eu/it",
    "https://www.iqair.com/",
    "https://aqicn.org/",
    "https://www.greenme.it/",
    "https://www.inquinamento.com/"
]
testi_inquinamento = [
    (
        "L'inquinamento atmosferico è causato dall'emissione di gas nocivi, polveri sottili "
        "e sostanze chimiche nell'aria, principalmente dovuti ai gas di scarico dei veicoli, "
        "alle attività industriali e ai sistemi di riscaldamento. Questo fenomeno non solo "
        "danneggia la salute respiratoria degli esseri umani, ma contribuisce in modo determinante "
        "al riscaldamento globale e al cambiamento climatico attraverso l'effetto serra."
    ),
    (
        "Questo tipo di inquinamento si verifica quando sostanze inquinanti — come scarichi "
        "industriali non trattati, pesticidi agricoli, rifiuti plastici e prodotti chimici — "
        "vengono rilasciate in fiumi, laghi, mari e falde sotterranee. L'inquinamento idrico "
        "compromette la disponibilità di acqua potabile, altera gli ecosistemi acquatici "
        "e minaccia gravemente la sopravvivenza della fauna e della flora marine."
    ),
    (
        "L'inquinamento acustico è determinato da un livello eccessivo o fastidioso di suoni "
        "e rumori nell'ambiente, provocato soprattutto dal traffico stradale, dai mezzi di trasporto, "
        "dai cantieri edili e dalle attività industriali o ricreative. Un'esposizione prolungata "
        "a questi rumori può causare seri problemi di salute negli esseri umani, tra cui "
        "stress cronico, disturbi del sonno e perdita dell'udito."
    ),
    (
        "L'inquinamento del suolo consiste nella contaminazione della terra causata dall'accumulo "
        "di rifiuti solidi e tossici, dall'uso eccessivo di fertilizzanti chimici e pesticidi "
        "in agricoltura e da sversamenti industriali. Questo processo riduce drasticamente "
        "la fertilità del terreno, danneggia la microfauna sotterranea e permette alle sostanze "
        "tossiche di risalire lungo la catena alimentare."
    ),
    (
        "L'inquinamento luminoso è l'alterazione dei livelli di luce naturale notturna provocata "
        "da un uso eccessivo, scorretto o inefficiente dell'illuminazione artificiale esterna, "
        "come lampioni stradali non schermati e insegne pubblicitarie. Oltre a rappresentare "
        "un enorme spreco energetico, disturba i cicli biologici di molte specie animali "
        "e impedisce la visione del cielo stellato."
    )
]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Accesso come {bot.user}')

@bot.command()
async def inquinamento(ctx):
    testo = random.choice(testi_inquinamento)
    await ctx.send(testo)

@bot.command()
async def siti(ctx):
    sito = random.choice(siti_inquinamento)
    await ctx.send(sito)

@bot.command()
async def foto(ctx):
    scelto = random.choice(os.listdir("immagini"))
    with open('immagini/'+scelto, 'rb') as f:
        dc_file = discord.File(f)
    await ctx.send(file=dc_file)


bot.run("TOKEN")