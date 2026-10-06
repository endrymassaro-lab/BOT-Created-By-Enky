import os
from threading import Thread
from flask import Flask
import discord
from discord import app_commands
from discord.ext import commands

# 1. Web Server Flask per tenere il bot attivo
app = Flask('')

@app.route('/')
def home():
    return "Bot Online!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. Configurazione Bot Discord
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connesso come {bot.user}')
    # Sincronizza gli Slash Commands con Discord
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizzati {len(synced)} slash command(s)")
    except Exception as e:
        print(f"Errore nella sincronizzazione: {e}")

# --- SLASH COMMAND /WELCOME ---
@bot.tree.command(name="welcome", description="Invia il messaggio ufficiale di benvenuto")
async def welcome(interaction: discord.Interaction):
    embed = discord.Embed(
        title="WELCOME",
        description=(
            f"{interaction.user.mention}\n\n"
            "Preparati a vivere un'esperienza di simulazione senza precedenti su "
            "**Emergency Response: Liberty County (ER:LC)**.\n\n"
            "Nato a luglio del 2026 dall'ambizione e dall'amicizia di un piccolo gruppo di "
            "fondatori, **Authentic Italian RolePlay** rinasce oggi più forte, solido e "
            "appassionato che mai. Il nostro obiettivo? Portare su Roblox un **Roleplay "
            "Statunitense** autentico, curato nei minimi dettagli e fedele in tutto e per tutto "
            "alle dinamiche reali."
        ),
        color=discord.Color.from_rgb(255, 255, 255)
    )

    embed.set_thumbnail(url="https://i.imgur.com/8N4X0qG.png")

    embed.add_field(
        name="Primi Passi: Come Iniziare",
        value="> ***Verifica il tuo Account:** Collega il tuo profilo Roblox per sbloccare l'accesso al server. Trovi la procedura guidata nel canale: <#123456789012345678>*",
        inline=False
    )

    embed.add_field(
        name="Requisiti Importanti per Fare RP",
        value=(
            "• *Ottenere i **Documenti:** Richiedi la tua cittadinanza ufficiale compilando il modulo nel canale: <#123456789012345678>*\n"
            "• *Studiare le **Regole:** La legge non ammette ignoranza! Leggi con attenzione i nostri tre Regolamenti Ufficiali per evitare sanzioni: <#123456789012345678>*"
        ),
        inline=False
    )

    embed.set_image(url="https://i.imgur.com/8N4X0qG.png")

    await interaction.response.send_message(embed=embed)

# 3. Avvio Bot
keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
