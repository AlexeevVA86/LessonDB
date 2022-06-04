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

def currency_rates(currency):
    try:
        URL = "https://www.cbr-xml-daily.ru/daily_json.js"
        req = requests.get(URL)
        dict_cbr = json.loads(req.text)
        msg = currency.upper()
        exchange_rates = dict_cbr['Valute'][msg]['Value']
        # name_valute = dict_cbr['Valute'][msg]['Name'] # Если бы не условия задачи о том что должно вернутся 
        # return f"{name_valute} {exchange_rates}"      # числовое значение то так мне больше нравится
        return exchange_rates
    except KeyError:
        return None


print(currency_rates("uSd"))
print(currency_rates("euR"))
print(currency_rates("111111111111"))