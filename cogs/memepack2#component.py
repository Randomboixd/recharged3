import discord
from discord.ext import commands
import requests
from io import BytesIO
from PIL import Image


is_image_operation_run = False

class memepacktwo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="stare", description="do not")
    async def thousandquotastare(self, ctx, img: discord.Option(discord.Attachment, description="moments before disaster"), transparency: discord.Option(float, choices=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8], description="how visible he is", default=0.4)):
        global is_image_operation_run

        if is_image_operation_run:
            embed = discord.Embed(title="This command is ratelimited.", description="Image editing is a resource intensive task, to spare my poor hardware from commiting explod only ONE editing can be done at a time.\n \n**Thanks for understanding!**")
            await ctx.respond(embed=embed, ephemeral=True)
            return
        
        if "https://cdn.discordapp.com" not in img.url:
            embed = discord.Embed(title="Request blocked", description=f"Request to download image from <{img.url}> blocked.")
            await ctx.respond(embed=embed, ephemeral=True)
            return # Just in case... i know it will always be cdn.discordapp.com
        
        if "image/" not in img.content_type:
            embed = discord.Embed(title="This is not an image.", description="Sorry :(")
            await ctx.respond(embed=embed, ephemeral=True)
            return

        if img.size > 3145728:
            embed = discord.Embed(title="Image rejected. Size limit reached", description="To not blow up my hardware while processing an image, **max 3MB**. no more")
            await ctx.respond(embed=embed, ephemeral=True)
            return
        
        if img.width > 1920 or img.height > 1080:
            embed = discord.Embed(title="Image rejected. Resolution is too large", description="**max 1920x1080**")
            await ctx.respond(embed=embed, ephemeral=True)
            return

        await ctx.response.defer()

        try:
            retrieved_image_request = requests.get(img.url)
        except:
            embed = discord.Embed(title="Failed to download image!")
            await ctx.respond(embed=embed, ephemeral=True)
            return
        
        
        is_image_operation_run = True
    
        imageio = BytesIO(retrieved_image_request.content)
        image = Image.open(imageio)

        image_width, image_height = image.size

        stare = Image.open("stare.jpg")

        stare = stare.resize((image_width, image_height))

        stare = stare.convert("RGBA")

        stare_with_transparency = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))
        stare_with_transparency.paste(stare, (0, 0), stare)
        for x in range(stare_with_transparency.width):
            for y in range(stare_with_transparency.height):
                r, g, b, a = stare_with_transparency.getpixel((x, y))
                stare_with_transparency.putpixel((x, y), (r, g, b, int(a * transparency)))

        transparent_overlay = Image.new("RGBA", (image_width, image_height), (0, 0, 0, int(255 * transparency)))

        x = (image_width - stare.width) // 2
        y = (image_height - stare.height) // 2

        transparent_overlay.paste(stare_with_transparency, (x, y), stare_with_transparency)

        final = Image.alpha_composite(image.convert("RGBA"), transparent_overlay)

        finalio = BytesIO()
        final.save(finalio, format='PNG')
        finalio.seek(0)

        attachment = discord.File(finalio, "image.png")

        embed = discord.Embed(description="run")
        embed.set_footer(text="Hi there! This image operation is performed on LOCAL machine! This is a resource intensive task so its ratelimited. Thanks for understanding!")
        embed.set_image(url="attachment://image.png")

        await ctx.respond(embed=embed, file=attachment)
        is_image_operation_run = False
        return



    
def setup(bot):
    bot.add_cog(memepacktwo(bot))
