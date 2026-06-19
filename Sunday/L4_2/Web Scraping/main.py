import requests
import random as r
from bs4 import BeautifulSoup as bs

x = requests.get("https://quotes.toscrape.com/")
#print(x.text)

soup = bs(x.text, "html.parser")

print(soup.prettify())
# HINT: Find, Find all, Quick Start

first_quote = soup.find_all("span", class_="text")[0].string # quote is just a string!
print(first_quote)