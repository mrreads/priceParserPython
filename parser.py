from requests import Session
from bs4 import BeautifulSoup as bs

try:
    articles = open("./Артикулы.txt", "r")
    articles = articles.read()
    articles = articles.split("\n")
except FileNotFoundError:
    print("Файла с артикулами не найдено")
    input('Нажмите Enter, чтобы выйти из программы')
    raise SystemExit(1)
if (len(articles) == 1 and articles[0] == ''):
    print("Файл не содержит артикулов")
    input('Нажмите Enter, чтобы выйти из программы')
    raise SystemExit(1)

res = open("./Результат.txt", "a")

session = Session()

for i in range(len(articles)):
    currentArticle = articles[i].strip()
    request = session.get("http://www.komus.ru/product/" + articles[i] + "/")
    soup = bs(request.content, "html.parser")
    try:
        span = soup.find("span", attrs={"class": "i-fs30 i-fwb"}).text.strip()
        print(currentArticle + " " + span)
        res.write(currentArticle + " " + span + "\n")
    except AttributeError:
        print(currentArticle + " null")
        res.write(currentArticle + " null\n")
    print("Прочитано ", i + 1, " артикулов из ", len(articles))

input('Нажмите Enter, чтобы выйти из программы')
