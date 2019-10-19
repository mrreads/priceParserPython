import requests
from bs4 import BeautifulSoup as bs

url = "http://www.komus.ru/product/65617/"
# headers = {
#     'accept': '*/*',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
# }

session = requests.Session()
request = session.get(url)
soup = bs(request.content, 'html.parser')
span = soup.find('span', attrs={'class': 'i-fs30 i-fwb'}).text.strip()
print(span)