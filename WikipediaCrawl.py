import urllib
import time
import requests
from bs4 import BeautifulSoup

def continue_crawl(search_history, target_url, max_steps=25):
    """
    Determine whether we continue crwal.

    search_history : a list of strings which are the urls of Wikipedia articles
    target_url : a url which we want to find
    """
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search!")
        return False
    else:
        return True

def find_first_link(url):
    # return the first link as a string, or return None if there is no link
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    article_link = None

    for element in content_div.find_all("p", recursive=False):
        anchor = element.find('a', recursive=False)
        if anchor:
            article_link = anchor.get('href')
            break

    if not article_link:
        return
    
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link

def web_crawl(article_chain, target_url, delay=2):
    while continue_crawl(article_chain, target_url):
        print(article_chain[-1])
        first_link = find_first_link(article_chain[-1])
        if not first_link:
            print("We've arrived at an articel with no links, aborting search!")
            return
        article_chain.append(first_link)
        time.sleep(delay)

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

web_crawl([start_url], target_url)