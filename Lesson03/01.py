# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

numbers = {'zero': 'ноль', 'one': 'один', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
           'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(a):
    magick = numbers.get(a)
    return magick


print(num_translate('zero'))
