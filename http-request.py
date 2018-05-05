import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/Dead_Parrot_sketch")

html = response.text

soup = BeautifulSoup(html, 'html.parser')
print(soup.find(id="firstHeading"))