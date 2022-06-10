# 4. Представлен список чисел. Необходимо вывести те его элементы,
# значения которых больше предыдущего, например:
# result = [12, 44, 4, 10, 78, 123]
# Подсказка: использовать возможности python, изученные на уроке.


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 78]


def previous_greater(list):
    result = []
    for i in range(1, len(list)):
        if list[i] > list[i-1]:
            result.append(list[i])
    return result


print(previous_greater(src))
