# Welcome to coconutbot v3: RECHARGED! I tried everything!

Hello! So here i am... again. this time with Coconutbot RECHARGED.

Recharged was my effort to try and well "Recharge" coconutbot. It added brand new commands, like /stare, added SQLITE3 Support where it could, and added achievements as a native feature.

However due to it not being used i decided to kill it off... for good.

This guide will help you set up recharged. sooo get ready!

Oh yeah and make sure for exception logging to work to either:

- Have a Gitea server with a user account you're willing to use as a bot to report issues

- Have a discord server with a webhook.

Issues are disabled on this repository, so these mainly serve as a tool for you. Like if you're developing a brand new component, then any errors that are unhandled will be reported to a repository as an issue or on discord through a webhook!

# Recharged is the DEFINITIVE Edition

I tried to minimize setup... Unlike with OS_RELEASE, struggling with recharged will be unlikely. All you need is a .env, a deploy.json, a virtualenv, and copying the recharged database (which is called electricity.db)!

So if you wanna host or hack coconutbot to your needs, this is the edition you'll likely wanna go with!

# Things to understand

## Components

For easily adding stuff to coconutbot, you can use discord.py cogs!


Components are located in `./cogs`, and end with `#component.py`!

## Electricity.db tables

All electricity.db tables are documented in `./THECOCONUTBOTPROJECTDUMP/database-layout/`!

## Achievement registry (And `achievementmgmt.py`)

Achievement registry contains the well... registration for achievements! You can add new entries, and assign them with `achievementmgmt.Achievement_Management.award()`!

# SETUP

## 1, Database (electricity.db)

First of all, Go into `./THECOCONUTBOTPROJECTDUMP/database-layout/` and move the electricity.db file into this folder.

boom. database is solved!

## 2, Dependencies

First of all, create a virtual environment. I won't go into detail on how to do this as... im pretty sure you did it atleast *once*. if not, well... look it up. its easy!

Then install every single dependency using `pip install -r requirements.txt` and boom your done :3

## 3, Deploying using deploy.json and .env

go ahead and copy `deploy-template.json` into `deploy.json`!

Now go ahead and fill out some baseline data. Here is some you might be stuck on:

- `owner-id`: Your discord ID.
- `review-channel-id`: Should be set to a private channel where the bot can send stuff, and admins can access. Required for polls to work.
- `poll-channel-id`: Should be set to a public channel where users can't type but the bot can send messages.
- `admins`: Append every trusted user's discord id here to allow certain functions (you should add yourself in here aswell, used for approving and declining poll reviews).

- `troubleshoot-payload`: Leave blank if you don't want the bot to report exceptions on discord or a gitea server. otherwise copy codeblocks from `troubleshoot-payload-examples` into here. Note in the servicetoken field, you can use `fromenvironment;(environment variable name)` to load from an environment variable (Recommended).

Finally, create a `.env` file and add `TOKEN=(your discord bot token)` into here alongside other environment variables (like servicetokens).

## (optional), Stop the /stare command from erroring!

Solution is simple... add any resolution image into this folder (Coconutbot resizes it according to the source image), and name it `stare.jpg`. Usually i used a flashbacks meme but you can use anything.

