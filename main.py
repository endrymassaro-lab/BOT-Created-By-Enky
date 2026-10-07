async def on_submit(self, interaction: discord.Interaction):
        # Apre e chiude il blocco di codice HTML in modo sicuro
        testo_pulito = "```html\n" + self.testo_input.value + "\n```"

        embed = discord.Embed(
            title=self.titolo_input.value,
            description=testo_pulito,
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)
