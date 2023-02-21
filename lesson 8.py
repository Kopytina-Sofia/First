import requests

from bs4 import BeautifulSoup

response = requests.get("https://coinmarketcap.com/")
if requests.status_codes == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    print(soup)



