from ast import Import
import lightbulb
import hikari
import os
import secret

TOKEN = secret.BOT_TOKEN
bot = lightbulb.BotApp(token=TOKEN, prefix='.', default_enabled_guilds=(1028480665320165486))

if os.name != "nt":
    import uvloop

    uvloop.install()

@bot.command
@lightbulb.command('info', 'Send the Best Cavalry Equipment')
@lightbulb.implements(lightbulb.PrefixCommand)
async def info(ctx):
    await ctx.respond('Prefix: . \nFor Equipment type the prefix and the troop type \nFor talent trees type the prefix and the commander you wish to see')

@bot.command
@lightbulb.command('cavalry', 'Send the Best Cavalry Equipment', aliases=['cav', 'Cavalry', 'Cav'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def cavalry(ctx):
    f = hikari.File('images/Cavalry.png')
    embed = (
    hikari.Embed(title="Cavalry Equipment", description="Cavalry equipment guide")
    .set_image(f)
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)
    

@bot.command
@lightbulb.command('infantry', 'Send the Best Infantry Equipment', aliases=['inf', 'Infantry', 'Inf'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def cavalry(ctx):
    f = hikari.File('images/Infantry.png')
    embed = (
    hikari.Embed(title="Infantry Equipment", description="Infantry equipment guide")
    .set_image(f)
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('archers', 'Send the Best Archers Equipment', aliases=['arch', 'Archers', 'Arch', 'archer', 'Archer'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def cavalry(ctx):
    f = hikari.File('images/Archers.png')
    embed = (
    hikari.Embed(title="Archer Equipment", description="Archer equipment guide")
    .set_image(f)
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('xy', 'Send the Best Cavalry Equipment', aliases=['Xy, Xiang Yu, xiang yu', 'XY'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def xy(ctx):
    embed1 = (
    hikari.Embed(title="Xiang Yu", description="XY openfield build")
    .set_image(hikari.File('images/Xiang_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Xiang Yu", description="XY rally talent build")
    .set_image(hikari.File('images/Xiang_Rally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

bot.run()