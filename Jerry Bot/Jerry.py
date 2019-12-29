import discord
import json
import os
from discord.ext import commands

token = 'NjE0NTkzNTA3NzQ2OTA2MTQ1.XbjPJw.uYD9uJqiARfMg3ghlRZ_sxmC_kY'
client = commands.Bot(command_prefix = 'j!')
client.remove_command('help')
data = {}           #database to store json infos

with open('SongsDB.json', 'r') as songdb:
    data = (json.load(songdb))    #copies infos on SongsDB.json to our data dictionary
    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity =discord.Game("Praising Jesus"))
    print("Bot is ready")
    print(os.getcwd())

@client.event
async def on_member_join(member):
    member.send("Welcome to our Praise Team!")

@client.command()
async def hi(ctx):
    await ctx.send("Hello there! My name is Jerry")

@client.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name = 'Help')
    embed.add_field(name = 'hi:', value = "Jerry says hi!", inline = False)
    embed.add_field(name = 'sdb [songname]:', value = "returns the number of the songs in the storage", inline = False)
    embed.add_field(name = 'viewsongs:', value = "view all the songs in the data base", inline = False)
    await ctx.send(author, embed = embed )

@client.command()
async def sdb(ctx, songName):
    await ctx.send("There are "+str(data[songName.lower()])+" copies available")

@client.command()
async def viewsongs(ctx):
    for song in data:
        await ctx.send(song + " : " + str(data[song]))


client.run(token)