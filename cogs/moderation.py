import discord
from discord.ext import commands
import re

class ModerationCog(commands.Cog):
    """Cog for moderating and fixing TurboWrap comments"""
    
    def __init__(self, bot):
        self.bot = bot
        self.bot.moderation_active = True
    
    @commands.Cog.listener()
    async def on_message(self, message):
        """Monitor messages for TurboWrap comment issues"""
        if message.author == self.bot.user or not self.bot.moderation_active:
            return
        
        # Check for potential issues in TurboWrap comments
        if await self.check_comment_quality(message):
            await self.flag_message(message)
    
    async def check_comment_quality(self, message):
        """Check if a message contains TurboWrap comment issues"""
        content = message.content.lower()
        
        # List of patterns that indicate low-quality comments
        issues = [
            r'spam|flood|abuse',
            r'\.{3,}',  # Excessive dots
            r'!{2,}',   # Excessive exclamation marks
            r'\?{2,}',  # Excessive question marks
        ]
        
        for pattern in issues:
            if re.search(pattern, content):
                return True
        
        return False
    
    async def flag_message(self, message):
        """Flag a message that needs moderation"""
        try:
            embed = discord.Embed(
                title='⚠️ Comment Flagged for Review',
                description=f'**Author:** {message.author.mention}\n**Content:** {message.content[:100]}...',
                color=discord.Color.orange()
            )
            embed.add_field(name='Action', value='Use `/moderate review` to handle this message', inline=False)
            embed.set_footer(text=f'Message ID: {message.id}')
            
            # Send to a moderation channel if it exists
            mod_channel = discord.utils.get(message.guild.channels, name='moderation-logs')
            if mod_channel:
                await mod_channel.send(embed=embed)
        except Exception as e:
            print(f'Error flagging message: {e}')
    
    @commands.command(name='moderate', help='Moderate a TurboWrap comment')
    @commands.has_permissions(manage_messages=True)
    async def moderate_comment(self, ctx, action: str = 'info'):
        """Moderate TurboWrap comments"""
        if action.lower() == 'info':
            embed = discord.Embed(
                title='Moderation Tools',
                description='Tools for moderating TurboWrap comments',
                color=discord.Color.blue()
            )
            embed.add_field(name='!moderate enable', value='Enable auto-moderation', inline=False)
            embed.add_field(name='!moderate disable', value='Disable auto-moderation', inline=False)
            embed.add_field(name='!moderate status', value='Check moderation status', inline=False)
            await ctx.send(embed=embed)
        
        elif action.lower() == 'enable':
            self.bot.moderation_active = True
            await ctx.send('✅ Auto-moderation enabled!')
        
        elif action.lower() == 'disable':
            self.bot.moderation_active = False
            await ctx.send('❌ Auto-moderation disabled!')
        
        elif action.lower() == 'status':
            status = '✅ Enabled' if self.bot.moderation_active else '❌ Disabled'
            await ctx.send(f'Moderation Status: {status}')
    
    @commands.command(name='fix', help='Fix formatting in TurboWrap comments')
    async def fix_comment(self, ctx, *, text: str):
        """Fix formatting issues in text"""
        fixed = text
        
        # Remove excessive punctuation
        fixed = re.sub(r'\.{3,}', '...', fixed)
        fixed = re.sub(r'!{2,}', '!', fixed)
        fixed = re.sub(r'\?{2,}', '?', fixed)
        
        # Clean up whitespace
        fixed = ' '.join(fixed.split())
        
        embed = discord.Embed(
            title='Fixed Comment',
            description=f'**Original:** {text}\n\n**Fixed:** {fixed}',
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ModerationCog(bot))
