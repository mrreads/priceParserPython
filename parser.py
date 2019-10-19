from requests import Session
from bs4 import BeautifulSoup as bs

try:
    articles = open("./art.txt", "r")
    articles = articles.read()
    articles = articles.split("\n")
except FileNotFoundError:
    print("Файла с артикулами не найдено")
    raise SystemExit(1)
if (len(articles) == 1 and articles[0] == ''):
    print("Файл не содержит артикулов")
    raise SystemExit(1)

res = open("./res.txt", "a")

session = Session()

for i in range(len(articles)):
    request = session.get("http://www.komus.ru/product/" + articles[i] + "/")
    soup = bs(request.content, "html.parser")
    try:
        span = soup.find("span", attrs={"class": "i-fs30 i-fwb"}).text.strip()
        print(articles[i].strip() + " " + span)
        res.write(articles[i].strip() + " " + span + "\n")
    except AttributeError:
        print("Страницы с таким продуктом не существует, либо ценник не найден")
        res.write(articles[i].strip() + " null\n")