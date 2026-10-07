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

bot.run(TOKEN)