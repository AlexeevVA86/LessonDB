import pickle
import requests
import pprint


# URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
# response = requests.get(URL)
# txt = response.text.split(')"')
# # pprint.pprint(txt)

# ip_list = list()
# for i in txt:
#     end_index = i.find(' - - ')
#     remote_addr = i[:end_index].strip('\n')
#     ip_list.append(remote_addr)
# # print(ip_list)

# with open('2.txt', 'wb') as file:
#     pickle.dump(ip_list, file)

with open('2.txt', 'rb') as file:
    data_new = pickle.load(file)
    # print(data_new)

ip_list_set = set(data_new)
most_common = None  # наиболее часто встречаемое значение
qty_most_common = 0  # его количество

# в цикле перебираются элементы (item) множества
for item in ip_list_set:
    # переменной qty присваивается количество случаев
    # item в списке ip_list
    qty = data_new.count(item)
    # Если это количество больше максимального,
    if qty > qty_most_common:
        qty_most_common = qty  # то заменяем на него максимальное,
        most_common = item  # запоминаем само значение

# вывод значения на экран
print(f"Мамкин дудосер {most_common}")
