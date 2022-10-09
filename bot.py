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
@lightbulb.command('xy', 'Xiang Yu Talent Builds', aliases=['Xy', 'Xiang', 'xiang', 'XY'])
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

@bot.command
@lightbulb.command('zeno', 'Zenobia Talent Builds', aliases=['Zeno', 'Zenobia', 'zenobia'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def zeno(ctx):
    embed = (
    hikari.Embed(title="Zenobia", description="Zenobia garrison build")
    .set_image(hikari.File('images/Zenobia_Garrison.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('nevsky', 'Alexander Nevsky Talent Builds', aliases=['Nev', 'Nevsky', 'nev'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def nev(ctx):
    embed = (
    hikari.Embed(title="Alexander Nevsky", description="Nevsky universal build")
    .set_image(hikari.File('images/Nevsky.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('freddie', 'Frederick Talent Builds', aliases=['Frederick', 'Freddie', 'Fred', 'fred', 'frederick'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def fred(ctx):
    embed = (
    hikari.Embed(title="Frederick", description="Frederick mixed troops rally build")
    .set_image(hikari.File('images/Frederick_MixTroopsRally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('ragnar', 'Ragnar Talent Builds', aliases=['Ragnar'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def ragnar(ctx):
    embed = (
    hikari.Embed(title="Ragnar", description="Ragnar mixed troops rally build")
    .set_image(hikari.File('images/Ragnar_Rally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('aethel', 'Aethelflaed Talent Builds', aliases=['Aethel', 'Aethelflaed', 'aethelflaed'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def aethel(ctx):
    embed = (
    hikari.Embed(title="Aethelflaed", description="Aethelflaed mixed troops openfield")
    .set_image(hikari.File('images/Aethelflaed_FieldMixTroops.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Alex', 'Alexander The Great Talent Builds', aliases=['alex', 'Alexander', 'alexander'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def alex(ctx):
    embed1 = (
    hikari.Embed(title="Alexander The Great", description="Alex no skill damage build")
    .set_image(hikari.File('images/Alexander_FieldNoSkillDMG.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Alexander The Great", description="Alex skill damage build")
    .set_image(hikari.File('images/Alexander_FieldRallySkillDMG.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)


bot.run()