import bs4
import requests
import random

def get_dark_joke():
    url="https://ponly.com/dark-humor-jokes/"
    r=requests.get(url)
    soup=bs4.BeautifulSoup(r.content,"html.parser")
    jokes = [i.text for i in soup.find_all("p")]
    joke = random.choice(jokes)
    if "Next:" not in joke and "Dark humor focuses on" not in joke and "120 jokes" not in joke and "ponly" not in joke:
        return joke



