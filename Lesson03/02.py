# 1. Доработать предыдущую функцию в num_translate_adv(): реализовать
# корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
# должен быть с заглавной.

numbers = {'zero': 'ноль', 'one': 'один', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
           'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(arg):
    if arg.islower() == True:
        magick = numbers.get(arg)
        return magick
    else:
        magick = numbers.get(arg.lower())
        return f"{magick.capitalize()}"


print(num_translate_adv('One'))
