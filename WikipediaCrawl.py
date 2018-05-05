import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/Dead_Parrot_sketch")

html = response.text

soup = BeautifulSoup(html, 'html.parser')
print(soup.find(id="firstHeading"))

def continue_crawl(search_history, target_url, max_steps=25):
    """
    Determine whether we continue crwal.

    search_history : a list of strings which are the urls of Wikipedia articles
    target_url : a url which we want to find
    """
    if search_history[-1] == target_url:
        return False
    elif len(search_history) > max_steps:
        return False
    elif search_history[-1] in search_history[:-1]:
        return False
    else:
        return True