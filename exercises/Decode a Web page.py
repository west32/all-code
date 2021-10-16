import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass


#
# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on
# the New York Times homepage.

def article_title_h3(tag):
    return tag.name == "h3"


class TheNewYorkTimesParser():
    PAGE_URL = "https://www.nytimes.com/"

    def __init__(self):
        self.parsed_page = None
        self.last_post_index = 0
        self.found_post_preview = []

    def load_page(self):
        response = requests.get(self.PAGE_URL)
        response.raise_for_status()
        self.parsed_page = BeautifulSoup(response.text, features="html.parser")

    def parse_all_preview(self):
        article_titles = self.parsed_page.find_all("h3")
        for article_title in article_titles:
            self.found_post_preview.append(article_title.string)


def run_example():
    parser = TheNewYorkTimesParser()
    parser.load_page()
    parser.parse_all_preview()
    print(parser.found_post_preview)


if __name__ == "__main__":
    run_example()
