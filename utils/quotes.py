import bs4
import requests
import random


def get_quote():
    r = requests.get("https://www.wow4u.com/quote-of-the-day/")
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    quotes = [i["src"] for i in soup.find_all("img", {"data-orig-height": "446"})]
    quote = random.choice(quotes)
    if quote.startswith(".."):
        quote = quote.replace("..", "")
    return "https://www.wow4u.com" + quote
