#which website i will scrap
#what will i scrap from the website
#how will i scrap
import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
books = soup.find_all("article")
for book in books:
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    price_container = book.select_one("div p.price_color")
    price = price_container.get_text(strip=True)
    print(f"the book titled {title} has a rate of {rating} and it costs {price}")
   