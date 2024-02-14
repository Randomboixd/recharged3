import discord
from discord.ext import tasks
import os
import random
import json
import asyncio
import requests
import hashlib
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import sqlite3
from icecream import ic
from achievementmgmt import Achievement_Management, Achievement_Registry, AssignmentErrors

load_dotenv()

global deployment
with open("deploy.json", "r") as depl:
  deployment = json.load(depl)

isProd = deployment["prod"]

version = deployment["version"]


def hashmii(data:str):
  return hashlib.sha512(data).hexdigest().decode()

ReviewChanneld = deployment["review-channel-id"]
PollChanneld = deployment["poll-channel-id"]


def getdeckey(type:str="gln"):
  return False


def enc(text:str, type:str="gln"): # Just an encryption function
    return text

def dec(enctext:str, type:str="gln"): # same for decryption.
    return enctext

# btw those WERE encryption functions. i just removed their contents as im going to rework em'

# When companies say they use 'Military Grade Encryption' be like

Administrators = deployment["admins"]

Owner_name = deployment["instance-owner"]

activity= discord.Activity(name=f"{str(version)}", type=discord.ActivityType.watching)

bot = discord.Bot(intents=discord.Intents.all() ,activity=activity)

fun = discord.SlashCommandGroup("fun", "99% of the commands here are 4 fun")

bulletinboard = discord.SlashCommandGroup("bulletinboard", "Revival of my old 'message board system'")

howto = discord.SlashCommandGroup("guide", "Your One step guide to everything coconutbot")

connectpass = discord.SlashCommandGroup("fancyannouncements", "Ngl They be fancy doe")

gln = discord.SlashCommandGroup("gamelabnetwork", "Integration With GLN")

settings = discord.SlashCommandGroup("settings", "Control CoconutBot to your liking!")

hints = discord.SlashCommandGroup("hints", "Get Hints on Secret Roles.")

insiders = discord.SlashCommandGroup("insider", "Under Developement Content!")

password = discord.SlashCommandGroup("keys", "Redeem your CoconutKeys!")


eco = discord.SlashCommandGroup("economy", "?")

vote_system = discord.SlashCommandGroup("polls", "Make your own polls!")


review = vote_system.create_subgroup(name="review", description="These are for admins only!")

cards = discord.SlashCommandGroup("cards", "Check out your cards, configure em'.")

glnidsettings = discord.SlashCommandGroup("gln_id_settings", "Configure Your Gamelab Network identificant!")

administrative = discord.SlashCommandGroup("administrative", "Warning! Make sure this is on ADMINS Only!")


GLNADDRESS = "https://< Your GLN Address here >" # Set this if you want GLN Support, follow guide to set up gln

GLNREGISTERADR = GLNADDRESS + "/gameservice/Webservice/Accountserver/RegisterServiceID/Account"
GLNGAMERIDREG = GLNADDRESS + "/gameservice/Webservice/Accountserver/RegisterServiceID/GamerID"

GLNDATAREQUESTURL = GLNADDRESS + "/gameservice/Webservice/Accountserver/GetTag"



class rickroll(discord.ui.View): 
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.blurple, emoji="😀") 
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # 😏

def legacyMessage(string: str):
  """Converts a normal string into an embed. Use for easy porting on legacy commands"""
  embed = discord.Embed(title="-- Coconutbot 3.0 --", description=string)
  embed.set_footer(text="Hi! Im legacyMessage()! Tell bX to remaster this command!")
  return embed



@fun.command(name='billnye', description="he the scienc guy (my fav command)")
async def billnye(ctx):
  ra = random.randint(0, 99999)
  if ra != 69420:
    await ctx.respond('https://www.youtube.com/watch?v=1mHDuMJHyJo') # pls don't sue me disney. i'll remove this if needed.
  else:
    embed=discord.Embed(title="You Unlocked a (not so) Secret Advancement!", description="Wait so Coconutbot has these? (NO)", color=0x06776b)
    embed.add_field(name="Im Pretty sure thats not bill nye.", value="Get the Magic number! (69420)", inline=False)
    embed.add_field(name="Reward", value="Your Time wasted.", inline=False)
    embed.add_field(name="There is no context. Your Ears are now blessed.",value=".", inline=False)
    embed.set_footer(text="You are a lucky man walking!")
    await ctx.send(embed=embed)
    await ctx.respond('https://www.youtube.com/watch?v=rEcOzjg7vBU')
    

@fun.command(name="geometrydash2", description="get info about 2.0")
async def gd2(ctx):
  await ctx.respond('.', ephemeral=True)
  await ctx.send("https://www.wikihow.com/Make-Sex-Better") # uhm.
  await asyncio.sleep(6)
  await ctx.channel.purge(limit=1)
  await ctx.send(embed=legacyMessage('THERE WAS A MISINPUT'))
  await asyncio.sleep(0.4)
  await ctx.send(embed=legacyMessage('MISINPUT'))
  await asyncio.sleep(0.4)
  await ctx.send(embed=legacyMessage('CALM DOWN!'))
  await asyncio.sleep(0.4)
  await ctx.send(embed=legacyMessage('YOU CALM THE FK DOWN!'))
  await asyncio.sleep(3)
  await ctx.send(embed=legacyMessage('IT WAS A MISINPUT'))

@fun.command(name="drink", description="its very evil")
async def drink(ctx):
  await ctx.respond('https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831')

  try:
    mgmt = Achievement_Management(ctx.author.id)

    achievementid = "03"

    achievement_details = Achievement_Registry().getentry(achievementid)

    mgmt.award(achievementid, True)

    embed = discord.Embed(title=f"Achievement UNLOCKED: {achievement_details.name}", description=f"*{achievement_details.explainer}*\n \n**+{achievement_details.charges} Charges!**")
    await ctx.send(embed=embed)
  except AssignmentErrors.AlreadyAssigned:
    pass

@fun.command(name="has_bitches", description="Have bitches or dont. Its a life changeing question") # its Changing dumbass
async def bitches(ctx):
  a = random.randint(0,2)
  if a == 1:
    await ctx.respond(embed=legacyMessage(f"{str(ctx.author)} Has bitches."))
  else:
    await ctx.respond(embed=legacyMessage(f"{str(ctx.author)} Doesn't Have bitches."))

    try:
      mgmt = Achievement_Management(ctx.author.id)

      achievementid = "06"

      achievement_details = Achievement_Registry().getentry(achievementid)

      mgmt.award(achievementid, True)

      embed = discord.Embed(title=f"Achievement UNLOCKED: {achievement_details.name}", description=f"*{achievement_details.explainer}*\n \n**+{achievement_details.charges} Charges!**")
      await ctx.send(embed=embed)
    except AssignmentErrors.AlreadyAssigned:
      pass
    

@fun.command(name="giveneitro", description="give someone neitro")
async def neitro(ctx, membr:discord.Member):
  if os.path.exists(f'./ignore/{str(membr.id)}.acc') != True:
    await ctx.respond(embed=legacyMessage(f'successfully sent sht to {str(membr.mention)}'))
    try:
      await membr.send("Modmail: You successfully received neitro in our giveaway. (fake)")
      await membr.send("https://discord.gift/Udzwm3hrQECQBnEEFFCEwdSq")
    except:
      await ctx.respond(embed=legacyMessage(f'I cant send shit to {str(membr.mention)}"s discord dms. he locked his dms. :nerd: "'))
  else:
    await ctx.respond('Doughnut distrub mode is turned on for that user.')

@fun.command(name="suprise", description="nitro alert")
async def gibrealneitro(ctx):
  await ctx.respond(embed=legacyMessage('Click the button below!') ,view=rickroll())

@fun.command(name="sendnuke", description="Send a nuke to someone's door! (for legal reasons. this is a joke)")
async def sendnuke(ctx, luckyperson: discord.Member):
  if os.path.exists(f'./ignore/{str(luckyperson.id)}.acc') != True:
    try:
      await ctx.respond('they got a neic mail!')
      await luckyperson.send(embed=legacyMessage('You got mail!'))
      await asyncio.sleep(4)
      await luckyperson.send(embed=legacyMessage('What is it?'))
      await asyncio.sleep(2)
      await luckyperson.send(embed=legacyMessage('TACTICAL NUKE INCOMING!'))
      await asyncio.sleep(2)
      await luckyperson.send('https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831')
    except:
      await ctx.send(embed=legacyMessage(':nerd: THEY DISABLED DMS! :rofl: :rofl:'))
  else:
    await ctx.respond('Do not Distrub is turned on for that person...')


@fun.command(name="sendkfc", description="Send KFC to someone's Door! They WILL like it!")
async def kfc(ctx, person: discord.Member):
  if os.path.exists(f'./ignore/{str(person.id)}.acc') != True:
    try:
      
      await person.send(embed=legacyMessage(f'Hey you! Yes YOU! {str(ctx.author)} Sent you some KFC!'))
      await ctx.respond(embed=legacyMessage('They got some KFC!'))
      await person.send('https://tenor.com/view/fried-chicken-crispy-gif-26189851')
      try:
        if os.path.exists(f'./adv_how_dd_we_g/{str(ctx.author.id)}.prog1') == True:
          if os.path.exists(f'./adv_how_dd_we_g/{str(ctx.author.id)}.prog2') != True:
            open(f'./adv_how_dd_we_g/{str(ctx.author.id)}.prog2', 'x').close()
      except:
        pass
    except:
      await ctx.respond('They calmly refused. (Message was blocked by discord!) Possible Reasons: user has DMS turned off')
  else:
    await ctx.respond("I Was told Not to send fun stuff into this man's inbox. (Message blocked by CoconutBOT)")

@howto.command(name="cards", description="Learn about recharged's collectables.")
async def cardhelp(ctx):
    embed = discord.Embed(title="Cards and Reverse cards (But mostly just cards)", description="Cards are a brand new feature of Coconutbot Recharged 3.0!\nIt's a collectable! And one of a kind at that.", color=0x06776b)
    embed.add_field(name="Cards are dropped randomly", value="When you talk in chat, there is a chance for a pack of cards to drop!\nSimply click 'Collect' before anyone else, and its all yours baby!\nBuut you see.", inline=False)
    embed.add_field(name="Every. Single. Card. Is. UNIQUE!", value="Two cards can be named equal, but they are never the same...", inline=False)
    embed.add_field(name="So. okay. Cards. They are unique. Are they NFTs basically?", value="Kinda. but you're not wasting any money.", inline=False)
    embed.add_field(name="But if cards randomly appear, and each is different... How are they valuable?", value="There are limited event cards, and also every card has its own stats.\nBad cards also don't need to be thrown away, they can be squeezed into our currency, 'Charges' (albeit, you won't profit too much from squeezing), which can later be used to buy Better cards.", inline=False)
    await ctx.respond(embed=embed)

@howto.command(name="charges", description="It's Recharged's main currency!")
async def chargeshelp(ctx):
    embed = discord.Embed(title="Introducing Charges!", description="Charges are also new in Coconutbot Recharged 3.0!\nCharges power the marketplace, where you can sell or squeeze cards!", color=0x06776b)
    embed.add_field(name="Earning Charges", value="You can earn charges by either: Squeezing cards, or simply selling them! Perhaps trading em'!", inline=False)
    await ctx.respond(embed=embed)

@howto.command(name="fun_stuff", description="how do i fun stuff?")
async def ffguide(ctx):
  await ctx.respond('I have messaged you!')
  embed=discord.Embed(title="How to fun", description="So you wanna have some fun? Coconutbot has that!", color=0x06776b)
  embed.add_field(name="Cool! What can i do?", value="... spam your ''Friends'' with useless dms! and some cool stuff.", inline=False)
  embed.add_field(name="You got me. So what now?", value="Just start typing /fun and you'll See all avalable commands!", inline=False)
  embed.add_field(name="Bot said he doesnt send messages to that person!", value="It depends. if the bot says it CANNOT because discord. then the user has DMS off. If it says it can't because of Do Not Disturb then they enabled DO NUT distrub on their bot profile.", inline=False)
  embed.add_field(name="I want that too! How do i?", value="Simply use /settings toggledms. If its off. it will turn it on. if its on. it will turn it off. (This prevents me from sending messages other than guides and bulletinposts to you!)", inline=False)
  embed.set_footer(text=f"Guide is written by {Owner_name}!")
  try:
    await ctx.author.send(embed=embed)
  except:
    await ctx.send('It seems i cant message you... You may have to turn Direct Messages from Server Members on.')

@howto.command(name="cranberries", description="Cranberries are tasty. but what if we can taste them on discord?")
async def ccguide(ctx):
  await ctx.respond('I have messaged you!')
  embed=discord.Embed(title="Cranberries are tasty. and so are memes", description="Wanna cranberry was first made as a joke from King Squirrel on the server. Now it became our main meme distribution system... Lets Talk Cranberries.", color=0x06776b)
  embed.add_field(name="GIVE ME THE MEMES!", value="Great! Nice to see your appreciation for memes! Lets get right into it. You Can get a ''Cranberry'' By running /fun sprite_cranberry. Now Go and Enjoy Your Memes. Or Cranberries. Whatever.", inline=False)
  embed.add_field(name="Sharing is caring", value="So you wanna share your memes. (or cranberries) You can use the /fun submit_cranberry command alongside the url for your image, After a quick check it will register it to the berry system. What you don't have a link for your cranberry?", inline=False)
  embed.add_field(name="I Need some cranberrys right now.", value="you can find me at X City X Street XX in room 1 on pictochat! (please give me cranberries)", inline=False)
  embed.add_field(name="About our yummy api", value="You'll Be able to order Cranberrys free of charge for your app once i launch the api docs and well. the api. man if it would be this easy to get cranberries.", inline=False)
  embed.add_field(name="GIVE ME CRANBERRIES", value="I like how this got from just Sprite Cranberry to me literally being hungry lol (edit: i received cranberries)")
  embed.set_footer(text=f"Guide is written by {Owner_name}!")
  try:
    await ctx.author.send(embed=embed)
  except:
    await ctx.send('It seems i cant message you... You may have to turn Direct Messages from Server Members on.')

@howto.command(name="advancements", description="Wait those exist?")
async def advguide(ctx):
  await ctx.respond('I have messaged you!')
  embed = discord.Embed(title="Super Secret Tiny Developer Extra Virus Funky Kong Included Advancements", description="Wait those exist?", color=0x06776b)
  embed.add_field(name="Why does VS-Code bug when i try to just write embeds?", value="No idea.", inline=False)
  embed.add_field(name="How do i obtain them?", value="Well if you didnt read the title... you can't but also you can. Its up to you to find 'em All! Its like pokemon. Gotta Catch 'em all! (firered version)", inline=False)
  embed.add_field(name="What do i do with them?", value="nothing.", inline=False)
  embed.set_footer(text=f"Guide is written by {Owner_name}!")
  try:
    await ctx.author.send(embed=embed)
  except:
    await ctx.send('It seems i cant message you... You may have to turn Direct Messages from Server Members on.')

@settings.command(name="toggledms", description="I will happily refuse messages sent to you via coconutbot! (required stuff are not modified)")
async def disabledms(ctx):
  if os.path.exists(f'./ignore/{str(ctx.author.id)}.acc') == True:
    os.remove(f'./ignore/{str(ctx.author.id)}.acc')
    await ctx.respond('You have been deleted from the Do not disturb list!')
    await ctx.author.send('You removed yourself from the Do not disturb list! You will now receive other stuff')
  else:
    a = open(f'./ignore/{str(ctx.author.id)}.acc', 'x')
    a.close()
    await ctx.respond('You have been added to the chill zone! Wanna get out? run the command again!')
    await ctx.author.send('Do not distrub was turned on. However Important System messages like this will still be sent!')

@settings.command(name="remove_special_roles", description="Coconutbot can give you some secret roles. This tool can remove them!")
async def remove_special_roles(ctx):
  await ctx.respond('The proccess has been started! I will DM You when it finishes!')
  role = discord.utils.get(ctx.guild.roles, name="The Drink is Dangerous")
  user = ctx.author
  if role in user.roles:
    await user.remove_roles(role)

  role = discord.utils.get(ctx.guild.roles, name="How Did we get here?")
  user = ctx.author
  if role in user.roles:
    await user.remove_roles(role)
  await asyncio.sleep(20)
  try:

    await ctx.author.send(embed=legacyMessage('Notice: Your Request to remove your special roles have been completed! Thanks for Using CoconutBot - The Coconutbot Team'))
  except:
    await ctx.send('I Cant send messages to you! But your Request Have been completed!')

    

@hints.command(name="the_drink_is_dangerous", description="Stuck? I'll Help! Just Run and I'll Give you a tip!")
async def hintdrink(ctx):
  hints = ["There is a command in the fun category...", "You Can't Live without it!", "Its Connected with Red Dead Redemption 2!", "There is a squirrel on that tree!"]
  await ctx.respond('https://www.youtube.com/watch?v=hDpsnFnovUQ')
  await ctx.send(embed=legacyMessage('Your Hint will be sent in 10 seconds!'))
  await asyncio.sleep(10)
  await ctx.send(hints[random.randint(0, 3)])


@fun.command(name="news", description="Latest News: Everything is AWFUL")
async def news_insider(ctx):
  with open(f'news.json') as f:
    ff = json.load(f)

  owner = f"<@{deployment['owner-id']}>"

  embed = discord.Embed(title=f'News', description="What Happened on Coconutbot recently", color=0xd15705)
  embed.add_field(name="News", value=f'{str(ff["news"])}'.format(serverhost=owner))
  embed.set_footer(text="This is a user triggered event!")
  await ctx.respond(embed=embed)

  ## Remove the lines below to remove giving the "welcome to 3.0" achievement
  try:
    mgmt = Achievement_Management(ctx.author.id)

    achievementid = "02"

    achievement_details = Achievement_Registry().getentry(achievementid)

    mgmt.award(achievementid, True)

    embed = discord.Embed(title=f"Achievement UNLOCKED: {achievement_details.name}", description=f"*{achievement_details.explainer}*\n \n**+{achievement_details.charges} Charges!**")
    await ctx.send(embed=embed)
  except AssignmentErrors.AlreadyAssigned:
    pass


@vote_system.command(name="make", description="Make your own poll! (Will be reviewed by mod team)")
async def votemk(
  ctx,
  polltitle: discord.Option(str, description="This is the actual question! Make sure its pretty!"),
  poll_choice1 : discord.Option(str, description="The first choice. Something like 'I agree!' will do it"),
  poll_choice2 : discord.Option(str, description="The second choice. Something like 'I disagree' will do it"),
  poll_none : discord.Option(bool, description="If set to True the 'None' Option will appear. (Defaults to True)", default=True),
  poll_emoji1 : discord.Option(str, description="A Discord emoji for the first choice! (Defaults to Thumbsup)", default="👍"),
  poll_emoji2 : discord.Option(str, description="A Discord emoji for the second choice! (Defaults to thumbsdown)", default="👎")

):
  await ctx.defer()
  await ctx.respond(embed=discord.Embed(title="Starting... Please wait"), ephemeral=True)
  lool = await ctx.send(embed=legacyMessage('Waiting...'))
  try:
    await lool.add_reaction(poll_emoji1)
  except:
    await ctx.send("poll_emoji1 is not a valid discord emoticon!\nEither you are using a custom emoji i dont have access to\nOr you entered standard text!")
    return
  try:
    await lool.add_reaction(poll_emoji2)
  except:
    await ctx.send("poll_eEmoji2 is not a valid discord emoticon!\nEither you are using a custom emoji i dont have access to\nOr you entered standard text!")
    return
  Poll_ID = random.randint(0, 999999999999999)
  bolstring = str(poll_none)
  Poll_Structure= {
    "title": polltitle,
    "choice1": poll_choice1,
    "choice2": poll_choice2,
    "emoji1": poll_emoji1,
    "emoji2": poll_emoji2,
    "none": bolstring,
    "author": str(ctx.author),
    "author_id": str(ctx.author.id)
  }

  poll_structure_dump = json.dumps(Poll_Structure).encode()
  
  connection = sqlite3.connect("electricity.db")

  cursor = connection.cursor()

  cursor.execute("INSERT INTO polls VALUES(?,?)", (Poll_ID, poll_structure_dump,))

  connection.commit()
  connection.close()

  try:
    mgmt = Achievement_Management(ctx.author.id)

    achievementid = "04"

    achievement_details = Achievement_Registry().getentry(achievementid)

    mgmt.award(achievementid, True)

    embed = discord.Embed(title=f"Achievement UNLOCKED: {achievement_details.name}", description=f"*{achievement_details.explainer}*\n \n**+{achievement_details.charges} Charges!**")
    await ctx.send(embed=embed)
  except AssignmentErrors.AlreadyAssigned:
    pass
  
  
  Creator = str(ctx.author)
  Question = polltitle
  
  embed=discord.Embed(title="A Wild poll has appeared!", color=0x520303)
  embed.set_author(name="Coconutbot Polls")
  embed.add_field(name=f"Creator: {Creator}!", value=f"{Question}", inline=True)
  if poll_none == False:
    embed.add_field(name="Options:", value=f"|{poll_emoji1}| - {poll_choice1}, |{poll_emoji2}| - {poll_choice2}", inline=False)
  else:
    embed.add_field(name="Options:", value=f"|{poll_emoji1}| - {poll_choice1}, |{poll_emoji2}| - {poll_choice2}, |🚫| - None", inline=False)
  embed.set_footer(text="These polls are reviewed by a moderation team before they are out.")

    
  ReviewChannel = bot.get_channel(ReviewChanneld)
  await ReviewChannel.send(f'Submission ID: {str(Poll_ID)}')
  await ReviewChannel.send(embed=embed)



@review.command(name="approve", description="Approve a poll! you'll need a submission id!")
async def voteaprove(
  ctx,
  submission_id : discord.Option(str, description="You know where to find these!")
):
  submission_id = int(submission_id)
  if ctx.author.id in Administrators:
    await ctx.respond('Submission Approved!')
    
    connection = sqlite3.connect("electricity.db")
    cursor = connection.cursor()

    f = cursor.execute("SELECT data FROM polls WHERE id = ?", (int(submission_id),)).fetchone()

    

    if f == None:
      embed = discord.Embed(title="Submission not found.")
      await ctx.send(embed=embed)
      connection.close()
      return
    
    f = json.loads(f[0].decode())

    author_id = int(dec(f["author_id"]))
    op = bot.get_user(author_id)
    try:
      await op.send('Hey! Your Poll Submission has been Approved!')
    except:
      pass
    pollchnl = bot.get_channel(PollChanneld)
    Creator = str(dec(f["author"]))
    Question = str(dec(f["title"]))
    poll_none = str(f["none"])
    poll_emoji1 = f["emoji1"]
    poll_emoji2 = f["emoji2"]
    poll_choice1 = str(dec(f["choice1"]))
    poll_choice2 = str(dec(f["choice2"]))
    
    cursor.execute("DELETE FROM polls WHERE id = ?", (int(submission_id),))

    connection.commit()
    connection.close()

    embed=discord.Embed(title="A Wild poll has appeared!", color=0x520303)
    embed.set_author(name="Coconutbot Polls")
    embed.add_field(name=f"Creator: {Creator}!", value=f"{Question}", inline=True)

    if poll_none == "False":
      embed.add_field(name="Options:", value=f"|{poll_emoji1}| - {poll_choice1}, |{poll_emoji2}| - {poll_choice2}", inline=False)
    else:
      embed.add_field(name="Options:", value=f"|{poll_emoji1}| - {poll_choice1}, |{poll_emoji2}| - {poll_choice2}, |🚫| - None", inline=False)

    embed.set_footer(text="These polls are reviewed by a moderation team before they are out.")
    ohnoes = await pollchnl.send(embed=embed)
    await ohnoes.add_reaction(poll_emoji1)
    await ohnoes.add_reaction(poll_emoji2)
    if poll_none != "False":
      await ohnoes.add_reaction("🚫")

  else:
    await ctx.respond(embed=legacyMessage("You are not an administrator!"))

@review.command(name="disapprove", description="Disapprove a poll!")
async def votedisaprove(
  ctx,
  submission_id : discord.Option(str, description="You know where to get this from")
):
  submission_id = int(submission_id)
  if ctx.author.id in Administrators:
    await ctx.respond("Submission Disapproved!")

    connection = sqlite3.connect("electricity.db")
    cursor = connection.cursor()

    f = cursor.execute("SELECT data FROM polls WHERE id = ?", (int(submission_id),)).fetchone()
    f = json.loads(f[0].decode())
    cursor.execute("DELETE FROM polls WHERE id = ?", (int(submission_id),))

    connection.commit()
    connection.close()
    
    author_id = int(dec(f["author_id"]))
    op = bot.get_user(author_id)
    await op.send("Hey! Your Poll submission didnt go through.")
  else:
    bruh = await ctx.respond(embed=legacyMessage("You are not an administrator! I mean i kind of have OCD\nYou mean O :b: CD \nhttps://ih1.redbubble.net/image.3497596780.2775/st,small,507x507-pad,600x600,f8f8f8.jpg"))
    

@bot.event
async def on_application_command_error(context, exception):
  print(exception)
  payloads = deployment["troubleshoot-payload"]
  for payload in payloads:

    if payload["type"] == "gitea":

      print("Executing payload> Gitea issue")

      token_request = payload["servicetoken"].split(";")

      if token_request[0] == "fromenvironment":
        token = os.getenv(token_request[1])
      else:
        token = token_request[0]

      print(token)

      payload_url = payload["push"]

      print(payload_url)

      errorlog = ic(exception)

      try:
        request = requests.post(payload_url, headers={"Authorization": f"token {token}"}, data={"body": f"# Exception occured!\nError dump: `{errorlog}`", "title": "Exception occured."})
        print(request.status_code)
      except Exception as e:
        print(e)
      
      print("Payload Executed> Gitea issue")
    
    elif payload["type"] == "webhook":

      print("Executing payload> Webhook")

      token_request = payload["servicetoken"].split(";")

      if token_request[0] == "fromenvironment":
        token = os.getenv(token_request[1])
      else:
        token = token_request[0]

      errorlog = ic(exception)

      try:
        request = requests.post(token, data={"content": f"# Exception occured!\nError dump: `{errorlog}`"})
      except Exception as e:
        print(e)

      print("Payload Executed> Webhook")

      
  embed = discord.Embed(title="Uh oh. here's the problem", description="Coconutbot Recharged encountered an error!\nThis incident has been reported.")
  embed.set_image(url="https://pbs.twimg.com/media/D6p6RynUcAAUiZ5.png")

  await context.respond(embed=embed)

  try:
    mgmt = Achievement_Management(context.author.id)

    achievementid = "05"

    achievement_details = Achievement_Registry().getentry(achievementid)

    mgmt.award(achievementid, True)

    embed = discord.Embed(title=f"Achievement UNLOCKED: {achievement_details.name}", description=f"*{achievement_details.explainer}*\n \n**+{achievement_details.charges} Charges!**")
    await context.send(embed=embed)
  except AssignmentErrors.AlreadyAssigned:
    pass


bot.add_application_command(fun)
bot.add_application_command(howto)
bot.add_application_command(settings)
bot.add_application_command(hints)
bot.add_application_command(vote_system)

for component in os.listdir("./cogs/"):
    if component.endswith("#component.py"):
        bot.load_extension(f"cogs.{component[:-3]}")

bot.run(os.getenv("TOKEN"))
