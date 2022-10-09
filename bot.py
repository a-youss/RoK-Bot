from ast import alias
from imaplib import Commands
import lightbulb
import hikari
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = lightbulb.BotApp(token=TOKEN, prefix='.', default_enabled_guilds=(1028480665320165486))

@bot.command
@lightbulb.command('cavalry', 'Send the Best Cavalry Equipment', aliases=['cav', 'Cavalry', 'Cav'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def cavalry(ctx):
    f = hikari.File('images/Cavalry.png')
    await ctx.respond(f)

@bot.command
@lightbulb.command('infantry', 'Send the Best Cavalry Equipment', aliases=['inf', 'Infantry', 'Inf'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def cavalry(ctx):
    f = hikari.File('images/Infantry.png')
    await ctx.respond(f)

@bot.command
@lightbulb.command('archers', 'Send the Best Cavalry Equipment', aliases=['arch', 'Archers', 'Arch', 'archer', 'Archer'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def cavalry(ctx):
    f = hikari.File('images/Archers.png')
    await ctx.respond(f)



bot.run()