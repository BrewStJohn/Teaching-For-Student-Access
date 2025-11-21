import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"

# Send a GET request to the website
response = requests.get(url)

# Optional: save the HTML to a file for debugging
# with open("quotes_page.html", "w", encoding="utf-8") as f:
#     f.write(response.text)
# print("HTML saved as quotes_page.html")

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all quote blocks
quotes = soup.find_all("div", class_="quote")

if quotes:
    print(f"Found {len(quotes)} quotes!\n")
    for i, quote in enumerate(quotes):
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        print(f"Quote {i+1}: {text}")
        print(f"   — {author}\n")
else:
    print("No quotes found. Check your HTML or classes.")