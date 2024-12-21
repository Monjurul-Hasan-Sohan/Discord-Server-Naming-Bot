# Discord Server Naming Bot

This is a Discord bot designed to automate the process of creating and managing server channels, applying naming conventions, and adding emojis. It is capable of setting up channels based on a predefined list, ensuring proper naming formats, and making it easier to manage server structures.

## Features

- **Auto-creates channels**: The bot automatically creates channels based on a predefined list.
- **Adds Emojis**: The bot adds emojis to channel names based on naming conventions.
- **Name Formatting**: Ensures that the channel names follow a specified format, including emojis and separators (`|`).
- **Reset Function**: Allows for resetting the server by deleting and recreating the channels with correct names and emojis.

## Prerequisites

Before running the bot, you need to have the following:

- Python 3.x installed on your system.
- A Discord bot created on the [Discord Developer Portal](https://discord.com/developers/applications).
- The `discord.py` library installed.

## Installation

Follow these steps to get the bot running on your local machine:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/discord-server-naming-bot.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd discord-server-naming-bot
    ```

3. **Install required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create your Discord bot**:
    - Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new bot.
    - Copy your bot token from the portal.

5. **Set up the bot token**:
    - In `setup_bot.py`, replace `"YOUR_BOT_TOKEN"` with your actual bot token:
    ```python
    bot.run("YOUR_BOT_TOKEN")
    ```

## Configuration

You can customize the bot’s behavior by adjusting the following configuration settings in `setup_bot.py`:

- **command_prefix**: The prefix for bot commands (default is `!`).
- **intents**: Specify which events the bot should listen to (e.g., messages, reactions).

Example:

```python
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

bot = commands.Bot(command_prefix="!", intents=intents)
```

Make sure to enable the **MESSAGE CONTENT INTENT** in the Discord Developer Portal if you need to interact with message content.

## Commands

### `!setup`

This command sets up the channels, adds emojis, and formats them according to the specified rules.

Usage:
```bash
!setup
```

Example:
```bash
!setup
```

### `!reset`

This command deletes all channels and recreates them from scratch with the correct format.

Usage:
```bash
!reset
```

Example:
```bash
!reset
```

## Example Code Snippet

Below is an example of how to set up and run the bot:

```python
import discord
from discord.ext import commands

# Create intents to read messages
intents = discord.Intents.default()
intents.message_content = True  # This is required to read message content

# Initialize the bot with the chosen command prefix and intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Event triggered when the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Command to set up channels
@bot.command()
async def setup(ctx):
    # Add logic here to create channels and apply naming conventions
    await ctx.send("Channels have been set up!")

# Command to reset channels (delete and recreate)
@bot.command()
async def reset(ctx):
    # Add logic to delete and recreate channels
    await ctx.send("Channels have been reset!")

# Run the bot with your token
bot.run("YOUR_BOT_TOKEN")
```

## Troubleshooting

If you encounter issues, check the following:

### 1. **401 Unauthorized Error**:
   - If you get an error like `discord.errors.LoginFailure: Improper token has been passed.`, ensure that your bot token is correctly copied and hasn't been regenerated in the Discord Developer Portal.
   - Double-check that you are using the correct bot token in the `bot.run()` function.

### 2. **Privileged Intents Error**:
   - If the bot doesn't work because of missing intents (e.g., `discord.errors.PrivilegedIntentsRequired`), go to the [Discord Developer Portal](https://discord.com/developers/applications) and enable the `MESSAGE CONTENT INTENT` under the **Privileged Gateway Intents** section of your bot's page.

### 3. **Missing Dependencies**:
   - If you see errors related to missing modules, ensure all dependencies are installed using the command:
     ```bash
     pip install -r requirements.txt
     ```

### 4. **Bot Not Responding**:
   - Make sure the bot has appropriate permissions to manage channels in the server.
   - Check if the bot is online and has a valid session.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
