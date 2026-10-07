async def on_submit(self, interaction: discord.Interaction):
        # Utilizza il prefisso r'' per trattare i caratteri come testo normale
        testo_formattato = r"```html" + "\n" + self.testo_input.value + "\n" + r"```"

        embed = discord.Embed(
            title=self.titolo_input.value,
            description=testo_formattato,
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)
