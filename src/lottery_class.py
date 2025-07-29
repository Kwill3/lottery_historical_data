import requests
from enum import Enum
from bs4 import BeautifulSoup

URL = "https://www.national-lottery.co.uk/results"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

class Draw_Type(Enum):
    SFL = "set-for-life"
    THUNDERBALL = "thunderball"
    LOTTO = "lotto"
    EUROMILLIONS = "euromillions"

class Lottery:
    def __init__(self, draw_type: Draw_Type):
        self.draw_type = Draw_Type.value

    # remove multiple instances of the same tag from inside a html element
    def filter_tags(self, html: BeautifulSoup, tag_name: str):
        filtered = html.find_all(tag_name)
        for tag in filtered:
            tag.extract()
        return html
