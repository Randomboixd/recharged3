import discord
from discord.ext import commands
import requests
from io import BytesIO
import random

class memepackone(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="procreate", description="the sex update is real")
    async def procreate_sex(self, ctx, that_special_someone: discord.Option(discord.Member, description="The person you wanna mate with")):

        invokername = str(ctx.author)

        invokername_size = len( invokername )

        someonename = str(that_special_someone)

        someonenam_size = len( someonename )

        total_namesize = len( invokername + someonename )

        total_name = invokername + someonename

        cursedname = invokername[:- round(invokername_size / 2)] + someonename[:- round(someonenam_size / 2)]

        embed = discord.Embed(title="Congratulations on having a baby!", description=f"Well <@{ctx.author.id}> and <@{that_special_someone.id}>!\n**I got some exciting news!**\n*{cursedname}* was born!", color=0xff69b4)

        await ctx.respond(embed=embed)
    
    @commands.slash_command(name="nobitches", description="Generate a no X meme.")
    async def nobitches(self, ctx, what: discord.Option(str, description="ex: no bitches?")):
        try:
            request = requests.get("https://some-random-api.com/canvas/misc/nobitches", params={"no": what})
        except:
            embed = discord.Embed(name="This is awkward.", description="Cannot connect to some-random-api!\n*maybe try turning it off and on again?*")
            await ctx.respond(embed=embed)
            return

        if request.status_code != 200:
            embed = discord.Embed(title="This is awkward.", description=f"Request error @ some-random-api!\n*if you're nerdy enough, here is the status code: {request.status_code}*")
            await ctx.respond(embed=embed)
            return


        image_bytes_request = request.content

        image_bytes = BytesIO(image_bytes_request)

        attachment = discord.File(image_bytes, "image.png")

        embed = discord.Embed(title="Here ya go!", color=0x5865F2)
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text="service provided by some-random-api.com")

        await ctx.respond(embed=embed, file=attachment)
        return

    @commands.slash_command(name="fakeyt", description="generates a fake Youtube comment.")
    async def noway(self, ctx, message: discord.Option(str, description="The comment text. Max 1000 Characters"), person: discord.Option(discord.Member, description="Person you want to comment as. Defaults to you if not provided", default=None)):

        if person == None:
            person = ctx.author 
        
        try:
            request = requests.get("https://some-random-api.com/canvas/misc/youtube-comment", params={"username": str(person), "comment": message, "avatar": person.avatar.url})
        except Exception as e:
            print(e)
            embed = discord.Embed(title="This is awkward.", description="Cannot connect to some-random-api!")
            await ctx.respond(embed=embed)
            return
        
        if request.status_code != 200:
            embed = discord.Embed(title="this is awkward", description=f"Status: {request.status_code}")
            await ctx.respond(embed=embed)
            return
        
        image_bytes_request = request.content

        image_bytes = BytesIO(image_bytes_request)

        attachment = discord.File(image_bytes, "image.png")

        embed = discord.Embed(title="W H A T", color=0x5865F2)
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text="service provided by some-random-api.com")

        await ctx.respond(embed=embed, file=attachment)
        return
    
    @commands.slash_command(name="faketweet", description="drama")
    async def faketweet(self, ctx, message: discord.Option(str, description="Text of the tweet. Max 1000 chars"), person: discord.Option(discord.Member, description="Tweet as someone else! whats the worst that can happen? (If not provided, defaults to yourself.)", default=None), replies: discord.Option(int, description="how much replies should the tweet have? (Defaults to 420)", default=420), retweets: discord.Option(int, description="how much rt-s should it have? (Defaults to 69)", default=69)):
        
        if person == None:
            person = ctx.author

        try:
            request = requests.get("https://some-random-api.com/canvas/misc/tweet", params={"username": str(person), "displayname": person.display_name, "comment": message, "avatar": person.avatar.url, "replies": replies, "retweets": retweets, "theme": random.choice(["light", "dim", "dark"])})
        except Exception as e:
            print(e)
            embed = discord.Embed(title="This is awkward.", description="Cannot connect to some-random-api!")
            await ctx.respond(embed=embed)
            return
        
        if request.status_code != 200:
            embed = discord.Embed(title="this is awkward", description=f"Status: {request.status_code}")
            await ctx.respond(embed=embed)
            return

        image_bytes_request = request.content

        image_bytes = BytesIO(image_bytes_request)

        attachment = discord.File(image_bytes, "image.png")

        embed = discord.Embed(color=0x5865F2)
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text="service provided by some-random-api.com")

        await ctx.respond(embed=embed, file=attachment)
        return
        

def setup(bot):
    bot.add_cog(memepackone(bot))
