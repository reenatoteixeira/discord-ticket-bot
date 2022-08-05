import discord
from discord import app_commands
from discord.ext import commands
import os

serverId = # Server ID goes here
supportRoleId = # Support Role ID goes here
botToken = # Bot Token goes here

class Dropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(value="ticket",label="Ticket", emoji="👋"),
            discord.SelectOption(value="denuncia",label="Fazer denúncia", emoji="📨"),
        ]
        super().__init__(
            placeholder="Selecione uma opção...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="persistent_view:dropdown_help"
        )
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "ticket":
            await interaction.response.send_message("O usuário escolheu ticket")
        elif self.values[0] == "denuncia":
            await interaction.response.send_message("O usuário escolheu denuncia")

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(Dropdown())

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def setup_hook(self) -> None:
        self.add_view(DropdownView())

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync(guild = discord.Object(id=serverId))
            self.synced = True
        print(f"Entramos como {self.user}.") 

aclient = client()

tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=serverId), name = 'setup', description='Insere o menu de tickets no canal.')
@commands.has_permissions(manage_guild=True)
async def setup(interaction: discord.Interaction):
    await interaction.channel.send("Mensagem do painel", view=DropdownView()) 
    await interaction.response.send_message("Menu inserido com sucesso", ephemeral=True) 

aclient.run(botToken)