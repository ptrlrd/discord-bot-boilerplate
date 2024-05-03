
# Basic Discord Bot Boilerplate

This project contains a simple Discord bot using Nextcord, specifically, stable. Their wrapper for the Discord API can be found here https://docs.nextcord.dev/en/stable/. The bot is containerized using Docker, making deployment and management straightforward.

## Setting Up Your Discord Bot

### Create a Bot on Discord

1. **Create an Application**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click on the "New Application" button.
   - Enter a name for your application, check the terms and services agreement, and click "Create".
   - Give it a image, name, and description

2. **Copy the Bot Token**:
   - Under the "TOKEN" section, click "Copy" to get your bot's token. **Do not share this token with anyone or post it on github, people will post stuff to your discord**.

3. **Invite Bot to Your Server**:
   - Navigate to the "OAuth2" tab.
   - Under "SCOPES", select "bot".
   - Under "BOT PERMISSIONS", select the permissions your bot needs.
   - Copy the generated URL, open it in a web browser, and invite your bot to a server where you have administrative privileges.

### Configure Your Environment

Create a `.env` file in your project directory and add the following lines (replace placeholder values with your actual data):

```plaintext
TOKEN=your_discord_bot_token
GUILD_ID=your_discord_guild_id
```

## Building and Running the Bot Using Docker

### Build the Docker Image

To build the Docker image for your bot, run the following command in the directory containing your Dockerfile:

```bash
docker build -t ‎gonk-disdroid‎ .
```

### Run the Bot Using Docker Compose

Ensure you have Docker Compose installed, and run the following command to start your bot:

```bash
docker-compose up -d
```

## Stopping and Removing the Bot

To stop the Docker container running the bot, use the following Docker Compose command:

```bash
docker-compose down
```
