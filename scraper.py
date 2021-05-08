import requests
from bs4 import BeautifulSoup




respons = requests.get("https://www.ceneo.pl/63419968#tab=reviews")

page_dom = BeautifulSoup(respons.text, "html.parser")

#print(page_dom.prettify())

opinions = page_dom.select("div.js_product-review")
opinion = opinions.pop(0)

opinion_id = opinion["data-entry-id"]

author = opinion.select_one("span.user-post__author-name").text.strip()