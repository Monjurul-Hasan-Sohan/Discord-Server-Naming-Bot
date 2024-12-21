# Discord Server Naming Bot

This is a Discord bot that automatically manages server channels by adding custom emojis and handling naming conventions. The bot performs actions like creating channels, adding emojis, and ensuring consistency in naming formats.

## Features

- **Auto-creates channels**: The bot creates server channels based on a predefined list of categories.
- **Adds Emojis**: The bot adds emojis to channels based on naming conventions.
- **Name Formatting**: Ensures that channel names follow the correct format with emojis and separators (`|`).

## Prerequisites

Before running the bot, ensure you have the following:

- Python 3.x installed on your machine.
- A Discord bot created and token generated.
- `discord.py` library installed.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/discord-server-naming-bot.git
    ```

2. Navigate to the project directory:
    ```bash
    cd discord-server-naming-bot
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create your bot on the [Discord Developer Portal](https://discord.com/developers/applications).
    - After creating your bot, copy the bot token.

5. Add your bot token in `setup_bot.py`:
    ```python
    bot.run("YOUR_BOT_TOKEN")
    ```

## Configuration

You can modify the behavior of the bot by adjusting these variables in `setup_bot.py`:

- **command_prefix**: The prefix for bot commands (default is `!`).
- **intents**: Specify which events the bot should listen to, such as messages and reactions.

```python
intents = discord.Intents.default()
intents.message_content = True  # This is required to read message content

bot = commands.Bot(command_prefix="!", intents=intents)
