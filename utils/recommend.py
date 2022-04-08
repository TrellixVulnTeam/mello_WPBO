# importing required modules
import random
import bs4
import requests


def get_random_movie():
    """returns a random but nice movie recommendation"""
    r = requests.get("https://www.imdb.com/chart/top/")

    soup = bs4.BeautifulSoup(r.content, "html.parser")

    movies_links = [
        "https://imdb.com" + i.a["href"]
        for i in soup.find_all("td", class_="titleColumn")
    ]

    return random.choice(movies_links)


def get_random_show():
    """returns a random but nice tv show recommendation"""
    r = requests.get("https://www.imdb.com/chart/toptv/")

    soup = bs4.BeautifulSoup(r.content, "html.parser")

    movies_links = [
        "https://imdb.com" + i.a["href"]
        for i in soup.find_all("td", class_="titleColumn")
    ]

    return random.choice(movies_links)


def get_random_anime():
    """returns a random but nice anime recommendation"""
    r = requests.get(
        "https://www.imdb.com/search/keyword/?keywords=anime&ref_=fn_al_kw_1"
    )

    soup = bs4.BeautifulSoup(r.content, "html.parser")

    movies_links = [
        "https://imdb.com" + i.a["href"]
        for i in soup.find_all("h3", class_="lister-item-header")
    ]

    return random.choice(movies_links)


def get_movie_by_genre(genre):
    """returns a list of nice movies on the given genre"""
    r = requests.get(f"https://www.imdb.com/search/title/?genres={genre}")
    message = ""
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    movies_links = [
        "https://imdb.com" + i.a["href"]
        for i in soup.find_all("h3", class_="lister-item-header", limit=10)
    ]
    for i in movies_links:
        message += i + "\n"
    return message
