import discord
from discord.ext import commands
from tokenimm import *
import os, random
import requests
import string

"""
todo interneten veri çek 

todo reklam ver

todo yeni özelikler getir

todo wikipedia dan ctrl c/ctrl v yap ve kaynak belirt
"""

intents = discord.Intents.default()
intents.message_content = True
dosya = tokenem()
bot = commands.Bot(command_prefix="!eco ", intents=intents)


@bot.command()
async def help_eco(ctx):
    yardim_mesaji = """
    Hello! I'm an eco-friendly Discord bot. Here are the commands you can use:
    
    !eco information - Learn about environmental cleanliness and sustainability.
    !eco recycling - Get tips on recycling.
    !eco energy_saving - Get suggestions on saving energy.

    """
    await ctx.send(yardim_mesaji)


@bot.command()
async def information(ctx):
    bilgi_mesaji = "You can visit the websites of environmental organizations to get information about environmental cleanliness and sustainability."
    await ctx.send(bilgi_mesaji)


# Geri dönüşüm komutunu oluşturun
@bot.command()
async def recycling(ctx):
    geri_donusum_mesaji = "Recycling is the process of converting waste materials into new materials and objects. This concept often includes the recovery of energy from waste materials. The recyclability of a material depends on its ability to reacquire the properties it had in its original state.[1] It is an alternative to 'conventional' waste disposal that can save material and help lower greenhouse gas emissions. It can also prevent the waste of potentially useful materials and reduce the consumption of fresh raw materials, reducing energy use, air pollution (from incineration) and water pollution (from landfilling).  source: wikipedia"
    await ctx.send(geri_donusum_mesaji)


# Enerji tasarrufu komutunu oluşturun
@bot.command()
async def energy_saving(ctx):
    enerji_tasarrufu_mesaji = "You can make small changes at home and at work to save energy. For example, remember to turn off the lights and turn off unnecessary electronics💡."
    await ctx.send(enerji_tasarrufu_mesaji)


bot.run(dosya)
