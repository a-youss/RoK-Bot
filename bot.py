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

@bot.listen(lightbulb.CommandErrorEvent)
async def info(event):
    await event.context.respond('Commander was not found!')

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

@bot.command
@lightbulb.command('Amanitore', 'Amanitore Talent Builds', aliases=['Amani', 'amani', 'amanitore'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def amani(ctx):
    embed1 = (
    hikari.Embed(title="Amanitore", description="Amanitore open field")
    .set_image(hikari.File('images/Amanitore_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Amanitore", description="Amanitore garrison")
    .set_image(hikari.File('images/Amanitore_Garrison.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)


@bot.command
@lightbulb.command('Artemisia', 'Artemisia Talent Builds', aliases=['Arte', 'arte', 'artemisia', 'arti', 'Arti'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def arte(ctx):
    embed1 = (
    hikari.Embed(title="Artemisia", description="Artemisia open field")
    .set_image(hikari.File('images/Artemisia_TankyOpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Artemisia", description="Artemisia garrison")
    .set_image(hikari.File('images/Artemisia_Garrison.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Attila', 'Attila Talent Builds', aliases=['At', 'at', 'AT', 'attila'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def attila(ctx):
    embed1 = (
    hikari.Embed(title="Attila", description="Attila open field")
    .set_image(hikari.File('images/Attila_OpenField_InOut.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Attila", description="Attila Takeda rally")
    .set_image(hikari.File('images/Attila_GenericRally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)
    embed3 = (
    hikari.Embed(title="Attila", description="Attila Nevsky rally")
    .set_image(hikari.File('images/AttilaNevRally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed3)

@bot.command
@lightbulb.command('JC', 'Caesar Talent Builds', aliases=['jc', 'Jc', 'Caesar', 'caesar', 'Julius', 'julius'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def JC(ctx):
    embed = (
    hikari.Embed(title="Juilus Caesar", description="Caesar mixed troops rally build")
    .set_image(hikari.File('images/Caesar_MixTroopsRally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('CC', 'Cao Cao Talent Builds', aliases=['Caocao', 'Cc', 'cc', 'caocao', 'cao', 'Cao'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def CC(ctx):
    embed = (
    hikari.Embed(title="Cao Cao", description="Cao Cao speed build")
    .set_image(hikari.File('images/Cao-Cao_SpeedyTalents.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Chandra', 'Chandra Gupta Talent Builds', aliases=['chandra', 'Gupta', 'gupta'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Chandra(ctx):
    embed1 = (
    hikari.Embed(title="Chandra Gupta", description="Chandra Gupta open field")
    .set_image(hikari.File('images/Chandragupta_Field.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Chandra Gupta", description="Chandra Gupta rally")
    .set_image(hikari.File('images/Chandragupta_Rally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Charlemagne', 'Charlemagne Talent Builds', aliases=['charlemagne'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Charlemagne(ctx):
    embed = (
    hikari.Embed(title="Charlemagne", description="Charlemagne rally")
    .set_image(hikari.File('images/Charlemagne_Rally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('CM', 'Charles Martel Talent Builds', aliases=['cm', 'Cm', 'Charles', 'charles', 'Martel', 'martel'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def CM(ctx):
    embed1 = (
    hikari.Embed(title="Charles Martel", description="Charles Martel open field")
    .set_image(hikari.File('images/Charles-Martel_Field.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Charles Martel", description="Charles Martel garrison")
    .set_image(hikari.File('images/Charles-Martel_Garrison.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Cheok', 'Cheok Talent Builds', aliases=['cheok', 'cj', 'Cj', 'CJ'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def CJ(ctx):
    embed = (
    hikari.Embed(title="Cheok Jun-gyeong", description="Cheok Jun-gyeong open field")
    .set_image(hikari.File('images/Cheok_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Cleopatra', 'Cleopatra Talent Builds', aliases=['cleopatra', 'Cleo', 'cleo'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def CJ(ctx):
    embed = (
    hikari.Embed(title="Cleopatra", description="Cleopatra gathering")
    .set_image(hikari.File('images/Cleopatra_Gathering.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Constantine', 'Constantine Talent Builds', aliases=['constantine', 'Connie', 'connie'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Constantine(ctx):
    embed1 = (
    hikari.Embed(title="Constantine", description="Constantine open field")
    .set_image(hikari.File('images/Constantine_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Constantine", description="Constantine garrison")
    .set_image(hikari.File('images/Constantine_GarrisonGeneric.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Cyrus', 'Cyrus Talent Builds', aliases=['cyrus'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Cyrus(ctx):
    embed = (
    hikari.Embed(title="Cyrus The Great", description="Cyrus universal")
    .set_image(hikari.File('images/Cyrus_OpenFieldRally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Edward', 'Edward Talent Builds', aliases=['edward', 'Ed', 'ed'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Cyrus(ctx):
    embed = (
    hikari.Embed(title="Edward of Woodstock", description="Edward openfield")
    .set_image(hikari.File('images/Edward_OpenFieldTomy.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Cid', 'El Cid Talent Builds', aliases=['cid'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Cyrus(ctx):
    embed = (
    hikari.Embed(title="El Cid", description="El Cid universal build")
    .set_image(hikari.File('images/El-Cid_Universal.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Flavius', 'El Cid Talent Builds', aliases=['Flav', 'flav', 'flavious'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Cyrus(ctx):
    embed = (
    hikari.Embed(title="Flavius", description="Flavius garrison")
    .set_image(hikari.File('images/Flavius_Garrison.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

bot.run()