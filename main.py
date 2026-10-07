import os
from threading import Thread
from flask import Flask
import discord
from discord import app_commands
from discord.ext import commands

app = Flask('')

@app.route('/')
def home():
    return "Bot Online!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connesso come {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizzati {len(synced)} slash command(s)")
    except Exception as e:
        print(f"Errore nella sincronizzazione: {e}")

@bot.tree.command(name="msg", description="Invia un messaggio formattato con titolo e testo")
@app_commands.describe(titolo="Il titolo in alto nell'embed", testo="Il corpo del messaggio")
async def msg(interaction: discord.Interaction, titolo: str, testo: str):
    # Converte i simboli \n scritti in chat in veri e propri a capo
    testo_formattato = testo.replace('\\n', '\n')

    embed = discord.Embed(
        title=titolo,
        description=testo_formattato,
        color=discord.Color.red()
    )
    await interaction.response.send_message(embed=embed)

keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
