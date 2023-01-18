from discord import Intents, Embed, Game, Interaction
from discord.ext.commands import Bot
from random import randint

client = Bot(command_prefix="/", intents=Intents.all(), help_command=None)
embed_color = 0x00ff2a

@client.event
async def on_ready():
    await client.tree.sync()
    print("HAZIR!")
    await client.change_presence(activity=Game(name="/yardım"))

@client.tree.command(name="zar_at", description="Zar atar.")
async def zar_at(interaction : Interaction):
    num = randint(1,6)
    msg = Embed(description=f"Zar Atıldı!\nSonuç: {num}", color=embed_color)
    await interaction.response.send_message(embed=msg)

@client.tree.command(name="davet", description="Botu kendi sunucunuza eklemeniz için gereken linki verir.")
async def davet(interaction : Interaction):
    link = "https://discord.com/api/oauth2/authorize?client_id=1053667622606090341&permissions=8&scope=bot"
    msg = Embed(description=f"Link : {link}", color=embed_color)
    await interaction.response.send_message(embed=msg)


@client.tree.command(name="yardım", description="Botta bulunan komutların listesini verir.")
async def yardım(interaction : Interaction):
    msg = Embed(title="KOMUTLAR:\n------------------", description="/zar_at\n/yardım", color=embed_color)
    await interaction.response.send_message(embed=msg)

client.run("MTA1MzY2NzYyMjYwNjA5MDM0MQ.Gntm-m.MnL5Qv4vQPsw5HzMs8BcrnCLh5DcGteg3IPSgM")