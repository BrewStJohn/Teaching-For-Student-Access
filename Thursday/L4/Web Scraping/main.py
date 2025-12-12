import requests
from bs4 import BeautifulSoup

x = requests.get('http://quotes.toscrape.com/')
#print(x.text)
soup = BeautifulSoup(x.text, 'html.parser')

#print(soup.prettify())

quotes = soup.find_all('div', "quote")
print(f"Found {len(quotes)} quotes!\n")

# print("Found " + str(len(quotes)) + " quotes! ")
# print()

for i, quote in enumerate(quotes):
    text = quote.find("span", class_="text")
    author = quote.find("small", class_ = "author")
    print(f"Quote {i+1}: {text}")
    print(f"   -{author}\n")


# INDEPENDANT TASKS:
# - You can webscrape from either the quotes page
# or the books page (if you have another page, let me know)

# QUOTES (IDEAS):
# 1) Tell me how many quotes are from Albert Einstein
# and there quotes
# 2) Ask the user for a tag. Then, print out
# the quotes that have that tag

# BOOKS (IDEAS):
# 1) How many books have 1, 2, 3, 4 and 5 star ratings?
# 2) Which book is the most expensive? The least expensive?
# 3) Print out all books of a genre asked by the user