import discord
from discord.ext import commands
import uuid
import sqlite3
import json
import random
import secrets
from achievementmgmt import Achievement_Management, AssignmentErrors

drop_token_length = 16

names = ["Drink", "kokxolyzs", "plsdmmewithnewnamespls", "coconut", "EVIL coconut", "e", "i really dont know.", "pls give me more names", "ok?"]

global drops
drops = {}

class Card:
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio


def createCardObject() -> Card:
    bio = str(uuid.uuid4())

    name = random.choice(names)

    return Card(name, bio)


def toRegionalIndicator(num: int):
    basenum_bind = {
            "0": ":zero:",
            "1": ":one:",
            "2": ":two:",
            "3": ":three:",
            "4": ":four:",
            "5": ":five:",
            "6": ":six:",
            "7": ":seven:",
            "8": ":eight:",
            "9": ":nine:"
    }
    
    numstr = str(num)

    final = ""

    for n in numstr:
        final += basenum_bind[str(n)]

    return final

def createDrop(card_amount: int = 1) -> str:
    dropid = secrets.token_hex(drop_token_length)
    drop_attributes = {
            "drop_info": {
                "total_cards": card_amount
        }
    }
    
    drops[dropid] = drop_attributes

    return dropid


class Views:

    class cards_cardclaim_view(discord.ui.View):

        def __init__(self, dropid: str):
            super().__init__(timeout=None)
            self.drop = dropid

        @discord.ui.button(label="Claim card", style=discord.ButtonStyle.primary)
        async def claim_callback(self, button, interaction):
            if self.drop not in drops:
                embed = discord.Embed(title="Drop expired!", description="A person already claimed this drop! Try again next time!")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                return
            
            total_dropped_cards = drops[self.drop]["drop_info"]["total_cards"] # integer

            connection = sqlite3.connect("electricity.db")

            cur = connection.cursor()

            _userexist = cur.execute("SELECT cards, totalcards FROM cardcfg WHERE id = ?", (interaction.user.id,)).fetchone()

            if _userexist == None:
                example_dump = json.dumps([]).encode()
                cards = []
                cur.execute("INSERT INTO cardcfg VALUES(?,?,?)", (interaction.user.id, 0, example_dump,))
                connection.commit()
                totalcardsinventory = 0
            else:
                cards = json.loads(_userexist[0].decode())
                totalcardsinventory = _userexist[1]
            
            for x in range(total_dropped_cards):
                card = createCardObject()

                card_name = card.name
                card_bio = card.bio

                cards.append({"name": card_name, "bio": card_bio})
                totalcardsinventory += 1

            cards_final = json.dumps(cards).encode()

            cur.execute("UPDATE cardcfg SET cards = ? WHERE id = ?", (cards_final, interaction.user.id,))
            cur.execute("UPDATE cardcfg SET totalcards = ? WHERE id = ?", (totalcardsinventory, interaction.user.id,))

            connection.commit()

            connection.close()

            del drops[self.drop]

            embed = discord.Embed(title="This drop has already been claimed", description="**Gotta go fast!**", color=0x2e8b57)

            await interaction.response.edit_message(embed=embed)

class Cards(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name="cards", description="Lists the cards you have!")
    async def cardlist(self, ctx):
        userid = ctx.author.id

        connection = sqlite3.connect("electricity.db")

        cur = connection.cursor()

        _result = cur.execute("SELECT totalcards, cards FROM cardcfg WHERE id = ?", (userid,)).fetchone()

        if _result == None:
            connection.close()
            embed = discord.Embed(title="No cards!", description="You don't seem to have any cards...\nTry catching some packs in chat!", color=0xe25822)
            await ctx.respond(embed=embed, ephemeral=True)
            return

        connection.close()
        del cur
        
        totalcards = _result[0] # Integer

        user_cards = json.loads(_result[1].decode())

        # user_cards = [{"name": ":smirk:", "bio": str(uuid.uuid4())}] # An example of how user_cards look like

        rendered_text = ""
        
        cardid = -1

        for card in user_cards:
            cardid += 1
            render = f"{toRegionalIndicator(cardid)} - {card['name']}\nBIO: {card['bio']}\n \n"
            rendered_text += render


        embed = discord.Embed(title=f"Your cards ({totalcards})", description=rendered_text)
        await ctx.respond(embed=embed)


        if totalcards > 6:


            achievementobj = Achievement_Management(ctx.author.id)

            try:

                achievementobj.award("01", True)
                embed = discord.Embed(title="Achievement UNLOCKED: The whole deck", description="Have more than 7 cards in your inventory\n \n**+40 Charges**")
                await ctx.send(embed=embed)


            except AssignmentErrors.AlreadyAssigned:
                pass

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.bot:
            return
        
        shoulddrop = random.randint(0, 99)

        chance = 5

        if shoulddrop < chance:

            drop_cards = random.randint(1, 2)

            dropid = createDrop(drop_cards)


            embed = discord.Embed(title="Card delivery!", description=f"This pack contains **{drop_cards}** random cards!\nHit the button below faster than the others to claim it!", color=0x2e8b57)
            await ctx.reply(embed=embed, view=Views.cards_cardclaim_view(dropid=dropid))
            return

        


def setup(bot):
    bot.add_cog(Cards(bot))
