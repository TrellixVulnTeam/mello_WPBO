import requests
import json
import random

def get_meme():

    response = requests.get("https://meme-api.herokuapp.com/gimme/50")
    json_data = json.loads(response.text)
    imgs = [i["url"] for i in json_data["memes"]]
    
    return random.choice(imgs)
