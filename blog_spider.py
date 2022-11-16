import requests


def crawl_func(url):
    r = requests.get(url)
    print(url, len(r.text), r.status_code)
