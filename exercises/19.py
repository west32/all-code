import requests
from bs4 import BeautifulSoup


url_page="https://www.nytimes.com/"

def is_it_title_tag(tag):
    return tag.name == "h3" and tag.has_attr("class")

response = requests.get(url_page)
response.raise_for_status()
parsed_page = BeautifulSoup(response.text, "html.parser")
titles_list = []
title_tags= parsed_page.find_all(is_it_title_tag)
for title in title_tags:
    titles_list.append(title.string)



#
file_name=input("what should be name of that file?")
with open(f"{file_name}.txt","w",encoding='utf-8') as open_file:
    for article in titles_list:
        open_file.write (f"{str(article)}\n")