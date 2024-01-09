import time

from bs4 import BeautifulSoup
import requests

from .menu import SaveToJson as STJ, TrakersTools as TT
from .tg_bot import send_notify as sn
url = "https://www.cbr.ru/currency_base/daily/"
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
}

req = requests.get(url, headers= headers)
src = req.text
soup = BeautifulSoup(src, 'lxml')


def get_vppo(val_name):
    val_name = soup.find("td", text=f"{val_name}")
    val_count = val_name.find_next_sibling()
    val_course = str(val_count.find_next_sibling().find_next_sibling().text).replace(",", ".")
    val_price_per_one = float(val_course) / float(val_count.string)

    if val_price_per_one < 1:
        rounded_vppo = round(val_price_per_one, 2)
    else:
        rounded_vppo = int(val_price_per_one)
    return rounded_vppo


def work():
    while True:
        data = {
            "AUD": get_vppo("AUD"),
            "AZN": get_vppo("AZN"),
            "AMD": get_vppo("AMD"),
            "BYN": get_vppo("BYN"),
            "BGN": get_vppo("BGN"),
            "BRL": get_vppo("BRL"),
            "HUF": get_vppo("HUF"),
            "KRW": get_vppo("KRW"),
            "VND": get_vppo("VND"),
            "HKD": get_vppo("HKD"),
            "GEL": get_vppo("GEL"),
            "DKK": get_vppo("DKK"),
            "AED": get_vppo("AED"),
            "USD": get_vppo("USD"),
            "EUR": get_vppo("EUR"),
            "EGP": get_vppo("EGP"),
            "INR": get_vppo("INR"),
            "IDR": get_vppo("IDR"),
            "KZT": get_vppo("KZT"),
            "CAD": get_vppo("CAD"),
            "QAR": get_vppo("QAR"),
            "KGS": get_vppo("KGS"),
            "CNY": get_vppo("CNY"),
            "MDL": get_vppo("MDL"),
            "NZD": get_vppo("NZD"),
            "TMT": get_vppo("TMT"),
            "NOK": get_vppo("NOK"),
            "PLN": get_vppo("PLN"),
            "RON": get_vppo("RON"),
            "XDR": get_vppo("XDR"),
            "RSD": get_vppo("RSD"),
            "SGD": get_vppo("SGD"),
            "TJS": get_vppo("TJS"),
            "THB": get_vppo("THB"),
            "TRY": get_vppo("TRY"),
            "UZS": get_vppo("UZS"),
            "UAH": get_vppo("UAH"),
            "GBP": get_vppo("GBP"),
            "CZK": get_vppo("CZK"),
            "SEK": get_vppo("SEK"),
            "CHF": get_vppo("CHF"),
            "ZAR": get_vppo("ZAR"),
            "JPY": get_vppo("JPY")
        }
        STJ("libs/data.json").save_new_value(data)

        trakers = STJ("libs/trakers.json").chek_value()
        course = STJ("libs/data.json").chek_value()

        for name in trakers:
            for name_v in course:
                if name == name_v and int(trakers[name]) <= int(course[name]):
                   sn("%s: %s" % (name, course[name]))
                   TT.delete_traker_in_file(name)
        time.sleep(20)
