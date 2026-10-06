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

# --- NUOVO SLASH COMMAND /MSG (FORMATTATO) ---
@bot.tree.command(name="msg", description="Invia un messaggio formattato con il tuo testo")
@app_commands.describe(testo="Il testo che vuoi appaia nell'embed")
async def msg(interaction: discord.Interaction, testo: str):
    # Questa riga permette di inserire a capo scrivendo \n nel messaggio
    messaggio_formattato = testo.replace('\\n', '\n')

    # Crea l'Embed (la cornice) con il tuo testo personalizzato
    embed = discord.Embed(
        description=messaggio_formattato,
        color=discord.Color.from_rgb(255, 255, 255) # Colore del bordo (Bianco)
    )

    # --- OPZIONALE: Immagini ---
    # Se vuoi anche il logo e il banner, togli il '#' dalle righe qui sotto e metti i link
    # embed.set_thumbnail(url="LINK_DEL_TUO_LOGO")
    # embed.set_image(url="LINK_DEL_TUO_BANNER")

    # Invia l'Embed
    await interaction.response.send_message(embed=embed)

# 3. Avvio Bot
keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
