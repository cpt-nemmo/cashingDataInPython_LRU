import requests

link = "https://proglib.io/p/vse-chto-nuzhno-znat-o-dekoratorah-python-2020-05-09"
cache = dict()

def get_article_from_server(url):
    print("Забираем статью с сервера...")
    response = requests.get(url)
    return response.text

def get_article(url):
    print("Получаем статью...")
    if url not in cache:
        cache[url] = get_article_from_server(url)

    return cache[url]

get_article(link)[:1000]
get_article(link)[:1000]