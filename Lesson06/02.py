ip_list = []
with open("nginx_logs.txt", encoding="utf-8") as g:
    for z in g.readlines():
        ip = (z.split('-')[0])
        ip_list.append(ip)

# считал файл и получил список всех IP запросов
# да бы не изобретать велосипед нагуглил конструкцию поиска
# самого часто повторяющегося значения

# Список преобразуется в множество.
# В нем все элементы уникальны.
ip_list_set = set(ip_list)

most_common = None  # наиболее часто встречаемое значение
qty_most_common = 0  # его количество

# в цикле перебираются элементы (item) множества
for item in ip_list_set:
    # переменной qty присваивается количество случаев
    # item в списке ip_list
    qty = ip_list.count(item)
    # Если это количество больше максимального,
    if qty > qty_most_common:
        qty_most_common = qty  # то заменяем на него максимальное,
        most_common = item  # запоминаем само значение

# вывод значения на экран
print(f"Мамкин дудосер {most_common}")

# и тут вспомнили что там че то про файлы и память было
