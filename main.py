import os
from threading import Thread
from flask import Flask
import discord
from discord import app_commands
from discord.ext import commands

# 1. Web Server Flask
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

# --- POPUP MODAL PER SCRIVERE TESTI MULTILINEA ---
class EmbedModal(discord.ui.Modal, title="Crea Messaggio Embed"):
    titolo_input = discord.ui.TextInput(
        label="Titolo",
        placeholder="Inserisci il titolo qui...",
        required=True,
        max_length=256
    )

    testo_input = discord.ui.TextInput(
        label="Contenuto del Messaggio",
        style=discord.TextStyle.paragraph, # Permette l'uso di INVIO e testi multilinea
        placeholder="Scrivi o incolla il tuo messaggio andando a capo liberamente...",
        required=True,
        max_length=4000
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=self.titolo_input.value,
            description=self.testo_input.value,
            color=discord.Color.red() # Bordo ROSSO
        )
        await interaction.response.send_message(embed=embed)

@bot.event
async def on_ready():
    print(f'Bot connesso come {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizzati {len(synced)} slash command(s)")
    except Exception as e:
        print(f"Errore nella sincronizzazione: {e}")

# --- SLASH COMMAND /MSG CHE APRE IL POPUP ---
@bot.tree.command(name="msg", description="Apre la finestra per creare un messaggio formattato")
async def msg(interaction: discord.Interaction):
    await interaction.response.send_modal(EmbedModal())

# 3. Avvio Bot
keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
