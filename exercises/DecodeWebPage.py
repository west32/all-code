import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.nytimes.com/")
response.raise_for_status()
parsed_page = BeautifulSoup(response.text,features="html.parser")

titles_list=[]

titles=parsed_page.find_all("h3")
for title in titles:
    titles_list.append(title.string)

print(titles_list)