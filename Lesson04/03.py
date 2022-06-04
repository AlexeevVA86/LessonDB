# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, 
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date. 
# Подумайте, как извлечь дату из ответа, 
# какой тип данных лучше использовать в ответе функции?
import requests
import json
import datetime as dt

def currency_rates(currency):
    try:
        URL = "https://www.cbr-xml-daily.ru/daily_json.js"
        req = requests.get(URL)
        dict_cbr = json.loads(req.text)
        msg = currency.upper()
        exchange_rates = dict_cbr['Valute'][msg]['Value']
        name_valute = dict_cbr['Valute'][msg]['Name']
        date_get = (dict_cbr['Date'][0:-15])
        date_tru = dt.datetime.strptime(date_get, '%Y-%m-%d').date() # зачем ?
        return f"Курс {name_valute} {exchange_rates} руб. на {date_tru}"
    except KeyError:
        return None


print(currency_rates("uSd"))
print(currency_rates("euR"))
print(currency_rates("111111111111"))