import requests
from bs4 import BeautifulSoup

x = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(x.text, 'html.parser')

# print(soup.prettify())

quotes = soup.find_all("div", "quote")
# print(x.text)
# print(type(quotes))

print(f"Found {len(quotes)} quotes!\n")
for i, quote in enumerate(quotes):
    text = quote.find("span", "text")
    author = quote.find("small", "author")
    print(f"Quote {i+1}: {text}")
    print(f"   — {author}\n")
    #print(f"Quote {i}")
    #print(quote)

