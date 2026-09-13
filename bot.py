import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Load cogs
async def load_cogs():
    """Load all cogs from the cogs directory"""
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded cog: {filename}')
            except Exception as e:
                print(f'Failed to load cog {filename}: {e}')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Latency: {bot.latency}')

@bot.event
async def on_message(message):
    """Handle message events"""
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)

@bot.command(name='ping', help='Check bot latency')
async def ping(ctx):
    """Ping command to check bot latency"""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! Latency: {latency}ms')

@bot.command(name='help', help='Show help message')
async def help_command(ctx):
    """Display help information"""
    embed = discord.Embed(
        title='TurboBot Help',
        description='TurboBot is a moderation bot for TurboWrap communities',
        color=discord.Color.blue()
    )
    embed.add_field(name='!ping', value='Check bot latency', inline=False)
    embed.add_field(name='!moderate', value='Check and moderate TurboWrap comments', inline=False)
    embed.add_field(name='!fix', value='Fix formatting in TurboWrap comments', inline=False)
    
    await ctx.send(embed=embed)

async def main():
    """Main entry point"""
    async with bot:
        await load_cogs()
        token = os.getenv('DISCORD_TOKEN')
        if not token:
            raise ValueError('DISCORD_TOKEN not found in environment variables')
        await bot.start(token)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
