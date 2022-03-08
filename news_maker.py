from bs4 import BeautifulSoup
import requests


source = "https://vc.ru"

def get_last_news(source):
    result = requests.get(source)
    soup = BeautifulSoup(result.content, "lxml")
    return soup.find_all(class_="l-inline")[0].a.text


if __name__ == "__main__":

    last_new = get_last_news(source)
    print(last_new)

