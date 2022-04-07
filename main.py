from utils import get_random_movie, get_random_show, get_random_anime
from utils import get_meme, get_joke, get_animals, get_sticker, get_gif, get_quote
from utils import first_msg, cmds, get_movie_by_genre
from discord.utils import find
from decouple import config
import discord
import random


client = discord.Client()


@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == "general", guild.text_channels)
    if general and general.permissions_for(guild.me):
        await general.send(first_msg)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content.startswith("$movie"):
        if len(msg.content) == 6:
            message = get_random_movie()
            await msg.channel.send(message)
        else:
            try:
                query = msg.content.split("$genre ")[1]
                message = get_movie_by_genre(str(query))
                await msg.channel.send(message)
            except discord.errors.HTTPException:
                query = msg.content.split("$genre ")[1]
                message = get_movie_by_genre(str(query))
                await msg.channel.send(message)

    if msg.content.startswith("$show"):
        message = get_random_show()
        await msg.channel.send(message)

    if msg.content.startswith("$anime"):
        message = get_random_anime()
        await msg.channel.send(message)

    if msg.content.startswith("$hello"):
        await msg.channel.send(f"Hello {msg.author}")

    if msg.content.startswith("$gif"):
        query = msg.content.split("$gif ")[1]
        gif_url = get_gif(query)
        await msg.channel.send(gif_url)

    if msg.content.startswith("$sticker"):
        query = msg.content.split("$sticker ")[1]
        sticker_url = get_sticker(query)
        await msg.channel.send(sticker_url)

    if msg.content.startswith("$meme"):
        meme = get_meme()
        await msg.channel.send(meme)

    if msg.content.startswith("$choose"):
        queries = [msg.content.split(" ")[1], msg.content.split(" ")[2]]
        await msg.channel.send("I choose " + random.choice(queries))

    if msg.content.startswith("$toss"):
        await msg.channel.send(random.choice(["heads", "tails"]))
    if msg.content.startswith("$joke"):
        try:
            joke = get_joke()
            await msg.channel.send(joke)
        except discord.errors.HTTPException:
            joke = get_joke()
            await msg.channel.send(joke)
    if msg.content.startswith("$animals"):
        animal = get_animals()
        await msg.channel.send(animal)
    if msg.content.startswith("$quote"):
        quote = get_quote()
        await msg.channel.send(quote)
    if msg.content.startswith("$cmds"):
        await msg.channel.send(cmds)


client.run(config("DISCORD_BOT_KEY"))
