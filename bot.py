import os
from dotenv import load_dotenv
import nextcord
from nextcord import Interaction, SlashOption, Embed, Intents
from nextcord.ext import commands

# Load environment variables
load_dotenv()
TOKEN = os.getenv("token")
GUILD_ID = int(os.getenv("guild_id"))

# Create intents
intents = Intents.default()
intents.members = True
intents.message_content = True

# Define a bot instance with a command prefix
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# Example of a slash command
@bot.slash_command(name="hello", description="Responds with Hello!", guild_ids=[GUILD_ID])
async def hello(interaction: Interaction):
    await interaction.response.send_message("Hello!")


# Run the bot
bot.run(TOKEN)
