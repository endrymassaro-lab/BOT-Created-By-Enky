async def on_submit(self, interaction: discord.Interaction):
        # Racchiude il testo nel blocco di codice senza spezzare la stringa
        testo_formattato = "```html\n" + self.testo_input.value + "\n```"

        embed = discord.Embed(
            title=self.titolo_input.value,
            description=testo_formattato,
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)
