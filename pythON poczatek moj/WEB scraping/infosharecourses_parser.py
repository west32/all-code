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


# def is_time_contiain_tag(tag):
#     return tag.name == "span" and tag.has_attr("class") and "courses-page__item__details courses-page__item__details--time" in tag["class"]
#
# def is_type_contain_tag(tag):
#     return tag.name == "span" and tag.has_attr("class") and "courses-page" in tag["class"]

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
            time= span_tag[0]
            type = span_tag[1]
            course_preview= CoursePreview()



        # time_tags = self.parsed_page.find_all(is_time_contiain_tag)
        # type_tags = self.parsed_page.find_all(is_type_contain_tag)
        # for title_tags,time_tags,type_tags in zip(title_tags,time_tags,type_tags):
        #     course_preview = PostPreview(title_tags.string, time_tags.string, type_tags.string)
        #     self.found_course_previews.append(course_preview)



    def check(self):
        title_tag = self.parsed_page.find_all(is_title_contain_tag)

        print(title_tag.string)

    # def _find_title(self):
    #     title_header_open = self.page_html.index('<div class="courses-page', self.last_post_index)
    #     title_url_open_end = self.page_html.index("<p>" , title_header_open) + len("<p>")
    #     title_url_close = self.page_html.index("</p>", title_url_open_end)
    #     return self.page_html[title_url_open_end:title_url_close], title_url_close
    #
    # def _find_time(self,title_index ):
    #     time_header_open = self.page_html.index("<span class=",title_index)
    #     time_header_end= self.page_html.index('time">',time_header_open) +len('time">')
    #     time_url_close= self.page_html.index("</span>",time_header_end)
    #     return self.page_html[time_header_end:time_url_close], time_url_close
    #
    # def _find_type(self,time_index):
    #     type_open_begin = self.page_html.index("<span class=",time_index)
    #     type_open_end = self.page_html.index('mode">',type_open_begin) + len('mode">')
    #     type_url_close= self.page_html.index("</span>",type_open_end)
    #     return self.page_html[type_open_end:type_url_close], type_url_close

def run_example():
    parser = InfoShareParser()
    parser.load_page()
    parser.parse_all_previews()
    # parser.check()
    print(parser.found_course_previews)

if __name__=="__main__":
    run_example()