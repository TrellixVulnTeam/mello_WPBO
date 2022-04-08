# importing required modules
import bs4
import requests
import random


def get_joke():
    """returns a hilarious dad joke"""
    url = "https://ponly.com/best-dad-jokes/"
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    jokes = soup.find_all("p", class_=None)
    joke = random.choice(jokes).text
    if joke != None:
        return joke
    else:
        return get_joke()
