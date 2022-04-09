# importing everything
from utils import get_random_movie, get_random_show, get_random_anime
from utils import get_meme, get_joke, get_animals, get_sticker, get_gif, get_quote
from utils import first_msg, cmds, get_movie_by_genre
from discord.utils import find
from decouple import config
import discord
import random

# initializing the client
client = discord.Client()


@client.event
# when a server is joined
async def on_guild_join(guild):
    general = find(lambda x: x.name == "general", guild.text_channels)
    if general and general.permissions_for(guild.me):
        await general.send(first_msg)


@client.event
# when ready
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
# when a message is recieved
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content.startswith("$movie"):
        # random but nice movie recommendation
        if len(msg.content) == 6:
            message = get_random_movie()
            await msg.channel.send(message)

    if msg.content.startswith("$genre"):
        # movie recommendation by genre
        try:
            query = msg.content.split("$genre ")[1]
            message = get_movie_by_genre(str(query))
            await msg.channel.send(message)
        except discord.errors.HTTPException:
            
            await msg.channel.send("No such genre.Try again please.")

    if msg.content.startswith("$tvshow"):
        # random but nice tv show recommendation
        message = get_random_show()
        await msg.channel.send(message)

    if msg.content.startswith("$anime"):
        # random but nice anime recommendation
        message = get_random_anime()
        await msg.channel.send(message)

    if msg.content.startswith("$hello"):
        # greet users
        await msg.channel.send(f"Hello {msg.author}")

    if msg.content.startswith("$gif"):
        # get a gif based on the query passed
        query = msg.content.split("$gif ")[1]
        gif_url = get_gif(query)
        await msg.channel.send(gif_url)

    if msg.content.startswith("$sticker"):
        # get a sticker based on the query passed
        query = msg.content.split("$sticker ")[1]
        sticker_url = get_sticker(query)
        await msg.channel.send(sticker_url)

    if msg.content.startswith("$meme"):
        # summons a random meme
        meme = get_meme()
        await msg.channel.send(meme)

    if msg.content.startswith("$choose"):
        # chooses a random value among the given values
        queries = [msg.content.split(" ")[1], msg.content.split(" ")[2]]
        await msg.channel.send("I choose " + random.choice(queries))

    if msg.content.startswith("$toss"):
        # makes a toss
        await msg.channel.send(random.choice(["heads", "tails"]))
    if msg.content.startswith("$joke"):
        # makes an amazing dad joke
        try:
            joke = get_joke()
            await msg.channel.send(joke)
        except discord.errors.HTTPException:
            joke = get_joke()
            await msg.channel.send(joke)
    if msg.content.startswith("$animals"):
        # gets a picture of a random animal (There is a 10 sec latency)
        animal = get_animals()
        await msg.channel.send(animal)
    if msg.content.startswith("$quote"):
        # gets a nice quote picture
        quote = get_quote()
        await msg.channel.send(quote)
    if msg.content.startswith("$cmds"):
        # gets the list of available commands
        await msg.channel.send(cmds)


# running the bot
client.run(config("DISCORD_BOT_KEY"))
