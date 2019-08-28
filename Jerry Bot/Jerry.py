import discord
from discord.ext import commands

token = 'NjE0NTkzNTA3NzQ2OTA2MTQ1.XWbdOw.i-YHhnMxKBF9fYP101Ocn0zJNEM'
client = commands.Bot(command_prefix = 'j!')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity =discord.Game("Praising Jesus"))
    print("Bot is ready")

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

    await ctx.send(author, embed = embed )



client.run(token)