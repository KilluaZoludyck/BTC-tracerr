import requests
from bs4 import BeautifulSoup
import time
sleep = 3


def update_ticker():
    BTC = "https://www.rbc.ru/crypto/currency/btcusd"
    headers = {
            'user agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/131.0.0.0 Safari/537.36"}


    html = requests.get(BTC, headers)
    soap = BeautifulSoup(html.content, "html.parser")
    convert = soap.findAll("div", {"class": "chart__subtitle js-chart-value"})
    convert_list = list(convert[0])

    price = str(convert_list[0]).strip()
    print(f'BitCoin now: {price}$\n')

    time.sleep(sleep)
    update_ticker()


update_ticker()
