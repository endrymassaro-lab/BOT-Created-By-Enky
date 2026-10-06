import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connesso come {bot.user}")

@bot.command(name="ciao")
async def ciao(ctx):
    await ctx.send(f"Ciao {ctx.author.mention}! Il bot è online e funzionante.")

app = Flask('')

@app.route('/')
def home():
    return "Il bot è attivo!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    TOKEN = os.getenv("DISCORD_TOKEN")
    bot.run(TOKEN)
import os
from threading import Thread
from flask import Flask, request
import discord
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

# --- COMANDO BENVENUTO (EMBED) ---
@bot.command(name='welcome')
async def welcome(ctx):
    # Crea la scheda Embed
    embed = discord.Embed(
        title="WELCOME",
        description=(
            f"{ctx.author.mention}\n\n"
            "Preparati a vivere un'esperienza di simulazione senza precedenti su "
            "**Emergency Response: Liberty County (ER:LC)**.\n\n"
            "Nato a luglio del 2026 dall'ambizione e dall'amicizia di un piccolo gruppo di "
            "fondatori, **Authentic Italian RolePlay** rinasce oggi più forte, solido e "
            "appassionato che mai. Il nostro obiettivo? Portare su Roblox un **Roleplay "
            "Statunitense** autentico, curato nei minimi dettagli e fedele in tutto e per tutto "
            "alle dinamiche reali."
        ),
        color=discord.Color.from_rgb(255, 255, 255) # Colore del bordo (Bianco)
    )

    # Imposta la miniatura in alto a destra (Logo)
    # Sostituisci questo link con il link della tua immagine/logo
    embed.set_thumbnail(url="https://i.imgur.com/8N4X0qG.png")

    # Campo 1: Primi Passi
    embed.add_field(
        name="Primi Passi: Come Iniziare",
        value="> ***Verifica il tuo Account:** Collega il tuo profilo Roblox per sbloccare l'accesso al server. Trovi la procedura guidata nel canale: <#123456789012345678>*",
        inline=False
    )

    # Campo 2: Requisiti Importanti
    embed.add_field(
        name="Requisiti Importanti per Fare RP",
        value=(
            "• *Ottenere i **Documenti:** Richiedi la tua cittadinanza ufficiale compilando il modulo nel canale: <#123456789012345678>*\n"
            "• *Studiare le **Regole:** La legge non ammette ignoranza! Leggi con attenzione i nostri tre Regolamenti Ufficiali per evitare sanzioni: <#123456789012345678>*"
        ),
        inline=False
    )

    # Immagine grande in basso (Banner)
    # Sostituisci questo link con il link del tuo banner
    embed.set_image(url="https://i.imgur.com/8N4X0qG.png")

    # Invia l'Embed nel canale
    await ctx.send(embed=embed)

# 3. Avvio Bot
keep_alive()
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
