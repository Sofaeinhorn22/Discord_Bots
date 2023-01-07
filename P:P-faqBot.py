import interactions
from discord import Client

bot = Client()
bot = interactions.Client(token="XXXXXXXXX")
print('Bot ok')

### /example
@bot.command(
    name="xxx",
    description="XXxXX",
    scope=918234675061878855,
)
async def mc(ctx: interactions.CommandContext):
        await ctx.send("xXx")
    
    
### /M4
@bot.command(
    name="m4",
    description="Details on the M4",
    scope=918234675061878855,
)
async def m4(ctx: interactions.CommandContext):
        embed=discord.Embed(title="M4", description="Details on the M4", color=0x0000ff)
        embed.set_author(name="#1.0.2.0")
        embed.set_thumbnail(url="https://www.kotte-zeller.de/$WS/kotte-zeller-shop/websale8_shop-kotte-zeller-shop/produkte/medien/bilder/gross/44791a_1.jpg")
        embed.add_field(name="Basic Stats", value="", inline=True)
        embed.add_field(name="Attachment", value="undefined", inline=False)
        embed.set_footer(text="Mady by Sofaeinhorn")
        await ctx.send(embed=embed)
