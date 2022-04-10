import json
import requests

trivia_categories={
        "science": "17",
        "general knowledge":"9",
        "computers":"18",
        "mathematics":"19",
        "film":"11",
        "music":"12",
        "video-games":"15",
        "board-games":"16",
        "sports":"21",
        "geography":"22",
        "history":"23",
        "art":"25",
        "celebrities":"26",
        "animals":"27"

    }

def get_trivia(category,difficulty,trivia_categories=trivia_categories):
    url = f"https://opentdb.com/api.php?amount=10&category={trivia_categories[category.lower()]}&difficulty={difficulty}&type=multiple"
    r = requests.get(url)
    return json.loads(r.text)["results"]



