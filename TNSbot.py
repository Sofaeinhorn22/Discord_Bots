import interactions
from discord import Client


bot = Client()
bot = interactions.Client(token="XXXXXXXXX")
print('Eingeloggt als')


### /example
@bot.command(
    name="xxx",
    description="XXxXX",
    scope=918234675061878855,
)
async def mc(ctx: interactions.CommandContext):
        await ctx.send("xXx")









### /mr-beast_1
@bot.command(
    name="mr-beast_1",
    description="MR. Beast hip-jazz",
    scope=918234675061878855,
)
async def mc(ctx: interactions.CommandContext):
        await ctx.send("https://cdn.discordapp.com/attachments/918234675959447617/1061328983997816924/mr-beast_1.mp4")

### /mrbeast-hip-jazz
@bot.command(
    name="mrbeast-hip-jazz",
    description="MR. Beast hip-jazz",
    scope=918234675061878855,
)
async def mc(ctx: interactions.CommandContext):
        await ctx.send("https://cdn.discordapp.com/attachments/918234675959447617/1061330184764137623/mr-hip-jazz-mrbeast-ytpmv.mp4")


### /r14
@bot.command(
    name="r14",
    description="Ruel 14.",
    scope=918234675061878855,
)
async def mc(ctx: interactions.CommandContext):
        await ctx.send("https://media.tenor.com/dcxOO-080OcAAAAM/discord-moderators.gif")


### /PROPAGANDA
@bot.command(
    name="propaganda",
    description="PROPAGANDA",
    scope=918234675061878855,
)
async def mc(ctx: interactions.CommandContext):
        await ctx.send("https://media.tenor.com/W7z6EeVRU00AAAAM/warning-this.gif")

### /mods
@bot.command(
    name="mods",
    description="MOD CHECK",
    scope=918234675061878855,
)
async def mc(ctx: interactions.CommandContext):
        await ctx.send("https://media.tenor.com/qj9y9K3nqPkAAAAC/txacky.gif")

### /ask
@bot.command(
    name="ask",
    description="When i didnt ask",
    scope=918234675061878855,
)
async def server(ctx: interactions.CommandContext):
        await ctx.send("https://media.tenor.com/ha3akd-n2wAAAAAS/when-i-didnt-ask-didnt-ask.gif")
 

### /ip
@bot.command(
    name="ip",
    description="Die IP's der Server",
    scope=918234675061878855,
)
async def ip(ctx: interactions.CommandContext):
    if ctx.channel.id == 918234676269830157:
        await ctx.send("Die generelle ip von unseren Server ist 135.125.201.201\nNur der port ist was Sich ändert\nSCP:SL = 7777\nMinecraft = 25565\nProject Zomboid = 16261 UND 16262")
    
### /cm
@bot.command(
    name="cm",
    description="CedMod Info",
    scope=918234675061878855,
)
async def cm(ctx: interactions.CommandContext):
    if ctx.channel.id == 918234676269830157:
        await ctx.send("Du findest unsere CedMod Seite hier\nhttps://thenextstep.cmod.app")
    
    
### /server
@bot.command(
    name="server",
    description="Eine Liste unserer Game Server",
    scope=918234675061878855,
)
async def server(ctx: interactions.CommandContext):
    if ctx.channel.id == 918234676269830157:
        await ctx.send("**Project Zomboid:** '[GER] The Next Step' https://prnt.sc/57Y-MVj1iMx8\n**SCP:SL:** '[GER] TheNextStep' https://prnt.sc/qh5c1JPAOI4Q\n**Minecraft 1.16.5:** Würde ich wießen wie der dort heißt...")
 
### /cum
@bot.command(
    name="cum",
    description="Cum",
    scope=918234675061878855,
)
async def cum(ctx: interactions.CommandContext):
    if ctx.channel.id == 918234676269830157:
        await ctx.send("https://media.tenor.com/y9M0u2PJrF4AAAAd/explosion-milk.gif")
 
bot.start()
