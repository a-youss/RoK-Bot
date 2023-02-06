import lightbulb
import hikari
import os
import secret

TOKEN = secret.BOT_TOKEN
bot = lightbulb.BotApp(token=TOKEN, prefix='.', default_enabled_guilds=([1028480665320165486, 874863931284410399]))

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
async def cleo(ctx):
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
async def ed(ctx):
    embed = (
    hikari.Embed(title="Edward of Woodstock", description="Edward openfield")
    .set_image(hikari.File('images/Edward_OpenFieldTomy.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Cid', 'El Cid Talent Builds', aliases=['cid'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def cid(ctx):
    embed = (
    hikari.Embed(title="El Cid", description="El Cid universal build")
    .set_image(hikari.File('images/El-Cid_Universal.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Flavius', 'El Cid Talent Builds', aliases=['Flav', 'flav', 'flavious'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def flav(ctx):
    embed = (
    hikari.Embed(title="Flavius", description="Flavius garrison")
    .set_image(hikari.File('images/Flavius_Garrison.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Khan', 'Genghis Khan Talent Builds', aliases=['khan'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Khan(ctx):
    embed = (
    hikari.Embed(title="Genghis Khan", description="Genghis Khan universal build")
    .set_image(hikari.File('images/Genghis_Universal.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Gilgamesh', 'Gilgamesh Talent Builds', aliases=['gilgamesh', 'gilga', 'Gilga'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def gilga(ctx):
    embed1 = (
    hikari.Embed(title="Gilgamesh", description="Gilgamesh open field")
    .set_image(hikari.File('images/Gilgamesh_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Gilgamesh", description="Gilgamesh rally")
    .set_image(hikari.File('images/Gilgamesh_Rally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Guan', 'Guan Yu Talent Builds', aliases=['guan'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def guan(ctx):
    embed1 = (
    hikari.Embed(title="Guan Yu", description="Guan Yu open field")
    .set_image(hikari.File('images/Guan_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Guan Yu", description="Guan Yu rally")
    .set_image(hikari.File('images/Guan_Rally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Barca', 'Hannibal Barca Talent Builds', aliases=['barca', 'hannibal', 'Hannibal'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def barca(ctx):
    embed1 = (
    hikari.Embed(title="Hannibal Barca", description="Hannibal Barca mixed troop rally")
    .set_image(hikari.File('images/Hannibal_MixTroops.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)

@bot.command
@lightbulb.command('Harald', 'Harald Sigurdsson Talent Builds', aliases=['harald', 'Harold', 'harold'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def harald(ctx):
    embed1 = (
    hikari.Embed(title="Harald Sigurdsson", description="Harald open field")
    .set_image(hikari.File('images/Harald_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Harald Sigurdsson", description="Harald rally")
    .set_image(hikari.File('images/Harald_Rally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Honda', 'Honda Tadakatsu Talent Builds', aliases=['honda'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def honda(ctx):
    embed1 = (
    hikari.Embed(title="Honda Tadakatsu", description="Honda open field")
    .set_image(hikari.File('images/Honda_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Honda Tadakatsu", description="Honda/Tomyris open field")
    .set_image(hikari.File('images/Honda_Tomy.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Ishida', 'Ishida Talent Builds', aliases=['ishida'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Ishida(ctx):
    embed = (
    hikari.Embed(title="Ishida", description="Ishida gathering")
    .set_image(hikari.File('images/Ishida_Gathering.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Jadwiga', 'Jadwiga Talent Builds', aliases=['jadwiga', 'Jad', 'jad'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def jad(ctx):
    embed = (
    hikari.Embed(title="Jadwiga", description="Jadwiga garrison")
    .set_image(hikari.File('images/Jadwiga_Garrison.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Leonidas', 'Leonidas Talent Builds', aliases=['Leo', 'leo', 'leonidas'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Leo(ctx):
    embed = (
    hikari.Embed(title="Leonidas", description="Leonidas open field")
    .set_image(hikari.File('images/Leonidas_Tanky.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Lubu', 'Lu Bu Talent Builds', aliases=['Lu', 'lu', 'lubu'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Lubu(ctx):
    embed = (
    hikari.Embed(title="Lu Bu", description="Lu Bu mixed rally")
    .set_image(hikari.File('images/Lu-Bu_Universal.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Mehmed', 'Mehmed Talent Builds', aliases=['mehmed'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Mehmed(ctx):
    embed = (
    hikari.Embed(title="Mehmed", description="Mehmed mixed rally")
    .set_image(hikari.File('images/Mehmed_MixCityRally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Ramesses', 'Ramesses Talent Builds', aliases=['ramesses', 'ram', 'Ram'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def ram(ctx):
    embed = (
    hikari.Embed(title="Ramesses", description="Ramesses universal")
    .set_image(hikari.File('images/Ramesses_OpenFieldRally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Scipio', 'Scipio Prime Talent Builds', aliases=['ScipioP', 'scipioP', 'scipiop', 'scipio', 'Scipiop'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def scipio(ctx):
    embed = (
    hikari.Embed(title="Scipio Prime", description="Scipio open field")
    .set_image(hikari.File('images/Scipio_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Seondeok', 'Seondeok Talent Builds', aliases=['seon', 'Seon', 'seondeok'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def seon(ctx):
    embed = (
    hikari.Embed(title="Seondeok", description="Seondeok gathering")
    .set_image(hikari.File('images/Seondeok_Gathering.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Takeda', 'Takeda Talent Builds', aliases=['takeda'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def takeda(ctx):
    embed = (
    hikari.Embed(title="Takeda Shingen", description="Takeda speed build")
    .set_image(hikari.File('images/Takeda_Speedy.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Tomyris', 'Tomyris Talent Builds', aliases=['Tomy', 'tomy', 'tomyris'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def tomy(ctx):
    embed = (
    hikari.Embed(title="Tomyris", description="Tomyris open field")
    .set_image(hikari.File('images/Tomyris_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('William', 'William Talent Builds', aliases=['william'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def william(ctx):
    embed = (
    hikari.Embed(title="William", description="William universal")
    .set_image(hikari.File('images/William_OpenRally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Wu', 'Wu Zetian Talent Builds', aliases=['wu'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def wu(ctx):
    embed = (
    hikari.Embed(title="Wu Zetian", description="Wu Zetian garrison")
    .set_image(hikari.File('images/Wu-Zetian_Garrison.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('YSS', 'Yi Sun-sin Talent Builds', aliases=['yss', 'Yss'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def yss(ctx):
    embed = (
    hikari.Embed(title="Yi Sun-sin", description="Yi Sun-sin garrison")
    .set_image(hikari.File('images/YSS_Garrison.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('YSG', 'Yi Seong-Gye Talent Builds', aliases=['ysg', 'Ysg'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def ysg(ctx):
    embed = (
    hikari.Embed(title="Yi Seong-Gye", description="Yi Seong-Gye garrison")
    .set_image(hikari.File('images/YSG_Open.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Minamoto', 'Minamoto no Yoshitsune Talent Builds', aliases=['mina', 'Mina', 'minamoto'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def mina(ctx):
    embed1 = (
    hikari.Embed(title="Minamoto no Yoshitsune", description="Minamoto open field")
    .set_image(hikari.File('images/Minamoto_SustainedOpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Minamoto no Yoshitsune", description="Minamoto barb fort rally")
    .set_image(hikari.File('images/Minamoto_NeutralUnitRally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Moctezuma', 'Moctezuma Talent Builds', aliases=['moct', 'Moct', 'moctezuma'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def moct(ctx):
    embed1 = (
    hikari.Embed(title="Moctezuma", description="Moctezuma open field")
    .set_image(hikari.File('images/Moctezuma_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Moctezuma", description="Moctezuma barb fort rally")
    .set_image(hikari.File('images/Moctezuma_Peacekeeping.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Saladin', 'Saladin Talent Builds', aliases=['saladin'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def saladin(ctx):
    embed1 = (
    hikari.Embed(title="Saladin", description="Saladin open field")
    .set_image(hikari.File('images/Saladin_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Saladin", description="Saladin/Aethelflaed open field")
    .set_image(hikari.File('images/Saladin_OpenFieldAeth.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Trajan', 'Trajan Talent Builds', aliases=['trajan'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def trajan(ctx):
    embed1 = (
    hikari.Embed(title="Trajan", description="Trajan open field")
    .set_image(hikari.File('images/Trajan_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Trajan", description="Trajan/Aethelflaed open field")
    .set_image(hikari.File('images/Trajan_OpenWithAeth.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Nebu', 'Nebuchadnezzar Talent Builds', aliases=['nebu', 'Nebuchadnezzar', 'nebuchadnezzar'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def nebu(ctx):
    embed1 = (
    hikari.Embed(title="Nebuchadnezzar", description="Nebuchadnezzar open field")
    .set_image(hikari.File('images/Nebu_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Nebuchadnezzar", description="Nebuchadnezzar rally")
    .set_image(hikari.File('images/Nebu_Rally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Pakal', "K'inich Janaab' Pakal Talent Builds", aliases=['pakal'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def pakal(ctx):
    embed1 = (
    hikari.Embed(title="K'inich Janaab' Pakal", description="Pakal open field")
    .set_image(hikari.File('images/Pakal_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="K'inich Janaab' Pakal", description="Pakal rally")
    .set_image(hikari.File('images/Pakal_Rally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Suleiman', "Suleiman Talent Builds", aliases=['suleiman'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def suleiman(ctx):
    embed1 = (
    hikari.Embed(title="Suleiman", description="Suleiman open field")
    .set_image(hikari.File('images/Suleiman_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Suleiman", description="Suleiman rally")
    .set_image(hikari.File('images/Suleiman_Rally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Richard', "Richard Talent Builds", aliases=['richard', 'dick', 'Dick'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def dick(ctx):
    embed1 = (
    hikari.Embed(title="Richard", description="Richard open field")
    .set_image(hikari.File('images/Richard_TankyOpen.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Richard", description="Richard garrison")
    .set_image(hikari.File('images/Richard_Garrison.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Theodora', "Theodora Talent Builds", aliases=['theodora', 'theo', 'Theo'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def theo(ctx):
    embed1 = (
    hikari.Embed(title="Theodora", description="Theodora city garrison")
    .set_image(hikari.File('images/Theodora_CityGarrison.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Theodora", description="Theodora garrison")
    .set_image(hikari.File('images/Theodora_Garrison.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Bertrand', "Bertrand Talent Builds", aliases=['bertrand', 'Bert', 'bert'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def bert(ctx):
    embed1 = (
    hikari.Embed(title="Bertrand", description="Bertrand open field")
    .set_image(hikari.File('images/Bertrand_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed1)
    embed2 = (
    hikari.Embed(title="Bertrand", description="Bertrand rally")
    .set_image(hikari.File('images/Bertrand_Rally.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed2)

@bot.command
@lightbulb.command('Boudica', 'Boudica Prime Talent Builds', aliases=['BoudicaP', 'boudicap', 'boudicaP', 'boudica', 'Boudicap'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def boudica(ctx):
    embed = (
    hikari.Embed(title="Boudica Prime", description="Boudica universal")
    .set_image(hikari.File('images/Boudica_Prime.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Joan', 'Joan Prime Talent Builds', aliases=['JoanP', 'joanp', 'joanP', 'joan', 'Joanp'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Joan(ctx):
    embed = (
    hikari.Embed(title="Joan Prime", description="Joan open field")
    .set_image(hikari.File('images/JoanP_OpenField.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Henry', 'Henry Talent Builds', aliases=['henry'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Henry(ctx):
    embed = (
    hikari.Embed(title="Henry", description="Henry universal")
    .set_image(hikari.File('images/Henry.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Jan', 'Jan Zizka Talent Builds', aliases=['jan'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def Henry(ctx):
    embed = (
    hikari.Embed(title="Jan Zizka", description="Jan Zizka garrison")
    .set_image(hikari.File('images/JanZizka_Garrison.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Tariq', 'Tariq Ibn Ziyad Talent Builds', aliases=['tariq'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def sargon(ctx):
    embed = (
    hikari.Embed(title="Tariq Ibn Ziyad", description="Tariq Ibn Ziyad Rally")
    .set_image(hikari.File('images/Sargon.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

@bot.command
@lightbulb.command('Sargon', 'Sargon The Geat Talent Builds', aliases=['sargon'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def sargon(ctx):
    embed = (
    hikari.Embed(title="Sargon The Geat", description="Sargon The Geat Universal")
    .set_image(hikari.File('images/Sargon.png'))
    .set_footer("Brought to you by kingdom 2545")
    )
    await ctx.respond(embed)

bot.run()