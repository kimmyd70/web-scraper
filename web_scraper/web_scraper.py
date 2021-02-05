# Scraping from wikipedia page:

import requests as req
from bs4 import BeautifulSoup as bs

url = 'https://en.wikipedia.org/wiki/UNESCO_Institute_for_Statistics'

response = req.get(url)
content = response.content
print(content)

soup = bs(content,'html.parser' )
print(soup.prettify())