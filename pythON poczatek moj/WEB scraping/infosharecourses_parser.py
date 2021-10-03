import requests
from dataclasses import dataclass
from bs4 import BeautifulSoup

@dataclass
class CoursePreview:
    title: str
    time:str
    type: str

def course_title_div(tag):
     return tag.name == "div" and tag.has_attr("class") and "courses-page__item__inner" in tag["class"]



class InfoShareParser:
    PAGE_URL = "https://infoshareacademy.com"

    def __init__(self):
        self.parsed_page = None
        self.last_post_index = 0
        self.found_course_previews= []

    def load_page(self):
        response = requests.get(self.PAGE_URL)
        response.raise_for_status()
        self.parsed_page= BeautifulSoup(response.text, features="html.parser")

    def parse_all_previews(self):
        course_titles = self.parsed_page.find_all(course_title_div)
        for course_title in course_titles:
            title_tag = course_title.p
            title= title_tag.string
            span_tag = course_title.find_all("span")
            time= span_tag[0].string
            type = span_tag[1].string
            course_preview= CoursePreview(title,time,type)
            self.found_course_previews.append(course_preview)







    def check(self):
        title_tag = self.parsed_page.find_all(is_title_contain_tag)

        print(title_tag.string)


def run_example():
    parser = InfoShareParser()
    parser.load_page()
    parser.parse_all_previews()
    print(parser.found_course_previews)

if __name__=="__main__":
    run_example()