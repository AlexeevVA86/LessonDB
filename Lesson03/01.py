# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

numbers = {'0': 'zero', '1': 'one', '3': 'tre', '4': 'four', '5': 'five', '6': 'secs', '7': 'seven', '8': 'eith', '9': 'night', '10': 'ten'}

def num_translate(a = 1):
    magick = numbers.get(a)
    print(magick)
    return magick

print(num_translate())