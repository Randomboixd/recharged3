import discord
from discord.ext import commands
import platform

class beta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="about", description="About Coconutbot")
    async def aboutcommand(self, ctx):
        

        embed = discord.Embed(title="Coconutbot Recharged 3.0", description="*Coconutbot Recharged is a heavily modified version of Coconutbot_osrelease [[check it out on github](https://github.com/RandomboiXD/Coconutbot_osrelease)]*", color=0xED4245)
        embed.add_field(name="Projects used:", value="py-cord [[check out their site](https://pycord.dev)]")
        embed.add_field(name=";)", value=f"node: {platform.node()}")

        await ctx.respond(embed=embed)
        return
    
def setup(bot):
    bot.add_cog(beta(bot))