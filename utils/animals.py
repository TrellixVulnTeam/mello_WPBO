import requests,bs4,random

def get_animals():
    r = requests.get("https://unsplash.com/s/photos/cute-animals")
    soup = bs4.BeautifulSoup(r.content,"html.parser")
    imgsrc=[i["src"] for i in soup.find_all("img",class_="YVj9w")]
    return random.choice(imgsrc)
