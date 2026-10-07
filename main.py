async def on_submit(self, interaction: discord.Interaction):
        # Utilizzo della concatenazione sicura scritta tutta su un'unica riga
        testo_formattato = "```html\n" + self.testo_input.value + "\n```"

        embed = discord.Embed(
            title=self.titolo_input.value,
            description=testo_formattato,
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)
