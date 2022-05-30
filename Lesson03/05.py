# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого):
from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(arg):
    i = int(arg)
    while i > 0:
        random_idx = randrange(len(nouns))
        random_idx = randrange(len(adverbs))
        random_idx = randrange(len(adjectives))
        jokes = f'"{nouns[random_idx]} {adverbs[random_idx]} {adjectives[random_idx]}"'
        print(jokes, end=" ")
        i = i - 1


get_jokes(3)
