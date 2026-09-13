# TurboBot - Discord Bot for TurboWrap

A Discord bot designed to moderate and fix TurboWrap comments with automated quality checks and moderation tools.

## Features

- **Comment Moderation**: Automatically flags and monitors TurboWrap comments for quality issues
- **Comment Fixing**: Helps fix formatting issues in TurboWrap comments
- **Auto-Moderation**: Enable/disable automatic moderation based on configurable patterns
- **Moderation Logs**: Sends flagged messages to a dedicated moderation channel
- **Admin Commands**: Full command set for server moderators

## Setup

### Prerequisites

- Python 3.8+
- Discord Bot Token
- A Discord server

### Installation

1. Clone the repository:
```bash
git clone https://github.com/TurboWrap/TurboBot.git
cd TurboBot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file from the template:
```bash
cp .env.example .env
```

4. Add your Discord bot token to `.env`:
```
DISCORD_TOKEN=your_discord_token_here
```

5. Run the bot:
```bash
python bot.py
```

## Commands

### User Commands

- `!ping` - Check bot latency
- `!help` - Show help message
- `!fix <text>` - Fix formatting in text

### Moderator Commands (requires manage_messages permission)

- `!moderate info` - Show moderation tools
- `!moderate enable` - Enable auto-moderation
- `!moderate disable` - Disable auto-moderation
- `!moderate status` - Check moderation status

## Configuration

Edit `.env` file to customize:
- `DISCORD_TOKEN` - Your bot token
- `BOT_PREFIX` - Command prefix (default: `!`)
- `MODERATION_ENABLED` - Enable/disable moderation (default: true)
- `LOG_CHANNEL` - Channel for moderation logs (default: moderation-logs)

## Project Structure

```
TurboBot/
├── bot.py              # Main bot file
├── requirements.txt    # Python dependencies
├── .env.example        # Environment template
├── cogs/               # Discord bot cogs
│   └── moderation.py   # Moderation cog
└── README.md           # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is part of TurboWrap - a nonprofit effort to add more features and advanced implementations.

## Support

For issues or questions, please open an issue on the GitHub repository.
