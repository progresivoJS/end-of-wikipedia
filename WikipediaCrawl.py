import time

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

def web_crawl():
    while continue_crawl(article_chain, target_url):
        first_link = find_first_link(article_chain[-1])
        time.sleep(2)