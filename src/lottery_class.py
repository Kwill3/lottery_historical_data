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
    def __init__(self, draw_type: Draw_Type) -> None:
        """Initialise Lottery class default values"""
        self.draw_type = draw_type
        self.draw_date = ""
        self.draw_day = ""
        self.main_numbers = []
        self.special_numbers = []

    def filter_tags(self, html: BeautifulSoup, tag_name: str) -> None:
        """
        Remove multiple instances of the same tag from inside the parsed html doc

        Parameters
        ----
            html: BeautifulSoup
                Parsed HTML document to perform filtering on
            tag_name : str
                The targeted tag to recursively remove

        Returns
        -------
            None
        """
        filtered = html.find_all(tag_name)
        for tag in filtered:
            tag.extract()
        return
    
    def get_numbers(self):
        # set for life
        if self.draw_type == Draw_Type.SFL:
            draw_html = soup.find("div", class_=Draw_Type.SFL.value)
            draw_numbers_html = draw_html.find("ul", class_="draw_numbers")
        # lotto
        elif self.draw_type == Draw_Type.LOTTO:
            draw_html = soup.find("div", class_=Draw_Type.LOTTO.value)
            draw_numbers_html = draw_html.find("ul", class_="draw_numbers")
        # euromillion
        elif self.draw_type == Draw_Type.EUROMILLIONS:
            draw_html = soup.find("div", class_=Draw_Type.EUROMILLIONS.value)
            draw_numbers_html = draw_html.find("ul", class_="draw_numbers")
        # thunderball
        elif self.draw_type == Draw_Type.THUNDERBALL:
            draw_html = soup.find("div", class_=Draw_Type.THUNDERBALL.value)
            draw_numbers_html = draw_html.find("ul", class_="draw_numbers")

        # scraped main numbers
        main_numbers_html = draw_numbers_html.find_all("li", class_="number main")
        for main_number in main_numbers_html:
            self.main_numbers.append(main_number.text.strip())

        # scraped special numbers
        special_numbers_html = draw_numbers_html.find_all("li", class_="number special")
        # remove span elements
        for list in special_numbers_html:
            self.filter_tags(list, "span")
        for special_number in special_numbers_html:
            self.special_numbers.append(special_number.text.strip())

        # get draw date details
        draw_date_full = draw_html.find(class_="draw_date").text.strip()
        self.draw_day = draw_date_full[:3]
        self.draw_date = draw_date_full[4:]
