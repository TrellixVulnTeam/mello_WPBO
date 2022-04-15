import requests
import json

def cat():
    """returns a random cat picuture"""
    r = requests.get("https://aws.random.cat/meow")
    return json.loads(r.text)["file"]
def dog():
    """returns a random dog picture"""
    r=requests.get("https://dog.ceo/api/breeds/image/random")
    return json.loads(r.text)["message"]
