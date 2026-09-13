import discord
from discord.ext import commands
import logging

class UtilitiesCog(commands.Cog):
    """Utility commands for TurboBot"""
    
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)
    
    @commands.command(name='status', help='Show bot status')
    async def bot_status(self, ctx):
        """Display bot status and statistics"""
        embed = discord.Embed(
            title='🤖 TurboBot Status',
            color=discord.Color.green()
        )
        embed.add_field(name='Latency', value=f'{round(self.bot.latency * 1000)}ms', inline=True)
        embed.add_field(name='Guilds', value=len(self.bot.guilds), inline=True)
        embed.add_field(name='Users', value=len(self.bot.users), inline=True)
        embed.add_field(name='Uptime', value='See logs for details', inline=False)
        
        await ctx.send(embed=embed)
    
    @commands.command(name='info', help='Show bot information')
    async def bot_info(self, ctx):
        """Display information about TurboBot"""
        embed = discord.Embed(
            title='TurboBot Information',
            description='A moderation bot for TurboWrap communities',
            color=discord.Color.blue()
        )
        embed.add_field(name='Purpose', value='Moderate and fix TurboWrap comments', inline=False)
        embed.add_field(name='Repository', value='[TurboWrap/TurboBot](https://github.com/TurboWrap/TurboBot)', inline=False)
        embed.add_field(name='Discord.py Version', value=discord.__version__, inline=True)
        
        await ctx.send(embed=embed)
    
    @commands.command(name='invite', help='Get bot invite link')
    async def invite(self, ctx):
        """Get bot invite link"""
        permissions = discord.Permissions(
            manage_messages=True,
            send_messages=True,
            embed_links=True,
            read_message_history=True
        )
        oauth_url = discord.utils.oauth_url(
            self.bot.user.id,
            permissions=permissions,
            scopes=['bot']
        )
        embed = discord.Embed(
            title='Invite TurboBot',
            description=f'[Click here to invite TurboBot]({oauth_url})',
            color=discord.Color.blurple()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(UtilitiesCog(bot))
