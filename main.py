# importing everything
from utils import get_random_movie, get_random_show, get_random_anime
from utils import get_meme, get_joke,cat,dog, get_sticker, get_gif, get_quote
from utils import first_msg, cmds, get_movie_by_genre
from utils import get_text
import json
from utils import trivia, get_trivia
from utils import tictactoewin
import asyncio
from utils import get_fact
from discord.ext import commands
from discord.utils import find
from decouple import config
import discord
import random
from utils import get_dark_joke
from discord.ext import commands

# initializing the client
intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", intents=intents)

# tictactoe vars
player1 = ""
player2 = ""
turn = ""
game_over = True
board = []


def check_win(cond, mark):
    global game_over
    for condition in cond:
        if (
            board[condition[0]] == mark
            and board[condition[1]] == mark
            and board[condition[2]] == mark
        ):
            game_over = True


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
        if msg.content == "$movie" or msg.content == "$movie ":
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
            
    if msg.content.startswith("$asciitext"):
        #[ONLY WORKS ON PC] Converts the text into nice figlet format
        content=msg.content.split("$asciitext ")[1]
        await msg.channel.send(f"```{get_text(content)}```")
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
        try:
            query = msg.content.split("$gif ")[1]
            gif_url = get_gif(query)
            await msg.channel.send(gif_url)
        except IndexError:
            await msg.channel.send("Pls specify a query to search for.")


    if msg.content.startswith("$fact"):
        # gets a random fact
        fact = get_fact()
        await msg.channel.send(fact)

    if msg.content.startswith("$sticker"):
        # get a sticker based on the query passed
        try:
            query = msg.content.split("$sticker ")[1]
            sticker_url = get_sticker(query)
            await msg.channel.send(sticker_url)
        except IndexError:
            await msg.channel.send("Pls specify a query to search for.")

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

    if msg.content.startswith("$cat"):
        # gets a picture of a random cat 
        try:
            catpic = cat()
            await msg.channel.send(catpic)
        except json.decoder.JSONDecodeError:
            await msg.channel.send("This service is currently unavailable.")
            

    if msg.content.startswith("$dog"):
        # gets a picture of a random dog 
        dogpic = dog()
        await msg.channel.send(dogpic)

    if msg.content.startswith("$quote"):
        # gets a nice quote picture
        quote = get_quote()
        await msg.channel.send(quote)

    if msg.content.startswith("$cmds"):
        # gets the list of available commands
        embed = discord.Embed(title=cmds["heading"], color=discord.Colour.random())
        for i in cmds.keys():
            if i != "heading":
                embed.add_field(name=i, value=cmds[i], inline=True)
        await msg.channel.send(embed=embed)

    if msg.content.startswith("$darkjoke"):
        #returns a dark humorous joke
        for i in range(1,5):
            try:
                await msg.channel.send(get_dark_joke())
                break
            except discord.errors.HTTPException:
                continue

        
    if msg.content.startswith("$trivia"):
        # starts a trivia game
        if msg.content == "$trivia" or msg.content == "$trivia ":
            embed = discord.Embed(title=trivia["info"], color=discord.Colour.random())
            embed.add_field(name="Categories:", value=trivia["categories"])
            embed.add_field(name="Difficulties:", value=trivia["difficulties"])

            await msg.channel.send(embed=embed)
        else:
            category = msg.content.split(" ")[1]
            difficulty = msg.content.split(" ")[2]
            the_trivia = get_trivia(category, difficulty)
            for i in the_trivia:
                question = i["question"].replace("&#039;", "'").replace("&quot;", '"')
                answers = list(i["incorrect_answers"] + [i["correct_answer"]])
                random.shuffle(answers)

                embed = discord.Embed(
                    title=question,
                    description="\n (or) \n".join(answers)
                    .replace("&#039;", "'")
                    .replace("&quot;", '"'),
                    color=discord.Colour.random(),
                )
                await msg.channel.send(embed=embed)
                await asyncio.sleep(1)
                message = await client.wait_for("message")
                if message.content.lower() == i["correct_answer"].lower():
                    await msg.channel.send("Correct!")
                elif message.content.startswith("$endtrivia"):
                    # ends the trivia game
                    break
                else:
                    await msg.channel.send(
                        f"Incorrect! The correct answer is {i['correct_answer'].replace('&#039;','`')}"
                    )
                await asyncio.sleep(1)
            if not question:
                await msg.channel.send("No Such category or difficulty.")
            await asyncio.sleep(1)
            await msg.channel.send("***Trivia Ended!***")

    if msg.content.startswith("$tictactoe"):
        # starts a tictactoe game
        global count
        global player1
        global player2
        global turn
        global game_over

        if game_over:
            global board
            board = [
                ":white_large_square:",
                ":white_large_square:",
                ":white_large_square:",
                ":white_large_square:",
                ":white_large_square:",
                ":white_large_square:",
                ":white_large_square:",
                ":white_large_square:",
                ":white_large_square:",
            ]
            turn = ""
            game_over = False
            count = 0

            player1 = msg.content.split(" ")[1]
            player2 = msg.content.split(" ")[2]

            if "@"+str(msg.author).split("#")[0] in [player1,player2]:
                pass
            else:
                game_over=False
            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await msg.channel.send(line)
                    line = ""
                else:
                    line += " " + board[x]

            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                await msg.channel.send(f"It is {player1}'s turn.")
            elif num == 2:
                turn = player2
                await msg.channel.send(f"It is {player2}'s turn.")
        else:
            await msg.channel.send("A game is already in progress!")

    if msg.content.startswith("$place"):
        # place your move in the board
        try:
            if not game_over:
                pos = int(msg.content.split(" ")[1])
            else:
                await msg.channel.send("Pls start a new game.")
        except ValueError:
            await msg.channel.send("Please enter a valid position")
        if not game_over:
            mark = ""
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await msg.channel.send(line)
                        line = ""
                    else:
                        line += " " + board[x]
                check_win(tictactoewin, mark)
                if game_over == True:
                    await msg.channel.send(mark + " wins!")
                elif count >= 9:
                    game_over = True
                    await msg.channel.send("It's a tie!")
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
                await msg.channel.send(f"it's {turn}'s turn")

            else:
                await msg.channel.send(
                    "Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile."
                )

        else:
            await msg.channel.send(
                "Please start a new game using the $tictactoe command."
            )
    if msg.content.startswith("$endtictactoe"):
        game_over=True
        await msg.channel.send("Game ended!")
         


# running the bot
client.run(config("DISCORD_BOT_KEY"))
