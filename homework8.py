import requests

from bs4 import BeautifulSoup
list_curs = {}

responce = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
if responce.status_code == 200:
    soup = BeautifulSoup(responce.text, features="html.parser")
    curs_kod = soup.find_all("td", {"data-label": "Код літерний"})
    curs_val = soup.find_all("td", {"data-label": "Офіційний курс"})
    for i in range(len(curs_kod)):
        list_curs[curs_kod[i].text] = curs_val[i].text

print(list_curs)
print(list_curs['USD'])

