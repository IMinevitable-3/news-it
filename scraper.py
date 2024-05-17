import requests
from bs4 import BeautifulSoup as bs


class BBC:
    def __init__(self, url: str):
        article = requests.get(url)
        self.soup = bs(article.content, "html.parser")
        self.body = self.get_body()
        self.title = self.get_title()

    def get_body(self) -> list:
        body = self.soup.find(property="articleBody")
        return [p.text for p in body.find_all("p")]

    def get_title(self) -> str:
        return self.soup.find(class_="story-body__h1").text
