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
        self.draw_type = draw_type.value
        self.draw_date = ""
        self.draw_day = ""
        self.main_numbers = []
        self.special_number = None

    # remove multiple instances of the same tag from inside a html element
    def filter_tags(self, html: BeautifulSoup, tag_name: str):
        filtered = html.find_all(tag_name)
        for tag in filtered:
            tag.extract()
        return html
    
    def get_numbers(self):
        # set for life draws
        if self.draw_type == Draw_Type.SFL.value:
            set_for_life = soup.find("div", class_="set-for-life")
            draw_numbers_sfl = set_for_life.find("ul", class_="draw_numbers")

            # 5 main numbers from 1 to 47
            main_numbers_html = draw_numbers_sfl.find_all("li", class_="number main")
            for main_number in main_numbers_html:
                self.main_numbers.append(main_number.text.strip())

            # 1 special number from 1 to 10
            special_number_html = draw_numbers_sfl.find("li", class_="number special")
            # remove span elements
            self.filter_tags(special_number_html, "span")
            self.special_number = special_number_html.text.strip()

            # get draw date details
            draw_date_full = set_for_life.find("p", class_="draw_date").text.strip()
            self.draw_day = draw_date_full[:3]
            self.draw_date = draw_date_full[4:]


