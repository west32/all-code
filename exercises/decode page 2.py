
import requests
from bs4 import BeautifulSoup

def is_div_inner_container(tag):
    return tag.name == "div" and tag.has_attr("class") and "dek" in tag["class"]


PAGE_URL= "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
response = requests.get(PAGE_URL)
response.raise_for_status()
parsed_page=BeautifulSoup(response.content,features="html.parser")

article_text=""
data1= parsed_page.find(is_div_inner_container)
print(data1)


print(article_text)