import discord
from discord.ext import commands
from transactionlib import user_retrieval_transaction


class Marketplace(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="balance", description="Check how much charges you have!")
    async def bal(self, ctx, ephemeralresponse: discord.Option(bool, default=False, description="Should i only show it to you?")):

        user = user_retrieval_transaction(ctx.author.id)
        userprofilepic = ctx.author.avatar.url

        transactionlength = len(user["transactions"]) - 1


        embed = discord.Embed(title=f"{ctx.author.name}'s balance", description=f"**{user['coins']} charges**\n*Latest transaction*: {user['transactions'][transactionlength]['item']}", color=0xEB459E)
        embed.set_thumbnail(url=userprofilepic)

        await ctx.respond(embed=embed, ephemeral=ephemeralresponse)




def setup(bot):
    bot.add_cog(Marketplace(bot))
