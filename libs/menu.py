import pywebio.input as inp
from pywebio.output import *
from pywebio.session import run_js
import json
import time
from functools import partial


class SaveToJson(object):
    def __init__(self, filename):
        self.filename = filename

    def save_new_value(self, data):
        data = json.dumps(data)
        data = json.loads(str(data))
        with open(self.filename, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def chek_value(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            current_price = json.load(file)
            return current_price


class TrakersTools(object):
    def __init__(self, __money):
        self.__money = __money


    async def add_traker(self):
        coin_ticker = await inp.select("Выберите монету", self.__money, multiple=False)
        price = await inp.input('Введите ожидаемую цену')
        dict_trakers = dict(SaveToJson("libs/trakers.json").chek_value())
        dict_trakers[coin_ticker] = price
        SaveToJson("libs/trakers.json").save_new_value(dict_trakers)
        toast("Отслежаватель создан")
        time.sleep(0.5)
        run_js("location.reload()")
        return coin_ticker, price

    @staticmethod
    def delete_traker_in_file(coin_name):
        traker_list = SaveToJson("libs/trakers.json").chek_value()
        del traker_list[coin_name]
        SaveToJson("libs/trakers.json").save_new_value(traker_list)
        run_js("location.reload()")

    @staticmethod
    def get_trakers():
        result = []
        tasks = SaveToJson("libs/trakers.json").chek_value()
        for name, price in tasks.items():
            result.append([
                name,
                price,
                put_button(f"delete {name}", onclick=partial(TrakersTools.delete_traker_in_file, name))
            ])

        put_table(
            result,
            header=["name", "price to alert", "delete?"]
        )
        put_button("Назад", onclick=lambda: run_js("location.reload()"))
