#importing modules
import bs4
import requests
import random

def get_fact():
    """scrapes a random interesting fact from a website"""
    r = requests.get("https://www.cosmopolitan.com/uk/worklife/a33367076/fun-facts-random/")
    soup = bs4.BeautifulSoup(r.content,"html.parser")
    li = [i.find_all("li") for i in soup.find_all("ol" ,class_="body-ol")]
    facts = [i.text for i in li[0]]
    return random.choice(facts)


