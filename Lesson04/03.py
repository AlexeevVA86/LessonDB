# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) 
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. 
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. 
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. 
# Можно ли, используя только методы класса str, решить поставленную задачу? 
# Функция должна возвращать результат числового типа, например float. 
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? 
# Сильно ли усложняется код функции при этом? 
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. 
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? 
# В качестве примера выведите курсы доллара и евро.
# https://www.cbr-xml-daily.ru/
import requests
import json
import pprint

URL = "https://www.cbr-xml-daily.ru/daily_json.js"
req = requests.get(URL)
dict_cbr = json.loads(req.text)


def currency_rates(currency):
    msg = currency.upper()
    exchange_rates = dict_cbr['Valute'][msg]['Value']
    print(exchange_rates)

currency_rates("usd")


# date_get = dict_cbr['Date']
# name_valute = dict_cbr['Valute']['USD']['Name']

# print(f"Курс {name_valute} на {date_get} составляет {exchange_rates} руб. ")

#     print()
#     return 0

# #pprint.pprint(req.text)
