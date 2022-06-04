# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, 
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date. 
# Подумайте, как извлечь дату из ответа, 
# какой тип данных лучше использовать в ответе функции?

import requests
import json
import pprint

def currency_rates(currency):
    try:
        URL = "https://www.cbr-xml-daily.ru/daily_json.js"
        req = requests.get(URL)
        dict_cbr = json.loads(req.text)
        msg = currency.upper()
        exchange_rates = dict_cbr['Valute'][msg]['Value']
        # name_valute = dict_cbr['Valute'][msg]['Name'] # Если бь не условия задачи о том что должно вернутся 
        # return f"{name_valute} {exchange_rates}"      # числовое значение то так мне больше нравится
        return exchange_rates
    except KeyError:
        return None


print(currency_rates("uSd"))
print(currency_rates("euR"))
print(currency_rates("111111111111"))


# date_get = dict_cbr['Date']
# name_valute = dict_cbr['Valute']['USD']['Name']

# print(f"Курс {name_valute} на {date_get} составляет {exchange_rates} руб. ")

#     print()
#     return 0

# #pprint.pprint(req.text)
