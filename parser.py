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
headers = {"accept": "*/*", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"}

for i in range(len(articles)):
    currentArticle = articles[i].strip()
    request = session.get("http://www.komus.ru/product/" + articles[i] + "/", headers=headers)
    soup = bs(request.content, "html.parser")
    try:
        span = soup.find("span", attrs={"class": "i-fs30 i-fwb"}).text.strip().replace(" ", '')
        print(currentArticle + " " + span)
        res.write(currentArticle + " " + span + "\n")
    except AttributeError:
        print(currentArticle + " null")
        res.write(currentArticle + " null\n")
    print("Прочитано ", i + 1, " артикулов из ", len(articles))
