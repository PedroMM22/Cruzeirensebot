import discord
from discord.ext import commands
from config import TOKEN
from bot_logic import gen_pass
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def oi(ctx):
    await ctx.send(f'Olá! eu sou um {bot.user}!!!!!!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def senha(ctx, size = 10):
    await ctx.send(gen_pass(size))

@bot.command()
async def sixseven(ctx):
    await ctx.send('https://klipy.com/gifs/nub-nub-cat-25')

@bot.command()
async def meme(ctx):
    escolha = random.choice(os.listdir('Memes'))
    with open(f'Memes/{escolha}', 'rb') as f:
        image = discord.File(f)
    await ctx.send(file = image)

@bot.command()
async def hino(ctx):

    text = '*Este é o hino do maior de Minas:*'


    with open(f'sounds/hino-cruzeiro.mp3', 'rb') as f:
        sound = discord.File(f)
    await ctx.send(text, file = sound)

bot.run(TOKEN)