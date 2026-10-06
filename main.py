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
