import os
import threading
import pywebio
import pywebio.input as inp
from pywebio.output import clear,put_image

from libs import menu, parse


async def main():
    clear()
    threading.Thread(target=parse.work).start()

    logo_path = os.path.join("data", "logo.png")
    put_image(open(logo_path, "rb").read())

    method = await inp.select(
        "Выберите действие",
        [
            "Добавить трекер",
            "Список трекеров"
        ]
    )

    if "Добавить трекер" == method:
        await menu.TrakersTools([
        "AUD", "AZN", "AMD", "BYN", "BGN", "BRL", "HUF", "KRW", "VND", "HKD", "GEL", "DKK",
        "AED", "USD", "EUR", "EGP", "INR", "IDR", "KZT", "CAD", "QAR", "KGS", "CNY", "MDL", "NZD", "TMT", "NOK", "PLN", "RON",
        "XDR", "RSD", "SGD", "TJS", "THB", "TRY", "UZS", "UAH", "GBP", "CZK", "SEK", "CHF", "ZAR", "JPY"]).add_traker()
    elif "Список трекеров" == method:
        menu.TrakersTools.get_trakers()

if __name__ == '__main__':
    pywebio.start_server(main, host="0.0.0.0", port=4444)