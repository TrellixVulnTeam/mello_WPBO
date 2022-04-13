# message variables



tictactoewin=[
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

trivia = {
    "info": """Welcome to trivia!
    $trivia <category> <difficulty> - starts a trivia game based of 10 questions based on the category and difficulty""",
    "categories": """    
⠀⠀ 1.science
        2.general knowledge
        3.computers
        4.mathematics
        5.film
        6.music
        7.video-games
        8.board-games
        9.sports
        10.geography
        11.history
        12.art
        13.celebrities
        14.animals
        """,
    "difficulties": """    
⠀⠀ 1.easy
        2.medium
        3.hard 
""",
}

first_msg = """
Hello Everyone I'm MELLO(Make Everyday a Little Less Ordinary)! 
type $cmds to view the commands available.😃
"""

cmds = {
    "heading": "Commands Available :-",
    "$trivia <category> <difficulty>": "starts a trivia game of 10 questions based on the category",
    "$fact": "gives you a random fact",
    "$choose <value-1> <value-2> ": "chooses between the two values",
    "$toss ": "tosses a coin.",
    "$gif <query>": "gives a gif related to the query.",
    "$sticker <query>": "gives a sticker related to the query.",
    "$meme": "summons a random meme.",
    "$animals": " gives a random picture of an animal (but there is a 10 sec latency).",
    "$quote": "gives a random quote picture.",
    "$movie": "gives a random but great movie recommendation.",
    "$show": "gives a random but great TV show recommendation.",
    "$joke": " makes a hilarous dad joke.",
    "$genre <genre>": "gives a nice movie or a TV show recomendation in the genre you have passed.",
}
