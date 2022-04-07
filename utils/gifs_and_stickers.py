import requests
import json
import random
from decouple import config

def get_sticker(query):
    response = requests.get(
        "http://api.giphy.com/v1/stickers/search",
        {"q": query, "api_key": config("GIPHY_API"), "limit": "1000"},
    )
    json_data = json.loads(response.text)
    links = [i["images"]["original"]["url"] for i in json_data["data"]]
    if len(links) > 0:
        return random.choice(links)
    else:
        return "Oops Not Found!"


def get_gif(query):
    response = requests.get(
        "http://api.giphy.com/v1/gifs/search",
        {"q": query, "api_key": config("GIPHY_API"), "limit": "1000"},
    )
    json_data = json.loads(response.text)
    links = [i["url"] for i in json_data["data"]]
    if len(links) > 0:
        return random.choice(links)
    else:
        return "Oops Not Found!"